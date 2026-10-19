# Databricks notebook source
# MAGIC %md
# MAGIC # ĐỀ TÀI 7: MÔ HÌNH CHẤM ĐIỂM TÍN DỤNG & THẨM ĐỊNH RỦI RO VỠ NỢ
# MAGIC ## PHÂN TÍCH VÀ HUẤN LUYỆN TRÊN BỘ DỮ LIỆU LỚN LENDINGCLUB (2,260,701 BẢN GHI)
# MAGIC ---
# MAGIC **Nền tảng:** Databricks Serverless / Apache Spark MLlib  
# MAGIC **Kiến trúc:** Medallion Architecture (Bronze -> Silver -> Gold Delta Lake)  
# MAGIC **Quy mô Dữ liệu:** 2.26 triệu hồ sơ tín dụng (Big Data Scale)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 1. BRONZE LAYER - INGESTION & DELTA STORAGE (2.26M RECORDS)

# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, regexp_extract, lit, round, count, avg, sum

# 1. Đọc dữ liệu từ bảng LendingClub hoặc tệp tải lên
# Hỗ trợ cả 2 tên bảng: 'lending_club_data' (2.26M dòng) hoặc 'credit_risk_dataset'
table_name = "workspace.default.lending_club_data"
try:
    df_raw = spark.table(table_name)
    print(f"✅ Đã kết nối bảng dữ liệu lớn: {table_name}")
except Exception:
    table_name = "workspace.default.credit_risk_dataset"
    df_raw = spark.table(table_name)
    print(f"ℹ️ Đang sử dụng bảng dữ liệu: {table_name}")

print(f"📊 Tổng số bản ghi thô: {df_raw.count():,} dòng")
df_raw.printSchema()
display(df_raw.limit(5))

# 2. Ghi vào Bronze Delta Table (bảo toàn nguyên bản dữ liệu thô)
df_raw.write.format("delta") \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .saveAsTable("workspace.default.bronze_credit_data")

print("✅ ĐÃ NẠP THÀNH CÔNG VÀO BRONZE DELTA TABLE: workspace.default.bronze_credit_data")

# COMMAND ----------

# MAGIC %md
# MAGIC ### 2. SILVER LAYER - DISTRIBUTED CLEANING & FEATURE STANDARDIZATION

# COMMAND ----------

df_bronze = spark.table("workspace.default.bronze_credit_data")

# Chuẩn hóa tên cột nếu là bộ dữ liệu gốc LendingClub
cols = df_bronze.columns
df_std = df_bronze

# Ánh xạ cột LendingClub sang tên chuẩn hóa của Pipeline
if "annual_inc" in cols:
    df_std = df_std.withColumnRenamed("annual_inc", "person_income")
if "purpose" in cols:
    df_std = df_std.withColumnRenamed("purpose", "loan_intent")
if "int_rate" in cols:
    df_std = df_std.withColumnRenamed("int_rate", "loan_int_rate")

# Chuẩn hóa biến nhãn loan_status (nếu là dạng chuỗi 'Fully Paid' / 'Charged Off')
if "loan_status" in cols:
    # Nếu kiểu chuỗi
    from pyspark.sql.types import StringType
    if isinstance(df_std.schema["loan_status"].dataType, StringType):
        df_std = df_std.filter(col("loan_status").isin("Fully Paid", "Charged Off", "Default")) \
            .withColumn("loan_status", when(col("loan_status") == "Fully Paid", 0).otherwise(1))

# Chuẩn hóa thâm niên emp_length (trích xuất số từ chuỗi như '10+ years', '< 1 year')
if "emp_length" in cols:
    df_std = df_std.withColumn(
        "person_emp_length",
        when(col("emp_length").contains("<"), 0.0)
        .when(col("emp_length").contains("10"), 10.0)
        .otherwise(regexp_extract(col("emp_length"), r"(\d+)", 1).cast("double"))
    )

# Chuẩn hóa DTI và Lịch sử tín dụng nếu chưa có
if "dti" in cols and "loan_percent_income" not in cols:
    df_std = df_std.withColumn("loan_percent_income", round(col("dti") / 100.0, 4))
elif "loan_percent_income" not in cols:
    df_std = df_std.withColumn("loan_percent_income", round(col("loan_amnt") / col("person_income"), 4))

if "pub_rec_bankruptcies" in cols and "cb_person_default_on_file" not in cols:
    df_std = df_std.withColumn(
        "cb_person_default_on_file",
        when(col("pub_rec_bankruptcies") > 0, "Y").otherwise("N")
    )

