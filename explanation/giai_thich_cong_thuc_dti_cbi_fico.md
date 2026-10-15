# GIẢI THÍCH CHI TIẾT CƠ SỞ TOÁN HỌC & NGHIỆP VỤ CÁC CHỈ SỐ: DTI, CBI VÀ FICO SCORE

> **Đề tài:** Mô Hình Chấm Điểm Tín Dụng & Thẩm Định Rủi Ro Vỡ Nợ (Loan Default & Credit Scoring)  
> **Sinh viên thực hiện:** Lê Thành Hiệu  
> **Giảng viên hướng dẫn:** TS. Trần Mạnh Tường  
> **Tài liệu chuyên sâu:** Bổ trợ giải trình công thức định lượng trong Báo cáo Đồ án

---

## 📌 TỔNG QUAN VỀ BỘ BA CHỈ SỐ ĐỊNH LƯỢNG RỦI RO

Trong hệ thống chấm điểm tín dụng hiện đại, việc đánh giá năng lực tài chính và xác suất trả nợ của khách hàng không thể dựa vào các con số rời rạc (như chỉ nhìn vào thu nhập hay số tiền vay). Thay vào đó, hệ thống sử dụng **bộ ba chỉ số định lượng cốt lõi** kết hợp giữa kinh tế học ngân hàng, hành vi tài chính và xác suất thống kê:

1. **Chỉ số DTI (Debt-to-Income Ratio):** Thước đo đòn bẩy nợ và áp lực chi trả tài chính cơ bản.
2. **Chỉ số CBI (Credit Burden Index):** Thước đo gánh nặng tín dụng toàn diện có tính đến lãi suất và độ ổn định thâm niên công tác.
3. **Điểm FICO Score ($S$):** Thước đo chuẩn hóa độ tín nhiệm cá nhân trên thang điểm $300 - 850$ thông qua phép biến đổi hàm Log-Odds (Logit Transformation).

---

## 🧮 1. CHỈ SỐ TỶ LỆ NỢ TRÊN THU NHẬP (DEBT-TO-INCOME - DTI)

### 1.1. Bản chất Nghiệp vụ & Khái niệm
Chỉ số **DTI (Debt-to-Income Ratio)** là thước đo kinh điển được Ngân hàng Thanh toán Quốc tế (BIS), các ngân hàng trung ương và các tổ chức xếp hạng tín nhiệm quốc tế (Moody's, Standard & Poor's) sử dụng làm tiêu chuẩn bắt buộc hàng đầu trong thẩm định tín dụng tiêu dùng.

DTI phản ánh **tỷ trọng phần trăm thu nhập mà người đi vay phải trích ra để thực hiện nghĩa vụ nợ**. Về mặt bản chất kinh tế, DTI đại diện cho mức độ đòn bẩy tài chính cá nhân (Financial Leverage) và khả năng hấp thụ các cú sốc chi tiêu bất ngờ (như ốm đau, giảm lương, biến động kinh tế vĩ mô).

### 1.2. Công thức Toán học
Trong quy trình xử lý dữ liệu của đề tài (tại Tầng Silver của Medallion Lakehouse), chỉ số DTI được tính toán trực tiếp từ dữ liệu đăng ký vay:

$$DTI = \frac{\text{Loan Amount}}{\text{Person Income}}$$

*Nếu tính theo chu kỳ nghĩa vụ trả nợ định kỳ hàng tháng:*
$$DTI_{\text{monthly}} = \frac{\text{Monthly Debt Service}}{\text{Monthly Gross Income}}$$

Trong đó:
- $\text{Loan Amount}$: Tổng số tiền khách hàng yêu cầu được vay (USD/VND).
- $\text{Person Income}$: Tổng thu nhập hàng năm của khách hàng được ghi nhận và xác minh (USD/VND).

### 1.3. Khung Phân tầng Ngưỡng Rủi ro DTI trong Ngân hàng
Theo chuẩn mực thẩm định của các ngân hàng thương mại:

| Khoảng Giá Trị DTI | Mức Độ Rủi Ro | Đánh Giá Năng Lực Chi Trả | Quyết Định Nghiệp Vụ Tương Ứng |
| :---: | :---: | :--- | :--- |
| **$DTI \le 0.20$** (< 20%) | **Rất Thấp (An toàn)** | Khách hàng chỉ dùng dưới 20% thu nhập để trả nợ. Dư địa tích lũy và an toàn tài chính cực cao. | Phê duyệt tự động hạn mức tối đa (100%). |
| **$0.20 < DTI \le 0.35$** (20% - 35%) | **Trung Bình (Tiêu chuẩn)** | Áp lực trả nợ ở mức vừa phải, vẫn nằm trong khả năng cân đối chi tiêu sinh hoạt thông thường. | Phê duyệt hạn mức có điều chỉnh (duyệt 70% số tiền vay). |
| **$0.35 < DTI \le 0.45$** (35% - 45%) | **Cao (Cảnh báo)** | Nguy cơ vỡ nợ tăng vọt gấp **3.2 lần** so với nhóm an toàn. Khách hàng dễ mất khả năng thanh toán nếu có rủi ro nhỏ. | Yêu cầu tài sản thế chấp / người bảo lãnh. |
| **$DTI > 0.45$** (> 45%) | **Báo Động Đỏ (Nguy hiểm)** | Vượt ngưỡng an toàn cấp tín dụng. Gần như chắc chắn mất khả năng thanh toán khi gặp cú sốc tài chính. | Từ chối cấp tín dụng (Reject). |

### 1.4. Ví dụ Tính toán Minh họa & Cơ chế "Cứu khoản vay"
- **Tình huống thực tế:** Khách hàng Nguyễn Văn A có thu nhập 20 triệu đồng/tháng (240 triệu đồng/năm), nộp hồ sơ xin vay 96 triệu đồng.
  $$DTI_{\text{initial}} = \frac{96,000,000}{240,000,000} = 0.40$$
  *(tương đương 40%)*
  Mức DTI = 40% rơi vào vùng rủi ro cao, nguy cơ bị hệ thống tự động từ chối là rất lớn.
- **Cơ chế điều chỉnh hạn mức 70% của Nhóm 2:**
  Hệ thống can thiệp bằng cách giảm hạn mức giải ngân xuống 70% số tiền xin vay:
  $$\text{Adjusted Loan Amount} = 96,000,000 \times 0.70 = 67,200,000 \text{ VND}$$
  Lúc này, chỉ số DTI mới là:
  $$DTI_{\text{adjusted}} = \frac{67,200,000}{240,000,000} = 0.28$$
  *(tương đương 28%)*
  Chỉ số $DTI$ ngay lập tức giảm từ 40% xuống 28%, đưa hồ sơ từ vùng "Nguy cơ cao" quay trở lại vùng "An toàn chấp nhận được", giải cứu thành công khoản vay mà vẫn bảo vệ nguồn vốn ngân hàng.

---

## 🛡️ 2. CHỈ SỐ GÁNH NẶNG TÍN DỤNG (CREDIT BURDEN INDEX - CBI)

### 2.1. Tại sao cần CBI bên cạnh chỉ số DTI?
Chỉ số DTI tuy kinh điển nhưng có một nhược điểm lớn: **Chỉ xem xét quy mô khoản nợ gốc so với thu nhập, hoàn toàn bỏ qua hai yếu tố cực kỳ quan trọng là Lãi suất vay và Độ ổn định nghề nghiệp của người vay**.

