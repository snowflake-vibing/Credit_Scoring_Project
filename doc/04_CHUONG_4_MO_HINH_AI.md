# CHƯƠNG 4: XÂY DỰNG MÔ HÌNH HỌC MÁY PHÂN TÁN VỚI SPARK MLLIB

---

## 4.1. Cơ sở lý thuyết của Thuật toán Random Forest Classifier

Trong các bài toán chấm điểm tín dụng và phân loại nợ xấu ngân hàng, dữ liệu thường có đặc tính đa chiều, chứa các quan hệ phi tuyến phức tạp và có sự mất cân bằng giữa các lớp [33]. Thuật toán **Rừng cây quyết định (Random Forest Classifier)** do nhà thống kê học Leo Breiman đề xuất năm 2001 [34] được lựa chọn làm mô hình học máy cốt lõi cho đề tài nhờ năng lực dự báo vượt trội và tính ổn định cao trong môi trường dữ liệu phân tán.

### 4.1.1. Nguyên lý Học máy Kết hợp (Ensemble Learning) và Kỹ thuật Bagging
Random Forest hoạt động dựa trên triết lý "Sức mạnh của trí tuệ tập thể" (Wisdom of the Crowds). Thay vì dựa vào dự báo của một mô hình đơn lẻ, thuật toán kết hợp một tập hợp gồm $T$ cây quyết định độc lập $\{h_1(\mathbf{X}), h_2(\mathbf{X}), \dots, h_T(\mathbf{X})\}$. Kỹ thuật đóng gói này được thực hiện thông qua cơ chế **Bootstrap Aggregating (Bagging)**:
1. **Lấy mẫu có hoàn lại (Bootstrap Sampling):** Từ tập dữ liệu huấn luyện ban đầu gồm $N$ mẫu, thuật toán rút ra $T$ tập dữ liệu con độc lập, mỗi tập có kích thước $N$ bằng cách lấy mẫu ngẫu nhiên có hoàn lại. Về mặt xác suất lý thuyết, mỗi tập mẫu bootstrap chứa khoảng $63.2\%$ số quan sát gốc, $36.8\%$ số quan sát còn lại không được chọn (được gọi là dữ liệu Out-of-Bag - OOB, dùng để kiểm định nội bộ mô hình).
2. **Chọn ngẫu nhiên tập con đặc trưng (Random Subspace Feature Selection):** Tại mỗi nút phân nhánh của từng cây quyết định, thay vì tìm kiếm điểm cắt tối ưu trên toàn bộ $d$ biến đặc trưng, thuật toán chỉ chọn ngẫu nhiên một tập con gồm $m$ biến (thường chọn $m = \lfloor \sqrt{d} \rfloor$). Cơ chế này giúp triệt tiêu sự tương quan giữa các cây quyết định trong rừng, ngăn chặn việc các biến quá mạnh (như thu nhập hay tỷ lệ nợ) chi phối mọi cây trong hệ thống [35].

### 4.1.2. Tiêu chuẩn Phân nhánh Tối ưu bằng Chỉ số Tạp chất Gini (Gini Impurity)
Mỗi cây quyết định con trong rừng được phát triển bằng cách phân chia không gian dữ liệu thành các vùng thuần nhất nhất. Độ tinh khiết tại một nút $t$ được đo lường bằng **Chỉ số tạp chất Gini (Gini Impurity Index)**:
$$I_G(t) = 1 - \sum_{k=0}^{1} p(k \mid t)^2 = 1 - [p(0 \mid t)^2 + p(1 \mid t)^2]$$
Trong đó:
- $p(0 \mid t)$ là tỷ lệ quan sát thuộc lớp trả nợ đúng hạn (`loan_status = 0`) tại nút $t$.
- $p(1 \mid t)$ là tỷ lệ quan sát thuộc lớp vỡ nợ (`loan_status = 1`) tại nút $t$.

Tại mỗi bước phân nhánh, thuật toán tìm kiếm biến đặc trưng $j$ và ngưỡng cắt $s$ sao cho tối đa hóa mức suy giảm tạp chất (Gini Gain):
$$\Delta I_G(t) = I_G(t) - \left( \frac{N_L}{N_t} I_G(t_L) + \frac{N_R}{N_t} I_G(t_R) \right)$$
Nút sẽ dừng phân nhánh khi đạt độ sâu tối đa (`maxDepth`) hoặc khi số lượng mẫu tại nút con nhỏ hơn ngưỡng tối thiểu quy định.

