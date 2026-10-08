# CHƯƠNG 2: KIẾN TRÚC LUỒNG DỮ LIỆU LAKEHOUSE (MEDALLION ARCHITECTURE)

---

## 2.1. Tổng quan Nền tảng Databricks Lakehouse & Delta Lake

Hệ thống được thiết kế và triển khai trên nền tảng **Databricks Community / Serverless Cloud Edition**, kết hợp sức mạnh xử lý phân tán của **Apache Spark** và định dạng lưu trữ **Delta Lake**.

### Các ưu điểm vượt trội của Delta Lake trong dự án:
1. **Đảm bảo tính toàn vẹn dữ liệu (ACID Transactions):** Đảm bảo các thao tác ghi/đọc dữ liệu lớn không bị xung đột hoặc hư hỏng file khi nhiều tiến trình chạy song song.
2. **Khả năng truy vết lịch sử (Time Travel / Versioning):** Cho phép kiểm tra lại trạng thái dữ liệu ở bất kỳ thời điểm nào trong quá khứ để phục vụ công tác kiểm toán tín dụng.
3. **Hiệu năng truy vấn vượt trội:** Tự động tối ưu hóa lưu trữ (Indexing, Data Skipping, Partitioning) giúp truy vấn PySpark và Spark SQL đạt tốc độ gấp 10-50 lần so với file CSV/Parquet thông thường.

---

## 2.2. Chi tiết 3 tầng kiến trúc Medallion (Bronze - Silver - Gold)

Dữ liệu được tổ chức phân tầng chặt chẽ theo mô hình chuẩn **Medallion Architecture**:

```text
[ Nguồn Dữ Liệu Thô: credit_risk_dataset.csv ]
                       │
                       ▼ (GUI Upload / Catalog Ingestion)
[ TẦNG BRONZE: workspace.default.bronze_credit_data ]
- Bảng Delta thô, lưu trữ nguyên bản cấu trúc ban đầu
                       │
                       ▼ (PySpark Cleaning & Data Preprocessing)
[ TẦNG SILVER: workspace.default.silver_credit_data ]
- Làm sạch missing values, lọc outliers, chuẩn hóa kiểu dữ liệu
- Tính toán chỉ số KPIs & Phân tích khám phá (Spark SQL)
                       │
                       ▼ (Spark MLlib Pipeline & CrossValidation)
[ TẦNG GOLD: workspace.default.gold_credit_scoring ]
- Bảng kết quả dự báo (Prediction, Probability, Risk Score)
- Phân tầng rủi ro & Chính sách phê duyệt vay tự động
```

### 1. Tầng BRONZE (`workspace.default.bronze_credit_data`)
* **Nhiệm vụ:** Tiếp nhận và bảo toàn dữ liệu thô ban đầu ngay sau khi nạp từ hệ thống.
* **Định dạng:** Delta Table.
* **Nguyên tắc:** Không chỉnh sửa hay xóa bỏ bất kỳ bản ghi thô nào để đảm bảo khả năng khôi phục và phục vụ công tác audit.

### 2. Tầng SILVER (`workspace.default.silver_credit_data`)
* **Nhiệm vụ:** Xử lý và nâng cao chất lượng dữ liệu.
* **Các thao tác chính:**
  - Điền giá trị thiếu (`.na.fill()`) cho thuộc tính thâm niên `person_emp_length` và lãi suất `loan_int_rate`.
  - Lọc bỏ các bản ghi ngoại lai (outliers) phi thực tế (tuổi <18 hoặc >80, thu nhập <=0).
  - Ép kiểu dữ liệu chuẩn (Double, Integer) cho các biến số học.
* **Mục đích:** Cung cấp nguồn dữ liệu tin cậy cho công tác phân tích Spark SQL Analytics và Feature Engineering.

### 3. Tầng GOLD (`workspace.default.gold_credit_scoring`)
* **Nhiệm vụ:** Lưu trữ kết quả đầu ra cao nhất từ mô hình Học máy phân tán **Spark MLlib**.
* **Các thuộc tính giá trị gia tăng:**
  - `prediction`: Nhãn dự báo (0: Trả đúng hạn, 1: Nợ xấu).
  - `probability`: Véc-tơ xác suất vỡ nợ do mô hình Random Forest tính toán.
  - `Risk_Segment`: Phân tầng rủi ro (Rủi ro Thấp, Trung bình, Cao, Rất cao).
  - `Credit_Policy_Decision`: Quyết định phê duyệt tín dụng và hạn mức cho vay tự động.

---

## 2.3. Sơ đồ luồng dữ liệu phân tán (Data Pipeline Architecture)

Luồng xử lý từ dữ liệu thô đến quyết định quản trị được tự động hóa 100% trong Databricks Notebook:

1. **Ingestion Layer:** Upload CSV vào `Catalog` $\rightarrow$ `workspace.default.credit_risk_dataset`.
2. **Bronze Transformation:** Đọc bằng PySpark `spark.table()` $\rightarrow$ lưu bảng Delta `bronze_credit_data`.
3. **Silver Transformation:** PySpark Filter & Imputer $\rightarrow$ lưu bảng Delta `silver_credit_data`.
4. **Spark SQL Analytics:** Thực thi truy vấn `%sql` tính toán chỉ số NPL %, DTI và Window Functions.
5. **Gold MLlib Execution:** Đóng gói `Pipeline([StringIndexer, OneHotEncoder, VectorAssembler, StandardScaler, RandomForestClassifier])` $\rightarrow$ huấn luyện với `CrossValidator` $\rightarrow$ ghi bảng Delta `gold_credit_scoring`.
6. **Dashboard & Action:** Trực quan hóa biểu đồ và tự động xuất ma trận phê duyệt vay.
