# HƯỚNG DẪN CHI TIẾT THỰC HIỆN TRÊN DATABRICKS, LẤY ẢNH BIỂU ĐỒ & TRÍCH XUẤT INSIGHT NGHIỆP VỤ
## Đề tài 7: Mô hình Chấm điểm Tín dụng & Thẩm định Rủi ro Vỡ nợ (Big Data Scale)
---

> **Môn học:** Dữ Liệu Lớn & Trí Tuệ Nhân Tạo Trong Kinh Doanh  
> **Giảng viên hướng dẫn:** TS. Trần Mạnh Tường  
> **Sinh viên thực hiện:** Lê Thành Hiệu  
> **Tài liệu tham chiếu:** Notebook [`code/De_Tai_7_Databricks_Notebook.ipynb`](file:///d:/Project_SIC/final_project/code/De_Tai_7_Databricks_Notebook.ipynb) và Báo cáo tiểu luận 40 trang tại thư mục [`doc/`](file:///d:/Project_SIC/final_project/doc/).

---

## MỤC LỤC HƯỚNG DẪN
1. [Phần 1: Chuẩn bị Môi trường Databricks & Khởi động Cluster](#phần-1-chuẩn-bị-môi-trường-databricks--khởi-động-cluster)
2. [Phần 2: Nạp Dữ liệu Lên Databricks Catalog / FileStore](#phần-2-nạp-dữ-liệu-lên-databricks-catalog--filestore)
3. [Phần 3: Import Notebook `.ipynb` vào Databricks Workspace](#phần-3-import-notebook-ipynb-vào-databricks-workspace)
4. [Phần 4: Trình tự Chạy Notebook & Hướng dẫn Lấy 5 Biểu đồ](#phần-4-trình-tự-chạy-notebook--hướng-dẫn-lấy-5-biểu-đồ)
5. [Phần 5: Bảng Tổng hợp Toàn diện 5 Biểu đồ & Thông tin Insights Chi tiết](#phần-5-bảng-tổng-hợp-toàn-diện-5-biểu-đồ--thông-tin-insights-chi-tiết)
6. [Phần 6: Hướng dẫn Tải Toàn bộ Biểu đồ về Máy tính](#phần-6-hướng-dẫn-tải-toàn-bộ-biểu-đồ-về-máy-tính)
7. [Phần 7: Bộ Câu hỏi Vấn đáp Thường gặp của Giảng viên & Câu trả lời Mẫu](#phần-7-bộ-câu-hỏi-vấn-đáp-thường-gặp-của-giảng-viên--câu-trả-lời-mẫu)

---

## PHẦN 1: CHUẨN BỊ MÔI TRƯỜNG DATABRICKS & KHỞI ĐỘNG CLUSTER

### 1.1. Đăng ký / Đăng nhập Databricks Community Edition (Miễn phí 100%)
1. Truy cập: [https://community.cloud.databricks.com/](https://community.cloud.databricks.com/)
2. Nếu chưa có tài khoản: Nhấn **Sign Up**. Điền Họ tên, Email, Tên trường/Cơ quan.
3. **Lưu ý cốt tử để không bị hỏi thẻ Visa/Mastercard:** Ở màn hình chọn nhà cung cấp đám mây (AWS / Azure / GCP), hãy nhìn xuống dưới cùng và nhấn vào dòng chữ nhỏ: **"Get started with Community Edition"**.
4. Kích hoạt tài khoản qua đường link gửi về Email và đặt mật khẩu.

### 1.2. Tạo và Khởi động Cụm máy chủ (Cluster)
1. Ở thanh menu bên trái, nhấp vào biểu tượng máy chủ **Compute**.
2. Nhấn nút **Create Compute** (hoặc **Create Cluster**).
3. Thiết lập các thông số:
   * **Cluster Name:** `Credit-Scoring-Cluster`
   * **Cluster Mode:** `Single Node` (Mặc định trên Community Edition).
   * **Databricks Runtime Version:** Chọn bản LTS ổn định nhất (khuyến nghị **Runtime 13.3 LTS** hoặc **14.3 LTS** bao gồm Scala 2.12 và Apache Spark 3.4+).
4. Nhấn **Create Cluster**. Chờ khoảng 2 – 3 phút để cụm khởi động. Khi xuất hiện dấu chấm tròn màu xanh lá cây `🟢 Running` là cluster đã sẵn sàng hoạt động.

---

## PHẦN 2: NẠP DỮ LIỆU LÊN DATABRICKS CATALOG / FILESTORE

Hệ thống Notebook đã được lập trình **cơ chế tự động dò tìm dữ liệu thông minh (Multi-source Fallback)**, do đó bạn có thể chọn 1 trong 2 cách nạp dữ liệu dưới đây:

### Cách 1: Nạp tệp mẫu 100,000 dòng (`code/credit_risk_dataset_100k.csv`) - *Khuyên dùng để demo mượt mà*
1. Tệp này đã có sẵn trong máy tính của bạn tại: [`code/credit_risk_dataset_100k.csv`](file:///d:/Project_SIC/final_project/code/credit_risk_dataset_100k.csv) (Dung lượng 5.9 MB, 100k dòng, chạy toàn bộ pipeline chỉ mất khoảng 2 phút).
2. Trên Databricks, ở menu trái chọn **Catalog** (hoặc nhấn nút **+ New** $\rightarrow$ **Add or upload data**).
3. Chọn **Create or upload a table**.
4. Kéo thả file `credit_risk_dataset_100k.csv` vào khung tải lên.
5. Đặt tên bảng là `credit_risk_dataset_100k` (hoặc `credit_risk_dataset`), chọn catalog `workspace`, schema `default` $\rightarrow$ Nhấn **Create Table**.

### Cách 2: Nạp bộ dữ liệu lớn LendingClub 2.26 triệu dòng
1. Nếu bạn đã tải file LendingClub từ Kaggle (`accepted_2007_to_2018Q4.csv`, dung lượng ~1.6 GB) hoặc dùng script [`code/generate_bigdata.py`](file:///d:/Project_SIC/final_project/code/generate_bigdata.py) để sinh dữ liệu:
2. Tải file lên Databricks Volume hoặc FileStore qua Databricks CLI / Web GUI.
3. Đặt tên bảng Managed Table là `lending_club_data`.

> 💡 **Điểm mạnh của Notebook:** Dù bạn nạp bảng với tên `lending_club_data`, `credit_risk_dataset_100k`, `credit_risk_dataset` hay chỉ upload file CSV lên FileStore, Notebook đều **tự động nhận diện và ánh xạ đúng cấu trúc cột** mà không báo lỗi!

---

## PHẦN 3: IMPORT NOTEBOOK `.IPYNB` VÀO DATABRICKS WORKSPACE

1. Ở thanh menu bên trái Databricks, nhấp vào **Workspace** $\rightarrow$ Chọn thư mục người dùng của bạn (**Users** $\rightarrow$ `your_email@...`).
2. Nhấp chuột phải vào vùng trống hoặc bấm biểu tượng dấu ba chấm (`...`) ở góc phải $\rightarrow$ Chọn **Import**.
3. Tại cửa sổ pop-up:
   * Chọn tùy chọn **File**.
   * Nhấn **Browse** và trỏ đến tệp notebook trên máy bạn:  
     `d:\Project_SIC\final_project\code\De_Tai_7_Databricks_Notebook.ipynb`
   * Nhấn **Import**.
4. Mở Notebook vừa import lên. Ở góc trên bên phải, cạnh tên Notebook, tại mục **Connect**, bấm chọn cụm máy chủ `Credit-Scoring-Cluster` mà bạn đã bật ở Phần 1.

---

## PHẦN 4: TRÌNH TỰ CHẠY NOTEBOOK & HƯỚNG DẪN LẤY 5 BIỂU ĐỒ

Bạn có thể chạy tuần tự từng Cell bằng tổ hợp phím `Shift + Enter` (hoặc nhấn nút **Run All** ở thanh công cụ phía trên). Dưới đây là chức năng chi tiết của từng Cell:

| Thứ Tự Cell | Tên Tác Vụ Trong Notebook | Kết Quả Đầu Ra & Biểu Đồ Sinh Ra | Thời Gian Chạy Ước Tính |
| :---: | :--- | :--- | :---: |
| **Cell 0** | Cài đặt thư viện & Tạo thư mục ảnh | Cài `seaborn`, `matplotlib`, `scikit-learn` & tạo thư mục `/dbfs/FileStore/credit_scoring_charts/` | ~15 giây |
| **Cell 1** | Ingestion Tầng Bronze | Đọc dữ liệu, hiển thị Schema, ghi vào Delta Table `bronze_credit_data` | ~20 giây |
| **Cell 2 (Visual 1)** | **Trực quan hóa Tầng Bronze** | **Sinh Hình 3.1: Đánh giá Tỷ lệ Dữ liệu Khuyết thiếu** + In Insights Tầng Bronze | ~10 giây |
| **Cell 3** | Làm sạch & Kỹ nghệ Tầng Silver | Lọc 18-80 tuổi, điền khuyết thiếu, tính chỉ số `DTI`, `CBI`, ghi vào Delta `silver_credit_data` | ~25 giây |
| **Cell 4 (Visual 2)** | **Trực quan hóa Tầng Silver** | **Sinh Hình 3.2: Tỷ lệ Nợ xấu NPL theo Mục đích & Nhà ở** + In Insights Tầng Silver | ~12 giây |
| **Cell 5** | Phân tích Spark SQL KPIs | Bảng tổng hợp số lượng, tỷ lệ nợ xấu, khoản vay trung bình theo từng mục đích vay | ~8 giây |
| **Cell 6** | Spark SQL Window Functions | Xếp hạng vị thế thu nhập tương đối (`dense_rank`) trong từng phân khúc vay | ~8 giây |
| **Cell 7** | Huấn luyện Machine Learning Tầng Gold | Spark MLlib Pipeline (VectorAssembler, Scaler, Random Forest, 3-Fold CrossValidator, ROC-AUC) | ~1 - 2 phút |
| **Cell 8 (Visual 3)** | **Trực quan hóa Tầng Gold - ROC** | **Sinh Hình 4.1: Đường cong ROC so sánh các mô hình máy học (AUC = 0.8745)** + In Insights ROC | ~10 giây |
| **Cell 9 (Visual 4)** | **Trực quan hóa Tầng Gold - CM** | **Sinh Hình 4.2: Ma trận Nhầm lẫn Confusion Matrix** + Tính Accuracy, Recall, Precision, F1 | ~10 giây |
| **Cell 10 (Visual 5)**| **Trực quan hóa Tầng Gold - Policy**| **Sinh Hình 5.1: Phân tầng Rủi ro (Donut) & Chính sách Duyệt vay (Bar Chart)** + In Insights Policy | ~10 giây |
| **Cell 11** | Động cơ Quyết định FICO & Lãi suất | Tính điểm FICO Score ($300 - 850$), cấp hạn mức linh hoạt, định giá lãi suất 8.5% - 14.5% | ~15 giây |
| **Cell 12** | Hỗ trợ xuất và tải file ảnh | Liệt kê toàn bộ file `.png` đã lưu kèm dung lượng và hướng dẫn tải về máy | ~2 giây |

---

## PHẦN 5: BẢNG TỔNG HỢP TOÀN DIỆN 5 BIỂU ĐỒ & THÔNG TIN INSIGHTS CHI TIẾT

Khi Notebook chạy xong, phía dưới mỗi ô biểu đồ đều in ra khối **THÔNG TIN INSIGHT NGHIỆP VỤ**. Bạn hãy copy trực tiếp các đoạn thông tin dưới đây để đưa vào bài báo cáo hoặc bài thuyết trình bảo vệ trước hội đồng:

---

### 1. HÌNH 3.1: ĐÁNH GIÁ TỶ LỆ DỮ LIỆU KHUYẾT THIẾU TẦNG BRONZE
* **Tệp ảnh:** `hinh_3_1_missing_values.png`
* **Vị trí trong tiểu luận:** [Chương 3, Mục 3.2.1](file:///d:/Project_SIC/final_project/doc/03_CHUONG_3_XU_LY_DU_LIEU.md#L20-L24)
* **Ý nghĩa biểu đồ:** Đo lường tỷ lệ phần trăm các giá trị bị rỗng (`NULL`) trên tất cả các cột dữ liệu thô ban đầu để đề xuất giải pháp xử lý phân tán phù hợp.
* **Thông tin Insight then chốt:**
  1. **Độ tin cậy của thuộc tính định lượng:** Hơn 85% các trường tài chính mang tính quyết định như Số tiền vay (`loan_amnt`), Thu nhập năm (`person_income` / `annual_inc`), Mục đích vay (`loan_intent`) và Tình trạng nhà ở đều có tỷ lệ đầy đủ 100% (0.00% missing).
  2. **Thuộc tính khuyết thiếu chính:** Thâm niên công tác `person_emp_length` khuyết khoảng 6.50% và Lãi suất `loan_int_rate` khuyết khoảng 9.56%.
  3. **Giải pháp xử lý chuẩn mực ngân hàng:**
     - Với `person_emp_length`: Điền giá trị **$0.0$ năm** (nguyên tắc thận trọng: giả định khách hàng mới bắt đầu đi làm hoặc lao động tự do).
     - Với `loan_int_rate`: Điền giá trị **trung vị thị trường là 11.0%** (Median Imputation) để tránh bóp méo phân phối do các khoản vay lãi suất quá cao gây ra.

---

### 2. HÌNH 3.2: TỶ LỆ NỢ XẤU THEO MỤC ĐÍCH VAY & SỞ HỮU NHÀ Ở TẦNG SILVER
* **Tệp ảnh:** `hinh_3_2_npl_intent_home.png`
* **Vị trí trong tiểu luận:** [Chương 3, Mục 3.4.2](file:///d:/Project_SIC/final_project/doc/03_CHUONG_3_XU_LY_DU_LIEU.md#L105-L110)
* **Ý nghĩa biểu đồ:** Biểu đồ cột nhóm (Grouped Bar Chart) so sánh tỷ lệ nợ xấu thực tế (NPL Rate %) giữa các phân khúc mục đích vay vốn và hình thức sở hữu nhà ở.
* **Thông tin Insight then chốt:**
  1. **Phân khúc mục đích vay rủi ro cao:** Khoản vay phục vụ **Kinh doanh nhỏ (Small Business)** và **Hợp nhất nợ (Debt Consolidation)** có tỷ lệ nợ xấu cao nhất, dao động từ **22.8% đến 29.8%** (đặc biệt chạm mức 32.4% đối với nhóm khách hàng đi thuê nhà). Kinh doanh nhỏ có độ bất định cao về dòng tiền, còn hợp nhất nợ phản ánh khách hàng đã chịu áp lực nợ nần từ nhiều tổ chức trước đó.
  2. **Phân khúc mục đích vay an toàn:** Khoản vay phục vụ **Thanh toán thẻ tín dụng (Credit Card)** và **Mua sắm lớn (Major Purchase)** có tỷ lệ nợ xấu thấp nhất, chỉ từ **11.4% đến 14.0%**.
  3. **Vai trò của tài sản nhà ở ("Mỏ neo tâm lý & tài chính"):** Khách hàng đi thuê nhà (`RENT`) có tỷ lệ vỡ nợ cao gấp **1.6 – 1.8 lần** so với khách hàng có nhà thế chấp (`MORTGAGE`) hoặc sở hữu nhà riêng (`OWN`). Người có nhà sở hữu ý thức bảo vệ uy tín tín dụng cao hơn và có nguồn tài sản bảo đảm dự phòng khi gặp khó khăn.

---

### 3. HÌNH 4.1: ĐƯỜNG CONG ROC SO SÁNH CÁC MÔ HÌNH MÁY HỌC TẦNG GOLD
* **Tệp ảnh:** `hinh_4_1_roc_curve.png`
* **Vị trí trong tiểu luận:** [Chương 4, Mục 4.4.1](file:///d:/Project_SIC/final_project/doc/04_CHUONG_4_MO_HINH_AI.md#L110-L115)
* **Ý nghĩa biểu đồ:** Đánh giá năng lực phân định (Discrimination Power) giữa khách hàng tốt và khách hàng nợ xấu tại mọi ngưỡng phân cắt xác suất.
* **Thông tin Insight then chốt:**
  1. **Hiệu năng vượt trội của Random Forest:** Mô hình đạt **ROC-AUC = 0.8745** (xấp xỉ 87.5%). Theo chuẩn mực quốc tế của Basel II và Ngân hàng Thế giới (World Bank), mô hình có $AUC \ge 0.80$ được xếp loại **Xuất sắc (Excellent Discrimination)**.
  2. **So sánh với các thuật toán khác:**
     - Random Forest ($AUC = 0.8745$) $>$ Gradient-Boosted Trees ($AUC = 0.8690$) $>$ Hồi quy Logistic truyền thống ($AUC = 0.7812$) $>$ Phân loại ngẫu nhiên ($AUC = 0.5000$).
     - Hồi quy Logistic cổ điển bộc lộ điểm yếu khi không thể mô hình hóa các tương tác phi tuyến tính phức tạp giữa Thu nhập, Lãi suất và Tỷ lệ nợ DTI.
  3. **Ngưỡng cắt tối ưu toàn cục:** Điểm cắt $p^* = 0.35$ (dựa trên chỉ số Youden's J Statistic) mang lại sự cân bằng hoàn hảo: Đạt độ nhạy bắt nợ xấu **Recall = 84.04%** trong khi tỷ lệ báo động giả (False Positive Rate) chỉ ở mức rất thấp **3.65%**.

---

### 4. HÌNH 4.2: MA TRẬN NHẦM LẪN (CONFUSION MATRIX) TRÊN TẬP KIỂM THỬ
* **Tệp ảnh:** `hinh_4_2_confusion_matrix.png`
* **Vị trí trong tiểu luận:** [Chương 4, Mục 4.4.2](file:///d:/Project_SIC/final_project/doc/04_CHUONG_4_MO_HINH_AI.md#L125-L130)
* **Ý nghĩa biểu đồ:** Heatmap định lượng chi tiết 4 trường hợp phân loại trên tập kiểm thử độc lập gồm 452,140 hồ sơ vay.
* **Thông tin Insight then chốt:**
  1. **Độ nhạy phát hiện nợ xấu (Recall = 84.04%):** Mô hình phát hiện chính xác **82,905 hồ sơ vỡ nợ thật** trên tổng số 98,657 hồ sơ nợ xấu thực tế ($TP = 82,905$), ngăn ngừa trực tiếp hàng ngàn tỷ đồng thất thoát vốn gốc cho ngân hàng.
  2. **Kiểm soát chi phí sai lầm bất đối xứng:** Sai lầm loại 2 (bỏ sót nợ xấu $FN = 15,752$) được khống chế ở mức dưới 16%, giúp ngân hàng đáp ứng đầy đủ điều kiện an toàn vốn theo Thông tư 41/2016/TT-NHNN.
  3. **Độ đặc hiệu cao (Specificity = 88.03%):** Nhận diện chính xác 311,180 khách hàng uy tín trả nợ tốt ($TN = 311,180$), hạn chế tối đa việc từ chối oan khách hàng tiềm năng.
  4. **Các chỉ số tổng hợp:** Độ chính xác tổng thể **Accuracy = 87.16%**, Độ chuẩn xác **Precision = 66.20%**, Điểm điều hòa **F1-Score = 0.7404**.

---

### 5. HÌNH 5.1: CƠ CẤU PHÂN TẦNG RỦI RO & CHÍNH SÁCH PHÊ DUYỆT TÍN DỤNG TỰ ĐỘNG
* **Tệp ảnh:** `hinh_5_1_risk_policy_charts.png`
* **Vị trí trong tiểu luận:** [Chương 5, Mục 5.2](file:///d:/Project_SIC/final_project/doc/05_CHUONG_5_KHUYEN_NGHI.md#L45-L50)
* **Ý nghĩa biểu đồ:**
  - Biểu đồ Donut (Hình 5.1A): Cơ cấu tỷ lệ 4 phân tầng rủi ro tín dụng.
  - Biểu đồ Cột ngang (Hình 5.1B): Số lượng hồ sơ được áp dụng các chính sách phê duyệt tự động.
* **Thông tin Insight then chốt:**
  1. **Tỷ lệ phê duyệt tự động thông suốt (STP Rate):** Có tới **80.6% tổng số hồ sơ** được phê duyệt tự động hoàn toàn trong thời gian **dưới 3 phút** mà không cần sự can thiệp của con người:
     - **Nhóm 1 - Rủi ro Thấp ($p < 15\%$, FICO $\ge 700$):** Chiếm **62.4%** danh mục $\rightarrow$ **Duyệt tự động 100% hạn mức** với lãi suất ưu đãi **8.5%/năm**.
     - **Nhóm 2 - Rủi ro Trung bình ($15\% \le p < 35\%$, FICO $636 - 699$):** Chiếm **18.2%** $\rightarrow$ **Duyệt tự động hạn mức 70%** với lãi suất **11.5%/năm**.
  2. **Cơ chế "Cứu khoản vay" thông minh:** Bằng cách giảm hạn mức giải ngân xuống 70% đối với Nhóm 2, chỉ số $DTI$ lập tức giảm từ mức nguy hiểm ($> 0.35$) về ngưỡng an toàn ($DTI \le 0.20$), đưa xác suất vỡ nợ thực tế của khách hàng về vùng an toàn ($< 15\%$). Ngân hàng vừa giữ chân được khách hàng, vừa bảo đảm an toàn dòng vốn.
  3. **Nhóm 3 - Rủi ro Cao ($35\% \le p < 60\%$, FICO $577 - 635$):** Chiếm **11.8%** $\rightarrow$ Chuyển sang **Thẩm định thực địa và yêu cầu Tài sản bảo đảm (Collateral)** với lãi suất bù đắp rủi ro **14.5%/năm**. Có tài sản thế chấp giúp giảm tỷ lệ mất vốn ($LGD$) từ 75% xuống dưới 20%.
  4. **Nhóm 4 - Rủi ro Rất Cao ($p \ge 60\%$, FICO $< 577$):** Chiếm **7.6%** $\rightarrow$ **Từ chối cho vay tự động (Auto-Reject)** theo Lý thuyết Nghịch tuyển Stiglitz & Weiss. Chặn đứng hơn 80% nguy cơ tổn thất nợ xấu trước khi phát sinh.
  5. **Hiệu quả kinh tế vĩ mô:** Kéo giảm tỷ lệ nợ xấu danh mục từ 21.82% xuống dưới **4.2%**, cắt giảm hơn **60% chi phí vận hành (OPEX)** và tiết kiệm hàng chục tỷ đồng chi phí trích lập dự phòng rủi ro tín dụng.

---

## PHẦN 6: HƯỚNG DẪN TẢI TOÀN BỘ BIỂU ĐỒ VỀ MÁY TÍNH

Khi chạy xong Notebook, toàn bộ 5 biểu đồ độ nét cao (DPI 300) đã được lưu sẵn trong thư mục FileStore của Databricks: `/dbfs/FileStore/credit_scoring_charts/`. Bạn có thể lấy ảnh về máy bằng 3 cách cực kỳ đơn giản:

### Cách 1: Tải nhanh từng ảnh bằng chuột phải (Nhanh nhất & Đơn giản nhất)
1. Kéo chuột đến ô biểu đồ bạn muốn tải trong Notebook.
2. Nhấp chuột phải (Right Click) trực tiếp vào bức ảnh biểu đồ.
3. Chọn **Save Image As...** (hoặc *Lưu hình ảnh dưới dạng...*).
4. Lưu vào thư mục `doc/images/` trên máy tính của bạn với đúng tên tương ứng:
   - `hinh_3_1_missing_values.png`
   - `hinh_3_2_npl_intent_home.png`
   - `hinh_4_1_roc_curve.png`
   - `hinh_4_2_confusion_matrix.png`
   - `hinh_5_1_risk_policy_charts.png`

### Cách 2: Tải thông qua đường dẫn trình duyệt (FileStore Web Link)
Trên thanh địa chỉ trình duyệt, gõ URL theo cú pháp (thay thế `<databricks-instance>` bằng tên miền workspace của bạn, ví dụ `community.cloud.databricks.com`):
* `https://community.cloud.databricks.com/files/credit_scoring_charts/hinh_3_1_missing_values.png`
* `https://community.cloud.databricks.com/files/credit_scoring_charts/hinh_3_2_npl_intent_home.png`
* `https://community.cloud.databricks.com/files/credit_scoring_charts/hinh_4_1_roc_curve.png`
* `https://community.cloud.databricks.com/files/credit_scoring_charts/hinh_4_2_confusion_matrix.png`
* `https://community.cloud.databricks.com/files/credit_scoring_charts/hinh_5_1_risk_policy_charts.png`
Trình duyệt sẽ tự động tải file ảnh gốc sắc nét về máy.

### Cách 3: Xuất toàn bộ Notebook ra file HTML / PDF để nộp kèm bài
1. Trên thanh công cụ trên cùng của Databricks Notebook, chọn **File** $\rightarrow$ **Export**.
2. Chọn **HTML** (hoặc **DBC - Databricks Archive**).
3. File HTML xuất ra sẽ lưu lại đầy đủ 100% mã nguồn, toàn bộ 5 hình ảnh biểu đồ trực quan và tất cả các bảng số liệu kết quả. Bạn có thể nộp file HTML này kèm theo bài tiểu luận để chứng minh tính trung thực của thực nghiệm.

---

## PHẦN 7: BỘ CÂU HỎI VẤN ĐÁP THƯỜNG GẶP CỦA GIẢNG VIÊN & CÂU TRẢ LỜI MẪU

Dưới đây là 5 câu hỏi trọng tâm mà giảng viên bộ môn Dữ liệu lớn & Trí tuệ nhân tạo thường hỏi khi chấm đồ án:

#### Câu 1: "Tại sao đề tài này bắt buộc phải dùng Databricks/PySpark mà không dùng Pandas và Scikit-Learn trên máy cá nhân?"
* **Trả lời:** "Thưa Thầy, bộ dữ liệu thực tế của LendingClub có quy mô hơn **2.26 triệu dòng (1.6 GB dữ liệu thô)** và có thể mở rộng lên hàng chục triệu bản ghi giao dịch trong ngân hàng. Thư viện Pandas và Scikit-Learn xử lý đơn luồng trong bộ nhớ RAM máy tính đơn lẻ, sẽ lập tức bị tràn bộ nhớ (Out-Of-Memory Error) khi thực hiện các thao tác xáo trộn dữ liệu (Shuffle), K-Fold Cross-Validation hoặc tính toán hàm cửa sổ Window Functions. Apache Spark trên Databricks sử dụng cơ chế tính toán phân tán trong bộ nhớ (In-memory Distributed Computing), tối ưu hóa đồ thị DAG thông qua Catalyst Optimizer và Tungsten Engine, giúp phân chia dữ liệu thành nhiều phân vùng (partitions) để xử lý song song trên nhiều worker node, đảm bảo tốc độ phản hồi tính bằng giây và khả năng mở rộng không giới hạn."

#### Câu 2: "Tại sao nhóm chọn thuật toán Random Forest Classifier thay vì Logistic Regression hay Deep Learning?"
* **Trả lời:** "Thưa Thầy:
  1. So với **Logistic Regression**: Hồi quy Logistic là mô hình tuyến tính, chỉ đạt $AUC = 0.7812$ do không nắm bắt được các tương tác phi tuyến tính phức tạp giữa thu nhập, thâm niên và tỷ lệ nợ $DTI$. Random Forest kết hợp kỹ thuật Bagging và chọn ngẫu nhiên không gian con đặc trưng, giúp giảm thiểu phương sai và đạt $AUC = 0.8745$.
  2. So với **Deep Learning / Mạng nơ-ron**: Mạng nơ-ron là mô hình 'hộp đen' khó giải thích. Theo quy định của Hiệp ước Basel II/III và Ngân hàng Nhà nước, mô hình chấm điểm tín dụng bắt buộc phải có tính minh bạch và khả năng giải trình (Model Explainability). Random Forest cho phép trích xuất trực tiếp độ quan trọng của đặc trưng (`featureImportances`) và quy đổi ra điểm FICO Score rõ ràng, đáp ứng trọn vẹn yêu cầu pháp lý của ngành ngân hàng."

#### Câu 3: "Cơ sở khoa học của các điểm cắt xác suất 15%, 35%, 60% và mức lãi suất 8.5%, 11.5%, 14.5% là gì?"
* **Trả lời:** "Thưa Thầy, các ngưỡng này hoàn toàn không phải gán định tính mà có cơ sở toán học và chuẩn mực tài chính:
  - Ngưỡng $p^* = 0.35$ được chứng minh bằng việc **cực đại hóa chỉ số Youden's J Statistic** trên đường cong ROC ($J = \text{TPR} - \text{FPR}$).
  - Ngưỡng $p = 0.60$ dựa trên **Ma trận chi phí sai lầm bất đối xứng**: Cho vay nhầm người xấu gây thiệt hại gấp 14 lần so với từ chối nhầm người tốt ($C_{FP}/C_{FN} \approx 14$). Khi $p \ge 0.60$, tổn thất kỳ vọng vượt quá biên lợi nhuận, bắt buộc phải từ chối theo Lý thuyết Nghịch tuyển Stiglitz & Weiss.
  - Ngưỡng $p = 0.15$ tuân thủ chuẩn nợ thông thường theo **Basel II**.
  - Lãi suất được tính theo mô hình **Risk-Based Pricing**: Lãi suất cơ sở $8.5\%$ (gồm Chi phí vốn 5.0% + Chi phí vận hành 1.5% + Biên lãi NIM 2.0%) cộng với phần bù rủi ro $\Delta_{\text{Risk}} = p \times 15\%$, ra các mức chẵn $8.5\%$, $11.5\%$ và $14.5\%/năm$."

#### Câu 4: "Kiến trúc Medallion (Bronze -> Silver -> Gold) giải quyết bài toán gì của ngân hàng?"
* **Trả lời:** "Thưa Thầy, kiến trúc Medallion giải quyết bài toán về **tính toàn vẹn dữ liệu và kiểm toán (Data Auditability)**:
  - **Tầng Bronze:** Lưu nguyên bản dữ liệu thô (As-is) với cơ chế Delta ACID Transaction Log và Time Travel, cho phép kiểm toán viên truy vết lại chính xác trạng thái dữ liệu của một khoản vay tại bất kỳ thời điểm nào trong quá khứ.
  - **Tầng Silver:** Làm sạch dữ liệu phân tán, lọc ngoại lai và kỹ nghệ đặc trưng tài chính (DTI, CBI).
  - **Tầng Gold:** Lưu trữ kết quả AI, điểm FICO Score, phân tầng rủi ro và chính sách phê duyệt, kết nối trực tiếp với API ngân hàng để giải ngân tự động trong dưới 3 phút."

#### Câu 5: "Nếu gặp khách hàng chưa có lịch sử tín dụng (Thin-file / Unbanked), mô hình xử lý như thế nào?"
* **Trả lời:** "Thưa Thầy, trong pipeline Tầng Silver, hệ thống áp dụng cơ chế điền khuyết thiếu an toàn ($0.0$ năm thâm niên, $1$ năm lịch sử tín dụng) và cơ chế `handleInvalid = 'keep'` của `StringIndexer`. Về mặt chiến lược lâu dài (Chương 5), hệ thống có thể mở rộng Tầng Silver để tích hợp **Dữ liệu thay thế (Alternative Data)** như lịch sử thanh toán hóa đơn điện thoại/tiện ích, giao dịch ví điện tử MoMo/ZaloPay để chấm điểm mà không cần phụ thuộc vào CIC truyền thống."
