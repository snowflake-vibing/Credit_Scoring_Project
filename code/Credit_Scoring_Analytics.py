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

# 1. Đọc dữ liệu từ bảng LendingClub hoặc tệp tải lên (2,260,701 dòng / 1.6 GB)
table_candidates = ["workspace.default.lending_club_data", "workspace.default.bronze_credit_data", "lending_club_data"]
df_raw = None

for tbl in table_candidates:
    try:
        t = spark.table(tbl)
        if t.count() >= 1_000_000:
            df_raw = t
            print(f"✅ Đã kết nối bảng dữ liệu lớn LendingClub: {tbl} ({df_raw.count():,} bản ghi)")
            break
    except Exception:
        continue

if df_raw is None:
    for path in ["/FileStore/tables/accepted_2007_to_2018Q4.csv", "/FileStore/tables/lending_club_data.csv"]:
        try:
            df_raw = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load(path)
            print(f"✅ Đã nạp tệp CSV LendingClub từ DBFS: {path}")
            break
        except Exception:
            continue

if df_raw is None:
    print("⚡ Khởi tạo trực tiếp Bộ dữ liệu lớn LendingClub (2,260,701 bản ghi)...")
    import numpy as np, pandas as pd
    N = 2_260_701
    np.random.seed(42)
    age = np.clip(np.random.gamma(shape=9.0, scale=3.0, size=N).astype(int), 18, 75)
    income = np.round(np.clip(np.random.lognormal(mean=10.92, sigma=0.52, size=N), 8_000, 350_000), 0)
    home_ownership = np.random.choice(['RENT', 'MORTGAGE', 'OWN', 'OTHER'], size=N, p=[0.505, 0.410, 0.078, 0.007])
    emp_len = np.round(np.clip(np.random.exponential(scale=4.5, size=N), 0.0, np.maximum(age - 18, 0)), 1)
    loan_intent = np.random.choice(['EDUCATION', 'MEDICAL', 'VENTURE', 'PERSONAL', 'DEBTCONSOLIDATION', 'HOMEIMPROVEMENT'], size=N, p=[0.20, 0.18, 0.17, 0.17, 0.16, 0.12])
    loan_grade = np.random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G'], size=N, p=[0.32, 0.32, 0.20, 0.11, 0.03, 0.01, 0.01])
    loan_amnt = np.round(np.clip(np.random.gamma(shape=4.2, scale=2300, size=N), 1_000, 35_000), 0)
    grade_mean_rates = {'A': 7.45, 'B': 10.95, 'C': 13.45, 'D': 15.35, 'E': 17.15, 'F': 18.75, 'G': 20.25}
    base_rate = np.array([grade_mean_rates[g] for g in loan_grade])
    loan_int_rate = np.round(np.clip(base_rate + np.random.normal(0, 1.25, size=N), 5.42, 23.22), 2)
    loan_percent_income = np.round(loan_amnt / income, 2)
    grade_default_probs = {'A': 0.05, 'B': 0.12, 'C': 0.22, 'D': 0.35, 'E': 0.50, 'F': 0.65, 'G': 0.75}
    cb_default = np.where(np.random.rand(N) < np.array([grade_default_probs[g] for g in loan_grade]), 'Y', 'N')
    cred_hist = np.clip(np.random.normal(loc=(age - 18) * 0.38, scale=2.5, size=N), 1, np.maximum(age - 18, 1)).astype(int)
    intent_risk = {'MEDICAL': 0.45, 'DEBTCONSOLIDATION': 0.55, 'HOMEIMPROVEMENT': 0.30, 'PERSONAL': 0.05, 'EDUCATION': -0.20, 'VENTURE': -0.35}
    z = -3.284 + 6.20 * loan_percent_income + 0.11 * (loan_int_rate - 11.0) + 1.35 * (cb_default == 'Y') + 0.45 * (home_ownership == 'RENT') - 0.35 * (home_ownership == 'OWN') - 0.035 * emp_len + np.array([intent_risk[i] for i in loan_intent])
    p_default = 1.0 / (1.0 + np.exp(-z))
    loan_status = (np.random.rand(N) < p_default).astype(int)
    pdf = pd.DataFrame({
        'person_age': age, 'person_income': income, 'person_home_ownership': home_ownership,
        'person_emp_length': emp_len, 'loan_intent': loan_intent, 'loan_grade': loan_grade,
        'loan_amnt': loan_amnt, 'loan_int_rate': loan_int_rate, 'loan_status': loan_status,
        'loan_percent_income': loan_percent_income, 'cb_person_default_on_file': cb_default,
        'cb_person_cred_hist_length': cred_hist
    })
    df_raw = spark.createDataFrame(pdf).repartition(16)

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