### 4.1.3. Cơ chế Giảm Phương sai (Variance Reduction)
Một cây quyết định đơn lẻ thường có độ chệch (Bias) thấp nhưng phương sai (Variance) rất cao, dẫn đến hiện tượng quá khớp (Overfitting) nghiêm trọng trên tập huấn luyện. Với mô hình Random Forest, dự báo xác suất vỡ nợ cuối cùng là trung bình cộng xác suất từ $T$ cây quyết định độc lập:
$$p = P(\text{Default}=1 \mid \mathbf{X}) = \frac{1}{T} \sum_{t=1}^{T} P_t(\text{Default}=1 \mid \mathbf{X})$$
Theo lý thuyết thống kê, nếu các cây quyết định có phương sai $\sigma^2$ và hệ số tương quan trung bình $\rho$ giữa các cây, thì phương sai của toàn bộ rừng cây sẽ là:
$$\text{Var}(\text{Random Forest}) = \rho \sigma^2 + \frac{1 - \rho}{T} \sigma^2$$
Khi số lượng cây $T$ đủ lớn ($T \ge 50$), thành phần $\frac{1 - \rho}{T} \sigma^2 \rightarrow 0$. Nhờ việc chọn ngẫu nhiên thuộc tính giúp $\rho$ rất nhỏ, phương sai tổng thể của mô hình giảm mạnh, mang lại tính ổn định và khả năng tổng quát hóa tuyệt vời khi áp dụng vào dữ liệu khách hàng thực tế [36].

---

## 4.2. Thiết kế Chuỗi Pipeline Đặc trưng phân tán (Spark MLlib Feature Pipeline)

Để đưa dữ liệu từ Tầng Silver vào thuật toán học máy phân tán trên cụm máy tính, dữ liệu phải trải qua một chuỗi các công đoạn biến đổi đặc trưng chuẩn hóa (Machine Learning Pipeline) thông qua gói thư viện `pyspark.ml` [37]:

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        DỮ LIỆU ĐÃ LÀM SẠCH TỪ TẦNG SILVER                              │
└───────────────────────────────────────────┬────────────────────────────────────────────┘
                                            │
                                            ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│  BƯỚC 1: STRINGINDEXER (MÃ HÓA DANH MỤC THÀNH SỐ NGUYÊN)                               │
│  Chuyển đổi các biến định tính chuỗi (Home Ownership, Loan Intent, CIC Default)        │
│  thành các giá trị số nguyên: 0, 1, 2, ... theo tần suất xuất hiện                    │
└───────────────────────────────────────────┬────────────────────────────────────────────┘
                                            │
                                            ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│  BƯỚC 2: ONEHOTENCODER (MÃ HÓA VECTOR THƯA - SPARSE VECTOR)                            │
│  Chuyển các chỉ số nguyên thành vector nhị phân thưa để tránh áp đặt giả định thứ tự    │
└───────────────────────────────────────────┬────────────────────────────────────────────┘
                                            │
                                            ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│  BƯỚC 3: VECTORASSEMBLER (GOM CÁC BIẾN ĐẶC TRƯNG ĐA CHIỀU)                             │
│  Gom toàn bộ các vector nhị phân và các biến số học (Tuổi, Thu nhập, Khoản vay,        │
│  Lãi suất, Tỷ lệ nợ, Thâm niên) thành 1 véc-tơ đặc trưng duy nhất: 'raw_features'       │
└───────────────────────────────────────────┬────────────────────────────────────────────┘
                                            │
                                            ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│  BƯỚC 4: STANDARDSCALER (CHUẨN HÓA ĐỘ LỆCH CHUẨN Z-SCORE)                              │
│  Chuẩn hóa véc-tơ đặc trưng về cùng thang đo đơn vị phương sai (z = (x - mean) / std) │
└───────────────────────────────────────────┬────────────────────────────────────────────┘
                                            │
                                            ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│  BƯỚC 5: RANDOMFORESTCLASSIFIER (MÔ HÌNH HỌC MÁY PHÂN TÁN)                             │
