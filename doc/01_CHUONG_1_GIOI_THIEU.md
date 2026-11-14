# CHƯƠNG 1: GIỚI THIỆU

---

## 1.1 Đặt vấn đề và Lý do chọn đề tài

Trong nền kinh tế thị trường hiện đại, hệ thống tài chính - ngân hàng giữ vai trò huyết mạch trong việc dẫn truyền dòng vốn từ các chủ thể tiết kiệm đến các chủ thể có nhu cầu đầu tư và tiêu dùng [1]. Phân khúc tín dụng bán lẻ (Retail Banking) và cho vay tiêu dùng cá nhân (Consumer Lending) đã chứng kiến tốc độ tăng trưởng bùng nổ, đặc biệt là khi chuyển dịch từ các kênh giao dịch tại quầy sang các nền tảng số hóa (Digital Banking, Mobile Banking và các ứng dụng FinTech) [2]. Khách hàng ngày nay kỳ vọng những trải nghiệm vay vốn tức thì (Instant Credit / Buy Now Pay Later - BNPL), quy trình đăng ký 100% trực tuyến và thời gian phê duyệt giải ngân chỉ tính bằng phút [3].

Tuy nhiên, song hành cùng cơ hội mở rộng biên lãi thuần (Net Interest Margin - NIM), hoạt động cấp tín dụng luôn tiềm ẩn bản chất cố hữu là **rủi ro tín dụng (Credit Risk)** mà đỉnh điểm là **biến cố vỡ nợ (Loan Default)** [4]. Theo Ủy ban Basel về Giám sát Ngân hàng (BCBS), biến cố vỡ nợ xảy ra khi người vay không thực hiện nghĩa vụ trả nợ gốc hoặc lãi theo thỏa thuận hợp đồng sau thời hạn quy định (quá hạn từ 90 ngày trở lên) [5]. Sự gia tăng của tỷ lệ nợ xấu (Non-Performing Loans - NPL) không chỉ bào mòn nguồn vốn tự có của ngân hàng thông qua chi phí trích lập dự phòng tổn thất, mà còn đe dọa hệ số an toàn vốn (Capital Adequacy Ratio - CAR) và tính thanh khoản của toàn hệ thống [6].

Trước áp lực đó, các định chế tài chính đối mặt với bài toán chiến lược: *Làm thế nào để vừa tối đa hóa tốc độ phê duyệt và mở rộng tệp khách hàng vay tiêu dùng số, vừa kiểm soát chặt chẽ tỷ lệ nợ xấu và bảo toàn nguồn vốn của ngân hàng?* Lời giải nằm ở việc ứng dụng công nghệ Dữ liệu lớn (Big Data) và Trí tuệ nhân tạo (AI/Machine Learning) nhằm tự động hóa quy trình thẩm định rủi ro và chấm điểm tín dụng [7].

---

## 1.2 Mục tiêu nghiên cứu

### 1.2.1 Mục tiêu tổng quát
Nghiên cứu, thiết kế và phát triển hệ thống tự động hóa chấm điểm tín dụng và dự báo xác suất vỡ nợ quy mô lớn dựa trên nền tảng điện toán phân tán Databricks Lakehouse và thuật toán học máy Spark MLlib, phục vụ hoạt động thẩm định và định giá rủi ro tín dụng trong ngân hàng thương mại và FinTech.

### 1.2.2 Mục tiêu cụ thể
1. **Xây dựng Kiến trúc Hồ Dữ liệu Lakehouse phân tán:** Thiết lập luồng dữ liệu tự động theo mô hình Huy chương Medallion (Bronze -> Silver -> Gold) trên nền tảng Databricks Serverless và Delta Lake, bảo đảm tính toàn vẹn giao dịch ACID và khả năng xử lý dữ liệu lớn.
2. **Tiền xử lý và Kỹ nghệ đặc trưng tài chính phân tán:** Xây dựng quy trình làm sạch dữ liệu lớn, xử lý ngoại lai, làm giàu dữ liệu và thiết lập các chỉ số tài chính chuyên sâu (DTI, CBI, Window Functions) bằng Spark SQL.
3. **Phát triển Mô hình Học máy phân tán hiệu năng cao:** Huấn luyện thuật toán Random Forest Classifier trên Spark MLlib, tinh chỉnh siêu tham số bằng 3-Fold Cross-Validation, hướng đến chỉ số ROC-AUC vượt trội ($> 0.85$) và cân bằng tối ưu giữa Precision và Recall.
4. **Thiết kế Động cơ Ra quyết định (Decision Engine) và Khung định giá theo rủi ro:** Chuẩn hóa xác suất vỡ nợ thành điểm FICO tiêu chuẩn (300 - 850), thiết lập ma trận 4 phân tầng rủi ro dựa trên chỉ số Youden's J và chuẩn mực Basel II, đồng thời xây dựng mô hình định giá lãi suất theo rủi ro (Risk-Based Pricing Model: 8.5%, 11.5%, 14.5%).
5. **Đánh giá hiệu quả kinh tế và đề xuất chiến lược quản trị:** Định lượng tác động tài chính đối với việc kéo giảm tỷ lệ nợ xấu NPL, cắt giảm chi phí dự phòng rủi ro và nâng cao năng lực cạnh tranh số của tổ chức tài chính.

