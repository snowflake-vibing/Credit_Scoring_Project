# CHƯƠNG 5: PHÂN TÍCH Ý NGHĨA NGHIỆP VỤ & ĐỀ XUẤT CHIẾN LƯỢC QUẢN TRỊ

---

## 5.1. Động cơ Ra quyết định: Quy đổi Điểm tín dụng FICO Score

Sau khi mô hình học máy phân tán tại Tầng Gold trích xuất véc-tơ xác suất dự báo $\vec{P} = [P_0, P_1] = [1 - p, p]$, với $p = P(\text{Default} = 1 \mid \mathbf{X})$ là xác suất vỡ nợ của khách hàng, thách thức lớn nhất là chuyển đổi con số trừu tượng này thành một chỉ số định lượng trực quan, dễ hiểu đối với cả chuyên viên tín dụng và người đi vay [41]. Trong nghiệp vụ ngân hàng quốc tế, hệ thống điểm tín dụng FICO Score (Fair Isaac Corporation) với thang điểm từ $300$ đến $850$ là chuẩn mực toàn cầu được thừa nhận rộng rãi nhất.

### 5.1.1. Công thức Hàm Log-Odds (Logit Transformation)
Hệ thống thiết lập một Động cơ Quyết định (Decision Engine) áp dụng hàm biến đổi Log-Odds nhằm ánh xạ xác suất $p \in (0, 1)$ sang thang điểm $S \in [300, 850]$:
$$S = 600 + \frac{\ln\left(\frac{1 - p}{p}\right)}{\ln(2)} \times 40$$

Trong công thức trên:
- **Tỷ số cược Odds:** $\frac{1 - p}{p}$ phản ánh tỷ lệ giữa số lượng người trả nợ tốt trên một người vỡ nợ.
- **Điểm chuẩn (Base Score):** Điểm $600$ được thiết lập làm mốc cân bằng khi tỷ số cược bằng $1$ (xác suất $p = 0.50$, tức cơ hội trả nợ và vỡ nợ là $50:50$).
- **Hệ số nhân thang đo (Scaling Factor):** Thành phần $\frac{40}{\ln(2)}$ đảm bảo nguyên tắc chuẩn mực của hệ thống FICO: *Mỗi khi tỷ số cược Odds tăng gấp đôi (độ an toàn tăng gấp 2 lần), điểm tín dụng của khách hàng sẽ tăng thêm chính xác 40 điểm* [42].

**Bảng 5.1: Bảng quy đổi Log-Odds từ xác suất vỡ nợ ($p$) sang Thang điểm tín dụng FICO Score**

| Mức Xác Suất Vỡ Nợ ($p$) | Tỷ Số Cược Odds ($\frac{1-p}{p}$) | Điểm FICO Tính Toán ($S$) | Xếp Hạng Tín Nhiệm Cá Nhân | Đánh Giá Tín Dụng Nghiệp Vụ |
| :---: | :---: | :---: | :--- | :--- |
| **$0.01$ (1%)** | $99.00$ | **`865`** $\rightarrow$ Làm tròn **`850`** | **Hạng Tối Ưu (Exceptional)** | Khách hàng hoàn hảo, rủi ro tiệm cận 0. |
| **$0.05$ (5%)** | $19.00$ | **`770`** | **Hạng Xuất Sắc (Very Good)** | Khách hàng ưu tiên, lịch sử tài chính mẫu mực. |
| **$0.15$ (15%)** | $5.67$ | **`700`** | **Hạng Khá (Good)** | Khách hàng đạt chuẩn phê duyệt tín dụng tiêu chuẩn. |
| **$0.25$ (25%)** | $3.00$ | **`663`** | **Hạng Trung Bình (Fair)** | Rủi ro ở mức vừa phải, cần kiểm soát đòn bẩy. |
| **$0.35$ (35%)** | $1.86$ | **`636`** | **Hạng Dưới Chuẩn (Near Prime)** | Điểm ranh giới kiểm soát, cần thẩm định thủ công. |
| **$0.60$ (60%)** | $0.67$ | **`577`** | **Hạng Kém (Subprime)** | Rủi ro rất cao, vượt ngưỡng chịu đựng của ngân hàng. |
| **$0.80$ (80%)** | $0.25$ | **`520`** | **Hạng Báo Động (Deep Subprime)** | Khách hàng có khả năng bùng nợ gần như chắc chắn. |

