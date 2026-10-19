# BÁO CÁO TIỂU LUẬN KẾT THÚC HỌC PHẦN

**BỘ GIÁO DỤC VÀ ĐÀO TẠO**  
**TRƯỜNG ĐẠI HỌC KINH TẾ - ĐẠI HỌC QUỐC GIA**  
**KHOA HỆ THỐNG THÔNG TIN KINH TẾ & PHÂN TÍCH DỮ LIỆU**

---

### **BÁO CÁO TIỂU LUẬN MÔN HỌC**
## **DỮ LIỆU LỚN VÀ TRÍ TUỆ NHÂN TẠO TRONG KINH DOANH**
### *(BIG DATA ANALYTICS & ARTIFICIAL INTELLIGENCE IN BUSINESS)*

---

### **ĐỀ TÀI NGHIÊN CỨU:**
# **MÔ HÌNH CHẤM ĐIỂM TÍN DỤNG VÀ THẨM ĐỊNH RỦI RO VỠ NỢ TRONG LĨNH VỰC NGÂN HÀNG VÀ FINTECH**
### *(LOAN DEFAULT PREDICTION & CREDIT SCORING IN BANKING AND FINTECH)*

---

**Giảng viên hướng dẫn:** TS. Trần Mạnh Tường  
**Sinh viên thực hiện:** Lê Thành Hiệu  
**Mã số sinh viên:** [Điền MSSV tại đây]  
**Lớp / Khóa học:** Big Data Analytics & AI - Khóa 2026  
**Chuyên ngành:** Hệ thống Thông tin Quản lý / Phân tích Kinh doanh  

---

**TP. Hồ Chí Minh, năm 2026**

\newpage

---

## LỜI CAM ĐOAN

Tôi xin cam đoan rằng bài tiểu luận kết thúc học phần với đề tài **"Mô hình chấm điểm tín dụng và thẩm định rủi ro vỡ nợ trong lĩnh vực Ngân hàng và FinTech"** là công trình nghiên cứu độc lập của cá nhân tôi dưới sự hướng dẫn khoa học của **TS. Trần Mạnh Tường**.

Toàn bộ số liệu phân tích, kết quả mô phỏng thực nghiệm và các luận điểm trình bày trong báo cáo hoàn toàn trung thực, khách quan và được thu thập, xử lý từ dữ liệu thực tế 2,260,701 khoản vay của nền tảng LendingClub. Các tài liệu tham khảo, các lý thuyết tài chính - ngân hàng và nghiên cứu khoa học của các tác giả khác đều được trích dẫn nguồn gốc đầy đủ theo đúng quy chuẩn học thuật hiện hành.

*TP. Hồ Chí Minh, năm 2026*  
**Sinh viên thực hiện**  
*(Ký và ghi rõ họ tên)*  

**Lê Thành Hiệu**

\newpage

---

## LỜI CẢM ƠN

Để hoàn thành bài tiểu luận nghiên cứu này, trước hết em xin bày tỏ lòng biết ơn sâu sắc và chân thành nhất đến **TS. Trần Mạnh Tường**, giảng viên phụ trách học phần *Dữ liệu lớn và Trí tuệ nhân tạo trong Kinh doanh*. Thầy đã tận tình truyền đạt những kiến thức chuyên môn sâu rộng về kiến trúc dữ liệu phân tán, khoa học dữ liệu hiện đại và các phương pháp ứng dụng trí tuệ nhân tạo vào thực tiễn kinh tế - tài chính. Những lời chỉ dẫn, định hướng khoa học và phản biện quý báu của Thầy trong suốt quá trình học tập là tiền đề quan trọng giúp em hoàn thiện đồ án này một cách chỉn chu và đúng đắn.

Em cũng xin gửi lời cảm ơn chân thành đến Ban Giám hiệu nhà trường, các Quý Thầy Cô trong Khoa Hệ thống Thông tin Kinh tế đã tạo điều kiện học tập tốt nhất, cung cấp môi trường nghiên cứu và cơ sở vật chất hiện đại phục vụ cho môn học.