*Hãy xem xét kịch bản so sánh:*
- Khách hàng X và Khách hàng Y đều có thu nhập $60,000$ USD/năm và cùng xin vay $15,000$ USD $\rightarrow$ Cả hai đều có $DTI = \frac{15,000}{60,000} = 0.25$.
- Tuy nhiên:
  - Khách hàng X vay với lãi suất ưu đãi 8.5%/năm và đã làm việc ổn định **10 năm** tại một tập đoàn viễn thông lớn.
  - Khách hàng Y vay với lãi suất cao 18.5%/năm và mới đi làm được **4 tháng** (thâm niên công tác xem như $0$ năm).
- Rõ ràng rủi ro của Khách hàng Y cao hơn gấp nhiều lần Khách hàng X, nhưng chỉ số DTI không thể phân biệt được. Do đó, đề tài xây dựng chỉ số nâng cao **Credit Burden Index (CBI)**.

### 2.2. Công thức Toán học
$$CBI = \frac{\text{Loan Amount} \times (1 + \text{Interest Rate} / 100)}{\text{Person Income} \times \max(\text{Emp Length}, 1)}$$

### 2.3. Phân tích Chi tiết Từng Thành phần trong Công thức

1. **Tử số: $\text{Loan Amount} \times (1 + \text{Interest Rate} / 100)$ - Tổng Nghĩa vụ Chi trả Thực tế**
   - Không chỉ tính tiền nợ gốc, tử số phản ánh toàn bộ số tiền gốc cộng tiền lãi phát sinh mà người vay có trách nhiệm pháp lý phải hoàn trả cho ngân hàng.
   - Khi lãi suất càng cao, tử số càng phình to, phản ánh gánh nặng chi phí vốn đè nặng lên người đi vay.
2. **Mẫu số: $\text{Person Income} \times \max(\text{Emp Length}, 1)$ - Năng lực Tài chính Tích lũy có Trọng số Thâm niên**
   - $\text{Person Income}$: Dòng tiền thu nhập hàng năm tạo ra nguồn trả nợ.
   - $\text{Emp Length}$ (Số năm làm việc liên tục tại cơ quan hiện tại): Thể hiện độ vững chắc của vị trí việc làm. Nhân viên có thâm niên 5 - 10 năm có xác suất bị sa thải hoặc đứt gãy thu nhập thấp hơn rất nhiều so với người thử việc. Thâm niên càng cao làm mẫu số càng lớn, kéo giảm chỉ số rủi ro $CBI$.
   - **Hàm $\max(\text{Emp Length}, 1)$:** Đóng vai trò chốt chặn toán học (Mathematical Safeguard):
     - Ngăn ngừa lỗi chia cho 0 khi khách hàng có thâm niên làm việc dưới 1 năm ($\text{Emp Length} = 0$).
     - Chuẩn hóa mức thâm niên sàn tối thiểu là 1 năm đối với lao động mới tham gia thị trường.

### 2.4. So sánh Thực nghiệm Giữa 2 Hồ sơ Khách hàng

| Tiêu Chí So Sánh | Khách Hàng X (Rất An Toàn) | Khách Hàng Y (Rủi Ro Cao) |
| :--- | :---: | :---: |
| Thu nhập hàng năm (`person_income`) | $60,000$ USD | $60,000$ USD |
| Số tiền xin vay (`loan_amnt`) | $15,000$ USD | $15,000$ USD |
| Lãi suất vay (`loan_int_rate`) | 8.5% | 18.5% |
| Thâm niên công tác (`person_emp_length`)| 8 năm | 0 năm (mới đi làm) |
| **Chỉ số DTI thông thường** | **0.25 (25%)** | **0.25 (25%)** *(Không phân biệt được)* |
| **Tính toán Tử số CBI (Nghĩa vụ trả)** | $15,000 \times (1 + 0.085) = 16,275$ USD | $15,000 \times (1 + 0.185) = 17,775$ USD |
| **Tính toán Mẫu số CBI (Năng lực tích lũy)**| $60,000 \times \max(8, 1) = 480,000$ USD | $60,000 \times \max(0, 1) = 60,000$ USD |
| **Chỉ số CBI cuối cùng** | $\frac{16,275}{480,000} = \mathbf{0.0339}$ | $\frac{17,775}{60,000} = \mathbf{0.2963}$ |
| **Đánh giá rủi ro từ CBI** | **Cực kỳ an toàn** ($CBI$ rất thấp) | **Rủi ro cao gấp 8.7 lần** Khách hàng X |

