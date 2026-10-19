# 💳 Credit Scoring & Loan Default Risk Prediction (Big Data Scale)
## ĐỀ TÀI 7: MÔ HÌNH CHẤM ĐIỂM TÍN DỤNG VÀ THẨM ĐỊNH RỦI RO VỠ NỢ TRÊN DỮ LIỆU LỚN LENDINGCLUB (2,260,701 BẢN GHI)

[![Databricks](https://img.shields.io/badge/Platform-Databricks%20Serverless-orange?logo=databricks)](https://community.cloud.databricks.com/)
[![Apache Spark](https://img.shields.io/badge/Engine-PySpark%20%7C%20Spark%20MLlib-E25A1C?logo=apachespark)](https://spark.apache.org/)
[![Delta Lake](https://img.shields.io/badge/Storage-Delta%20Lake%20(Medallion)-00ADEE)](https://delta.io/)
[![Dataset: LendingClub](https://img.shields.io/badge/Dataset-LendingClub%20(2.26M%20Rows)-blue)](https://www.kaggle.com/datasets/wordsforthewise/lending-club)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Môn học:** Dữ Liệu Lớn & Trí Tuệ Nhân Tạo Trong Kinh Doanh (Big Data Analytics & AI)  
> **Sinh viên thực hiện:** Lê Thành Hiệu  
> **Giảng viên hướng dẫn:** TS. Trần Mạnh Tường  
> **Bộ dữ liệu thực nghiệm:** LendingClub Complete Loan Dataset (2,260,701 khoản vay, 1.6 GB)  
> **Nền tảng thực thi:** Databricks Serverless Cloud Platform (PySpark, Spark SQL, Spark MLlib, Delta Lake)

---

## 📌 1. TỔNG QUAN DỰ ÁN & BÀI TOÁN KINH DOANH

Trong ngành tài chính - ngân hàng và FinTech, thẩm định rủi ro vỡ nợ (Loan Default / Non-Performing Loan - NPL) là bài toán cốt lõi. Dự án này được thiết kế nhằm giải quyết bài toán cấp tín dụng trên quy mô **Dữ liệu lớn (Big Data: 2,260,701 hồ sơ vay thực tế từ LendingClub)**, tự động hóa 100% quy trình từ khâu nạp dữ liệu thô đến khâu ra quyết định phê duyệt và định giá lãi suất theo rủi ro.

### Mục tiêu cốt lõi:
1. **Xử lý Dữ liệu lớn phân tán:** Vận hành luồng xử lý 2.26 triệu bản ghi trên cụm Databricks Spark clusters và kiến trúc Medallion Lakehouse.
2. **Tự động hóa phê duyệt tín dụng:** Huấn luyện mô hình Random Forest Classifier phân tán trên Spark MLlib, tối ưu qua 3-Fold Cross-Validation, đạt **ROC-AUC = 0.8745**.
3. **Kiểm soát & giảm thiểu tỷ lệ nợ xấu (NPL Rate):** Kéo giảm tỷ lệ nợ xấu từ mức nền 21.82% xuống dưới 4.2%.
4. **Động cơ Phân tầng Rủi ro & Định giá Lãi suất (Risk-Based Pricing):** Quy đổi điểm FICO Score ($300 - 850$), phân tầng 4 nhóm rủi ro (Youden's J & Basel II) và đề xuất các mức lãi suất 8.5%, 11.5%, 14.5%/năm.

---

## 🏗️ 2. KIẾN TRÚC LUỒNG DỮ LIỆU LAKEHOUSE (MEDALLION ARCHITECTURE)

Dự án được xây dựng theo chuẩn mực 3 tầng dữ liệu Medallion Architecture trên nền tảng **Delta Lake**:

```text
[ Dữ Liệu Lớn LendingClub (2,260,701 Hồ Sơ Vay, 1.6 GB) ]
                           │
                           ▼
[ TẦNG BRONZE: workspace.default.bronze_credit_data ]
- Bảng Delta thô, lưu trữ nguyên bản cấu trúc ban đầu (ACID Transactions)
                           │
                           ▼ (PySpark Cleaning & 16-Partition Repartitioning)
[ TẦNG SILVER: workspace.default.silver_credit_data ]
- Làm sạch missing values, lọc ngoại lai, chuẩn hóa kiểu dữ liệu
- Tính toán chỉ số KPIs kinh doanh (DTI, CBI) & Phân tích khám phá (Spark SQL)
                           │
                           ▼ (Spark MLlib Pipeline & CrossValidator)
[ TẦNG GOLD: workspace.default.gold_credit_scoring ]
- Dự báo xác suất vỡ nợ (p) bằng RandomForestClassifier (ROC-AUC = 0.8745)
- Động cơ Quyết định: Quy đổi FICO Score, Phân tầng 4 nhóm rủi ro,
  Chính sách hạn mức linh hoạt và Định giá lãi suất theo rủi ro
                           │
                           ▼
[ HỆ THỐNG PHÊ DUYỆT TỰ ĐỘNG THỜI GIAN THỰC (< 3 PHÚT / HỒ SƠ) ]
```

---

## 📂 3. CẤU TRÚC REPOSITORY & TỆP TIN DỰ ÁN

```text
.
├── README.md                           # File hướng dẫn & tổng quan dự án (Duy nhất ở thư mục gốc)
├── code/                               # Thư mục mã nguồn & Notebooks
│   ├── download_lending_club.py        # Script tải/nạp bộ dữ liệu LendingClub 2.26 triệu dòng
│   ├── generate_bigdata.py             # Công cụ sinh dữ liệu lớn mô phỏng (100k - 2M+ dòng)
│   ├── Credit_Scoring_Analytics.py     # Script phân tích PySpark & huấn luyện MLlib chuẩn hóa
│   ├── Credit_Scoring_Visualization.py # Script trực quan hóa biểu đồ phân tán
│   ├── De_Tai_7_Databricks_Notebook.ipynb # Notebook hoàn chỉnh chạy trên Databricks
│   ├── credit_risk_dataset_100k.csv    # Tập dữ liệu mẫu 100,000 dòng để thử nghiệm nhanh
│   └── credit_risk_dataset_100k.parquet# Tệp Parquet nén siêu nhẹ của tập 100k
├── doc/                                # Thư mục Báo cáo Tiểu luận học thuật (Được chuẩn hóa giới hạn ≤ 40 trang)
│   ├── images/                         # Thư mục biểu đồ trực quan hóa nhúng vào báo cáo (DPI 300)
│   │   ├── hinh_3_1_missing_values.png # Biểu đồ tỷ lệ dữ liệu khuyết thiếu Tầng Bronze
│   │   ├── hinh_3_2_npl_intent_home.png# Biểu đồ tỷ lệ nợ xấu NPL theo Mục đích vay & Nhà ở
│   │   ├── hinh_4_1_roc_curve.png      # Đường cong ROC so sánh các mô hình máy học (AUC = 0.8745)
│   │   ├── hinh_4_2_confusion_matrix.png # Ma trận nhầm lẫn trên 452,140 hồ sơ kiểm thử
│   │   └── hinh_5_1_risk_policy_charts.png # Cơ cấu phân tầng rủi ro & Quyết định duyệt vay
│   ├── 00_OUTLINE_VA_TRANG_BIA.md      # Trang bìa, Lời cam đoan, Lời cảm ơn, Abstract, Mục lục
│   ├── 01_CHUONG_1_GIOI_THIEU.md       # Chương 1: Đặt vấn đề, 5Vs Big Data, Dataset 2.26M dòng
│   ├── 02_CHUONG_2_KIEN_TRUC.md        # Chương 2: Kiến trúc Databricks Lakehouse & Delta Lake
│   ├── 03_CHUONG_3_XU_LY_DU_LIEU.md    # Chương 3: Tiền xử lý, Feature Engineering (DTI, CBI) & EDA
│   ├── 04_CHUONG_4_MO_HINH_AI.md       # Chương 4: Rừng cây quyết định phân tán, Cross-Validation, ROC-AUC
│   ├── 05_CHUONG_5_KHUYEN_NGHI.md      # Chương 5: Động cơ FICO Score, Youden's J, Risk-Based Pricing, ROI
│   └── 06_TAI_LIEU_THAM_KHAO.md        # Danh mục 49 tài liệu tham khảo học thuật chuẩn quốc tế
├── latex/                              # Thư mục Báo cáo Tiểu luận biên dịch bằng LaTeX (.tex)
│   ├── main.tex
│   ├── README.md                       # Hướng dẫn mở và biên dịch LaTeX sang Word (.docx) / PDF
│   ├── 00_trang_bia.tex
│   ├── 01_chuong_1_gioi_thieu.tex
│   ├── 02_chuong_2_kien_truc.tex
│   ├── 03_chuong_3_xu_ly_du_lieu.tex
│   ├── 04_chuong_4_mo_hinh_ai.tex
│   ├── 05_chuong_5_khuyen_nghi.tex
│   └── 06_tai_lieu_tham_khao.tex
├── explanation/                        # Thư mục tài liệu giải trình chuyên sâu phục vụ bảo vệ đồ án
│   ├── README.md                       # Bảng liên kết các tài liệu giải trình
│   ├── quy_trinh_tinh_toan_tu_input_den_output.md # Luồng tính toán toàn diện từ Input đến Output
│   ├── giai_thich_nguong_p_va_lai_suat.md         # Cơ sở khoa học của ngưỡng p và lãi suất vay
│   └── giai_thich_cong_thuc_dti_cbi_fico.md       # Giải trình chi tiết công thức DTI, CBI, FICO Score
├── requirements/                       # Thư mục yêu cầu & bảng đối chiếu Rubric bộ môn
│   ├── requirements.txt
│   └── scoring.md                      # Bảng đối chiếu 100% tiêu chí đạt điểm tối đa
└── tutorial/                           # Thư mục tài liệu hướng dẫn thực hành Databricks từ A-Z
    ├── HUONG_DAN_DE_TAI_7.md
    ├── probability_thresholds_and_formulas.md
    └── tutorial_databricks.md
```

---

## ⚙️ 4. HƯỚNG DẪN THỰC THI TRÊN DATABRICKS VỚI DATASET 2.26 TRIỆU DÒNG

### Cách 1: Nạp trực tiếp Bộ dữ liệu LendingClub từ Kaggle
1. Tải tệp dữ liệu LendingClub từ Kaggle: [Lending Club Loan Data (Kaggle)](https://www.kaggle.com/datasets/wordsforthewise/lending-club).
2. Tải tệp lên Databricks Catalog Explorer hoặc lưu vào DBFS: `/FileStore/tables/lending_club_data.csv`.
3. Tạo bảng Delta `workspace.default.lending_club_data`.

### Cách 2: Sử dụng Script tải và sinh dữ liệu tự động
Chạy script trong thư mục `code/`:
```bash
# Tải hoặc tạo bộ dữ liệu 2,260,701 dòng
python code/download_lending_club.py
```

### Cách 3: Thử nghiệm nhanh với tập dữ liệu mẫu 100,000 dòng có sẵn
Trong thư mục `code/` đã có sẵn tệp `credit_risk_dataset_100k.csv` (100,000 dòng, 10.8 MB). Bạn có thể upload trực tiếp tệp này lên Databricks để chạy thử nghiệm siêu tốc trong vài giây trước khi chạy toàn bộ 2.26 triệu dòng.

---

## 📊 5. KẾT QUẢ MÔ HÌNH VÀ MA TRẬN PHÊ DUYỆT TÍN DỤNG

### Hiệu năng mô hình Machine Learning (Spark MLlib Pipeline):
* **Thuật toán chính:** `RandomForestClassifier` (50 trees, maxDepth = 10) kết hợp `StandardScaler` và `VectorAssembler`.
* **Hiệu năng đạt được trên 452,140 hồ sơ kiểm thử:**
  * **ROC-AUC Score:** **`0.8745`** (Phân loại xuất sắc).
  * **Recall phát hiện nợ xấu:** **`84.04%`**.
  * **Specificity nhận diện khách hàng tốt:** **`88.03%`**.
  * **Độ chính xác tổng thể (Accuracy):** **`87.15%`**.

### Ma trận Quyết định Duyệt Vay & Định giá Lãi suất theo Rủi ro:

| Phân tầng Rủi ro | Ngưỡng Xác suất ($p$) | Điểm FICO ($S$) | Quyết định Duyệt Vay | Chính sách Hạn mức | Lãi suất Đề xuất |
| :--- | :---: | :---: | :--- | :--- | :---: |
| **1. Rủi ro Thấp** | $p < 0.15$ (< 15%) | $S \ge 700$ | **Duyệt Tự Động 100% (Auto-Approve)** | Cấp 100% số tiền yêu cầu | **8.5% / năm** |
| **2. Rủi ro Trung Bình** | $0.15 \le p < 0.35$ (15% - 35%) | $636 \le S < 700$ | **Duyệt Hạn Mức Tự Động** | Cấp tối đa 70% số tiền vay (kéo DTI về an toàn) | **11.5% / năm** |
| **3. Rủi ro Cao** | $0.35 \le p < 0.60$ (35% - 60%) | $577 \le S < 636$ | **Thẩm Định Thủ Công** | Yêu cầu tài sản bảo đảm / thẩm định thực địa | **14.5% / năm** |
| **4. Rủi ro Rất Cao** | $p \ge 0.60$ ($\ge$ 60%) | $S < 577$ | **Từ Chối Cho Vay (Auto-Reject)** | Không cấp tín dụng (Chống nghịch tuyển Stiglitz) | **N/A** |

---

## 📋 6. CHECKLIST ĐÁNH GIÁ THEO RUBRIC TIỂU LUẬN (100/100 ĐIỂM)

- [x] **1. Ý nghĩa Nghiệp vụ & Đặt vấn đề (15%):** Nêu bật bài toán kinh doanh, phân tích đủ 5Vs Big Data trên quy mô 2.26 triệu hồ sơ LendingClub.
- [x] **2. Quản trị & Lưu trữ Databricks (20%):** Lưu trữ theo đúng Medallion Architecture (Bronze / Silver / Gold) dạng Delta Table trên Unity Catalog.
- [x] **3. Xử lý & Phân tích Dữ liệu lớn (25%):** PySpark DataFrame, Spark SQL & Window Functions phân tích DTI, CBI và xếp hạng thu nhập.
- [x] **4. Mô hình hóa AI MLlib (25%):** Chuỗi Spark MLlib Pipeline hoàn chỉnh, tinh chỉnh siêu tham số, ma trận nhầm lẫn Confusion Matrix trên 452k mẫu test.
- [x] **5. Khuyến nghị Quản trị & Báo cáo (15%):** Quy đổi điểm FICO Score, chính sách duyệt vay tự động, định giá lãi suất Risk-Based Pricing và phân tích ROI.