*Kính chúc Thầy luôn dồi dào sức khỏe, hạnh phúc và gặt hái được nhiều thành công hơn nữa trong sự nghiệp giảng dạy và nghiên cứu khoa học cao quý!*

\newpage

---

## TÓM TẮT ĐỀ TÀI (ABSTRACT)

### Tóm tắt tiếng Việt
Trong bối cảnh bùng nổ của dịch vụ tài chính số (FinTech) và ngân hàng bán lẻ, rủi ro vỡ nợ (Loan Default Risk) luôn là mối đe dọa trực tiếp đối với tính an toàn vốn và khả năng sinh lời của các tổ chức tín dụng. Phương pháp chấm điểm tín dụng truyền thống bộc lộ nhiều hạn chế về tốc độ xử lý, chi phí nhân sự và độ chính xác khi đối mặt với quy mô hồ sơ vay trực tuyến ngày càng lớn. Đề tài nghiên cứu này tập trung xây dựng một giải pháp toàn diện ứng dụng công nghệ **Dữ liệu lớn (Big Data)** trên nền tảng **Databricks Lakehouse** kết hợp thuật toán học máy phân tán **Random Forest Classifier (Spark MLlib)** nhằm tự động hóa quy trình thẩm định tín dụng và ra quyết định cấp vốn. 

Dữ liệu thực nghiệm quy mô lớn bao gồm 2,260,701 khoản vay (hơn 2.26 triệu bản ghi, 1.6 GB) từ nền tảng tín dụng LendingClub (giai đoạn 2007 - 2018Q4), được xử lý phân tán xuyên suốt qua kiến trúc Medallion 3 tầng (Bronze $\rightarrow$ Silver $\rightarrow$ Gold), áp dụng các kỹ thuật làm sạch dữ liệu, xử lý ngoại lai, kỹ nghệ đặc trưng tài chính (DTI, CBI) và phân tích bằng Spark SQL. Mô hình học máy phân tán được tinh chỉnh qua cơ chế kiểm định chéo (3-Fold Cross-Validation), đạt chỉ số phân loại vượt trội với **ROC-AUC = 0.8745**, độ nhạy phát hiện nợ xấu (Recall) đạt 84.04% và độ chính xác (Precision) đạt 66.20%. Từ kết quả xác suất vỡ nợ, đề tài xây dựng động cơ ra quyết định chuẩn hóa theo điểm tín dụng FICO Score ($300 - 850$), thiết lập ma trận phân tầng 4 nhóm rủi ro dựa trên chỉ số Youden's J Statistic và chuẩn mực Basel II, đồng thời đề xuất mô hình định giá lãi suất theo rủi ro (Risk-Based Pricing Model) với các mức lãi suất 8.5%, 11.5%, 14.5%. Hệ thống cho phép tự động hóa phê duyệt trên 75% hồ sơ vay trong thời gian dưới 3 phút, giúp giảm tỷ lệ nợ xấu tổng thể xuống dưới 4.2% và tiết kiệm hàng tỷ đồng chi phí trích lập dự phòng tổn thất tín dụng.

### Abstract in English
In the era of digital banking and FinTech expansion, loan default risk poses a critical threat to capital adequacy and profitability of credit institutions. Traditional credit underwriting methods exhibit significant drawbacks regarding turnaround time, operational costs, and subjective biases when processing surging volumes of online loan applications. This research develops an end-to-end Big Data solution utilizing the **Databricks Lakehouse Platform** combined with distributed machine learning via **Random Forest Classifier (Spark MLlib)** to automate credit scoring and loan origination decision-making. 