Nhờ có chỉ số $CBI$, mô hình Machine Learning nhận diện chính xác sự khác biệt về độ ổn định dòng tiền giữa các khách hàng, tránh được bẫy định giá sai lệch của chỉ số DTI đơn lẻ.

---

## 📈 3. ĐIỂM TÍN DỤNG FICO SCORE (FAIR ISAAC CORPORATION)

### 3.1. Bản chất Nghiệp vụ & Khái niệm
Trong hệ sinh thái tài chính toàn cầu, **FICO Score** là thước đo chuẩn mực được sử dụng bởi hơn 90% các ngân hàng và định chế tài chính hàng đầu tại Hoa Kỳ và thế giới. Điểm FICO chuẩn dao động trong khoảng từ **300 đến 850 điểm**: Điểm số càng cao phản ánh mức độ uy tín tín dụng càng lớn và xác suất vỡ nợ càng thấp.

Mô hình học máy Random Forest tại Tầng Gold xuất ra kết quả là xác suất vỡ nợ $p = P(\text{Default} = 1 \mid \mathbf{X}) \in [0, 1]$. Để phục vụ người dùng cuối và ban giám đốc, hệ thống phải chuyển đổi xác suất $p$ này sang thang điểm FICO tiêu chuẩn.

### 3.2. Công thức Toán học Hàm Log-Odds (Logit Transformation)

$$S = 600 + \frac{\ln\left(\frac{1 - p}{p}\right)}{\ln(2)} \times 40$$

### 3.3. Cơ sở Toán học & Thống kê Chi tiết của Từng Thành phần

#### 1. Thành phần Tỷ số Cược (Odds Ratio): $\text{Odds} = \frac{1 - p}{p}$
- $1 - p$ là xác suất khách hàng trả nợ tốt (`loan_status = 0`).
- $p$ là xác suất khách hàng vỡ nợ (`loan_status = 1`).
- Tỷ số $\frac{1 - p}{p}$ phản ánh tỷ lệ cược: *Trung bình có bao nhiêu khách hàng trả nợ tốt trên một khách hàng bị vỡ nợ*.
  - Nếu $p = 0.50 \Rightarrow \text{Odds} = \frac{0.50}{0.50} = 1$ (Tỷ lệ 1:1, cơ hội trả nợ và bùng nợ ngang nhau).
  - Nếu $p = 0.10 \Rightarrow \text{Odds} = \frac{0.90}{0.10} = 9$ (Cứ 9 người trả nợ tốt thì mới có 1 người bùng nợ).
  - Nếu $p = 0.01 \Rightarrow \text{Odds} = \frac{0.99}{0.01} = 99$ (Độ an toàn cực cao).

#### 2. Thành phần Hàm Logarit Tự nhiên: $\ln\left(\frac{1 - p}{p}\right)$ (Log-Odds)
Hàm Log-Odds (Logit) có nhiệm vụ co giãn phi tuyến: chuyển đổi miền giá trị của Odds từ khoảng $(0, +\infty)$ thành một biến liên tục trải dài trên toàn bộ trục số thực $(-\infty, +\infty)$, tạo điều kiện chuẩn hóa tuyến tính sang thang điểm mong muốn.

#### 3. Điểm Chuẩn Cân bằng (Base Score): $600$ điểm
Tại điểm mà cơ hội trả nợ và vỡ nợ là ngang ngửa nhau ($p = 0.50$), ta có:
$$\text{Odds} = \frac{1 - 0.50}{0.50} = 1 \Rightarrow \ln(1) = 0$$
Khi đó:
$$S = 600 + 0 \times \frac{40}{\ln(2)} = 600$$
*(tương đương 600 điểm)*
Như vậy, **600 điểm là điểm chuẩn trung tâm (Base Reference Point)** của toàn bộ thang đo.