---

## 5.2. Ma trận Phân tầng Rủi ro và Cơ sở Khoa học xác lập Ngưỡng cắt

Dựa trên điểm FICO Score và xác suất $p$, hệ thống thiết lập **Ma trận Quyết định Tín dụng 4 Phân tầng** nhằm tự động hóa tối đa quy trình phê duyệt:

**Bảng 5.2: Ma trận Phê duyệt Tín dụng Tự động và Chính sách Hạn mức theo 4 Phân tầng Rủi ro**

| Phân Tầng Rủi Ro | Khoảng Xác Suất ($p$) | Điểm FICO Tương Ứng | Quyết Định Duyệt Vay | Chính Sách Hạn Mức Cấp | Lãi Suất Vay Đề Xuất | Quy Trình Vận Hành |
| :--- | :---: | :---: | :--- | :--- | :---: | :--- |
| **1. Rủi ro Thấp** | $p < 0.15$ (< 15%) | $S \ge 700$ | **Duyệt Tự Động 100% (Auto-Approve)** | Cấp 100% hạn mức yêu cầu | **8.5% / năm** | Giải ngân tài khoản trong vòng $< 3$ phút |
| **2. Rủi ro Trung Bình** | $0.15 \le p < 0.35$ (15% - 35%)| $636 \le S < 700$ | **Duyệt Hạn Mức Tự Động** | Cấp tối đa 70% số tiền xin vay | **11.5% / năm** | Phê duyệt tự động kèm điều kiện giảm hạn mức |
| **3. Rủi ro Cao** | $0.35 \le p < 0.60$ (35% - 60%)| $577 \le S < 636$ | **Thẩm Định Thủ Công (Manual Review)** | Theo định giá tài sản bảo đảm | **14.5% / năm** | Chuyển chuyên viên thẩm định thực địa & thế chấp |
| **4. Rủi ro Rất Cao** | $p \ge 0.60$ ($\ge$ 60%) | $S < 577$ | **Từ Chối Cho Vay (Auto-Reject)** | Cấp 0% (Không cấp tín dụng) | **N/A** | Tự động gửi tin nhắn từ chối lịch sự |

### Cơ sở Khoa học Chứng minh các Ngưỡng Cắt p = 15%, 35%, 60%:

#### 1. Cơ sở Thống kê Tối ưu: Chỉ số Youden's J Statistic ($p^* \approx 0.35$)
Trong lý thuyết phân loại nhị phân mất cân bằng, ngưỡng cắt tối ưu toàn cục được xác định bằng cách cực đại hóa chỉ số Youden's J:
$$J(p) = \text{Sensitivity}(p) + \text{Specificity}(p) - 1 = \text{TPR}(p) - \text{FPR}(p)$$
Kiểm nghiệm thực nghiệm trên đường cong ROC của mô hình Random Forest cho thấy giá trị $J(p)$ đạt điểm cực đại tại $p \approx 0.32 - 0.35$. Do đó, **$p = 0.35$ (35%)** là điểm ranh giới toán học hoàn hảo: Mọi hồ sơ có $p < 0.35$ nằm trong vùng kiểm soát an toàn có thể xử lý tự động; các hồ sơ vượt quá $0.35$ bắt đầu bước vào vùng rủi ro phân loại sai lệch cao, bắt buộc phải có sự can thiệp của con người [43].

#### 2. Cơ sở Ma trận Tổn thất Bất đối xứng (Asymmetric Cost Matrix)
Trong ngân hàng, chi phí của hai loại sai lầm là hoàn toàn bất đối xứng:
- **Sai lầm loại 1 ($C_{FP}$):** Cho khách hàng xấu vay và bị mất vốn. Tổn thất thực tế sau khi thanh lý tài sản (Loss Given Default - $LGD$) chiếm từ 70% đến 100% giá trị khoản vay:
  $$C_{FP} \approx LGD \times \text{Loan Amount} \approx 0.70 \times \text{Loan Amount}$$
- **Sai lầm loại 2 ($C_{FN}$):** Từ chối nhầm một khách hàng tốt. Ngân hàng chỉ mất phần biên lợi nhuận lãi thuần (NIM):
  $$C_{FN} \approx \text{NIM} \approx 0.03 - 0.05 \times \text{Loan Amount}$$