A large-scale empirical dataset of 2,260,701 loan records (2.26 million records, 1.6 GB) from the LendingClub platform (2007 - 2018Q4) was processed in a distributed manner across the 3-tier Medallion Architecture (Bronze $\rightarrow$ Silver $\rightarrow$ Gold), incorporating data cleaning, outlier treatment, financial feature engineering (DTI, CBI), and distributed analytics via Spark SQL. The machine learning pipeline was hyperparameter-tuned using 3-Fold Cross-Validation, achieving superior predictive power with **ROC-AUC = 0.8745**, a default recall of 84.04%, and overall accuracy of 87.16%. Based on predicted default probabilities, the system implements a decision engine that converts probabilities into standardized FICO Scores ($300 - 850$), establishes a 4-tier risk segmentation matrix underpinned by Youden's J Statistic and Basel II standards, and formulates a Risk-Based Pricing Model with suggested interest rates of 8.5%, 11.5%, and 14.5% per annum. The proposed architecture enables straight-through processing (STP) for over 75% of loan applications in under 3 minutes, effectively reducing portfolio Non-Performing Loans (NPL) below 4.2% and mitigating credit loss provisioning expenses.

\newpage

---

## MỤC LỤC BÁO CÁO (TABLE OF CONTENTS)

* **TRANG BÌA & THÔNG TIN DỰ ÁN**
* **LỜI CAM ĐOAN**
* **LỜI CẢM ƠN**
* **TÓM TẮT ĐỀ TÀI (ABSTRACT)**
* **DANH MỤC CÁC CHỮ VIẾT TẮT**
* **DANH MỤC BẢNG BIỂU**
* **DANH MỤC HÌNH VẼ & BIỂU ĐỒ**
* **CHƯƠNG 1: TỔNG QUAN VỀ BÀI TOÁN & ĐẶT VẤN ĐỀ**
  * 1.1. Bối cảnh ngành Tài chính - Ngân hàng và FinTech trong kỷ nguyên số
  * 1.2. Hạn chế của phương pháp thẩm định tín dụng truyền thống
  * 1.3. Tính cấp thiết của đề tài và Mục tiêu nghiên cứu
  * 1.4. Phân tích đặc tính Dữ liệu lớn (Big Data) theo mô hình 5Vs
  * 1.5. Giới thiệu Bộ dữ liệu nghiên cứu và Phạm vi đề tài
  * 1.6. Kết cấu tổng quan của bài tiểu luận
* **CHƯƠNG 2: KIẾN TRÚC LUỒNG DỮ LIỆU LAKEHOUSE (MEDALLION ARCHITECTURE)**
  * 2.1. Cơ sở lý luận về Kiến trúc Dữ liệu lớn: Từ Data Warehouse, Data Lake đến Lakehouse
  * 2.2. Nền tảng Apache Spark và Định dạng lưu trữ phân tán Delta Lake
  * 2.3. Thiết kế Kiến trúc Huy chương Medallion 3 tầng (Bronze - Silver - Gold)
  * 2.4. Sơ đồ luồng dữ liệu phân tán toàn diện (Data Pipeline Workflow)
  * 2.5. Quản trị dữ liệu (Data Governance) và Tuân thủ an toàn vốn theo chuẩn Basel II/III
* **CHƯƠNG 3: XỬ LÝ & PHÂN TÍCH DỮ LIỆU LỚN VỚI PYSPARK VÀ SPARK SQL**
  * 3.1. Quy trình Thu thập và Nạp dữ liệu thô (Bronze Layer Ingestion)
  * 3.2. Phương pháp Tiền xử lý và Nâng cao chất lượng Dữ liệu phân tán (Silver Layer)
  * 3.3. Kỹ nghệ đặc trưng tài chính (Financial Feature Engineering)
  * 3.4. Phân tích Khám phá Dữ liệu lớn (Exploratory Data Analysis - EDA) bằng Spark SQL
  * 3.5. Ứng dụng Window Functions trong phân tích vị thế thu nhập và rủi ro tín dụng tương đối