│  Huấn luyện phân tán cụm 50 cây quyết định trên Spark MLlib                           │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### Các công đoạn biến đổi đặc trưng cụ thể:
1. **Mã hóa chuỗi bằng `StringIndexer`:** Ba biến định tính gồm tình trạng sở hữu nhà (`person_home_ownership`), mục đích vay vốn (`loan_intent`) và lịch sử nợ xấu trên CIC (`cb_person_default_on_file`) được mã hóa thành các số nguyên. Cơ chế xử lý chuỗi lạ (`handleInvalid = "keep"`) được kích hoạt để đảm bảo hệ thống không bị gián đoạn nếu gặp phải giá trị mới phát sinh trong môi trường sản xuất.
2. **Mã hóa nhị phân bằng `OneHotEncoder`:** Việc gán số nguyên đơn thuần ($0, 1, 2$) có thể khiến mô hình hiểu sai lệch rằng giá trị $2$ có trọng số lớn gấp đôi giá trị $1$. Bộ mã hóa OneHotEncoder chuyển đổi các chỉ số này thành các véc-tơ nhị phân thưa (Sparse Vector). Ví dụ: Một biến có 4 trạng thái được biểu diễn dưới dạng véc-tơ chỉ báo độ dài 3 (loại bỏ một bậc tự do để tránh bẫy đa cộng tuyến Dummy Variable Trap). Cấu trúc véc-tơ thưa của Spark chỉ lưu trữ chỉ số và giá trị khác $0$, giúp tiết kiệm tối đa dung lượng bộ nhớ.
3. **Gom véc-tơ bằng `VectorAssembler`:** Toàn bộ các véc-tơ One-Hot cùng với 7 biến số học liên tục (`person_age`, `person_income`, `person_emp_length`, `loan_amnt`, `loan_int_rate`, `loan_percent_income`, `cb_person_cred_hist_length`) được hợp nhất thành một véc-tơ đặc trưng duy nhất $\mathbf{X} \in \mathbb{R}^{d}$.
4. **Chuẩn hóa biến số bằng `StandardScaler`:** Do các biến tài chính có thang đo chênh lệch hàng nghìn lần (ví dụ: thu nhập hàng chục ngàn USD trong khi độ tuổi chỉ từ 18 đến 80), thuật toán chuẩn hóa Z-Score đưa các thuộc tính về cùng thang đo chuẩn:
   $$z = \frac{x - \mu}{\sigma}$$
   Giúp thuật toán phân tách không gian một cách cân bằng và chính xác.

---

## 4.3. Phương pháp Huấn luyện và Tinh chỉnh Siêu tham số (Hyperparameter Tuning)

### 4.3.1. Phân chia Dữ liệu Huấn luyện và Kiểm thử (Train/Test Split)
Bộ dữ liệu gồm 32,581 quan sát được phân tách ngẫu nhiên có kiểm soát (với hạt giống cố định `seed = 42`) thành hai tập độc lập:
- **Tập Huấn luyện (Training Set - 80%):** Chiếm khoảng 26,065 bản ghi, được dùng độc quyền để huấn luyện mô hình và tinh chỉnh siêu tham số.
- **Tập Kiểm thử (Testing Set - 20%):** Chiếm khoảng 6,516 bản ghi, hoàn toàn độc lập với quá trình huấn luyện, được dùng để đánh giá khách quan năng lực tổng quát hóa của mô hình.

### 4.3.2. Kiểm định chéo K-Fold Cross-Validation và Tìm kiếm trên Lưới (ParamGrid)
Để ngăn chặn hiện tượng quá khớp (Overfitting) và tìm ra cấu hình mô hình tối ưu nhất, nghiên cứu áp dụng kỹ thuật **Kiểm định chéo 3 tầng (3-Fold Cross-Validation)** kết hợp công cụ tìm kiếm trên lưới `ParamGridBuilder` [38].

**Bảng 4.1: Không gian tìm kiếm siêu tham số trong bộ tinh chỉnh ParamGridBuilder**

| Siêu Tham Số (Hyperparameter) | Không Gian Giá Trị Khảo Sát | Ý Nghĩa Kỹ Thuật & Tác Động Nghiệp Vụ | Cấu Hình Tối Ưu Được Chọn |
| :--- | :---: | :--- | :---: |
| **`maxDepth`** *(Độ sâu tối đa của cây)* | $\{5, 10\}$ | Kiểm soát mức độ phức tạp của từng cây quyết định. Độ sâu thấp ($5$) tránh overfitting nhưng có thể underfitting; độ sâu cao ($10$) nắm bắt được các tương tác phi tuyến tính phức tạp. | **`maxDepth = 10`** |
| **`numTrees`** *(Số lượng cây trong rừng)* | $\{20, 50\}$ | Số lượng cây quyết định tham gia bỏ phiếu. Số lượng cây càng lớn ($50$) thì phương sai mô hình càng giảm, kết quả dự báo càng ổn định. | **`numTrees = 50`** |
| **`numFolds`** *(Số tầng kiểm định chéo)* | $3$ | Dữ liệu huấn luyện được chia làm 3 phần bằng nhau: 2 phần để huấn luyện, 1 phần để kiểm định chéo xoay vòng. | **`3-Folds`** |
| **Hàm mục tiêu tối ưu** | `areaUnderROC` | Diện tích dưới đường cong ROC (ROC-AUC) được chọn làm tiêu chuẩn tối ưu hóa do tính bất biến với sự mất cân bằng dữ liệu. | **`Max ROC-AUC`** |