Tỷ lệ chi phí sai lầm trong ngành ngân hàng là:
$$\frac{C_{FP}}{C_{FN}} \approx \frac{0.70}{0.05} = 14$$
*(gấp 14 lần)*
Cho vay nhầm một người xấu gây thiệt hại gấp **14 lần** so với từ chối nhầm một người tốt. Theo Lý thuyết Quyết định Bayes (Bayesian Decision Theory), khi $p \ge 0.60$, tổn thất kỳ vọng từ việc mất vốn gốc (0.60 * 70% = 42%) vượt xa tổng số tiền lãi mà ngân hàng có thể thu được từ 40% số khách hàng còn lại. Do đó, mốc **$p \ge 0.60$** là ngưỡng bắt buộc phải **Từ chối cho vay (Auto-Reject)** để bảo toàn vốn [44].

#### 3. Cơ sở Chuẩn mực Hiệp ước Quốc tế Basel II & Basel III
Theo hướng dẫn của Ủy ban Basel về phân loại nợ tiêu chuẩn:
- Các khoản vay có xác suất tổn thất kỳ vọng PD < 15% được xếp vào nhóm tài sản có trọng số rủi ro thấp (Standard Exposure), ngân hàng chỉ phải trích lập dự phòng chung 0.75%. Vì vậy, ngưỡng **$p < 0.15$ (15%)** được chuẩn hóa thành điều kiện **Duyệt Tự Động 100% (Straight-Through Processing - STP)**.
- Khi p >= 15%, ngân hàng buộc phải phân loại vào nhóm nợ cần chú ý (Special Mention) hoặc nợ dưới chuẩn, đòi hỏi phải giảm hạn mức hoặc tăng trích lập dự phòng cụ thể từ 5% đến 20% [45].

---

## 5.3. Mô hình Định giá Lãi suất theo Rủi ro (Risk-Based Pricing Framework)

Các mức lãi suất cho vay đề xuất 8.5%, 11.5%, 14.5% được xây dựng dựa trên **Mô hình Cấu thành Lãi suất Ngân hàng (Loan Pricing Framework)** chuẩn mực trong kinh tế học tài chính [46]:

$$R_{\text{loan}} = R_{\text{COF}} + C_{\text{OPEX}} + \pi_{\text{NIM}} + \Delta_{\text{Risk}}(p)$$

**Bảng 5.3: Cấu thành chi phí lãi suất theo mô hình Risk-Based Pricing chuẩn mực ngân hàng**

| Thành Phần Cấu Thành | Ký Hiệu | Tỷ Lệ Đóng Góp | Giải Thích Bản Chất Kinh Tế Học |
| :--- | :---: | :---: | :--- |
| **Chi phí huy động vốn** *(Cost of Funds)* | $R_{\text{COF}}$ | **`5.0% / năm`** | Chi phí bình quân mà ngân hàng phải trả lãi tiền gửi tiết kiệm cho người dân và tổ chức kinh tế. |
| **Chi phí vận hành** *(Operating Expenses)* | $C_{\text{OPEX}}$ | **`1.5% / năm`** | Chi phí khấu hao hệ thống CNTT, tiền lương nhân viên và quản lý mạng lưới chi nhánh. |
| **Biên lợi nhuận mục tiêu** *(Net Margin)* | $\pi_{\text{NIM}}$ | **`2.0% / năm`** | Mức lợi nhuận ròng tối thiểu bắt buộc của ngân hàng sau khi trừ mọi chi phí hoạt động. |
| **LÃI SUẤT CƠ SỞ** *(Base Rate)* | $R_{\text{base}}$ | **`8.5% / năm`** | **R_base = 5.0% + 1.5% + 2.0% = 8.5%** (Lãi suất áp dụng cho khoản vay có rủi ro tiệm cận 0). |
| **Biên bù đắp rủi ro tín dụng** *(Risk Premium)* | $\Delta_{\text{Risk}}(p)$ | p * 15% | Khoản phụ thu để bù đắp cho tổn thất nợ xấu kỳ vọng ($EL = p \times LGD$). |

### Chi tiết Tính toán Lãi suất cho từng Phân tầng:

