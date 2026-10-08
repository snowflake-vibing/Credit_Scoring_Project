# HƯỚNG DẪN CHI TIẾT THỰC HIỆN ĐỀ TÀI 7
## MÔ HÌNH CHẤM ĐIỂM TÍN DỤNG VÀ THẨM ĐỊNH RỦI RO VỠ NỢ
**(Loan Default & Credit Scoring)**

---

> **Môn học:** Dữ Liệu Lớn & Trí Tuệ Nhân Tạo Trong Kinh Doanh (Big Data Analytics & AI)  
> **Nền tảng thực thi:** Databricks Community Cloud (PySpark, Spark SQL, Spark MLlib, Delta Lake)  
> **Lĩnh vực:** Tài Chính, Ngân Hàng & FinTech  

---

## MỤC LỤC
1. [Tổng Quan Đề Tài & Bài Toán Kinh Doanh](#1-tổng-quan-đề-tài--bài-toán-kinh-doanh)
2. [Phân Tích Bài Toán Theo Mô Hình 5Vs & Đối Chiếu Quy Chuẩn](#2-phân-tích-bài-toán-theo-mô-hình-5vs--đối-chiếu-quy-chuẩn)
3. [Kiến Trúc Luồng Dữ Liệu Lakehouse (Medallion Architecture)](#3-kiến-trúc-luồng-dữ-liệu-lakehouse-medallion-architecture)
4. [Hướng Dẫn Triển Khai 5 Bước Trên Databricks (Kèm Code Mẫu)](#4-hướng-dẫn-triển-khai-5-bước-trên-databricks-kèm-code-mẫu)
   - [Bước 1: Nạp & Lưu Trữ Dữ Liệu Thô (Bronze Layer)](#bước-1-nạp--lưu-trữ-dữ-liệu-thô-bronze-layer)
   - [Bước 2: Làm Sạch & Chuẩn Hóa Dữ Liệu (Silver Layer)](#bước-2-làm-sạch--chuẩn-hóa-dữ-liệu-silver-layer)
   - [Bước 3: Phân Tích Khám Phá & Chỉ Số Kinh Doanh (Spark SQL)](#bước-3-phân-tích-khám-phá--chỉ-số-kinh-doanh-spark-sql)
   - [Bước 4: Xây Dựng AI Machine Learning Pipeline Phân Tán (Gold Layer)](#bước-4-xây-dựng-ai-machine-learning-pipeline-phân-tán-gold-layer)
   - [Bước 5: Phân Tích Ý Nghĩa Nghiệp Vụ & Đề Xuất Chiến Lược Quản Trị](#bước-5-phân-tích-ý-nghĩa-nghiệp-vụ--đề-xuất-chiến-lược-quản-trị)
5. [Quy Chuẩn Bàn Giao & Tiêu Chí Đánh Giá (Rubric)](#5-quy-chuẩn-bàn-giao--tiêu-chí-đánh-giá-rubric)

---

## 1. TỔNG QUAN ĐỀ TÀI & BÀI TOÁN KINH DOANH

### 1.1. Bối cảnh nghiệp vụ
Trong lĩnh vực ngân hàng và tài chính tiêu dùng, việc cấp tín dụng cho khách hàng cá nhân luôn đi kèm với rủi ro vỡ nợ (Loan Default / Non-Performing Loan - NPL). Quy trình thẩm định thủ công thường mất nhiều thời gian, mang tính cảm quan và khó mở rộng khi số lượng hồ sơ gia tăng hàng ngày.

### 1.2. Mục tiêu dự án
- **Tự động hóa:** Xây dựng luồng xử lý và dự báo rủi ro tự động hóa 100% dựa trên Machine Learning phân tán với Apache Spark.
- **Tối ưu tỷ lệ nợ xấu (NPL):** Nhận diện sớm các hồ sơ có nguy cơ vỡ nợ cao để từ chối hoặc yêu cầu bổ sung tài sản đảm bảo.
- **Phân tầng rủi ro & Định giá theo rủi ro (Risk-Based Pricing):** Xếp hạng credit score cho từng khách hàng, từ đó quyết định **hạn mức tín dụng** và **lãi suất vay** tương ứng.

### 1.3. Bộ dữ liệu gợi ý (Dataset)
- **Home Credit Default Risk** (Kaggle) hoặc **Lending Club Loan Data** (Kaggle).
- Dữ liệu chứa thông tin:
  - *Nhân khẩu học:* Tuổi, giới tính, học vấn, tình trạng hôn nhân, số người phụ thuộc.
  - *Tài chính:* Thu nhập hàng tháng, tổng dư nợ hiện tại, giá trị tài sản thế chấp.
  - *Lịch sử tín dụng:* Số lần chậm trả nợ, số khoản vay hiện hữu, điểm tín dụng cũ.
  - *Biến mục tiêu (`TARGET` / `loan_status`):* `0` (Trả nợ đúng hạn), `1` (Vỡ nợ / Chậm trả > 90 ngày).

---

## 2. PHÂN TÍCH BÀI TOÁN THEO MÔ HÌNH 5Vs & ĐỐI CHIẾU QUY CHUẨN

### 2.1. Phân tích đặc tính Dữ liệu lớn (5Vs Mindset)
1. **Volume (Dung lượng):** Hàng triệu bản ghi giao dịch và lịch sử tín dụng từ nhiều hệ thống lõi (Core Banking, CRM).
2. **Velocity (Tốc độ):** Đánh giá điểm tín dụng tức thì ngay khi khách hàng nộp hồ sơ trực tuyến trên mobile banking.
3. **Variety (Đa dạng):** Dữ liệu bảng (tabular), dữ liệu chuỗi thời gian lịch sử thanh toán, dữ liệu danh mục phi cấu trúc/bán cấu trúc.
4. **Veracity (Độ tin cậy):** Xử lý triệt để dữ liệu thiếu (missing values), dữ liệu nhiễu và các hành vi khai báo không chính xác.
5. **Value (Giá trị kinh doanh):** Giảm thiểu chi phí trích lập dự phòng nợ xấu, tối đa hóa doanh thu từ lãi vay, cải thiện trải nghiệm duyệt vay nhanh.

### 2.2. Bảng đối chiếu quy chuẩn thực hiện Tiểu luận

| Tiêu chí | Cách làm CHƯA ĐẠT | Cách làm CHUẨN DATABRICKS BIG DATA |
| :--- | :--- | :--- |
| **Môi trường** | Chạy Jupyter Notebook rời rạc trên máy cá nhân | Thực thi trên **Databricks Community Cloud** |
| **Lưu trữ dữ liệu** | Đọc file `.csv` cục bộ từ ổ cứng | Lưu trữ tập trung trên **DBFS & Delta Lake** (Bronze/Silver/Gold) |
| **Công cụ xử lý** | Dùng thư viện `pandas` (RAM máy đơn) | Dùng **PySpark DataFrame** (`spark.read`) và **Spark SQL** |
| **Thuật toán ML** | Dùng `scikit-learn` đơn luồng | Dùng **Spark MLlib (`pyspark.ml`) Pipeline phân tán** |
| **Trực quan hóa** | Chụp ảnh màn hình thủ công | Dùng **Databricks Dashboards / Built-in Visualizations** |
| **Tư duy kết quả** | Chỉ báo cáo độ chính xác kỹ thuật (`Accuracy`) | Phân tích **tác động tài chính, chỉ số ROI, chi phí NPL & chiến lược quản trị** |

---

## 3. KIẾN TRÚC LUỒNG DỮ LIỆU LAKEHOUSE (MEDALLION ARCHITECTURE)

Dữ liệu được tổ chức theo 3 tầng chuẩn Lakehouse:

```
[ Nguồn Dữ Liệu Thô (CSV / JSON / Kaggle Dataset) ]
                       │
                       ▼
[ TẦNG BRONZE (Delta Table: bronze_credit_data) ]
- Lưu trữ dữ liệu thô nguyên bản trên DBFS
                       │
                       ▼ (PySpark DataFrame & Spark SQL Cleaning)
[ TẦNG SILVER (Delta Table: silver_credit_data) ]
- Xử lý missing values, làm sạch, trích xuất đặc trưng
- Tính toán KPIs tài chính & phân tích khám phá
                       │
                       ▼ (Spark MLlib Pipeline & CrossValidator)
[ TẦNG GOLD (Delta Table: gold_credit_scoring) ]
- Kết quả phân loại rủi ro (Risk Score, Prediction, Probability)
- Phân tầng hạn mức tín dụng & lãi suất vay
                       │
                       ▼
[ BUSINESS INSIGHTS & DASHBOARD QUẢN TRỊ ]
- Đề xuất chính sách duyệt vay & chiến lược kiểm soát nợ xấu
```

---

## 4. HƯỚNG DẪN TRIỂN KHAI 5 BƯỚC TRÊN DATABRICKS (KÈM CODE MẪU)

### Bước 1: Nạp & Lưu Trữ Dữ Liệu Thô (Bronze Layer)
- **Thao tác trên Databricks GUI:** `Catalog` $\rightarrow$ `Create Table` $\rightarrow$ `Upload Files` tải file `.csv` lên đường dẫn `dbfs:/FileStore/tables/`.
- **Thực thi bằng PySpark:** Đọc file CSV và lưu thành Delta Table chuẩn **Bronze Layer**.

```python
# ---------------------------------------------------------
# BƯỚC 1: BRONZE LAYER - INGESTION & DBFS STORAGE
# ---------------------------------------------------------
from pyspark.sql import SparkSession

# 1. Đọc dữ liệu thô từ DBFS
raw_data_path = "dbfs:/FileStore/tables/credit_risk_dataset.csv"

df_raw = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load(raw_data_path)

# Hiển thị cấu trúc dữ liệu thô
df_raw.printSchema()
display(df_raw.limit(5))

# 2. Lưu trữ vào bảng Bronze Delta Table
df_raw.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("bronze_credit_data")

print("-> Đã nạp thành công dữ liệu vào bảng Delta Bronze: bronze_credit_data")
```

---

### Bước 2: Làm Sạch & Chuẩn Hóa Dữ Liệu (Silver Layer)
Thực hiện các thao tác xử lý chất lượng dữ liệu:
1. Đọc dữ liệu từ `bronze_credit_data`.
2. Xử lý giá trị bị thiếu (`fillna`, `dropna`).
3. Lọc ngoại lai phi thực tế (ví dụ: tuổi < 18 hoặc thu nhập < 0).
4. Lưu dữ liệu sạch vào bảng `silver_credit_data`.

```python
# ---------------------------------------------------------
# BƯỚC 2: SILVER LAYER - DISTRIBUTED CLEANING & PREPROCESSING
# ---------------------------------------------------------
from pyspark.sql.functions import col, when

# 1. Đọc từ bảng Bronze
df_bronze = spark.table("bronze_credit_data")

# 2. Xử lý giá trị bị thiếu & lọc dữ liệu không hợp lệ
df_silver = df_bronze \
    .filter((col("person_age") >= 18) & (col("person_age") <= 80)) \
    .filter(col("person_income") > 0) \
    .na.fill({
        "person_emp_length": 0,
        "loan_int_rate": 11.0, # Điền giá trị trung vị/trung bình phù hợp
        "cb_person_cred_hist_length": 1
    })

# 3. Ép kiểu dữ liệu chuẩn (nếu cần)
df_silver = df_silver \
    .withColumn("person_income", col("person_income").cast("double")) \
    .withColumn("loan_amnt", col("loan_amnt").cast("double")) \
    .withColumn("loan_status", col("loan_status").cast("integer")) # 0: Trả đúng hạn, 1: Vỡ nợ

# 4. Lưu vào bảng Silver Delta Table
df_silver.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("silver_credit_data")

print("-> Đã làm sạch và ghi vào bảng Delta Silver: silver_credit_data")
```

---

### Bước 3: Phân Tích Khám Phá & Chỉ Số Kinh Doanh (Spark SQL)
Sử dụng **Spark SQL** và các hàm **Window Functions** để tính toán KPIs:
- Tỷ lệ vỡ nợ (NPL Rate) theo mục đích vay.
- Thu nhập trung bình và tỷ lệ nợ trên thu nhập (Debt-to-Income / Loan-to-Income).
- Xếp hạng nhóm khách hàng theo thu nhập.

```sql
-- ---------------------------------------------------------
-- BƯỚC 3: SPARK SQL ANALYTICS & KPIS COMPUTATION
-- ---------------------------------------------------------

-- 1. Thống kê tỷ lệ nợ xấu (NPL Rate) theo mục đích vay
SELECT 
    loan_intent AS Muc_Dich_Vay,
    COUNT(*) AS Tong_So_Khoan_Vay,
    SUM(loan_status) AS So_Khoan_Vay_Vo_No,
    ROUND(AVG(loan_status) * 100, 2) AS Ty_Le_Vo_No_Pct,
    ROUND(AVG(loan_amnt), 0) AS Khoan_Vay_Trung_Binh,
    ROUND(AVG(loan_int_rate), 2) AS Lai_Suat_Trung_Binh
FROM silver_credit_data
GROUP BY loan_intent
ORDER BY Ty_Le_Vo_No_Pct DESC;
```

```python
# 2. Ứng dụng Window Functions tính xếp hạng thu nhập & tỷ lệ nợ/thu nhập trong PySpark
from pyspark.sql.window import Window
from pyspark.sql.functions import rank, round, col

windowSpec = Window.partitionBy("loan_intent").orderBy(col("person_income").desc())

df_kpi = df_silver.withColumn("income_rank", rank().over(windowSpec)) \
    .withColumn("loan_to_income_ratio", round(col("loan_amnt") / col("person_income"), 4))

display(df_kpi.select("person_age", "person_income", "loan_intent", "loan_amnt", "loan_to_income_ratio", "income_rank").limit(10))
```

*Mẹo Trực quan hóa:* Sử dụng nút **+ (Visualization)** trên Notebook Databricks để vẽ biểu đồ cột (Bar chart) so sánh **Tỷ lệ vỡ nợ theo mục đích vay** hoặc biểu đồ hộp (Box plot) thể hiện **Tỷ lệ nợ/Thu nhập**.

---

### Bước 4: Xây Dựng AI Machine Learning Pipeline Phân Tán (Gold Layer)
Xây dựng mô hình dự báo rủi ro vỡ nợ bằng **Spark MLlib Pipeline**:
1. **Feature Engineering:** 
   - `StringIndexer` biến đổi các cột chuỗi (giới tính, mục đích vay, loại nhà ở).
   - `OneHotEncoder` mã hóa đa danh mục.
   - `VectorAssembler` gom tất cả biến đặc trưng thành 1 cột `features`.
   - `StandardScaler` chuẩn hóa thang đo dữ liệu.
2. **Huấn luyện & Tinh chỉnh siêu tham số:** 
   - Thuật toán: `LogisticRegression` và `DecisionTreeClassifier` / `RandomForestClassifier`.
   - `CrossValidator` với `ParamGridBuilder` để tìm tham số tối ưu.
3. **Đánh giá mô hình:** `BinaryClassificationEvaluator` (ROC-AUC & PR-AUC).
4. **Lưu trữ kết quả (Gold Layer):** Lưu bảng dự báo `gold_credit_scoring`.

```python
# ---------------------------------------------------------
# BƯỚC 4: SPARK MLLIB PIPELINE & CROSS-VALIDATION (GOLD LAYER)
# ---------------------------------------------------------
from pyspark.ml import Pipeline
from pyspark.ml.feature import StringIndexer, OneHotEncoder, VectorAssembler, StandardScaler
from pyspark.ml.classification import LogisticRegression, RandomForestClassifier
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator

# 1. Đọc dữ liệu từ Silver Table
data = spark.table("silver_credit_data")

# Chia tập Train/Test (80/20)
train_data, test_data = data.randomSplit([0.8, 0.2], seed=42)

# 2. Định nghĩa các công đoạn Feature Engineering
cat_cols = ["person_home_ownership", "loan_intent", "cb_person_default_on_file"]
indexers = [StringIndexer(inputCol=c, outputCol=f"{c}_index", handleInvalid="keep") for c in cat_cols]
encoders = [OneHotEncoder(inputCol=f"{c}_index", outputCol=f"{c}_vec") for c in cat_cols]

num_cols = ["person_age", "person_income", "person_emp_length", "loan_amnt", "loan_int_rate", "loan_percent_income", "cb_person_cred_hist_length"]
feature_cols = [f"{c}_vec" for c in cat_cols] + num_cols

assembler = VectorAssembler(inputCols=feature_cols, outputCol="raw_features")
scaler = StandardScaler(inputCol="raw_features", outputCol="features", withStd=True, withMean=False)

# 3. Khởi tạo Mô hình Machine Learning (Random Forest Classifier)
rf = RandomForestClassifier(labelCol="loan_status", featuresCol="features", seed=42)

# 4. Đóng gói chuỗi Pipeline
pipeline = Pipeline(stages=indexers + encoders + [assembler, scaler, rf])

# 5. Tinh chỉnh siêu tham số với CrossValidator
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

# 6. Huấn luyện mô hình
print("Đang huấn luyện mô hình MLlib Pipeline với CrossValidation...")
cv_model = cv.fit(train_data)

# 7. Dự báo trên tập kiểm thử Test Data
predictions = cv_model.transform(test_data)

# 8. Đánh giá độ chính xác mô hình
auc = evaluator.evaluate(predictions)
print(f"==========================================")
print(f"KẾT QUẢ ĐÁNH GIÁ MÔ HÌNH (ROC-AUC): {auc:.4f}")
print(f"==========================================")

# 9. Ghi kết quả dự báo vào bảng Gold Delta Table
predictions.select(
    "person_age", "person_income", "loan_amnt", "loan_intent", 
    "loan_status", "prediction", "probability"
).write.format("delta") \
 .mode("overwrite") \
 .saveAsTable("gold_credit_scoring")

print("-> Đã lưu bảng kết quả phân loại rủi ro tín dụng vào Gold Table: gold_credit_scoring")
```

---

### Bước 5: Phân Tích Ý Nghĩa Nghiệp Vụ & Đề Xuất Chiến Lược Quản Trị

#### 5.1. Phân tầng rủi ro & Xác định Hạn mức Tín dụng / Lãi suất
Dựa vào xác suất vỡ nợ (`probability`) trả về từ mô hình Gold Table, xây dựng quy tắc phân tầng khách hàng:

```python
from pyspark.sql.functions import udf
from pyspark.sql.types import DoubleType, StringType

# UDF trích xuất xác suất nợ xấu (lớp 1)
extract_prob_udf = udf(lambda v: float(v[1]), DoubleType())

df_gold = spark.table("gold_credit_scoring") \
    .withColumn("default_probability", extract_prob_udf(col("probability")))

# Phân tầng rủi ro và khuyến nghị chính sách tín dụng
df_policy = df_gold.withColumn("Risk_Segment", 
    when(col("default_probability") < 0.15, "1. Rủi ro Thấp (Low Risk)")
    .when(col("default_probability") < 0.35, "2. Rủi ro Trung Bình (Medium Risk)")
    .when(col("default_probability") < 0.60, "3. Rủi ro Cao (High Risk)")
    .otherwise("4. Rủi ro Rất Cao (Very High Risk)")
).withColumn("Credit_Decision",
    when(col("Risk_Segment") == "1. Rủi ro Thấp (Low Risk)", "Duyệt tự động - Hạn mức 100% - Lãi suất Ưu đãi (8-10%)")
    .when(col("Risk_Segment") == "2. Rủi ro Trung Bình (Medium Risk)", "Duyệt tự động - Hạn mức 70% - Lãi suất Thường (11-13%)")
    .when(col("Risk_Segment") == "3. Rủi ro Cao (High Risk)", "Thẩm định thủ công - Yêu cầu bảo lãnh - Lãi suất Cao (14-16%)")
    .otherwise("Từ chối cho vay (Reject)")
)

display(df_policy.select("person_income", "loan_amnt", "default_probability", "Risk_Segment", "Credit_Decision").limit(10))
```

#### 5.2. Đánh giá tác động tài chính & ROI cho Ngân hàng / Công ty Tài chính
1. **Giảm thiểu tỷ lệ nợ xấu (NPL Reduction):**
   - Loại bỏ hơn 80% hồ sơ nợ xấu ở nhóm *Rủi ro Rất Cao*, giúp giảm tỷ lệ NPL tổng thể từ 20% xuống dưới 4-5%.
2. **Tiết kiệm chi phí trích lập dự phòng:**
   - Việc phát hiện sớm giúp ngân hàng giảm hàng chục tỷ đồng tiền trích lập dự phòng rủi ro tín dụng hàng năm.
3. **Tối ưu hóa quy trình phê duyệt:**
   - Phê duyệt tự động (Auto-approval) cho 60-70% hồ sơ rủi ro thấp/trung bình, giảm thời gian xử lý từ 2 ngày xuống **dưới 5 phút**.

---

## 5. QUY CHUẨN BÀN GIAO & TIÊU CHÍ ĐÁNH GIÁ (RUBRIC)

### 5.1. Bộ sản phẩm bàn giao bắt buộc (Deliverables)
1. **Báo cáo tiểu luận hoàn chỉnh (File PDF):** Trình bày đầy đủ bài toán kinh doanh, phân tích 5Vs, kiến trúc Databricks Lakehouse, giải thích mô hình MLlib và các khuyến nghị quản trị.
2. **File Notebook Databricks (`.ipynb` hoặc `.dbc`):** Chứa toàn bộ mã nguồn PySpark, Spark SQL, Spark MLlib Pipeline và các biểu đồ trực quan hóa.
3. **Slide trình bày (File PDF / PPTX):** Tóm tắt các kết quả cốt lõi phục vụ bảo vệ đề tài trước hội đồng.

### 5.2. Rubric đánh giá chi tiết (Thang điểm 100%)

| STT | Tiêu chí đánh giá | Tỷ trọng | Yêu cầu đạt mức Tốt - Xuất sắc |
| :---: | :--- | :---: | :--- |
| **1** | **Ý nghĩa Nghiệp vụ & Đặt vấn đề** | **15%** | Nêu bật bài toán kinh doanh thực tế, phân tích đầy đủ đặc tính Dữ liệu lớn theo mô hình **5Vs**. |
| **2** | **Quản trị & Lưu trữ Dữ liệu trên Databricks** | **20%** | Nạp dữ liệu vào DBFS chuẩn xác; tổ chức dữ liệu theo đúng mô hình **Medallion (Bronze / Silver / Gold)** dạng **Delta Lake**. |
| **3** | **Xử lý & Phân tích Dữ liệu lớn (PySpark & SQL)** | **25%** | Sử dụng thành thạo PySpark DataFrame & Spark SQL; làm sạch, xử lý thiếu, Feature Engineering tối ưu. |
| **4** | **Mô hình hóa AI (Spark MLlib Pipeline)** | **25%** | Xây dựng hoàn chỉnh Machine Learning Pipeline phân tán; tinh chỉnh siêu tham số bằng **CrossValidator**; đánh giá mô hình đa chỉ số (ROC-AUC, PR-AUC). |
| **5** | **Báo cáo & Khuyến nghị Kinh doanh** | **15%** | Báo cáo trình bày mạch lạc, trực quan hóa biểu đồ trên Databricks; đưa ra đề xuất tác động tài chính & chiến lược quản trị thực tế. |

---
*Chúc các bạn hoàn thành xuất sắc Mini-Project Tiểu Luận Cuối Khóa!*