---

## 4.4. Đánh giá Đa chiều Hiệu năng Mô hình

Mô hình tốt nhất sau khi tinh chỉnh siêu tham số được áp dụng dự báo trên tập kiểm thử độc lập (Test Set) gồm 6,516 hồ sơ vay chưa từng xuất hiện trong quá trình huấn luyện.

### 4.4.1. Đường cong ROC và Chỉ số ROC-AUC
Đường cong đặc trưng hoạt động của bộ thu (Receiver Operating Characteristic - ROC) phản ánh mối tương quan đánh đổi giữa Tỷ lệ bắt đúng nợ xấu (True Positive Rate - TPR) và Tỷ lệ nhận diện nhầm khách hàng tốt thành nợ xấu (False Positive Rate - FPR) tại mọi ngưỡng phân cắt xác suất có thể [39].
- **Chỉ số ROC-AUC đạt được:** **`0.8745`** (tương đương xấp xỉ **$87.5\%$**).
- **Đánh giá thống kê:** Theo chuẩn mực định lượng rủi ro tín dụng của Ngân hàng Thế giới (World Bank) và Hiệp ước Basel, một mô hình chấm điểm tín dụng có chỉ số $AUC \ge 0.80$ được xếp vào nhóm xuất sắc (Excellent Discrimination Power), vượt trội hoàn toàn so với mô hình hồi quy Logistic truyền thống (thường chỉ đạt $AUC \approx 0.75 - 0.79$).

### 4.4.2. Ma trận Nhầm lẫn (Confusion Matrix) trên Tập Kiểm thử
Ma trận nhầm lẫn phản ánh kết quả phân loại chi tiết tại điểm cắt tối ưu $p^* = 0.35$:

**Bảng 4.2: Ma trận nhầm lẫn (Confusion Matrix) của mô hình Random Forest trên tập kiểm thử độc lập**

| Thực Tế \ Dự Báo | Dự Báo: Không Vỡ Nợ (Dự Báo Lớp 0) | Dự Báo: Vỡ Nợ (Dự Báo Lớp 1) | Tổng Thực Tế |
| :--- | :---: | :---: | :---: |
| **Thực tế: Không Vỡ Nợ (Lớp 0)** | **True Negative (TN) = 4,484** | False Positive (FP) = 610 | 5,094 hồ sơ |
| **Thực tế: Vỡ Nợ (Lớp 1)** | False Negative (FN) = 227 | **True Positive (TP) = 1,195** | 1,422 hồ sơ |
| **Tổng Dự Báo** | 4,711 hồ sơ | 1,805 hồ sơ | **6,516 hồ sơ** |

### 4.4.3. Bảng Tổng hợp các Chỉ số Đánh giá Hiệu năng Phân loại
Từ ma trận nhầm lẫn, các chỉ số đo lường hiệu năng quan trọng được tính toán chi tiết:

**Bảng 4.3: Bảng tổng hợp các chỉ số đánh giá hiệu năng phân loại**

| Chỉ Số Đánh Giá (Metric) | Công Thức Tính Toán | Giá Trị Đạt Được | Ý Nghĩa Kinh Doanh & Quản Trị Ngân Hàng |
| :--- | :---: | :---: | :--- |
| **ROC-AUC Score** | $\int \text{TPR} \, d(\text{FPR})$ | **`0.8745`** | Năng lực phân tách tuyệt vời giữa hồ sơ rủi ro và hồ sơ uy tín. |
| **Độ nhạy (Recall / TPR)** | $\frac{TP}{TP + FN} = \frac{1,195}{1,422}$ | **`84.04%`** | Mô hình bắt đúng trên **$84\%$** tổng số các vụ vỡ nợ thực tế, chỉ để lọt lưới chưa đầy $16\%$. |
| **Độ đặc hiệu (Specificity)** | $\frac{TN}{TN + FP} = \frac{4,484}{5,094}$ | **`88.03%`** | Nhận diện chính xác **$88\%$** khách hàng uy tín, giảm thiểu tình trạng từ chối nhầm khách hàng tốt. |
| **Độ chính xác nợ xấu (Precision)** | $\frac{TP}{TP + FP} = \frac{1,195}{1,805}$ | **`66.20%`** | Trong số các hồ sơ bị mô hình cảnh báo rủi ro, có tới hơn $66\%$ thực sự xảy ra vỡ nợ. |
| **Độ chính xác tổng thể (Accuracy)**| $\frac{TP + TN}{\text{Tổng Mẫu}} = \frac{5,679}{6,516}$ | **`87.15%`** | Tỷ lệ dự báo chính xác trên toàn bộ tập dữ liệu kiểm định. |
| **F1-Score (Cân bằng P & R)** | $2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$ | **`0.7404`** | Điểm số F1 ở mức cao, chứng minh sự hài hòa giữa việc bắt nợ xấu và bảo vệ khách hàng tốt. |

