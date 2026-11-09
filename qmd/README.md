# THƯ MỤC BÁO CÁO QUARTO (.QMD) - ĐỀ TÀI 7

Thư mục này chứa toàn bộ mã nguồn xuất bản khoa học đa định dạng sử dụng **Quarto (.qmd)** cho Đề tài 7: *Mô hình Chấm điểm Tín dụng & Thẩm định Rủi ro Vỡ nợ*.

---

## 📁 Cấu trúc Thư mục `qmd/`

```
qmd/
├── _quarto.yml                     # Cấu hình dự án Quarto Book đa chương
├── index.qmd                       # Trang chủ / Trang bìa & Mục lục Quarto Book
├── 00_OUTLINE_VA_TRANG_BIA.qmd     # Trang bìa, Lời cam đoan, Tóm tắt đề tài
├── 01_CHUONG_1_GIOI_THIEU.qmd      # Chương 1: Tổng quan & Mô hình 5Vs
├── 02_CHUONG_2_KIEN_TRUC.qmd       # Chương 2: Kiến trúc Lakehouse Medallion
├── 03_CHUONG_3_XU_LY_DU_LIEU.qmd   # Chương 3: Xử lý dữ liệu phân tán & Spark SQL
├── 04_CHUONG_4_MO_HINH_AI.qmd      # Chương 4: Machine Learning Pipeline Spark MLlib
├── 05_CHUONG_5_KHUYEN_NGHI.qmd     # Chương 5: FICO Score, Phân tầng rủi ro & ROI
├── 06_TAI_LIEU_THAM_KHAO.qmd       # Tài liệu tham khảo (49 nguồn học thuật)
├── full_report.qmd                 # File gộp toàn bộ các chương phục vụ render đơn
├── images/                         # Toàn bộ 6 biểu đồ phân tích thực nghiệm từ Databricks
└── _output/                        # Kết quả biên dịch (HTML Book, Word DOCX)
```

---

## 🚀 Hướng Dẫn Sử Dụng Quarto

### 1. Yêu cầu cài đặt
Đảm bảo đã cài đặt Quarto CLI trên máy tính:
```bash
quarto --version
```

### 2. Biên dịch toàn bộ Báo cáo (HTML Book + Word DOCX)
Mở terminal tại thư mục gốc dự án hoặc thư mục `qmd/`:
```bash
cd qmd
quarto render
```
Kết quả được tạo tự động trong thư mục `qmd/_output/`:
- `index.html`: Trang web báo cáo tương tác, có tìm kiếm toàn văn và điều hướng chương.
- `Đề-Tài-7--Mô-Hình-Chấm-Điểm-Tín-Dụng---Thẩm-Định-Rủi-Ro-Vỡ-Nợ.docx`: File Microsoft Word hoàn chỉnh, đầy đủ bảng biểu, công thức toán và hình ảnh 300 DPI.

### 3. Xem trước trực tiếp (Live Preview)
Để mở giao diện đọc trực tiếp trên trình duyệt với tính năng tự động cập nhật (Hot-reload):
```bash
cd qmd
quarto preview
```

### 4. Biên dịch từng chương riêng lẻ
```bash
cd qmd
quarto render 01_CHUONG_1_GIOI_THIEU.qmd --to html
```

### 5. Biên dịch sang PDF (Yêu cầu TinyTeX)
Nếu muốn xuất bản trực tiếp sang định dạng PDF:
```bash
quarto install tinytex
quarto render full_report.qmd --to pdf
```
Hoặc mở file `_output/index.html` trên trình duyệt Google Chrome và chọn **Print $\rightarrow$ Save as PDF** (A4, Background Graphics: Checked).