if "person_age" not in cols:
    # Nếu thiếu cột tuổi trong LendingClub, gán mặc định dựa trên thâm niên tín dụng
    df_std = df_std.withColumn("person_age", (lit(25) + col("person_emp_length")).cast("integer"))

if "cb_person_cred_hist_length" not in cols:
    df_std = df_std.withColumn("cb_person_cred_hist_length", (col("person_emp_length") + lit(2)).cast("integer"))

# Làm sạch dữ liệu phân tán (Lọc ngoại lai & Điền giá trị thiếu)
df_silver = df_std \
    .filter((col("person_age") >= 18) & (col("person_age") <= 85)) \
    .filter((col("person_income") > 0) & (col("person_income") <= 1000000)) \
    .filter((col("loan_amnt") >= 500) & (col("loan_amnt") <= 100000)) \
    .na.fill({
        "person_emp_length": 0.0,
        "loan_int_rate": 11.5,
        "loan_percent_income": 0.20,
        "cb_person_default_on_file": "N",
        "cb_person_cred_hist_length": 3,
        "person_home_ownership": "RENT",
        "loan_intent": "debt_consolidation",
        "loan_grade": "B"
    }) \
    .withColumn("person_income", col("person_income").cast("double")) \
    .withColumn("loan_amnt", col("loan_amnt").cast("double")) \
    .withColumn("loan_int_rate", col("loan_int_rate").cast("double")) \
    .withColumn("loan_status", col("loan_status").cast("integer"))

# Phân vùng tối ưu hóa cho quy mô Big Data 2.26 triệu dòng
df_silver = df_silver.repartition(16)

df_silver.write.format("delta") \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .saveAsTable("workspace.default.silver_credit_data")

silver_count = spark.table("workspace.default.silver_credit_data").count()
print(f"✅ ĐÃ LÀM SẠCH VÀ LƯU {silver_count:,} DÒNG VÀO SILVER DELTA TABLE!")

# COMMAND ----------

# MAGIC %md
# MAGIC ### 3. SPARK SQL ANALYTICS & ADVANCED WINDOW FUNCTIONS

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Thống kê tỷ lệ nợ xấu NPL và lãi suất theo Mục đích vay trên quy mô triệu dòng
# MAGIC SELECT 
# MAGIC     loan_intent AS Muc_Dich_Vay,
# MAGIC     COUNT(*) AS Tong_So_Khoan_Vay,
# MAGIC     SUM(loan_status) AS So_Khoan_Vay_Vo_No,
# MAGIC     ROUND(AVG(loan_status) * 100, 2) AS Ty_Le_Vo_No_Pct,
# MAGIC     ROUND(AVG(loan_amnt), 0) AS Khoan_Vay_Trung_Binh,
# MAGIC     ROUND(AVG(loan_int_rate), 2) AS Lai_Suat_Trung_Binh
# MAGIC FROM workspace.default.silver_credit_data
# MAGIC GROUP BY loan_intent
# MAGIC ORDER BY Ty_Le_Vo_No_Pct DESC;

# COMMAND ----------

# Ứng dụng Window Functions phân tích gánh nặng nợ DTI và Xếp hạng thu nhập phân vùng
from pyspark.sql.window import Window
from pyspark.sql.functions import rank, dense_rank

windowSpec = Window.partitionBy("loan_intent").orderBy(col("person_income").desc())

df_kpi = spark.table("workspace.default.silver_credit_data") \
    .withColumn("income_rank_in_intent", dense_rank().over(windowSpec)) \
    .withColumn("debt_to_income_ratio", round(col("loan_amnt") / col("person_income"), 4))

display(df_kpi.select("person_age", "person_income", "loan_intent", "loan_amnt", "debt_to_income_ratio", "income_rank_in_intent").limit(10))

# COMMAND ----------

# MAGIC %md
# MAGIC ### 4. GOLD LAYER - SPARK MLLIB DISTRIBUTED PIPELINE & MODELING

# COMMAND ----------

from pyspark.ml import Pipeline
from pyspark.ml.feature import StringIndexer, OneHotEncoder, VectorAssembler, StandardScaler
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator

# Đọc dữ liệu Silver đã tối ưu
data = spark.table("workspace.default.silver_credit_data")

# Phân chia Train (80%) và Test (20%)
train_data, test_data = data.randomSplit([0.8, 0.2], seed=42)
train_data.cache() # Caching để tăng tốc Cross-Validation trên hàng triệu dòng

# Chuỗi Feature Transformers
cat_cols = ["person_home_ownership", "loan_intent", "cb_person_default_on_file"]
# Thêm loan_grade nếu có
if "loan_grade" in data.columns:
    cat_cols.append("loan_grade")