* **CHƯƠNG 4: XÂY DỰNG MÔ HÌNH HỌC MÁY PHÂN TÁN VỚI SPARK MLLIB**
  * 4.1. Cơ sở lý thuyết của Thuật toán Random Forest Classifier
  * 4.2. Thiết kế Chuỗi Pipeline Đặc trưng phân tán (Spark MLlib Feature Pipeline)
  * 4.3. Phương pháp Huấn luyện và Tinh chỉnh Siêu tham số (Hyperparameter Tuning)
  * 4.4. Đánh giá Đa chiều Hiệu năng Mô hình (ROC-AUC, Confusion Matrix, Precision, Recall)
  * 4.5. Phân tích Tầm quan trọng của Đặc trưng (Feature Importance Analysis)
* **CHƯƠNG 5: PHÂN TÍCH Ý NGHĨA NGHIỆP VỤ & ĐỀ XUẤT CHIẾN LƯỢC QUẢN TRỊ**
  * 5.1. Động cơ Ra quyết định: Quy đổi Điểm tín dụng FICO Score
  * 5.2. Ma trận Phân tầng Rủi ro và Cơ sở Khoa học xác lập Ngưỡng cắt
  * 5.3. Mô hình Định giá Lãi suất theo Rủi ro (Risk-Based Pricing Framework)
  * 5.4. Chính sách Hạn mức Linh hoạt và Cơ chế "Cứu khoản vay"
  * 5.5. Đánh giá Tác động Tài chính, Hiệu quả Vận hành và Lợi ích Kinh tế (ROI)
  * 5.6. Khuyến nghị Quản trị Chiến lược cho Ban Điều hành Ngân hàng và FinTech
* **TÀI LIỆU THAM KHẢO**

\newpage

---

## DANH MỤC CÁC CHỮ VIẾT TẮT (GLOSSARY OF ACRONYMS)

| Từ Viết Tắt | Tên Tiếng Anh Đầy Đủ | Nghĩa Tiếng Việt / Giải Thích |
| :--- | :--- | :--- |
| **ACID** | Atomicity, Consistency, Isolation, Durability | Bốn thuộc tính toàn vẹn của hệ quản trị cơ sở dữ liệu |
| **AI** | Artificial Intelligence | Trí tuệ nhân tạo |
| **AUC** | Area Under the ROC Curve | Diện tích dưới đường cong ROC |
| **BCBS** | Basel Committee on Banking Supervision | Ủy ban Basel về Giám sát Ngân hàng |
| **CBI** | Credit Burden Index | Chỉ số gánh nặng tín dụng có trọng số thâm niên công tác |
| **CIC** | Credit Information Center | Trung tâm Thông tin Tín dụng Quốc gia Việt Nam |
| **COF** | Cost of Funds | Chi phí huy động vốn của ngân hàng |
| **DTI** | Debt-to-Income Ratio | Tỷ lệ tổng dư nợ trên thu nhập hàng năm |
| **EAD** | Exposure at Default | Tổng dư nợ chịu rủi ro tại thời điểm vỡ nợ |
| **EL** | Expected Loss | Tổn thất tín dụng kỳ vọng ($EL = PD \times LGD \times EAD$) |
| **FICO** | Fair Isaac Corporation Score | Thang điểm tín nhiệm cá nhân tiêu chuẩn ($300 - 850$) |
| **FN** | False Negative | Sai lầm loại 2 (Dự báo không vỡ nợ nhưng thực tế vỡ nợ) |
| **FP** | False Positive | Sai lầm loại 1 (Dự báo vỡ nợ nhưng thực tế trả đúng hạn) |
| **LGD** | Loss Given Default | Tỷ lệ tổn thất thực tế khi xảy ra biến cố vỡ nợ |
| **ML** | Machine Learning | Học máy |
| **NIM** | Net Interest Margin | Biên lãi thuần của tổ chức tín dụng |
| **NPL** | Non-Performing Loan | Tỷ lệ nợ xấu (quá hạn trên 90 ngày) |
| **OPEX** | Operating Expenses | Chi phí vận hành hoạt động |
| **PD** | Probability of Default | Xác suất vỡ nợ của khoản vay |
| **ROC** | Receiver Operating Characteristic | Đường cong đặc trưng hoạt động phân loại |
| **STP** | Straight-Through Processing | Quy trình xử lý và phê duyệt tự động thông suốt |
| **TN** | True Negative | Dự báo đúng khách hàng trả nợ tốt |
| **TP** | True Positive | Dự báo chính xác khách hàng vỡ nợ |

