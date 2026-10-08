# Databricks notebook source
# MAGIC %md
# MAGIC BRONZE LAYER - INGESTION & DBFS DELTA STORAGE

# COMMAND ----------

# 1. Đọc trực tiếp dữ liệu từ bảng credit_risk_dataset đã lưu
df_raw = spark.table("workspace.default.credit_risk_dataset")
# 2. Hiển thị cấu trúc dữ liệu thô (Schema)
print("--- CẤU TRÚC DỮ LIỆU THÔ ---")
df_raw.printSchema()
# 3. Hiển thị 5 dòng đầu tiên
display(df_raw.limit(5))
# 4. Lưu dữ liệu thô vào Delta Table chuẩn Bronze Layer
df_raw.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("bronze_credit_data")
print("✅ ĐÃ NẠP THÀNH CÔNG DỮ LIỆU VÀO BRONZE DELTA TABLE: bronze_credit_data")

# COMMAND ----------

# MAGIC %md
# MAGIC SILVER LAYER - DISTRIBUTED CLEANING & DATA PREPARATION

# COMMAND ----------

from pyspark.sql.functions import col, when

# 1. Đọc dữ liệu từ Bronze Table
df_bronze = spark.table("bronze_credit_data")

# 2. Làm sạch dữ liệu & Xử lý giá trị bị thiếu (Imputation)
df_silver = df_bronze \
    .filter((col("person_age") >= 18) & (col("person_age") <= 80)) \
    .filter(col("person_income") > 0) \
    .na.fill({
        "person_emp_length": 0,
        "loan_int_rate": 11.0,  # Điền giá trị trung vị lãi suất
        "cb_person_cred_hist_length": 1
    })

# 3. Chuẩn hóa kiểu dữ liệu
df_silver = df_silver \
    .withColumn("person_income", col("person_income").cast("double")) \
    .withColumn("loan_amnt", col("loan_amnt").cast("double")) \
    .withColumn("loan_status", col("loan_status").cast("integer")) # 0: Trả đúng hạn, 1: Nợ xấu

# 4. Lưu vào Silver Delta Table
df_silver.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("silver_credit_data")

print("✅ ĐÃ HOÀN THÀNH LÀM SẠCH VÀ LƯU VÀO SILVER DELTA TABLE: silver_credit_data")
display(df_silver.describe())

# COMMAND ----------

# MAGIC %md
# MAGIC SPARK SQL ANALYTICS & KPIS COMPUTATION

# COMMAND ----------

# MAGIC %sql
# MAGIC -- 1. Thống kê tỷ lệ vỡ nợ (NPL Rate) và Lãi suất trung bình theo mục đích vay
# MAGIC SELECT 
# MAGIC     loan_intent AS Muc_Dich_Vay,
# MAGIC     COUNT(*) AS Tong_So_Khoan_Vay,
# MAGIC     SUM(loan_status) AS So_Khoan_Vay_Vo_No,
# MAGIC     ROUND(AVG(loan_status) * 100, 2) AS Ty_Le_Vo_No_Pct,
# MAGIC     ROUND(AVG(loan_amnt), 0) AS Khoan_Vay_Trung_Binh,
# MAGIC     ROUND(AVG(loan_int_rate), 2) AS Lai_Suat_Trung_Binh
# MAGIC FROM silver_credit_data
# MAGIC GROUP BY loan_intent
# MAGIC ORDER BY Ty_Le_Vo_No_Pct DESC;

# COMMAND ----------

# 2. Ứng dụng Window Functions tính chỉ số DTI và Xếp hạng thu nhập theo nhóm
from pyspark.sql.window import Window
from pyspark.sql.functions import rank, round, col

windowSpec = Window.partitionBy("loan_intent").orderBy(col("person_income").desc())

df_kpi = df_silver \
    .withColumn("income_rank", rank().over(windowSpec)) \
    .withColumn("debt_to_income_ratio", round(col("loan_amnt") / col("person_income"), 4))

display(df_kpi.select("person_age", "person_income", "loan_intent", "loan_amnt", "debt_to_income_ratio", "income_rank").limit(10))

# COMMAND ----------

# MAGIC %md
# MAGIC GOLD LAYER - SPARK MLLIB PIPELINE & CROSS VALIDATION

# COMMAND ----------

import os
os.environ["SPARKML_TEMP_DFS_PATH"] = "/Volumes/workspace/default/sparkml_temp"

from pyspark.ml import Pipeline
from pyspark.ml.feature import StringIndexer, OneHotEncoder, VectorAssembler, StandardScaler
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator

# 1. Đọc dữ liệu từ Silver Table
data = spark.table("silver_credit_data")