---

## 1.3 Nội dung nghiên cứu

Để thực hiện các mục tiêu trên, đề tài triển khai 4 nội dung nghiên cứu cốt lõi:
1. Thu thập, nạp và quản trị bộ dữ liệu lớn LendingClub gồm 2,260,701 hồ sơ tín dụng (1.6 GB) vào kho lưu trữ phân tán Delta Lake trên Databricks.
2. Phân tích thực trạng khiếm khuyết dữ liệu, thiết kế quy trình tiền xử lý làm sạch phân tán tại Tầng Silver và tính toán các đặc trưng tài chính phái sinh.
3. Huấn luyện mô hình Random Forest phân tán trên Tầng Gold, thực thi K-Fold Cross-Validation và đánh giá đa chỉ số (ROC-AUC, Confusion Matrix, Feature Importance).
4. Thiết lập khung quy đổi FICO Score, xây dựng chính sách phê duyệt tự động Straight-Through Processing (STP) và lượng hóa lợi ích kinh tế (ROI) giảm nợ xấu.

---

## 1.4 Đối tượng và phạm vi nghiên cứu

### 1.4.1 Đối tượng nghiên cứu
- Đối tượng nghiên cứu trọng tâm là **hành vi vỡ nợ tín dụng (Loan Default)** của khách hàng cá nhân vay tiêu dùng tín chấp.
- Các thuộc tính kinh tế, tài chính, nhân khẩu học và lịch sử tín dụng của khách hàng ảnh hưởng trực tiếp đến xác suất hoàn trả nợ gốc và lãi.

### 1.4.2 Phạm vi nghiên cứu
- **Phạm vi không gian & dữ liệu:** Bộ dữ liệu thực tế 2,260,701 khoản vay từ nền tảng tín dụng LendingClub (San Francisco, Hoa Kỳ), phản ánh toàn diện các chu kỳ kinh tế giai đoạn 2007 - 2018Q4.
- **Phạm vi công nghệ:** Nền tảng Databricks Lakehouse (Apache Spark 3.5+, Delta Lake 3.0+, Spark MLlib) triển khai trên môi trường điện toán đám mây Serverless.
- **Phạm vi nghiệp vụ:** Hoạt động cấp tín dụng bán lẻ, cho vay tiêu dùng không có tài sản bảo đảm và quản trị rủi ro tín dụng tại các ngân hàng thương mại và công ty FinTech.

---

## 1.5 Ý nghĩa khoa học và thực tiễn của đề tài

### 1.5.1 Ý nghĩa khoa học
- Đề tài hiện thực hóa việc kết hợp giữa lý thuyết kinh tế học tài chính (mô hình thông tin bất cân xứng của Stiglitz & Weiss, chỉ số đòn bẩy DTI, CBI) với công nghệ xử lý dữ liệu lớn phân tán (Distributed Big Data) và học máy hiện đại (Ensemble Learning).
- Cung cấp phương pháp luận chuẩn mực về quy trình xây dựng Pipeline học máy phân tán trên nền tảng Lakehouse, bảo đảm tính tái lập (Reproducibility) và khả năng mở rộng (Scalability) ở quy mô hàng triệu bản ghi.