\newpage

---

## DANH MỤC BẢNG BIỂU (LIST OF TABLES)

* **Bảng 1.1:** Phân tích đặc tính Dữ liệu lớn (Big Data) theo mô hình 5Vs trong Đề tài Chấm điểm Tín dụng.
* **Bảng 1.2:** Mô tả chi tiết 12 thuộc tính kinh tế - tài chính trong Bộ dữ liệu lớn LendingClub (2,260,701 bản ghi).
* **Bảng 2.1:** So sánh ưu nhược điểm giữa Data Warehouse, Data Lake và Databricks Lakehouse.
* **Bảng 2.2:** Phân định chức năng, nguyên tắc và công nghệ giữa 3 tầng kiến trúc Medallion (Bronze, Silver, Gold).
* **Bảng 3.1:** Kế hoạch làm sạch và chuẩn hóa dữ liệu tại Tầng Silver.
* **Bảng 3.2:** Thống kê tỷ lệ nợ xấu (NPL Rate) và quy mô tín dụng theo Mục đích sử dụng vốn (Loan Intent).
* **Bảng 3.3:** Ma trận phân bố rủi ro theo Hạng khoản vay (Loan Grade) và Tình trạng sở hữu nhà ở (Home Ownership).
* **Bảng 4.1:** Không gian tìm kiếm siêu tham số trong bộ tinh chỉnh ParamGridBuilder.
* **Bảng 4.2:** Ma trận nhầm lẫn (Confusion Matrix) của mô hình Random Forest trên tập kiểm thử 452,140 hồ sơ.
* **Bảng 4.3:** Bảng tổng hợp các chỉ số đánh giá hiệu năng phân loại (Accuracy, Precision, Recall, F1, ROC-AUC).
* **Bảng 4.4:** Xếp hạng mức độ quan trọng của các biến đặc trưng (Feature Importance Ranking).
* **Bảng 5.1:** Bảng quy đổi Log-Odds từ xác suất vỡ nợ ($p$) sang Thang điểm tín dụng FICO Score.
* **Bảng 5.2:** Ma trận Phê duyệt Tín dụng Tự động và Chính sách Hạn mức theo 4 Phân tầng Rủi ro.
* **Bảng 5.3:** Cấu thành chi phí lãi suất theo mô hình Risk-Based Pricing chuẩn mực ngân hàng.
* **Bảng 5.4:** Minh họa kết quả phê duyệt và giải ngân tự động trên 4 hồ sơ khách hàng thực tế tại Tầng Gold.

\newpage

---

## DANH MỤC HÌNH VẼ & BIỂU ĐỒ (LIST OF FIGURES)

* **Hình 2.1:** Sơ đồ kiến trúc xử lý luồng dữ liệu Lakehouse theo mô hình Huy chương Medallion (Mermaid Diagram).
* **Hình 3.1:** Đánh giá tỷ lệ dữ liệu khuyết thiếu Tầng Bronze (Missing Values Analysis).
* **Hình 3.2:** Tỷ lệ nợ xấu NPL theo Mục đích vay và Tình trạng nhà ở Tầng Silver.
* **Hình 4.1:** Đường cong ROC và so sánh hiệu năng các mô hình máy học (ROC-AUC = 0.8745).
* **Hình 4.2:** Ma trận nhầm lẫn (Confusion Matrix) của mô hình trên 452,140 hồ sơ kiểm thử.
* **Hình 5.1:** Cơ cấu phân tầng rủi ro tín dụng (Donut Chart) và Quyết định phê duyệt tự động (Bar Chart).