#### 4. Hệ số Thang đo (Scaling Factor): $\frac{40}{\ln(2)}$
Hệ số này được thiết lập để hiện thực hóa nguyên tắc kinh điển của tổ chức Fair Isaac Corporation:
> **"Quy tắc Nhân đôi Tỷ số Cược" (Double the Odds):**  
> *Cứ mỗi khi mức độ an toàn của khách hàng tăng gấp đôi ($\text{Odds}_{\text{new}} = 2 \times \text{Odds}_{\text{old}}$), điểm tín dụng FICO của khách hàng sẽ tăng thêm đúng 40 điểm.*

**Chứng minh toán học:**
Giả sử khách hàng A có tỷ số cược là $\text{Odds}_A$, điểm số là $S_A$. Khách hàng B có mức độ an toàn gấp đôi khách hàng A ($\text{Odds}_B = 2 \times \text{Odds}_A$), điểm số là $S_B$.
Khoảng chênh lệch điểm giữa hai khách hàng là:
$$\Delta S = S_B - S_A = \left[ 600 + \frac{\ln(2 \times \text{Odds}_A)}{\ln(2)} \times 40 \right] - \left[ 600 + \frac{\ln(\text{Odds}_A)}{\ln(2)} \times 40 \right]$$
Áp dụng tính chất logarit của một tích $\ln(a \cdot b) = \ln(a) + \ln(b)$:
$$\Delta S = \frac{\ln(2) + \ln(\text{Odds}_A) - \ln(\text{Odds}_A)}{\ln(2)} \times 40 = \frac{\ln(2)}{\ln(2)} \times 40 = 40$$
*(tăng đúng 40 điểm theo chuẩn FICO)*

### 3.4. Bảng Tra cứu Quy đổi Chi tiết từ Xác suất $p$ sang Điểm FICO

