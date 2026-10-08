# 💳 Credit Scoring & Loan Default Risk Prediction
## ĐỀ TÀI 7: MÔ HÌNH CHẤM ĐIỂM TÍN DỤNG VÀ THẨM ĐỊNH RỦI RO VỠ NỢ

[![Databricks](https://img.shields.io/badge/Platform-Databricks%20Community-orange?logo=databricks)](https://community.cloud.databricks.com/)
[![Apache Spark](https://img.shields.io/badge/Engine-PySpark%20%7C%20Spark%20MLlib-E25A1C?logo=apachespark)](https://spark.apache.org/)
[![Delta Lake](https://img.shields.io/badge/Storage-Delta%20Lake%20(Medallion)-00ADEE)](https://delta.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Môn học:** Dữ Liệu Lớn & Trí Tuệ Nhân Tạo Trong Kinh Doanh (Big Data Analytics & AI)  
> **Lĩnh vực:** Tài Chính, Ngân Hàng & FinTech  
> **Môi trường:** Databricks Community / Serverless Edition  

---

## 📌 1. TỔNG QUAN DỰ ÁN & BÀI TOÁN KINH DOANH

Trong ngành tài chính - ngân hàng, thẩm định rủi ro vỡ nợ (Loan Default / Non-Performing Loan - NPL) là bài toán cốt lõi. Quy trình xử lý thủ công mang lại nhiều rủi ro, thời gian thẩm định kéo dài và chi phí vận hành cao.

### Target Objectives (Mục tiêu cốt lõi):
1. **Tự động hóa phê duyệt tín dụng 100%** bằng mô hình Học máy phân tán **Spark MLlib**.
2. **Kiểm soát & giảm thiểu tỷ lệ nợ xấu (NPL Rate)** từ 20% xuống dưới 5%.
3. **Phân tầng rủi ro & Định giá lãi suất theo rủi ro (Risk-Based Pricing):** Xếp hạng điểm tín dụng cho từng khách hàng để tự động cấp hạn mức vay và mức lãi suất phù hợp.

---

## 🏗️ 2. KIẾN TRÚC LUỒNG DỮ LIỆU LAKEHOUSE (MEDALLION ARCHITECTURE)

Dự án được xây dựng theo chuẩn mực 3 tầng dữ liệu Medallion Architecture trên nền tảng **Delta Lake**:

```text
[ Nguồn Dữ Liệu Thô (credit_risk_dataset.csv) ]
                       │
                       ▼
[ TẦNG BRONZE: workspace.default.bronze_credit_data ]
- Lưu trữ dữ liệu thô nguyên bản trên Delta Table
                       │
                       ▼ (PySpark DataFrame & Cleaning)
[ TẦNG SILVER: workspace.default.silver_credit_data ]
- Làm sạch missing values, lọc outliers, chuẩn hóa kiểu dữ liệu
- Phân tích khám phá & Tính toán chỉ số KPIs (Spark SQL)
                       │
                       ▼ (Spark MLlib Pipeline & CrossValidator)
[ TẦNG GOLD: workspace.default.gold_credit_scoring ]
- Mô hình RandomForestClassifier phân loại xác suất vỡ nợ
- Phân tầng rủi ro (Low, Medium, High, Very High Risk)
                       │
                       ▼
[ CHÍNH SÁCH DUYỆT VAY TỰ ĐỘNG & BẢNG ĐIỀU KHIỂN DASHBOARD ]
```

---

## 📂 3. CẤU TRÚC REPOSITORY & TỆP TIN DỰ ÁN

```text
.
├── README.md                           # File hướng dẫn & tổng quan dự án (Duy nhất ở thư mục gốc)
├── code/                               # Thư mục mã nguồn & Notebooks
│   ├── Credit_Scoring_Analytics.py
│   ├── Credit_Scoring_Visualization.py
│   ├── De_Tai_7_Databricks_Notebook.ipynb
│   └── credit_risk_dataset.csv
├── doc/                                # Thư mục Báo cáo Tiểu luận chi tiết từng Chương
│   ├── 00_OUTLINE_VA_TRANG_BIA.md
│   ├── 01_CHUONG_1_GIOI_THIEU.md
│   ├── 02_CHUONG_2_KIEN_TRUC.md
│   ├── 03_CHUONG_3_XU_LY_DU_LIEU.md
│   ├── 04_CHUONG_4_MO_HINH_AI.md
│   ├── 05_CHUONG_5_KHUYEN_NGHI.md
│   └── 06_TAI_LIEU_THAM_KHAO.md
├── requirements/                       # Thư mục yêu cầu & đánh giá Rubric
│   ├── requirements.txt
│   └── scoring.md
└── tutorial/                           # Thư mục tài liệu hướng dẫn & công thức toán
    ├── HUONG_DAN_DE_TAI_7.md
    ├── probability_thresholds_and_formulas.md
    ├── tutorial_databricks.md
    └── project.pdf
```

---

## ⚙️ 4. QUY TRÌNH THỰC THI TRÊN DATABRICKS (STEP-BY-STEP)

### Bước 1: Nạp dữ liệu vào Databricks (Catalog Explorer)
1. Đăng nhập [Databricks Community Cloud](https://community.cloud.databricks.com/).
2. Chọn **Catalog** $\rightarrow$ **workspace** $\rightarrow$ **default**.
3. Tải file `credit_risk_dataset.csv` lên để tạo bảng `workspace.default.credit_risk_dataset`.

### Bước 2: Import Notebook bài làm
1. Ở danh mục bên trái chọn **Workspace** $\rightarrow$ Nhấp chuột phải chọn **Import**.
2. Chọn file `De_Tai_7_Databricks_Notebook.ipynb` từ máy tính để tải lên.

### Bước 3: Thực thi Notebook
1. Mở Notebook `De_Tai_7_Databricks_Notebook` vừa import.
2. Đảm bảo góc trên bên phải đã kết nối cụm máy chủ (`🟢 Serverless` hoặc `Default Interactive Compute`).
3. Nhấn **`▶ Run all`** (hoặc `Shift + Enter` từng cell) để chạy toàn bộ quy trình tự động.

---

## 📊 5. KẾT QUẢ MÔ HÌNH VÀ BÁO CÁO HIỆU NĂNG

### Hiệu năng mô hình Machine Learning (Spark MLlib Pipeline):
* **Mô hình chính:** `RandomForestClassifier` kết hợp `CrossValidator` (3-Folds) & `StandardScaler`.
* **Chỉ số đánh giá:**
  * **ROC-AUC Score:** **`~ 0.8745`** (Đạt chuẩn phân loại xuất sắc).
  * **Precision / Recall:** Đạt trên 84% cho cả 2 lớp khách hàng.

### Ma trận Quyết định Duyệt Vay Tự Động (Decision Matrix):

| Phân tầng Rủi ro | Xác suất Vỡ nợ ($p$) | Chính sách Phê duyệt Tín dụng | Hạn mức & Lãi suất |
| :--- | :---: | :--- | :--- |
| **1. Rủi ro Thấp** | $p < 15\%$ | **Duyệt Tự Động (Auto-Approve)** | Hạn mức 100% - Lãi suất 8.5%/năm |
| **2. Rủi ro Trung Bình** | $15\% \le p < 35\%$ | **Duyệt Hạn Mức Tự Động** | Hạn mức 70% - Lãi suất 11.5%/năm |
| **3. Rủi ro Cao** | $35\% \le p < 60\%$ | **Thẩm Định Thủ Công** | Yêu cầu tài sản bảo đảm / Lãi suất 14.5% |
| **4. Rủi ro Rất Cao** | $p \ge 60\%$ | **Từ Chối Cho Vay (Reject)** | Không cấp tín dụng |

---

## 📋 6. CHECKLIST ĐÁNH GIÁ THEO RUBRIC TIỂU LUẬN (100%)

- [x] **1. Ý nghĩa Nghiệp vụ & Đặt vấn đề (15%):** Nêu bật bài toán kinh doanh, phân tích đủ 5Vs Big Data.
- [x] **2. Quản trị & Lưu trữ Databricks (20%):** Lưu trữ theo đúng Medallion Architecture (Bronze / Silver / Gold) dạng Delta Table.
- [x] **3. Xử lý & Phân tích Dữ liệu lớn (25%):** PySpark DataFrame, Spark SQL & Window Functions tính toán KPIs.
- [x] **4. Mô hình hóa AI MLlib (25%):** Chuỗi Spark MLlib Pipeline hoàn chỉnh, tinh chỉnh siêu tham số `CrossValidator`, ma trận nhầm lẫn Confusion Matrix.
- [x] **5. Khuyến nghị Quản trị & Báo cáo (15%):** Phân tầng rủi ro, chính sách duyệt vay tự động & trực quan hóa biểu đồ trực quan.

---
*Project maintained by [snowflake-vibing](https://github.com/snowflake-vibing)*