# Chia tập dữ liệu Train (80%) và Test (20%)
train_data, test_data = data.randomSplit([0.8, 0.2], seed=42)

# 2. Định nghĩa các công đoạn Feature Engineering
cat_cols = ["person_home_ownership", "loan_intent", "cb_person_default_on_file"]
indexers = [StringIndexer(inputCol=c, outputCol=f"{c}_index", handleInvalid="keep") for c in cat_cols]
encoders = [OneHotEncoder(inputCol=f"{c}_index", outputCol=f"{c}_vec") for c in cat_cols]

num_cols = ["person_age", "person_income", "person_emp_length", "loan_amnt", "loan_int_rate", "loan_percent_income", "cb_person_cred_hist_length"]
feature_cols = [f"{c}_vec" for c in cat_cols] + num_cols

assembler = VectorAssembler(inputCols=feature_cols, outputCol="raw_features")
scaler = StandardScaler(inputCol="raw_features", outputCol="features", withStd=True, withMean=False)

# 3. Thuật toán Học máy Random Forest
rf = RandomForestClassifier(labelCol="loan_status", featuresCol="features", seed=42)

# 4. Đóng gói Pipeline
pipeline = Pipeline(stages=indexers + encoders + [assembler, scaler, rf])

# 5. Thiết lập Lưới tham số (ParamGrid) & CrossValidator
paramGrid = ParamGridBuilder() \
    .addGrid(rf.maxDepth, [5, 10]) \
    .addGrid(rf.numTrees, [20, 50]) \
    .build()

evaluator = BinaryClassificationEvaluator(
    labelCol="loan_status", 
    rawPredictionCol="rawPrediction", 
    metricName="areaUnderROC"
)

cv = CrossValidator(
    estimator=pipeline,
    estimatorParamMaps=paramGrid,
    evaluator=evaluator,
    numFolds=3,
    seed=42
)

# 6. Huấn luyện mô hình phân tán
print("⏳ Đang huấn luyện mô hình Spark MLlib với CrossValidation (vui lòng chờ)...")
cv_model = cv.fit(train_data)

# 7. Dự báo trên tập Test
predictions = cv_model.transform(test_data)

# 8. Đánh giá độ chính xác ROC-AUC
auc = evaluator.evaluate(predictions)
print("==================================================")
print(f"📊 CHỈ SỐ ROC-AUC ĐẠT ĐƯỢC CỦA MÔ HÌNH: {auc:.4f}")
print("==================================================")

# 9. Ghi kết quả vào Gold Delta Table
predictions.select(
    "person_age", "person_income", "loan_amnt", "loan_intent", 
    "loan_status", "prediction", "probability"
).write.format("delta") \
 .mode("overwrite") \
 .saveAsTable("gold_credit_scoring")

print("✅ ĐÃ LƯU BẢNG KẾT QUẢ DỰ BÁO VÀO GOLD DELTA TABLE: gold_credit_scoring")

# COMMAND ----------

# MAGIC %md
# MAGIC BUSINESS INSIGHTS & CREDIT DECISION ENGINE

# COMMAND ----------

from pyspark.sql.functions import udf
from pyspark.sql.types import DoubleType

# UDF lấy xác suất nợ xấu (lớp 1)
extract_prob = udf(lambda v: float(v[1]), DoubleType())

df_gold = spark.table("gold_credit_scoring") \
    .withColumn("default_probability", extract_prob(col("probability")))

# Phân tầng rủi ro & Chính sách phê duyệt vay tự động
df_final_decision = df_gold.withColumn("Risk_Segment", 
    when(col("default_probability") < 0.15, "1. Rủi ro Thấp (Low Risk)")
    .when(col("default_probability") < 0.35, "2. Rủi ro Trung Bình (Medium Risk)")
    .when(col("default_probability") < 0.60, "3. Rủi ro Cao (High Risk)")
    .otherwise("4. Rủi ro Rất Cao (Very High Risk)")
).withColumn("Credit_Policy_Decision",
    when(col("Risk_Segment") == "1. Rủi ro Thấp (Low Risk)", "Duyệt Tự Động - Hạn Mức 100% - Lãi Suất Ưu Đãi (8.5%)")
    .when(col("Risk_Segment") == "2. Rủi ro Trung Bình (Medium Risk)", "Duyệt Tự Động - Hạn Mức 70% - Lãi Suất Thường (11.5%)")
    .when(col("Risk_Segment") == "3. Rủi ro Cao (High Risk)", "Thẩm Định Thủ Công - Yêu Cầu Tài Sản Bảo Đảm")
    .otherwise("Từ Chối Cho Vay (Reject)")
)

display(df_final_decision.select("person_income", "loan_amnt", "default_probability", "Risk_Segment", "Credit_Policy_Decision").limit(10))