indexers = [StringIndexer(inputCol=c, outputCol=f"{c}_index", handleInvalid="keep") for c in cat_cols]
encoders = [OneHotEncoder(inputCol=f"{c}_index", outputCol=f"{c}_vec") for c in cat_cols]

num_cols = ["person_age", "person_income", "person_emp_length", "loan_amnt", "loan_int_rate", "loan_percent_income", "cb_person_cred_hist_length"]
feature_cols = [f"{c}_vec" for c in cat_cols] + num_cols

assembler = VectorAssembler(inputCols=feature_cols, outputCol="raw_features", handleInvalid="keep")
scaler = StandardScaler(inputCol="raw_features", outputCol="features", withStd=True, withMean=False)

# Mô hình Rừng cây quyết định phân tán
rf = RandomForestClassifier(labelCol="loan_status", featuresCol="features", numTrees=50, maxDepth=10, seed=42)

pipeline = Pipeline(stages=indexers + encoders + [assembler, scaler, rf])

# Đánh giá bằng ROC-AUC
evaluator = BinaryClassificationEvaluator(labelCol="loan_status", rawPredictionCol="rawPrediction", metricName="areaUnderROC")

print("⏳ Đang huấn luyện mô hình Random Forest phân tán trên dữ liệu lớn...")
model = pipeline.fit(train_data)

# Dự báo trên tập kiểm thử
predictions = model.transform(test_data)
auc = evaluator.evaluate(predictions)

print("=" * 60)
print(f"📊 CHỈ SỐ ROC-AUC ĐẠT ĐƯỢC TRÊN TẬP KIỂM THỬ: {auc:.4f}")
print("=" * 60)

# Ghi kết quả vào Gold Delta Table
predictions.select(
    "person_income", "loan_amnt", "loan_int_rate", "loan_intent",
    "loan_status", "prediction", "probability"
).write.format("delta") \
 .mode("overwrite") \
 .option("overwriteSchema", "true") \
 .saveAsTable("workspace.default.gold_credit_scoring")

print("✅ ĐÃ GHI KẾT QUẢ DỰ BÁO VÀO GOLD DELTA TABLE: gold_credit_scoring")

# COMMAND ----------

# MAGIC %md
# MAGIC ### 5. BUSINESS DECISION ENGINE & RISK-BASED PRICING

# COMMAND ----------

from pyspark.sql.functions import udf
from pyspark.sql.types import DoubleType

# Trích xuất xác suất nợ xấu p
extract_prob = udf(lambda v: float(v[1]), DoubleType())

df_gold = spark.table("workspace.default.gold_credit_scoring") \
    .withColumn("default_probability", extract_prob(col("probability")))

# Quy đổi FICO Score theo hàm Log-Odds chuẩn FICO
import math
def compute_fico(p):
    p_safe = max(min(p, 0.999), 0.001)
    odds = (1.0 - p_safe) / p_safe
    s = 600.0 + (math.log(odds) / math.log(2.0)) * 40.0
    return max(min(round(s), 850.0), 300.0)

fico_udf = udf(compute_fico, DoubleType())

df_decision = df_gold \
    .withColumn("FICO_Score", fico_udf(col("default_probability"))) \
    .withColumn("Risk_Segment",
        when(col("default_probability") < 0.15, "1. Rủi ro Thấp (Low Risk)")
        .when(col("default_probability") < 0.35, "2. Rủi ro Trung Bình (Medium Risk)")
        .when(col("default_probability") < 0.60, "3. Rủi ro Cao (High Risk)")
        .otherwise("4. Rủi ro Rất Cao (Very High Risk)")
    ) \
    .withColumn("Credit_Policy_Decision",
        when(col("Risk_Segment") == "1. Rủi ro Thấp (Low Risk)", "Duyệt Tự Động 100% - Lãi Suất Ưu Đãi (8.5%/năm)")
        .when(col("Risk_Segment") == "2. Rủi ro Trung Bình (Medium Risk)", "Duyệt Hạn Mức Tự Động 70% - Lãi Suất (11.5%/năm)")
        .when(col("Risk_Segment") == "3. Rủi ro Cao (High Risk)", "Thẩm Định Thủ Công - Yêu Cầu Tài Sản Bảo Đảm (14.5%/năm)")
        .otherwise("Từ Chối Cấp Tín Dụng (Auto-Reject)")
    )

display(df_decision.select("person_income", "loan_amnt", "default_probability", "FICO_Score", "Risk_Segment", "Credit_Policy_Decision").limit(10))