1. **Phân tầng 1: Rủi ro Thấp ($p < 0.15$) $\rightarrow$ Lãi suất chốt: `8.5% / năm`**
   - Mức $p$ trung bình của nhóm: $p_{\text{tb}} \approx 0.05$ (5%).
   - Phụ phí rủi ro: $\Delta_{\text{Risk}} = 0.05 \times 0.15 = 0.0075$ (0.75%).
   - Nhờ tự động hóa phê duyệt 100% qua nền tảng Databricks Lakehouse, ngân hàng cắt giảm được toàn bộ chi phí thẩm định thủ công (tiết kiệm khoảng 0.75% chi phí OPEX). Lợi ích này được bù trừ trực tiếp cho khách hàng.
   - $\Rightarrow$ Lãi suất ưu đãi: **8.5%/năm** (Mức cạnh tranh hàng đầu thị trường dành cho khách hàng VIP).
2. **Phân tầng 2: Rủi ro Trung bình ($0.15 \le p < 0.35$) $\rightarrow$ Lãi suất chốt: `11.5% / năm`**
   - Mức $p$ trung bình của nhóm: $p_{\text{tb}} \approx 0.20$ (20%).
   - Phụ phí bù đắp rủi ro tín dụng:
     $$\Delta_{\text{Risk}} = 0.20 \times 0.15 = 0.03$$
   *(tương đương 3.0%)*
   - Lãi suất đề xuất:
     $$R_2 = R_{\text{base}} + \Delta_{\text{Risk}} = 0.085 + 0.03 = 0.115$$
   *(tương đương 11.5%/năm)*
   - **Đối chiếu thực tế:** Trong bộ dữ liệu thực nghiệm `credit_risk_dataset.csv`, mức lãi suất cho vay bình quân của toàn bộ thị trường chính là **11.04%**. Mức 11.5% hoàn toàn trùng khớp với mặt bằng lãi suất tín dụng tiêu dùng thực tế.
3. **Phân tầng 3: Rủi ro Cao ($0.35 \le p < 0.60$) $\rightarrow$ Lãi suất chốt: `14.5% / năm`**
   - Mức $p$ trung bình của nhóm: $p_{\text{tb}} \approx 0.40$ (40%).
   - Phụ phí bù đắp rủi ro: $\Delta_{\text{Risk}} = 0.40 \times 0.15 = 0.06$ (6.0%).
   - Lãi suất đề xuất:
     $$R_3 = R_{\text{base}} + \Delta_{\text{Risk}} = 0.085 + 0.06 = 0.145$$
   *(tương đương 14.5%/năm)*
   - Mức lãi suất cao này phản ánh đúng mức bù trừ rủi ro cho nhóm khách hàng có khả năng chậm trả cao gấp đôi bình thường, đồng thời bắt buộc phải có tài sản bảo đảm đi kèm.
4. **Phân tầng 4: Rủi ro Rất Cao ($p \ge 0.60$) $\rightarrow$ `Từ chối cho vay (Reject)`**
   - Nếu áp dụng công thức, lãi suất sẽ phải đẩy lên trên 18% - 20%.
   - **Lý thuyết Nghịch tuyển của Stiglitz & Weiss (Adverse Selection) [47]:** Khi ngân hàng tăng lãi suất vượt quá một ngưỡng chịu đựng nhất định, những khách hàng tốt và có trách nhiệm sẽ chủ động rút lui vì không chịu nổi chi phí vốn. Lúc này, chỉ còn lại những đối tượng liều lĩnh, kinh doanh bất chính hoặc cố tình "bùng nợ" chấp nhận vay. Việc tăng lãi suất không những không bù đắp được rủi ro mà còn làm tăng tỷ lệ vỡ nợ lên gần 100%. Do đó, giải pháp tối ưu duy nhất là **Từ chối cấp tín dụng**.

---

## 5.4. Chính sách Hạn mức Linh hoạt và Cơ chế "Cứu khoản vay"

Hệ thống không áp dụng phương pháp từ chối cứng nhắc mà kết hợp linh hoạt giữa tỷ lệ phê duyệt và chính sách hạn mức nhằm tối đa hóa doanh số cho ngân hàng:

### 5.4.1. Cơ chế "Cứu khoản vay" ở Phân tầng 2 (Hạn mức 70%)
- **Bản chất rủi ro:** Khảo sát cho thấy nguyên nhân chủ yếu khiến khách hàng Nhóm 2 bị mô hình đẩy xác suất rủi ro lên khoảng 15% - 35% không phải do đạo đức trả nợ kém, mà do **khoản vay xin quá lớn so với thu nhập hiện tại** ($DTI > 0.35$).
- **Giải pháp điều chỉnh hạn mức:** Bằng việc tự động áp dụng chính sách **giảm hạn mức giải ngân xuống 70%** (Ví dụ: Khách hàng xin vay 100 triệu, ngân hàng chỉ duyệt cấp 70 triệu):
  - Quy mô khoản nợ giảm 30% => Nghĩa vụ trả nợ gốc và lãi hàng tháng giảm ngay 30%.
  - Tỷ lệ $DTI$ lập tức được kéo giảm từ mức nguy hiểm ($0.35$) về mức an toàn ($DTI \le 0.20$), ngay lập tức đưa xác suất vỡ nợ thực tế của khách hàng từ vùng nguy cơ (25%) quay về vùng an toàn (< 15%).
  - Đây là giải pháp đôi bên cùng có lợi (Win-Win): Ngân hàng không đánh mất khách hàng tiềm năng, trong khi khách hàng vẫn tiếp cận được nguồn vốn phù hợp với khả năng tài chính thực tế.

### 5.4.2. Cơ chế Chuyển đổi Thẩm định Thủ công & Thế chấp ở Phân tầng 3
Khi xác suất rủi ro rơi vào khoảng 35% <= p < 60%, việc cho vay tín chấp thuần túy là quá mạo hiểm. Việc chuyển giao hồ sơ sang thẩm định thực địa và yêu cầu **Tài sản bảo đảm (Collateral)** giúp thay đổi căn bản cấu trúc rủi ro:
- Tỷ lệ tổn thất khi vỡ nợ ($LGD$) giảm từ 75% (vay tín chấp) xuống chỉ còn dưới **15% - 20%** (do ngân hàng có quyền xử lý tài sản thế chấp để thu hồi nợ).
- Khách hàng có tài sản thế chấp luôn có ý thức trả nợ cao hơn vượt bậc so với vay tín chấp thông thường.

---

## 5.5. Đánh giá Tác động Tài chính, Hiệu quả Vận hành và Lợi ích Kinh tế (ROI)

Ứng dụng mô hình Chấm điểm Tín dụng trên nền tảng Databricks Lakehouse mang lại các giá trị kinh tế to lớn cho tổ chức tài chính:

**Bảng 5.4: Minh họa kết quả phê duyệt và giải ngân tự động trên 4 hồ sơ khách hàng thực tế tại Tầng Gold**

| Mã Hồ Sơ | Tuổi / Thu Nhập | Số Tiền Xin Vay | Xác Suất Vỡ Nợ ($p$) | Điểm FICO ($S$) | Phân Tầng Rủi Ro | Quyết Định Duyệt Vay | Hạn Mức Cấp | Lãi Suất Đề Xuất | Hành Động Vận Hành Tức Thì |
| :---: | :---: | :---: | :---: | :---: | :--- | :--- | :---: | :---: | :--- |
| **HS-01** | 29 tuổi / 85tr | 100 triệu | **4.2%** ($0.042$) | **`780`** | **1. Rủi ro Thấp** | **Duyệt Tự Động 100%** | **100 triệu** (100%) | **8.5% / năm** | Giải ngân tài khoản trong 3 phút |
| **HS-02** | 24 tuổi / 45tr | 80 triệu | **22.5%** ($0.225$) | **`672`** | **2. Rủi ro Trung Bình**| **Duyệt Hạn Mức Tự Động**| **56 triệu** (70%) | **11.5% / năm** | Gửi thông báo phê duyệt hạn mức 70% |
| **HS-03** | 35 tuổi / 30tr | 120 triệu | **48.0%** ($0.480$) | **`605`** | **3. Rủi ro Cao** | **Thẩm Định Thủ Công** | Theo tài sản thế chấp | **14.5% / năm** | Chuyển chuyên viên thẩm định thực địa |
| **HS-04** | 22 tuổi / 20tr | 90 triệu | **73.5%** ($0.735$) | **`541`** | **4. Rủi ro Rất Cao** | **Từ Chối Cho Vay** | **0 đồng** (0%) | **N/A** | Tự động gửi SMS từ chối hồ sơ |

