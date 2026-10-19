# CHƯƠNG 1: TỔNG QUAN VỀ BÀI TOÁN & ĐẶT VẤN ĐỀ

---

## 1.1. Bối cảnh ngành Tài chính - Ngân hàng và FinTech trong kỷ nguyên số

Trong cấu trúc của nền kinh tế thị trường hiện đại, hệ thống tài chính - ngân hàng đóng vai trò huyết mạch trong việc dẫn truyền dòng vốn từ các chủ thể tiết kiệm đến các chủ thể có nhu cầu đầu tư và tiêu dùng [1]. Đặc biệt, trong những năm gần đây, phân khúc tín dụng bán lẻ (Retail Banking) và cho vay tiêu dùng tín chấp cá nhân (Consumer Lending) đã chứng kiến tốc độ tăng trưởng bùng nổ. Sự chuyển dịch mạnh mẽ từ các kênh giao dịch tại quầy truyền thống sang các nền tảng số hóa (Digital Banking, Mobile Banking và các ứng dụng Công nghệ Tài chính - FinTech) đã làm thay đổi căn bản hành vi và kỳ vọng của người tiêu dùng [2]. Khách hàng ngày nay đòi hỏi các trải nghiệm vay vốn tức thì (Instant Credit / Buy Now Pay Later - BNPL), quy trình đăng ký 100% trực tuyến và thời gian phê duyệt giải ngân chỉ tính bằng phút hoặc giây [3].

Tuy nhiên, song hành cùng cơ hội mở rộng thị phần và gia tăng thu nhập lãi thuần (Net Interest Margin - NIM), hoạt động cấp tín dụng luôn tiềm ẩn bản chất cố hữu là **rủi ro tín dụng (Credit Risk)** mà đỉnh điểm là **biến cố vỡ nợ (Loan Default)** [4]. Theo định nghĩa của Ủy ban Basel về Giám sát Ngân hàng (BCBS), biến cố vỡ nợ xảy ra khi người vay không có khả năng thực hiện nghĩa vụ trả nợ gốc hoặc lãi theo thỏa thuận hợp đồng sau một khoảng thời gian quy định (thông thường là quá hạn từ 90 ngày trở lên) [5]. Sự gia tăng của tỷ lệ nợ xấu (Non-Performing Loans - NPL) không chỉ bào mòn trực tiếp nguồn vốn tự có của tổ chức tín dụng thông qua gánh nặng trích lập chi phí dự phòng rủi ro, mà còn đe dọa đến hệ số an toàn vốn (Capital Adequacy Ratio - CAR) và tính thanh khoản của toàn bộ hệ thống ngân hàng [6].

Trước làn sóng số hóa, các định chế tài chính đối mặt với một bài toán nan giải: *Làm thế nào để vừa tối đa hóa tốc độ phê duyệt và mở rộng tệp khách hàng vay tiêu dùng số, vừa kiểm soát chặt chẽ tỷ lệ nợ xấu và bảo toàn nguồn vốn của ngân hàng?* Câu trả lời nằm ở năng lực ứng dụng công nghệ Dữ liệu lớn (Big Data) và Trí tuệ nhân tạo (AI/Machine Learning) nhằm tự động hóa quy trình thẩm định rủi ro và chấm điểm tín dụng [7].

---

## 1.2. Hạn chế của phương pháp thẩm định tín dụng truyền thống

Trong suốt nhiều thập kỷ, quy trình thẩm định tín dụng tại các ngân hàng thương mại truyền thống chủ yếu dựa trên hai phương pháp chính: phương pháp phán đoán chuyên gia (Expert Judgment) và bảng điểm tín dụng truyền thống (Traditional Scorecards xây dựng bằng hồi quy Logistic cổ điển) [8]. Mặc dù đã phục vụ tốt cho các mô hình kinh doanh truyền thống, những phương pháp này bộc lộ những khiếm khuyết mang tính hệ thống khi đối mặt với kỷ nguyên số:

1. **Thời gian thẩm định kéo dài (High Latency):** Quy trình truyền thống đòi hỏi khách hàng phải nộp nhiều loại giấy tờ chứng minh thu nhập (sao kê tài khoản ngân hàng, hợp đồng lao động, hóa đơn tiện ích), tiếp đó là quá trình thẩm định thực địa và phê duyệt qua nhiều cấp thẩm quyền. Thời gian xử lý trung bình từ 2 đến 5 ngày làm việc, hoàn toàn không tương thích với nhu cầu vay tức thì trên các nền tảng thương mại điện tử và ứng dụng di động [9].
2. **Chi phí vận hành đắt đỏ (High Operational Costs):** Việc duy trì một đội ngũ chuyên viên tín dụng đông đảo để thẩm định thủ công từng bộ hồ sơ dẫn đến chi phí vận hành (OPEX) trên mỗi khoản vay rất cao. Điều này khiến ngân hàng không thể phục vụ hiệu quả các khoản vay nhỏ lẻ (Micro-loans) do chi phí thẩm định đôi khi vượt quá cả biên lợi nhuận thu được từ khoản vay [10].
3. **Tính chủ quan và thiên vị cá nhân (Subjective Biases):** Quyết định tín dụng phụ thuộc lớn vào kinh nghiệm, tâm lý và góc nhìn chủ quan của cán bộ thẩm định, dẫn đến sự thiếu nhất quán giữa các chi nhánh hoặc các cán bộ khác nhau trong cùng một tổ chức tín dụng.
4. **Khả năng nắm bắt các mối quan hệ phi tuyến tính kém (Inability to Capture Non-linear Patterns):** Các mô hình bảng điểm tuyến tính cổ điển giả định mối quan hệ giữa các biến số là độc lập và tuyến tính. Trong thực tế, tương tác giữa các thuộc tính tài chính và nhân khẩu học (ví dụ: sự kết hợp giữa độ tuổi trẻ, thâm niên làm việc ngắn nhưng tỷ lệ nợ trên thu nhập cao) có tính phi tuyến tính và phức tạp cao mà chỉ các thuật toán học máy hiện đại mới có thể nắm bắt chính xác [11].
5. **Khó khăn trong việc mở rộng quy mô (Scalability Bottleneck):** Hệ thống truyền thống dựa trên cơ sở dữ liệu quan hệ (RDBMS) không được thiết kế để xử lý khối lượng dữ liệu khổng lồ phát sinh từ hàng chục ngàn lượt đăng ký vay mỗi ngày, dẫn đến hiện tượng tắc nghẽn cổ chai trong quá trình mở rộng kinh doanh [12].

---

## 1.3. Tính cấp thiết của đề tài và Mục tiêu nghiên cứu

### 1.3.1. Tính cấp thiết của đề tài
Nhằm giải quyết triệt để các hạn chế của quy trình truyền thống, việc xây dựng một hệ thống chấm điểm tín dụng thế hệ mới dựa trên kiến trúc **Dữ liệu lớn phân tán (Distributed Big Data Architecture)** và **Mô hình học máy tiên tiến (Advanced Machine Learning)** mang tính cấp thiết chiến lược đối với các ngân hàng thương mại và tổ chức FinTech hiện nay. Hệ thống này không chỉ giúp chuyển đổi quy trình thẩm định từ thủ công sang tự động hóa hoàn toàn (Straight-Through Processing - STP), mà còn nâng cao đáng kể độ chính xác trong việc dự báo nguy cơ vỡ nợ, bảo vệ ngân hàng trước các cú sốc tín dụng và tối ưu hóa lợi nhuận kinh doanh [13].

### 1.3.2. Mục tiêu nghiên cứu
Đề tài **"Mô hình chấm điểm tín dụng và thẩm định rủi ro vỡ nợ trong lĩnh vực Ngân hàng và FinTech"** được thực hiện nhằm đạt được các mục tiêu trọng tâm sau:

