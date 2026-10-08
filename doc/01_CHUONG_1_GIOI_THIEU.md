# CHƯƠNG 1: TỔNG QUAN VỀ BÀI TOÁN & ĐẶT VẤN ĐỀ

---

## 1.1. Bối cảnh ngành Tài chính - Ngân hàng & FinTech

Trong kỷ nguyên số hóa, tài chính tiêu dùng và cho vay tín chấp đóng vai trò đòn bẩy quan trọng giúp thúc đẩy tiêu dùng và tăng trưởng kinh tế. Tuy nhiên, hoạt động cấp tín dụng luôn gắn liền với **rủi ro vỡ nợ (Loan Default Risk)**. Khi khách hàng không hoàn trả khoản vay đúng hạn, tổ chức tài chính phải chịu tổn thất vốn trực tiếp và gia tăng tỷ lệ nợ xấu (Non-Performing Loan - NPL).

Quy trình thẩm định tín dụng truyền thống phụ thuộc nhiều vào đánh giá thủ công của cán bộ tín dụng, dẫn đến các hạn chế lớn:
- **Thời gian xử lý kéo dài:** Thường mất từ 1 đến 3 ngày làm việc để phê duyệt một hồ sơ.
- **Tính cảm quan cao:** Khó đảm bảo tính nhất quán và khách quan giữa các cán bộ thẩm định.
- **Chi phí vận hành đắt đỏ:** Khó mở rộng quy mô (Scale-up) khi số lượng hồ sơ vay đăng ký trực tuyến gia tăng hàng ngàn lượt mỗi ngày.

Do đó, việc ứng dụng **Dữ liệu lớn (Big Data)** và **Trí tuệ nhân tạo (AI/Machine Learning)** vào quy trình Chấm điểm tín dụng (Credit Scoring) là yêu cầu tất yếu để tự động hóa 100% khâu duyệt vay, giảm thiểu chi phí vận hành và kiểm soát nợ xấu.

---

## 1.2. Tính cấp thiết của đề tài & Mục tiêu tự động hóa

### Tính cấp thiết
Đề tài **"Mô Hình Chấm Điểm Tín Dụng Và Thẩm Định Rủi Ro Vỡ Nợ"** giải quyết bài toán cốt lõi của các ngân hàng và công ty FinTech hiện đại: *Làm thế nào để phân loại chính xác hồ sơ có nguy cơ vỡ nợ trước khi quyết định giải ngân?*

### Mục tiêu dự án
1. **Tự động hóa phê duyệt tín dụng 100%:** Xây dựng luồng xử lý và dự báo phân tán với Apache Spark trên nền tảng Databricks.
2. **Kiểm soát & Giảm tỷ lệ NPL:** Loại bỏ trên 80% rủi ro nợ xấu nhóm rủi ro cao, giảm tỷ lệ NPL tổng thể xuống dưới 5%.
3. **Phân tầng rủi ro & Risk-Based Pricing:** Xếp hạng điểm tín dụng cho từng khách hàng, từ đó quyết định tự động **hạn mức cho vay** và **mức lãi suất tương ứng** với độ rủi ro.

---

## 1.3. Phân tích đặc tính Dữ liệu lớn theo mô hình 5Vs

| Đặc tính Big Data | Biểu hiện cụ thể trong Đề tài 7 |
| :--- | :--- |
| **Volume (Dung lượng)** | Xử lý hàng chục nghàn đến hàng triệu bản ghi giao dịch lịch sử và thông tin vay từ hệ thống Core Banking / CRM. |
| **Velocity (Tốc độ)** | Phê duyệt khoản vay tức thì trong **< 5 phút** ngay khi khách hàng nộp hồ sơ trên ứng dụng Mobile Banking. |
| **Variety (Đa dạng)** | Kết hợp dữ liệu nhân khẩu học (tuổi, học vấn), dữ liệu tài chính (thu nhập, dư nợ) và lịch sử tín dụng (chậm trả, thâm niên). |
| **Veracity (Độ tin cậy)** | Tiền xử lý và làm sạch triệt để các giá trị thiếu (missing values), dữ liệu nhiễu và ngoại lai phi thực tế. |
| **Value (Giá trị kinh doanh)** | Cắt giảm hàng chục tỷ đồng tiền trích lập dự phòng nợ xấu, tăng doanh thu từ lãi vay và tối ưu chi phí vận hành. |

---

## 1.4. Bộ dữ liệu nghiên cứu & Phạm vi đề tài

Dự án sử dụng bộ dữ liệu thực nghiệm **Credit Risk Dataset** (nguồn Kaggle), bao gồm 32,581 bản ghi với 12 thuộc tính quan trọng:

- `person_age`: Tuổi khách hàng.
- `person_income`: Thu nhập hàng năm (USD/VND).
- `person_home_ownership`: Loại hình sở hữu nhà (RENT, OWN, MORTGAGE, OTHER).
- `person_emp_length`: Thâm niên làm việc (năm).
- `loan_intent`: Mục đích vay (PERSONAL, EDUCATION, MEDICAL, VENTURE, HOMEIMPROVEMENT, DEBTCONSOLIDATION).
- `loan_grade`: Xếp hạng khoản vay (A, B, C, D, E, F, G).
- `loan_amnt`: Số tiền đăng ký vay.
- `loan_int_rate`: Lãi suất khoản vay (%).
- `loan_percent_income`: Tỷ lệ nợ vay trên thu nhập.
- `cb_person_default_on_file`: Lịch sử nợ xấu trên CIC (Y/N).
- `cb_person_cred_hist_length`: Thâm niên lịch sử tín dụng (năm).
- **`loan_status` (Target Variable):** Nhãn mục tiêu (`0`: Trả đúng hạn, `1`: Vỡ nợ / Chậm trả > 90 ngày).