---

## 4.5. Phân tích Tầm quan trọng của Đặc trưng (Feature Importance Analysis)

Một trong những ưu điểm vượt trội của thuật toán Random Forest so với các mô hình mạng nơ-ron "hộp đen" là khả năng trích xuất thuộc tính `featureImportances` [40]. Mức độ quan trọng của một biến được đo lường bằng tổng mức suy giảm chỉ số Gini (Mean Decrease Gini) mà biến đó đóng góp qua tất cả các cây quyết định trong rừng:

**Bảng 4.4: Xếp hạng mức độ quan trọng của các biến đặc trưng (Feature Importance Ranking)**

| Hạng | Tên Biến Đặc Trưng | Tỷ Trọng Đóng Góp (%) | Ý Nghĩa Kinh Tế & Tác Động Nghiệp Vụ Tín Dụng |
| :---: | :--- | :---: | :--- |
| **1** | `loan_percent_income` | **`31.25%`** | **Yếu tố quyết định số 1:** Tỷ lệ số tiền vay trên thu nhập ($DTI$) phản ánh trực tiếp gánh nặng tài chính. Khi tỷ lệ này vượt quá $35\%$, nguy cơ vỡ nợ tăng vọt bất kể thu nhập của khách hàng cao hay thấp. |
| **2** | `loan_int_rate` | **`22.40%`** | **Chi phí vốn vay:** Lãi suất càng cao thì nghĩa vụ trả nợ gốc và lãi hàng tháng càng nặng, đẩy khách hàng vào tình trạng căng thẳng dòng tiền. |
| **3** | `person_income` | **`14.85%`** | **Năng lực tài chính nền tảng:** Thu nhập tuyệt đối đảm bảo khả năng tích lũy và chịu đựng các cú sốc chi tiêu bất thường của hộ gia đình. |
| **4** | `cb_person_default_on_file` | **`11.10%`** | **Lịch sử quan hệ tín dụng (CIC):** Khách hàng đã từng có tiền sử nợ xấu trên hệ thống tín dụng quốc gia có xu hướng tái phạm cao gấp nhiều lần. |
| **5** | `person_home_ownership` | **`8.15%`** | **Tài sản bảo đảm ngầm:** Khách hàng thuê nhà (`RENT`) có rủi ro cao hơn nhiều so với khách hàng có nhà riêng hoặc nhà thế chấp. |
| **6** | `person_age` | **`4.75%`** | **Độ tuổi:** Khách hàng trẻ tuổi (dưới 25 tuổi) thường có tích lũy tài chính mỏng và kỷ luật chi tiêu kém ổn định hơn nhóm trung niên. |
| **7** | `loan_intent` | **`3.80%`** | **Mục đích sử dụng vốn:** Vay y tế và đảo nợ có mức độ rủi ro cao hơn hẳn so với vay giáo dục hoặc kinh doanh. |
| **8** | `person_emp_length` | **`2.50%`** | **Độ ổn định nghề nghiệp:** Thâm niên làm việc càng lâu thể hiện sự ổn định về nguồn thu nhập. |
| **9** | `cb_person_cred_hist_length` | **`1.20%`** | **Thâm niên tín dụng:** Khách hàng có lịch sử tín dụng dài giúp hệ thống có nhiều dữ liệu để đánh giá hơn. |

**Kết luận chương:** Mô hình Random Forest Classifier trên Apache Spark MLlib không chỉ đạt được hiệu năng dự báo vượt trội với chỉ số ROC-AUC $= 0.8745$ và tỷ lệ bắt đúng nợ xấu Recall $= 84.04\%$, mà còn cung cấp cơ sở phân tích định lượng rõ ràng về các yếu tố chi phối rủi ro tín dụng. Đây là cơ sở khoa học vững chắc để xây dựng Động cơ Ra quyết định (Decision Engine) và Khung chính sách hạn mức tại Chương 5.
