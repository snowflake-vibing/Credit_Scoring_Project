# HƯỚNG DẪN CHI TIẾT TỪ A ĐẾN Z THỰC HIỆN ĐỀ TÀI TIỂU LUẬN TRÊN DATABRICKS COMMUNITY EDITION
## Đề Tài 7: Mô Hình Chấm Điểm Tín Dụng & Thẩm Định Rủi Ro Vỡ Nợ (Credit Scoring & Loan Default Prediction)

---

> **Dành cho:** Sinh viên học phần *Dữ Liệu Lớn & Trí Tuệ Nhân Tạo Trong Kinh Doanh*  
> **Môi trường:** Databricks Community Cloud (Miễn phí 100%)  
> **Ngôn ngữ & Công nghệ:** PySpark, Spark SQL, Spark MLlib, Delta Lake, DBFS Storage  

---

## MỤC LỤC
1. [Phần 1: Đăng ký & Khởi tạo Môi trường Databricks Community Edition](#phần-1-đăng-ký--khởi-tạo-môi-trường-databricks-community-edition)
2. [Phần 2: Tải & Upload Dữ Liệu Lên Hệ Thống Tệp DBFS](#phần-2-tải--upload-dữ-liệu-lên-hệ-thống-tệp-dbfs)
3. [Phần 3: Tạo Notebook & Khởi Động Cụm Máy Chủ (Cluster)](#phần-3-tạo-notebook--khởi-động-cụm-máy-chủ-cluster)
4. [Phần 4: Mã Nguồn PySpark & Spark SQL Chi Tiết Theo 5 Bước Medallion (Copy-Paste)](#phần-4-mã-nguồn-pyspark--spark-sql-chi-tiết-theo-5-bước-medallion-copy-paste)
   - [Cell 1: Nạp & Lưu Trữ Dữ Liệu Thô (Bronze Layer)](#cell-1-nạp--lưu-trữ-dữ-liệu-thô-bronze-layer)
   - [Cell 2: Làm Sạch & Chuẩn Hóa Dữ Liệu (Silver Layer)](#cell-2-làm-sạch--chuẩn-hóa-dữ-liệu-silver-layer)
   - [Cell 3: Phân Tích Khám Phá & Chỉ Số Kinh Doanh (Spark SQL Analytics)](#cell-3-phân-tích-khám-phá--chỉ-số-kinh-doanh-spark-sql-analytics)
   - [Cell 4: Xây Dựng AI Machine Learning Pipeline (Gold Layer)](#cell-4-xây-dựng-ai-machine-learning-pipeline-gold-layer)
   - [Cell 5: Đề Xuất Chiến Lược Quản Trị & Tự Động Phê Duyệt Tín Dụng](#cell-5-đề-xuất-chiến-lược-quản-trị--tự-động-phê-duyệt-tín-dụng)
5. [Phần 5: Hướng Dẫn Trực Quan Hóa (Built-in Visualizations) & Làm Dashboard](#phần-5-hướng-dẫn-trực-quan-hóa-built-in-visualizations--làm-dashboard)
6. [Phần 6: Xuất File Nộp Bài (Bàn Giao Báo Cáo & Notebook .ipynb/.dbc)](#phần-6-xuất-file-nộp-bài-bàn-giao-báo-cáo--notebook-ipynbdbc)
7. [Các Lỗi Thường Gặp & Cách Khắc Phục (Troubleshooting)](#các-lỗi-thường-gặp--cách-khắc-phục-troubleshooting)

---

## PHẦN 1: ĐĂNG KÝ & KHỦY TẠO MÔI TRƯỜNG DATABRICKS COMMUNITY EDITION

### 1.1. Đăng ký tài khoản Databricks miễn phí
1. Truy cập trang web chính thức: [https://community.cloud.databricks.com/](https://community.cloud.databricks.com/)
2. Điền thông tin cá nhân (Họ tên, Email sinh viên/cá nhân, Công ty/Trường học).
3. **LƯU Ý QUAN TRỌNG:** Ở bước chọn nhà cung cấp đám mây (AWS / Azure / GCP), nhấn vào đường link nhỏ phía dưới có chữ: **"Get started with Community Edition"** (hoặc chọn gói Miễn phí dành cho cá nhân/nghiên cứu). *Không điền thông tin thẻ tín dụng/Visa.*
4. Kiểm tra Email để xác nhận tài khoản và thiết lập mật khẩu đăng nhập.

---

### 1.2. Tạo cụm máy chủ xử lý dữ liệu (Cluster)
Databricks Community cho phép bạn dùng 1 cụm máy chủ miễn phí (Single Node ~15GB RAM).
1. Sau khi đăng nhập, ở menu bên trái chọn **Compute** (Biểu tượng máy chủ).
2. Nhấn nút **Create Cluster** (hoặc **Create with UI**).
3. Cấu hình thông số Cluster như sau:
   * **Cluster Name:** `Credit-Analytics-Cluster` (hoặc tên tùy chọn).
   * **Cluster Mode:** `Single Node` (Tự động chọn).
   * **Databricks Runtime Version:** Chọn bản LTS mới nhất, ví dụ `Runtime 13.3 LTS (Scala 2.12, Spark 3.4.1)` hoặc `14.3 LTS`.
4. Nhấn nút **Create Cluster**. Chờ khoảng 2 - 4 phút để cụm khởi động (Khi có biểu tượng hình tròn màu xanh lá cây `🟢 Running` là cluster đã sẵn sàng).

> ⚠️ **Lưu ý:** Trên bản Community Cloud, Cluster sẽ tự động dừng (Auto-terminate) sau 2 tiếng không hoạt động để tiết kiệm tài nguyên. Nếu bị dừng, bạn chỉ cần nhấn nút **Start** để bật lại.

---

## PHẦN 2: TẢI & UPLOAD DỮ LIỆU LÊN HỆ THỐNG TỆP DBFS

### 2.1. Tải bộ dữ liệu mẫu về máy tính
* Tải bộ dữ liệu Credit Risk từ Kaggle: [Credit Risk Dataset (Kaggle)](https://www.kaggle.com/datasets/laotse/credit-risk-dataset)
* Bạn sẽ nhận được file `credit_risk_dataset.csv`.

---

### 2.2. Upload dữ liệu lên hệ thống tệp Databricks (DBFS Storage)
1. Trên giao diện Databricks, ở thanh công cụ bên trái nhấn **Catalog** (hoặc nút **Data** / **+ New** $\rightarrow$ **Add or upload data**).
2. Chọn mục **Create or upload a table**.
3. Kéo thả file `credit_risk_dataset.csv` từ máy tính vào ô upload.
4. Đường dẫn lưu file thô trên hệ thống tệp DBFS sẽ có dạng:
   ```text
   dbfs:/FileStore/tables/credit_risk_dataset.csv
   ```
5. Đơn giản nhất, bạn **không cần nhấn Create Table UI**, chỉ cần ghi nhớ đường dẫn `dbfs:/FileStore/tables/credit_risk_dataset.csv` để nạp dữ liệu bằng PySpark code ở Phần 4.

---

## PHẦN 3: TẠO NOTEBOOK & KHỞI ĐỘNG CỤM MÁY CHỦ

1. Ở menu bên trái, nhấn **+ New** $\rightarrow$ Chọn **Notebook**.
2. Đặt tên Notebook: `De_Tai_7_Credit_Scoring_Databricks`.
3. Chọn ngôn ngữ mặc định (**Default Language**): `Python`.
4. Ở phần **Cluster**, chọn cụm máy chủ `Credit-Analytics-Cluster` mà bạn đã tạo ở Phần 1.
5. Nhấn **Create**.

---

## PHẦN 4: MÃ NGUỒN PYSPARK & SPARK SQL CHI TIẾT THEO 5 BƯỚC MEDALLION (COPY-PASTE)

Tạo lần lượt từng **Cell** trong Notebook và Copy-Paste các đoạn mã dưới đây vào để chạy.

---

### Cell 1: Nạp & Lưu Trữ Dữ Liệu Thô (Bronze Layer)
* **Nhiệm vụ:** Đọc dữ liệu CSV từ DBFS và lưu thành Delta Table thô nguyên bản (`bronze_credit_data`).

```python
# =========================================================
# CELL 1: BRONZE LAYER - INGESTION & DELTA STORAGE
# =========================================================
from pyspark.sql import SparkSession

# Đọc trực tiếp từ Bảng Managed Table mà Databricks đã lưu khi upload GUI
df_raw = spark.table("workspace.default.credit_risk_dataset")

print("--- CẤU TRÚC DỮ LIỆU THÔ (RAW SCHEMA) ---")
df_raw.printSchema()

# Hiển thị 5 dòng đầu tiên
display(df_raw.limit(5))

# Lưu dữ liệu thô vào Delta Table chuẩn Bronze Layer
df_raw.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("bronze_credit_data")

print("✅ ĐÃ NẠP THÀNH CÔNG DỮ LIỆU VÀO BRONZE DELTA TABLE: bronze_credit_data")
```

---

### Cell 2: Làm Sạch & Chuẩn Hóa Dữ Liệu (Silver Layer)
* **Nhiệm vụ:** Xử lý giá trị thiếu (`fillna`), loại bỏ ngoại lai phi thực tế, chuyển đổi kiểu dữ liệu và lưu vào `silver_credit_data`.

```python
# =========================================================
# CELL 2: SILVER LAYER - DISTRIBUTED CLEANING & DATA PREPARATION
# =========================================================
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
```

---

### Cell 3: Phân Tích Khám Phá & Chỉ Số Kinh Doanh (Spark SQL Analytics)
* **Nhiệm vụ:** Sử dụng Spark SQL và Window Functions để phân tích tỷ lệ nợ xấu (NPL Rate), DTI (Debt-to-Income) và xếp hạng thu nhập.

*Tạo một Cell mới và đổi ngôn ngữ cell thành `%sql` bằng cách gõ `%sql` ở dòng đầu tiên:*

```sql
-- =========================================================
-- CELL 3: SPARK SQL ANALYTICS & KPIS COMPUTATION
-- =========================================================

-- 1. Thống kê tỷ lệ vỡ nợ (NPL Rate) và Lãi suất trung bình theo mục đích vay
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

*Tạo thêm một Cell Python để chạy Window Function:*

```python
# 2. Ứng dụng Window Functions tính chỉ số DTI và Xếp hạng thu nhập theo nhóm
from pyspark.sql.window import Window
from pyspark.sql.functions import rank, round, col

windowSpec = Window.partitionBy("loan_intent").orderBy(col("person_income").desc())

df_kpi = df_silver \
    .withColumn("income_rank", rank().over(windowSpec)) \
    .withColumn("debt_to_income_ratio", round(col("loan_amnt") / col("person_income"), 4))

display(df_kpi.select("person_age", "person_income", "loan_intent", "loan_amnt", "debt_to_income_ratio", "income_rank").limit(10))
```

---

### Cell 4: Xây Dựng AI Machine Learning Pipeline (Gold Layer)
* **Nhiệm vụ:** Sử dụng **Spark MLlib** đóng gói chuỗi Pipeline (`StringIndexer`, `OneHotEncoder`, `VectorAssembler`, `StandardScaler`, `RandomForestClassifier`), tinh chỉnh siêu tham số với `CrossValidator` và lưu kết quả dự báo vào `gold_credit_scoring`.

```python
# =========================================================
# CELL 4: GOLD LAYER - SPARK MLLIB PIPELINE & CROSS VALIDATION
# =========================================================
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
```

---

### Cell 5: Đề Xuất Chiến Lược Quản Trị & Tự Động Phê Duyệt Tín Dụng
* **Nhiệm vụ:** Trích xuất xác suất nợ xấu, quy đổi thành Phân tầng Rủi ro, Quyết định Duyệt vay và Đánh giá tác động tài chính.

```python
# =========================================================
# CELL 5: BUSINESS INSIGHTS & CREDIT DECISION ENGINE
# =========================================================
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
```

---

## PHẦN 5: HƯỚNG DẪN TRỰC QUAN HÓA (BUILT-IN VISUALIZATIONS) & LÀM DASHBOARD

Databricks có công cụ vẽ biểu đồ cực kỳ mạnh mẽ tích hợp sẵn trong kết quả chạy của từng Cell.

### 5.1. Tạo biểu đồ cột (Bar Chart) Tỷ lệ vỡ nợ theo mục đích vay
1. Ở kết quả hiển thị của **Cell 3 (SQL Analytics)**, nhấn vào dấu **+** ở góc trên bảng kết quả $\rightarrow$ Chọn **Visualization**.
2. Chọn **Visualization Type:** `Bar` (Biểu đồ cột).
3. Cấu hình các trục:
   * **X Column:** `Muc_Dich_Vay`
   * **Y Column:** `Ty_Le_Vo_No_Pct` (Chọn phép tính `AVG` hoặc `SUM`).
4. Nhấn **Save**. Biểu đồ sẽ hiển thị ngay dưới Cell!

---

### 5.2. Chuyển kết quả thành Databricks Dashboard
1. Ở thanh menu trên cùng của Notebook, nhấn vào nút **View Mode** $\rightarrow$ Chọn **Dashboard** (hoặc nút **Dashboards** $\rightarrow$ **Create New Dashboard**).
2. Tích chọn các Biểu đồ và Bảng kết quả ở các Cell 3, Cell 4, Cell 5.
3. Nhấn **Done Editing**. Bạn đã có một Dashboard chuyên nghiệp để chụp ảnh đưa vào Slide trình bày!

---

## PHẦN 6: XUẤT FILE NỘP BÀI (BÀN GIAO BÁO CÁO & NOTEBOOK .IPYNB/.DBC)

Theo quy định sản phẩm bàn giao tiểu luận cuối khóa, bạn cần xuất các file sau từ Databricks:

1. **Xuất file mã nguồn Notebook `.ipynb` hoặc `.dbc`:**
   * Trên thanh menu Notebook của Databricks, chọn `File` $\rightarrow$ `Export` $\rightarrow$ `IPython Notebook (.ipynb)` (hoặc `Databricks Archive (.dbc)`).
   * File này sẽ được nộp đính kèm bài làm để giảng viên chấm code.

2. **Xuất file Báo cáo PDF trực tiếp từ Notebook:**
   * Chọn `File` $\rightarrow$ `Print` (hoặc nhấn `Ctrl + P`).
   * Chọn máy in là **Save as PDF** để xuất toàn bộ Notebook chứa cả Code, Kết quả chạy và Biểu đồ ra dạng PDF hoàn chỉnh.

---

## CÁC LỖI THƯỜNG GẶP & CÁCH KHẮC PHỤC (TROUBLESHOOTING)

| STT | Tên Lỗi | Nguyên nhân | Cách khắc phục |
| :---: | :--- | :--- | :--- |
| **1** | `AnalysisException: Path does not exist` | Sai đường dẫn file `.csv` trên DBFS | Kiểm tra lại tên file upload trong `Catalog` / `DBFS`. Đảm bảo đường dẫn chính xác: `dbfs:/FileStore/tables/...` |
| **2** | `AttributeError: 'NoneType' object has no attribute 'spark'` | Cluster bị ngắt kết nối hoặc chưa đính kèm Notebook | Nhấn vào góc trên bên trái Notebook (mục Connect/Detached), chọn lại Cluster `Credit-Analytics-Cluster` và nhấn **Attach**. |
| **3** | `OutOfMemoryError (OOM) / SparkContext shutdown` | Cụm máy chủ bị tràn RAM khi huấn luyện ML | Trong Cell 4, giảm số lượng cây `numTrees` xuống `[10, 20]` và số nếp gấp `numFolds` của CrossValidator xuống `2`. |
| **4** | `DATATYPE_MISMATCH: Input to StringIndexer should be string...` | Ép sai kiểu dữ liệu cột | Kiểm tra lại kiểu dữ liệu của biến danh mục bằng `df.printSchema()`. Đảm bảo dùng `.cast("string")` trước khi cho vào `StringIndexer`. |

---
*Chúc bạn thực hiện thành công bài Tiểu Luận Cuối Khóa đạt điểm số cao nhất trên Databricks!*
