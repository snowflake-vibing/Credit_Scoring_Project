# CHƯƠNG 5: KẾT LUẬN VÀ KIẾN NGHỊ

---

## 5.1 Kết luận

Đề tài nghiên cứu đã xây dựng thành công một giải pháp công nghệ toàn diện cho bài toán chấm điểm tín dụng và thẩm định rủi ro vỡ nợ quy mô lớn dựa trên nền tảng Databricks Lakehouse và thuật toán học máy phân tán Spark MLlib. Dưới đây là các kết quả cốt lõi đạt được:

1. **Về mặt kỹ thuật kiến trúc:** Thiết lập hoàn chỉnh luồng xử lý dữ liệu phân tán theo mô hình Huy chương Medallion 3 tầng (Bronze -> Silver -> Gold) dạng Delta Lake trên quy mô 2,260,701 hồ sơ tín dụng (1.6 GB), bảo đảm đầy đủ các thuộc tính toàn vẹn giao dịch ACID và cơ chế kiểm toán lịch sử Time Travel.
2. **Về mặt kỹ nghệ dữ liệu:** Chuẩn hóa quy trình làm sạch dữ liệu lớn, xử lý triệt để các trường khuyết thiếu và ngoại lai, đồng thời sáng tạo thành công hai chỉ số tài chính tổng hợp $DTI$ và $CBI$, đóng góp tới 39.6% mức độ phân hóa rủi ro của mô hình.
3. **Về mặt mô hình học máy:** Huấn luyện thành công thuật toán Random Forest Classifier phân tán qua 3-Fold Cross-Validation, đạt chỉ số phân loại xuất sắc với **ROC-AUC = 0.8745**, độ nhạy phát hiện nợ xấu (Recall) đạt **84.04%** và độ chính xác tổng thể đạt **87.16%** trên 452,140 hồ sơ kiểm thử độc lập.
4. **Về mặt ứng dụng kinh doanh:** Xây dựng thành công động cơ quy đổi điểm FICO Score tiêu chuẩn ($300 - 850$), thiết lập ma trận phê duyệt tự động 4 phân tầng rủi ro, cơ chế cứu khoản vay linh hoạt và khung định giá lãi suất theo rủi ro (Risk-Based Pricing: 8.5%, 11.5%, 14.5%). Hệ thống cho phép tự động hóa phê duyệt 76.2% hồ sơ trong thời gian dưới 3 phút và kéo giảm tỷ lệ nợ xấu NPL danh mục từ 21.82% xuống còn 4.18%.

---

## 5.2 Kiến nghị

### 5.2.1 Khuyến nghị quản trị chiến lược cho Ban Điều hành Ngân hàng và FinTech
1. **Chuyển dịch sang cơ chế phê duyệt tự động hóa thông suốt (STP):** Ngân hàng cần mạnh dạn phân quyền cho động cơ chấm điểm AI tự động giải ngân cho nhóm Rủi ro Thấp (FICO > 735) để tối ưu hóa trải nghiệm khách hàng và giải phóng nguồn lực chuyên viên tín dụng tập trung thẩm định các ca phức tạp.
2. **Áp dụng chính sách định giá lãi suất linh hoạt (Risk-Based Pricing):** Xóa bỏ cơ chế cào bằng lãi suất, thay vào đó áp dụng biên độ lãi suất co giãn theo điểm FICO nhằm thu hút tệp khách hàng thượng lưu và bù đắp rủi ro cho nhóm khách hàng thứ cấp.
3. **Thiết lập quy trình giám sát mô hình liên tục (Model Drift Monitoring):** Định kỳ kiểm thử lại mô hình hàng quý bằng dữ liệu mới phát sinh để phát hiện hiện tượng trôi dạt dữ liệu (Data Drift) và trôi dạt khái niệm (Concept Drift) khi chu kỳ kinh tế vĩ mô thay đổi.
4. **Tăng cường an toàn dữ liệu và tuân thủ an toàn vốn:** Tận dụng Unity Catalog trên Databricks để phân quyền truy cập theo vai trò (RBAC) và mã hóa dữ liệu nhạy cảm theo đúng quy định bảo vệ dữ liệu cá nhân (Nghị định 13/2023/NĐ-CP) và chuẩn Basel II/III.

### 5.2.2 Hướng nghiên cứu và phát triển tiếp theo
1. **Mở rộng nguồn dữ liệu thay thế (Alternative Data):** Tích hợp thêm các luồng dữ liệu phi cấu trúc như lịch sử giao dịch thanh toán hóa đơn tiện ích (điện, nước, viễn thông), dữ liệu thương mại điện tử và hành vi ứng dụng di động để chấm điểm cho nhóm khách hàng chưa có lịch sử tín dụng (Thin-file / Unbanked customers).
2. **Khám phá các thuật toán học máy tiên tiến:** Thử nghiệm các mô hình Gradient Boosting phân tán thế hệ mới (XGBoost on Spark, LightGBM) hoặc Deep Learning trên đồ thị (Graph Neural Networks - GNN) để phát hiện các đường dây gian lận tín dụng có tổ chức.
3. **Phát triển Trí tuệ Nhân tạo có thể giải thích (Explainable AI - XAI):** Tích hợp kỹ thuật SHAP (SHapley Additive exPlanations) phân tán để tạo lập các văn bản lý giải nguyên nhân từ chối hồ sơ minh bạch, đáp ứng quyền được giải trình của người tiêu dùng tài chính.
