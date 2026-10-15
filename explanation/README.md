# 📚 THƯ MỤC EXPLANATION: TỔNG HỢP GIẢI TRÌNH KHOA HỌC & NGHIỆP VỤ MÔ HÌNH CREDIT SCORING

Thư mục này chứa các tài liệu giải trình chi tiết về mặt **Toán học tài chính (Quantitative Finance)**, **Kinh tế học ngân hàng (Banking Economics)**, **Tiêu chuẩn Basel II/III** và **Kiến trúc xử lý dữ liệu lớn (Big Data Lakehouse)** dành cho Đề tài:

> **ĐỀ TÀI 7: MÔ HÌNH CHẤM ĐIỂM TÍN DỤNG VÀ THẨM ĐỊNH RỦI RO VỠ NỢ**  
> *(Loan Default & Credit Scoring in FinTech & Banking)*  
> **Sinh viên thực hiện:** Lê Thành Hiệu  
> **Giảng viên hướng dẫn:** Trần Mạnh Tường  

---

## 🗂️ DANH MỤC CÁC TÀI LIỆU VÀ LIÊN KẾT TRUY CẬP

### 1. [Quy Trình Tính Toán Toàn Diện Từ Input Đến Output](./quy_trinh_tinh_toan_tu_input_den_output.md)
* **Tên file:** `quy_trinh_tinh_toan_tu_input_den_output.md`
* **Mục đích:** Mô tả chi tiết dòng chảy dữ liệu từ khi khách hàng nộp hồ sơ đến khi hệ thống ra quyết định duyệt vay và giải ngân.
* **Nội dung trọng tâm:**
  - **Input đầu vào:** Cấu trúc 11 biến giải thích (nhân khẩu học, thu nhập, tình trạng nhà ở, thâm niên, mục đích vay, khoản vay, lịch sử tín dụng CIC) và nhãn mục tiêu `loan_status`.
  - **Quy trình xử lý Medallion:** Nạp dữ liệu thô (Bronze) $\rightarrow$ Tiền xử lý, lọc outliers và điền giá trị thiếu (Silver) $\rightarrow$ Tính toán các chỉ số tài chính $DTI$, $CBI$ và Window Functions.
  - **Pipeline học máy phân tán:** Chuỗi biến đổi `StringIndexer` $\rightarrow$ `OneHotEncoder` $\rightarrow$ `VectorAssembler` $\rightarrow$ `StandardScaler` $\rightarrow$ `RandomForestClassifier` tinh chỉnh siêu tham số với `CrossValidator` (3-Folds).
  - **Động cơ phân tầng & Định giá:** Công thức quy đổi điểm FICO Score $S$, phân tầng 4 nhóm rủi ro và mô hình định giá lãi suất theo rủi ro.
  - **Output đầu ra:** Bảng kết quả Gold Layer (`gold_credit_scoring`) với 4 trường hợp khách hàng thực tế minh họa trực quan.
* **Ghi chú sử dụng:** Dùng để giải thích quy trình kỹ thuật, kiến trúc hệ thống và cách thức vận hành của AI Pipeline khi thuyết trình hoặc làm báo cáo kỹ thuật.

---

### 2. [Cơ Sở Khoa Học Của Ngưỡng Xác Suất (p) Và Lãi Suất Vay](./giai_thich_nguong_p_va_lai_suat.md)
* **Tên file:** `giai_thich_nguong_p_va_lai_suat.md`
* **Mục đích:** Trả lời trực diện và thuyết phục các câu hỏi phản biện của hội đồng giảng viên về tính xác thực của các con số trong ma trận quyết định tín dụng.
* **Nội dung trọng tâm:**
  - **Tại sao lại chọn các ngưỡng xác suất $p = 15\%, 35\%, 60\%$?**
    + Cơ sở phân phối thực nghiệm dataset (tỷ lệ nợ xấu tự nhiên $21.82\%$).
    + Cơ sở thống kê tối ưu hóa điểm cắt bằng chỉ số **Youden's J Statistic** trên đường cong ROC ($p^* \approx 0.35$).
    + Cơ sở ma trận tổn thất bất đối xứng (chi phí mất vốn $C_{FP}$ gấp 14 lần chi phí mất lãi $C_{FN}$).
    + Cơ sở chuẩn mực hiệp ước ngân hàng **Basel II & Basel III**.
  - **Tại sao lãi suất đề xuất lại là $8.5\%, 11.5\%, 14.5\%$?**
    + Mô hình 4 thành phần kinh tế học cấu thành lãi suất: Chi phí vốn $R_{\text{COF}} = 5.0\%$, Chi phí vận hành $C_{\text{OPEX}} = 1.5\%$, Biên lợi nhuận $\pi_{\text{NIM}} = 2.0\%$ $\Rightarrow$ Lãi suất cơ sở $R_{\text{base}} = \mathbf{8.5\% / \text{năm}}$.
    + Công thức biên bù đắp rủi ro tín dụng: $\Delta_{\text{Risk}}(p) = p \times 15\%$.
    + Đối chiếu thực tế: Mức $11.5\%$ hoàn toàn trùng khớp với mức lãi suất vay bình quân trong bộ dữ liệu là $11.04\%$.
    + Lý do từ chối ở $p \ge 60\%$ theo **Lý thuyết Nghịch tuyển (Adverse Selection của Stiglitz & Weiss)**.
  - **Tại sao Nhóm 2 lại duyệt hạn mức 70%?** Cơ chế kéo tỷ lệ nợ trên thu nhập ($DTI$) về vùng an toàn để cứu khoản vay.
* **Ghi chú sử dụng:** Dùng làm "phao cứu sinh" chuẩn bị cho phần hỏi - đáp (Q&A) với hội đồng phản biện.

---

## 🧭 HƯỚNG DẪN KHI BẢO VỆ ĐỀ TÀI TRƯỚC HỘI ĐỒNG

Khi giảng viên hoặc hội đồng đặt câu hỏi:
1. *"Hệ thống của em xử lý dữ liệu từ đầu vào đến đầu ra như thế nào?"*  
   $\rightarrow$ Mở và trình bày theo sơ đồ tại [Mục 1 của file Quy Trình Tính Toán](./quy_trinh_tinh_toan_tu_input_den_output.md).
2. *"Tại sao em lại chọn ngưỡng xác suất 15%, 35%, 60% mà không phải 20%, 50%?"*  
   $\rightarrow$ Trình bày 3 luận điểm: Phân phối thực nghiệm dataset 21.82%, Điểm cực đại Youden's J ($p^* = 0.35$) và Chuẩn Basel II tại [Mục 2 của file Giải Thích Ngưỡng](./giai_thich_nguong_p_va_lai_suat.md).
3. *"Cơ sở nào đưa ra mức lãi suất 8.5%, 11.5%, 14.5%?"*  
   $\rightarrow$ Nêu công thức 4 thành phần (Cost of Funds 5% + OPEX 1.5% + NIM 2% = 8.5%) và biên bù rủi ro $\Delta_{\text{Risk}} = p \times 15\%$ tại [Mục 3 của file Giải Thích Ngưỡng](./giai_thich_nguong_p_va_lai_suat.md).

---
*Tài liệu được bảo vệ bản quyền thuộc Đồ án Tiểu luận của sinh viên **Lê Thành Hiệu** - Giảng viên hướng dẫn: **Trần Mạnh Tường**.*