| Xác Suất Vỡ Nợ ($p$) | Tỷ Số Cược Odds ($\frac{1-p}{p}$) | Điểm FICO Tính Được ($S$) | Phân Nhóm Tín Nhiệm | Quyết Định Duyệt Vay Tương Ứng |
| :---: | :---: | :---: | :--- | :--- |
| **0.01 (1%)** | 99.00 | **`865`** $\rightarrow$ Giới hạn trần **`850`** | **Exceptional (Tối ưu)** | Duyệt tự động 100%, Lãi suất siêu ưu đãi 8.5% |
| **0.03 (3%)** | 32.33 | **`800`** | **Exceptional (Xuất sắc)** | Duyệt tự động 100%, Lãi suất 8.5% |
| **0.05 (5%)** | 19.00 | **`770`** | **Very Good (Rất tốt)** | Duyệt tự động 100%, Lãi suất 8.5% |
| **0.10 (10%)** | 9.00 | **`727`** | **Good (Khá / Tốt)** | Duyệt tự động 100%, Lãi suất 8.5% |
| **0.15 (15%)** | 5.67 | **`700`** | **Good (Đạt chuẩn)** | Ranh giới Nhóm 1 và Nhóm 2 |
| **0.20 (20%)** | 4.00 | **`680`** | **Fair (Trung bình khá)** | Duyệt tự động hạn mức 70%, Lãi suất 11.5% |
| **0.35 (35%)** | 1.86 | **`636`** | **Near Prime (Dưới chuẩn)** | Ranh giới Nhóm 2 và Nhóm 3 (Điểm cực đại Youden's J) |
| **0.40 (40%)** | 1.50 | **`623`** | **Poor (Kém)** | Thẩm định thủ công, bắt buộc tài sản thế chấp |
| **0.50 (50%)** | 1.00 | **`600`** *(Điểm gốc)* | **Poor (Rủi ro cao)** | Thẩm định thực địa gắt gao |
| **0.60 (60%)** | 0.67 | **`577`** | **Subprime (Rất rủi ro)** | Ranh giới từ chối cho vay (Reject Threshold) |
| **0.70 (70%)** | 0.43 | **`551`** | **Deep Subprime (Báo động)**| Từ chối cho vay tự động (Auto-Reject) |
| **0.85 (85%)** | 0.18 | **`500`** | **Deep Subprime (Nguy hiểm)**| Từ chối cho vay tự động (Auto-Reject) |

---

## 📊 4. TỔNG HỢP VAI TRÒ CỦA BỘ BA CHỈ SỐ TRONG QUY TRÌNH THẨM ĐỊNH

Trong hệ thống xử lý hồ sơ tín dụng tự động, bộ ba chỉ số $DTI$, $CBI$ và $FICO$ phối hợp nhịp nhàng theo chuỗi logic khép kín:

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                          HỒ SƠ KHÁCH HÀNG NỘP TRỰC TUYẾN                               │
└───────────────────────────────────────────┬────────────────────────────────────────────┘
                                            │
                                            ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│  BƯỚC 1: SÀNG LỌC ĐÒN BẨY & GÁNH NẶNG TÀI CHÍNH (TẦNG SILVER)                          │
│  • Tính DTI: Đo lường tỷ lệ nợ / thu nhập.                                             │
│  • Tính CBI: Đo lường gánh nặng lãi suất có trọng số thâm niên công tác.               │
│  ==> Nếu DTI và CBI nằm trong ngưỡng khả thi, hồ sơ chuyển sang bước Mô hình hóa.     │
└───────────────────────────────────────────┬────────────────────────────────────────────┘
                                            │
                                            ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│  BƯỚC 2: DỰ BÁO XÁC SUẤT VỠ NỢ VỚI SPARK MLLIB (TẦNG GOLD)                             │
│  • Random Forest kết hợp DTI, CBI, Lịch sử CIC, v.v...                                 │
│  ==> Xuất ra Vector xác suất vỡ nợ: p = P(Default = 1 | X)                            │
└───────────────────────────────────────────┬────────────────────────────────────────────┘
                                            │
                                            ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│  BƯỚC 3: QUY ĐỔI ĐIỂM FICO SCORE & RA QUYẾT ĐỊNH GIẢI NGÂN (DECISION ENGINE)           │
│  • Hàm Log-Odds chuyển đổi p thành Điểm FICO S in [300, 850].                          │
│  • Phân tầng 4 nhóm rủi ro (Youden's J & Basel II).                                   │
│  • Áp dụng Mô hình Định giá Lãi suất theo Rủi ro (Risk-Based Pricing): 8.5% - 14.5%.   │
│  • Điều chỉnh hạn mức 70% để kéo DTI về vùng an toàn đối với Nhóm 2.                  │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 📚 TÀI LIỆU THAM KHẢO

1. **Fair Isaac Corporation (FICO).** (2020). *Understanding FICO Scores: How Credit Scoring Works*. FICO Technical Whitepaper.
2. **Thomas, L. C., Edelman, D. B., & Crook, J. N.** (2002). *Credit Scoring and Its Applications*. SIAM Monographs on Mathematical Modeling and Computation.
3. **Anderson, R.** (2007). *The Credit Scoring Toolkit: Theory and Practice for Retail Credit Risk Management and Decision Automation*. Oxford University Press.
4. **Basel Committee on Banking Supervision (BCBS).** (2006). *International Convergence of Capital Measurement and Capital Standards: A Revised Framework (Basel II)*. Bank for International Settlements.
5. **Altman, E. I.** (1968). *Financial ratios, discriminant analysis and the prediction of corporate bankruptcy*. The Journal of Finance, 23(4), 589-609.
6. **Mishkin, F. S.** (2018). *The Economics of Money, Banking, and Financial Markets (12th ed.)*. Pearson.