1. **Thiết kế và triển khai Kiến trúc Hồ Dữ liệu Lakehouse phân tán:** Xây dựng luồng dữ liệu tự động theo mô hình Huy chương chuẩn Medallion (Bronze $\rightarrow$ Silver $\rightarrow$ Gold) trên nền tảng Databricks Serverless và Delta Lake, đảm bảo tính toàn vẹn giao dịch ACID và khả năng mở rộng không giới hạn cho hệ thống dữ liệu lớn của ngân hàng.
2. **Tiền xử lý và Kỹ nghệ đặc trưng tài chính phân tán:** Xây dựng quy trình làm sạch dữ liệu lớn, xử lý giá trị ngoại lai, làm giàu dữ liệu và thiết lập các chỉ số tài chính chuyên sâu như Tỷ lệ nợ trên thu nhập (DTI), Chỉ số gánh nặng tín dụng (CBI) và hàm xếp hạng phân vùng (Window Functions) bằng Spark SQL.
3. **Phát triển Mô hình Học máy phân tán có hiệu năng cao:** Huấn luyện thuật toán Random Forest Classifier phân tán trên Spark MLlib, tối ưu hóa siêu tham số bằng kỹ thuật kiểm định chéo K-Fold Cross-Validation, hướng đến mục tiêu đạt chỉ số ROC-AUC vượt trội ($> 0.85$) và cân bằng tối ưu giữa độ chính xác (Precision) và độ nhạy (Recall) trong việc nhận diện nợ xấu.
4. **Xây dựng Động cơ Ra quyết định (Decision Engine) và Khung định giá theo rủi ro:** 
   - Chuẩn hóa xác suất vỡ nợ thành thang điểm FICO tiêu chuẩn ($300 - 850$).
   - Thiết lập ma trận phân tầng 4 nhóm rủi ro tín dụng dựa trên tối ưu hóa thống kê (Youden's J Statistic), phân tích tổn thất bất đối xứng và chuẩn mực an toàn vốn Basel II/III.
   - Xây dựng mô hình định giá lãi suất theo rủi ro (Risk-Based Pricing Model) với các mức lãi suất 8.5%, 11.5%, 14.5% tương ứng với từng phân khúc rủi ro.
5. **Đánh giá hiệu quả kinh tế và đề xuất chiến lược quản trị:** Định lượng tác động tài chính của mô hình đối với việc giảm thiểu tỷ lệ nợ xấu NPL, cắt giảm chi phí dự phòng rủi ro và nâng cao năng lực cạnh tranh số của định chế tài chính.

---

## 1.4. Phân tích đặc tính Dữ liệu lớn (Big Data) theo mô hình 5Vs

Để chứng minh tính xác đáng của việc áp dụng công nghệ xử lý dữ liệu lớn phân tán (Apache Spark) thay cho các công cụ xử lý đơn luồng truyền thống, bài toán chấm điểm tín dụng trong đề tài được phân tích đa chiều thông qua khung chuẩn **5Vs của Dữ liệu lớn** [14]:

**Bảng 1.1: Phân tích đặc tính Dữ liệu lớn theo mô hình 5Vs trong Đề tài Chấm điểm Tín dụng**

| Đặc tính 5Vs | Khái niệm chuẩn mực | Biểu hiện và Yêu cầu cụ thể trong Đề tài 7 | Giải pháp Công nghệ tương ứng |
| :--- | :--- | :--- | :--- |
| **Volume** *(Dung lượng)* | Khối lượng dữ liệu khổng lồ vượt quá khả năng lưu trữ và xử lý của một máy tính đơn lẻ. | Xử lý trực tiếp 2,260,701 hồ sơ vay tín dụng thực tế từ nền tảng LendingClub với dung lượng thô hơn 1.6 GB, tích lũy xuyên suốt từ năm 2007 đến 2018Q4. | Lưu trữ trên Cloud Object Storage kết hợp định dạng nén Parquet / Delta Lake trên cụm phân tán Databricks. |
| **Velocity** *(Tốc độ)* | Tốc độ phát sinh và yêu cầu xử lý dữ liệu gần thời gian thực (Real-time hoặc Near real-time). | Khách hàng nộp hồ sơ vay qua ứng dụng di động yêu cầu kết quả phê duyệt và báo lãi suất trong vòng **dưới 3 - 5 phút** thay vì chờ đợi vài ngày. | Động cơ tính toán phân tán trong bộ nhớ (In-memory Computing) của Apache Spark và PySpark MLlib Pipeline. |
| **Variety** *(Đa dạng)* | Dữ liệu phát sinh dưới nhiều định dạng khác nhau: có cấu trúc, bán cấu trúc và phi cấu trúc. | Tích hợp dữ liệu nhân khẩu học (tuổi, thâm niên), dữ liệu định lượng tài chính (thu nhập, khoản vay, lãi suất), và dữ liệu định tính (mục đích vay, tình trạng nhà ở, lịch sử CIC). | Cơ chế VectorAssembler, OneHotEncoder và Schema Enforcement của Databricks Delta Lake. |
| **Veracity** *(Độ tin cậy)* | Độ chính xác, tính nhất quán và chất lượng của nguồn dữ liệu trước khi đưa vào phân tích. | Dữ liệu đăng ký vay trực tuyến thường có nhiều giá trị thiếu (missing values), các điểm ngoại lai phi lý (tuổi > 100, thu nhập âm) do người dùng nhập sai. | Tầng dữ liệu Silver áp dụng các luật kiểm toán chất lượng dữ liệu tự động, điền khuyết thiếu bằng giá trị trung vị thị trường. |
| **Value** *(Giá trị kinh tế)* | Khả năng biến đổi nguồn dữ liệu thô thành lợi ích tài chính và giá trị kinh doanh thực tiễn. | Chuyển đổi hồ sơ dữ liệu thành quyết định duyệt vay tự động, cắt giảm hàng chục tỷ đồng nợ xấu và chi phí trích lập dự phòng tổn thất tín dụng. | Động cơ Phân tầng Rủi ro, Quy đổi FICO Score và Mô hình Định giá Lãi suất theo rủi ro (Risk-Based Pricing). |

---

## 1.5. Giới thiệu Bộ dữ liệu nghiên cứu và Phạm vi đề tài

### 1.5.1. Nguồn gốc dữ liệu LendingClub quy mô 2.26 triệu bản ghi
Đáp ứng yêu cầu khắt khe của một đề tài Dữ liệu lớn (Big Data Analytics), nghiên cứu sử dụng bộ dữ liệu thực tế **LendingClub Complete Loan Dataset (2007 - 2018Q4)** được công bố bởi LendingClub - nền tảng tài chính cho vay ngang hàng (P2P Lending) lớn nhất thế giới có trụ sở tại San Francisco, Hoa Kỳ [14]. Bộ dữ liệu phản ánh toàn diện hành vi vay vốn và trả nợ của **2,260,701 khoản vay thực tế (hơn 2.26 triệu hồ sơ, kích thước tệp hơn 1.6 GB)**. 

Đây là tập dữ liệu chuẩn mực (Gold Standard Benchmark) được cộng đồng khoa học quốc tế và các trường đại học tài chính hàng đầu sử dụng trong việc nghiên cứu mô hình chấm điểm tín dụng và thẩm định rủi ro tín dụng cá nhân.

### 1.5.2. Cấu trúc các thuộc tính cốt lõi trong bộ dữ liệu
Từ 151 biến số của LendingClub, hệ thống trích xuất và chuẩn hóa **12 thuộc tính cốt lõi** đại diện cho năng lực tài chính, mục đích vay, lịch sử tín dụng CIC và nhãn mục tiêu:

**Bảng 1.2: Mô tả chi tiết các thuộc tính cốt lõi trong Bộ dữ liệu lớn LendingClub (2,260,701 bản ghi)**

| STT | Tên Thuộc Tính Trong Pipeline | Tên Gốc LendingClub | Kiểu Dữ Liệu | Định Nghĩa Nghiệp Vụ & Ý Nghĩa Kinh Tế |
| :-: | :--- | :--- | :---: | :--- |
| 1 | `loan_amnt` | `loan_amnt` | Số thực | Số tiền khách hàng được phê duyệt vay (USD). |
| 2 | `person_income` | `annual_inc` | Số thực | Tổng thu nhập hàng năm của người đi vay (USD). |
| 3 | `loan_int_rate` | `int_rate` | Số thực | Lãi suất danh nghĩa hàng năm của khoản vay (%). |
| 4 | `loan_grade` | `grade` | Chuỗi danh mục | Xếp hạng tín nhiệm nội bộ từ `A` (an toàn nhất) đến `G` (rủi ro cao nhất). |
| 5 | `person_home_ownership` | `home_ownership` | Chuỗi danh mục | Tình trạng nhà ở (`RENT`: Thuê nhà; `OWN`: Sở hữu; `MORTGAGE`: Thế chấp). |
| 6 | `person_emp_length` | `emp_length` | Số thực | Thâm niên công tác liên tục (năm: từ $0$ đến $10+$ năm). |
| 7 | `loan_intent` | `purpose` | Chuỗi danh mục | Mục đích vay vốn (`debt_consolidation`, `credit_card`, `home_improvement`, `medical`, `small_business`,...). |
| 8 | `loan_percent_income` | `dti` | Số thực | Tỷ lệ nợ trên thu nhập ($DTI$ hàng năm). |
| 9 | `cb_person_default_on_file`| `pub_rec_bankruptcies`| Chuỗi danh mục | Tiền sử nợ xấu hoặc phá sản ghi nhận trên hệ thống tín dụng (`Y`: Có, `N`: Không). |
| 10 | `person_age` | Suy diễn từ `earliest_cr_line` | Số nguyên | Độ tuổi của người đi vay (ước tính từ lịch sử tín dụng). |
| 11 | `cb_person_cred_hist_length`| `earliest_cr_line` | Số nguyên | Thâm niên quan hệ tín dụng (năm). |
| 12 | **`loan_status` (Label)** | `loan_status` | Số nguyên | Nhãn phân loại: `0` đại diện cho Khoản vay trả đủ (`Fully Paid`); `1` đại diện cho Khoản vay vỡ nợ / xóa nợ (`Charged Off` / `Default`). |

### 1.5.3. Tỷ lệ nợ xấu nền trên quy mô 2.26 triệu hồ sơ (Baseline Default Rate)
Trong tổng số 2,260,701 khoản vay, sau khi lọc các khoản vay đã kết thúc chu kỳ thanh toán (hoàn thành nghĩa vụ hoặc xóa sổ do mất vốn), có khoảng 493,285 khoản vay bị vỡ nợ (`loan_status = 1`) trên tổng số 2,260,701 hồ sơ, thiết lập tỷ lệ nợ xấu nền thực tế là:
$$\text{Baseline Default Rate} = \frac{493,285}{2,260,701} \approx 0.2182$$
*(tương đương 21.82%)*

Quy mô dữ liệu hơn 2.26 triệu dòng mang lại độ tin cậy thống kê vượt trội, loại bỏ hoàn toàn các sai số do mẫu nhỏ và chứng minh năng lực tính toán phân tán của nền tảng Apache Spark.

---

## 1.6. Kết cấu tổng quan của bài tiểu luận

Báo cáo tiểu luận được tổ chức chặt chẽ thành 5 chương nghiên cứu chính:

* **Chương 1: Tổng quan về bài toán & Đặt vấn đề:** Trình bày bối cảnh kinh tế, các hạn chế của quy trình thẩm định tín dụng truyền thống, tính cấp thiết, mục tiêu nghiên cứu, phân tích bài toán theo khung 5Vs của Dữ liệu lớn và giới thiệu tổng quan bộ dữ liệu nghiên cứu.
* **Chương 2: Kiến trúc luồng dữ liệu Lakehouse (Medallion Architecture):** Phân tích nền tảng lý thuyết của kiến trúc Databricks Lakehouse, các ưu điểm công nghệ của Delta Lake (ACID, Time Travel, Parquet), chi tiết thiết kế 3 tầng Bronze - Silver - Gold và cơ chế quản trị dữ liệu theo chuẩn Basel II/III.
* **Chương 3: Xử lý & Phân tích dữ liệu lớn với PySpark và Spark SQL:** Trình bày phương pháp luận và kỹ thuật làm sạch dữ liệu lớn, xử lý khuyết thiếu và ngoại lai, kỹ nghệ đặc trưng tài chính (DTI, CBI), phân tích khám phá dữ liệu (EDA) và ứng dụng Window Functions để đánh giá tương đối rủi ro tín dụng.
* **Chương 4: Xây dựng mô hình học máy phân tán với Spark MLlib:** Trình bày cơ sở lý thuyết của thuật toán Random Forest Classifier, chuỗi pipeline đóng gói đặc trưng phân tán, quy trình tối ưu hóa siêu tham số bằng kiểm định chéo K-Fold Cross-Validation, đánh giá toàn diện hiệu năng phân loại qua đường cong ROC, ma trận nhầm lẫn và phân tích độ quan trọng của đặc trưng.
* **Chương 5: Phân tích ý nghĩa nghiệp vụ & Đề xuất chiến lược quản trị:** Trình bày thuật toán quy đổi điểm tín dụng FICO Score, ma trận phân tầng 4 nhóm rủi ro dựa trên cơ sở Youden's J và Basel II, mô hình định giá lãi suất theo rủi ro (Risk-Based Pricing), chính sách hạn mức tín dụng linh hoạt, định lượng tác động tài chính (ROI) và các khuyến nghị quản trị chiến lược cho ban điều hành ngân hàng.
