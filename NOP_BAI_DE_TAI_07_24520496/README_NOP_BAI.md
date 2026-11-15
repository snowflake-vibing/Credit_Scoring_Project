# HỒ SƠ NỘP BÀI TIỂU LUẬN CUỐI KHÓA (CAPSTONE PROJECT 2026)
**Chương trình:** Samsung Innovation Campus (SIC) - Hợp tác cùng NIC & Trường Đại học Tài chính - Marketing (UFM)  
**Học phần:** Dữ Liệu Lớn & Trí Tuệ Nhân Tạo Trong Kinh Doanh (Big Data Analytics & AI)  

---

### THÔNG TIN HỌC VIÊN & ĐỀ TÀI:
* **Họ và tên sinh viên:** Lê Thành Hiệu
* **Mã số sinh viên (MSSV):** 24520496
* **Giảng viên hướng dẫn:** TS. Trần Mạnh Tường
* **Tên đề tài:** **ĐỀ TÀI 07: MÔ HÌNH CHẤM ĐIỂM TÍN DỤNG & THẨM ĐỊNH RỦI RO VỠ NỢ TRONG LĨNH VỰC NGÂN HÀNG VÀ FINTECH**
* **Nền tảng thực thi:** Databricks Lakehouse (Apache Spark 3.4+, Spark SQL, Spark MLlib, Delta Lake)
* **Quy mô dữ liệu:** 2,260,701 hồ sơ vay thực tế (LendingClub 2007 - 2018Q4, 1.6 GB)
* **GitHub Repository:** https://github.com/snowflake-vibing/Credit_Scoring_Project

---

### CẤU TRÚC DANH MỤC SẢN PHẨM BÀN GIAO:

Thư mục nộp bài này chứa đầy đủ 100% các sản phẩm bàn giao theo đúng quy định tại Mục 1.2 của tài liệu hướng dẫn học phần:

`
NOP_BAI_DE_TAI_07_24520496/
├── BAO_CAO_TOAN_VAN.pdf                   <-- [BẮT BUỘC] Báo cáo tiểu luận hoàn chỉnh (PDF 14 trang)
├── slide_bao_ve_de_tai_7.pdf               <-- [BẮT BUỘC] Slide thuyết trình bảo vệ đề tài (PDF)
├── slide_bao_ve_de_tai_7.pptx              <-- Slide PowerPoint gốc (Font Montserrat, Spacing 1.5)
├── De_Tai_7_Databricks_Notebook.ipynb      <-- [BẮT BUỘC] Databricks Notebook chứa toàn bộ code & visual
├── README_NOP_BAI.md                       <-- File thông tin tổng hợp này
│
├── 01_Bao_Cao_Tieu_Luan/
│   ├── BAO_CAO_TOAN_VAN.pdf                <-- Báo cáo PDF theo chuẩn Rubric 5 phần (15%-20%-25%-25%-15%)
│   ├── BAO_CAO_TOAN_VAN.qmd                <-- Tệp nguồn Quarto gốc phục vụ biên dịch
│   └── images/                             <-- 6 biểu đồ độ phân giải cao phục vụ biên dịch Quarto
│       ├── hinh_2_1_medallion_architecture.png
│       ├── hinh_3_1_missing_values.png
│       ├── hinh_3_2_npl_intent_home.png
│       ├── hinh_4_1_roc_curve.png
│       ├── hinh_4_2_confusion_matrix.png
│       └── hinh_5_1_risk_policy_charts.png
│
├── 02_Slide_Thuyet_Trinh/
│   ├── slide_bao_ve_de_tai_7.pdf           <-- Slide PDF chuẩn 10 trang thuyết trình
│   └── slide_bao_ve_de_tai_7.pptx          <-- Slide PPTX 16:9, sơ đồ Medallion vector 5 cột trực quan
│
└── 03_Ma_Nguon_Va_Notebook/
    ├── De_Tai_7_Databricks_Notebook.ipynb  <-- 14 cells thực thi trên Databricks Community Cloud
    └── Credit_Scoring_Analytics.py         <-- Mã nguồn Python/PySpark phân tán độc lập
`

---

### HƯỚNG DẪN XEM VÀ CHẠY DỰ ÁN:
1. **Báo cáo tiểu luận:** Mở trực tiếp file BAO_CAO_TOAN_VAN.pdf. File đã được định dạng chuẩn mực theo quy chuẩn học thuật và rubric đánh giá của học phần.
2. **Slide bảo vệ đề tài:** Sử dụng file slide_bao_ve_de_tai_7.pdf hoặc mở file slide_bao_ve_de_tai_7.pptx trên Microsoft PowerPoint để trình chiếu bảo vệ trước hội đồng.
3. **Mã nguồn Databricks:** 
   - Truy cập vào workspace Databricks Community (https://community.cloud.databricks.com/).
   - Chọn **Workspace** -> **Import** -> Chọn file De_Tai_7_Databricks_Notebook.ipynb.
   - Kết nối vào cụm tính toán (Cluster Runtime 13.3 LTS hoặc mới hơn) và nhấn **Run All**.