### 1.5.2 Ý nghĩa thực tiễn
- Giúp các tổ chức tín dụng rút ngắn thời gian thẩm định từ 2 - 5 ngày xuống dưới 3 phút thông qua cơ chế phê duyệt tự động hóa thông suốt (STP).
- Cải thiện độ chính xác dự báo nợ xấu, giúp giảm tỷ lệ NPL danh mục xuống dưới 4.2% và tiết kiệm hàng tỷ đồng chi phí trích lập dự phòng theo Thông tư 11/2021/TT-NHNN.
- Toàn bộ mã nguồn phân tán và dữ liệu thực nghiệm được lưu trữ công khai tại GitHub: https://github.com/snowflake-vibing/Credit_Scoring_Project, đóng góp tài liệu tham khảo thực tiễn cho cộng đồng tài chính số.

---

## 1.6 Phân tích đặc tính Dữ liệu lớn theo mô hình 5Vs

Để chứng minh tính tương thích và sự cần thiết của nền tảng Big Data đối với bài toán tín dụng, nghiên cứu phân tích đề tài dựa trên khung lý thuyết 5Vs kinh điển [15]:

**Bảng 1.1 Phân tích đặc tính Dữ liệu lớn theo mô hình 5Vs trong Đề tài Chấm điểm Tín dụng**

| Chiều Kích 5Vs | Khái Niệm Lý Thuyết | Thách Thức Trong Nghiệp Vụ Tín Dụng Bán Lẻ | Giải Pháp Kỹ Thuật Đề Xuất Trong Đề Tài |
| :--- | :--- | :--- | :--- |
| **Volume** *(Quy mô dung lượng)* | Khối lượng dữ liệu khổng lồ vượt quá khả năng lưu trữ và xử lý của hệ thống máy đơn (Single-node RDBMS). | Quy mô 2.26 triệu hồ sơ (1.6 GB) với hàng chục biến số tài chính; hệ thống RDBMS truyền thống bị tràn RAM khi xử lý. | Lưu trữ phân tán trên Databricks Delta Lake, nạp dữ liệu vào Tầng Bronze và phân vùng (Partitioning) 16 luồng song song. |
| **Velocity** *(Tốc độ xử lý)* | Tốc độ phát sinh, thu thập và đòi hỏi phản hồi kết quả trong thời gian thực hoặc gần thời gian thực. | Khách hàng số kỳ vọng phê duyệt giải ngân tức thì (< 3 phút); thẩm định thủ công mất từ 2 đến 5 ngày làm việc. | Tận dụng công cụ Apache Spark tính toán trong bộ nhớ RAM (In-memory computing), tự động hóa dự báo bằng Spark MLlib Pipeline. |
| **Variety** *(Đa dạng định dạng)* | Sự kết hợp phức tạp giữa các dạng dữ liệu số, dữ liệu chuỗi danh mục và thông tin hành vi. | Dữ liệu chứa thuộc tính số (thu nhập, dư nợ), danh mục (mục đích vay, nhà ở) và chuỗi tự do (chức danh công việc). | Kỹ nghệ đặc trưng Spark MLlib: `StringIndexer` mã hóa nhãn, `OneHotEncoder` xử lý danh mục, `VectorAssembler` gộp vector đặc trưng. |
| **Veracity** *(Độ tin cậy dữ liệu)* | Mức độ nhiễu, sai sót, thiếu hụt hoặc mâu thuẫn trong dữ liệu khai báo thực tế của người vay. | Dữ liệu thực nghiệm chứa nhiều điểm ngoại lai phi lý (tuổi > 100, thu nhập <= 0) và tỷ lệ khuyết thiếu lãi suất, thâm niên cao. | Thiết kế Tầng Silver làm sạch phân tán: Lọc ngoại lai $18 \le \text{Age} \le 80$, $\text{Income} > 0$; điền khuyết bằng trung vị (Median) và giá trị thận trọng. |
| **Value** *(Giá trị kinh tế)* | Khả năng chuyển hóa dữ liệu thô thành lợi ích tài chính và giá trị kinh doanh thực tiễn. | Ngân hàng đối mặt nguy cơ thâm hụt vốn do nợ xấu hoặc đánh mất khách hàng tốt do chính sách lãi suất cào bằng. | Động cơ Phân tầng Rủi ro 4 cấp độ, Quy đổi FICO Score (300 - 850) và Mô hình Định giá Lãi suất theo rủi ro (Risk-Based Pricing). |

<p align="left"><em>(Nguồn: Tác giả tổng hợp và phân tích dựa trên chuẩn mực Dữ liệu lớn)</em></p>