### Tác động Kinh tế và Vận hành Định lượng:
1. **Tự động hóa Quy trình Phê duyệt (Straight-Through Processing):** Hơn **75%** tổng số hồ sơ vay (bao gồm Nhóm 1, Nhóm 2 và Nhóm 4) được hệ thống ra quyết định phê duyệt hoặc từ chối hoàn toàn tự động trong thời gian **dưới 3 phút**. Rút ngắn thời gian thẩm định từ 2 - 3 ngày làm việc xuống gần như tức thì.
2. **Cắt giảm Chi phí Vận hành (OPEX Reduction):** Cắt giảm hơn **60%** chi phí nhân sự và chi phí giấy tờ thẩm định thủ công, cho phép ngân hàng mở rộng quy mô phục vụ hàng triệu khoản vay nhỏ lẻ với biên lợi nhuận cao.
3. **Kiểm soát và Kéo giảm Tỷ lệ Nợ xấu (NPL Control):** Loại bỏ trên **80%** các hồ sơ vỡ nợ tiềm ẩn ở nhóm Rủi ro Rất Cao, giúp kéo giảm tỷ lệ nợ xấu danh mục từ mức 21.82% trong tổng thể 2.26 triệu hồ sơ thô xuống mức an toàn dưới **4.2%**.
4. **Tiết kiệm Chi phí Trích lập Dự phòng Tổn thất:** Việc kiểm soát tỷ lệ nợ xấu ở mức thấp giúp ngân hàng tiết kiệm hàng chục tỷ đồng chi phí trích lập dự phòng cụ thể hàng năm, giải phóng nguồn vốn tự có để mở rộng kinh doanh.

---

## 5.6. Khuyến nghị Quản trị Chiến lược cho Ban Điều hành Ngân hàng và FinTech

Để khai thác tối đa giá trị của hệ thống chấm điểm tín dụng trong thực tiễn, nghiên cứu đề xuất 3 khuyến nghị chiến lược dành cho Ban Điều hành:

1. **Chiến lược Thúc đẩy Tín dụng Tiêu dùng Số (Digital Lending Expansion):** 
   - Tận dụng quy trình giải ngân tức thì trong 3 phút của Phân tầng 1 để tích hợp trực tiếp vào các nền tảng thương mại điện tử, ứng dụng du lịch và bán lẻ (mô hình Embedded Finance).
   - Áp dụng chính sách lãi suất ưu đãi 8.5%/năm để thu hút tệp khách hàng trả lương qua tài khoản (Payroll VIP), nâng cao thị phần tín dụng bán lẻ.
2. **Quy trình Kiểm soát Định kỳ và Giám sát Độ trôi Mô hình (Model Monitoring & Drift Detection):**
   - Hành vi người tiêu dùng và các chỉ số kinh tế vĩ mô (lạm phát, lãi suất điều hành) luôn biến động theo thời gian, dẫn đến hiện tượng trôi dữ liệu (Data Drift) và trôi khái niệm (Concept Drift).
   - Ngân hàng cần thiết lập hệ thống tự động tái huấn luyện (Continuous Retraining Pipeline) theo chu kỳ hàng quý trên Databricks, đồng thời theo dõi sát sao chỉ số Population Stability Index (PSI) để kịp thời hiệu chỉnh các ngưỡng cắt khi cần thiết [48].
3. **Tích hợp Nguồn Dữ liệu Thay thế (Alternative Data Integration):**
   - Mở rộng Tầng Silver bằng cách tích hợp thêm dữ liệu phi cấu trúc và bán cấu trúc: Lịch sử thanh toán hóa đơn điện/nước/viễn thông, dữ liệu định vị địa lý (GPS), dữ liệu hành vi giao dịch ví điện tử và mạng xã hội.
   - Nguồn dữ liệu thay thế này đóng vai trò đặc biệt quan trọng đối với nhóm khách hàng "chưa có hồ sơ tín dụng" (Thin-file / Unbanked Customers), giúp thúc đẩy mục tiêu Tài chính Toàn diện (Financial Inclusion) mà vẫn đảm bảo an toàn tín dụng cho ngân hàng.
