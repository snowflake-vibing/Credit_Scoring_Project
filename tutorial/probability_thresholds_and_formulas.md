# HƯỚNG DẪN GIẢI THÍCH CÔNG THỨC TOÁN HỌC & LÝ DO CHỌN NGƯỠNG XÁC SUẤT (p) TRONG DỰ ÁN CREDIT SCORING

> **Đề tài 7:** Mô Hình Chấm Điểm Tín Dụng & Thẩm Định Rủi Ro Vỡ Nợ  
> **Tài liệu hướng dẫn chuyên sâu dành cho Tiểu luận & Thuyết trình Bảo vệ Dự án**

---

## 📐 PHẦN 1: TỔNG HỢP CÁC CÔNG THỨC TOÁN HỌC & CHỈ SỐ TÀI CHÍNH

### 1. Chỉ số Tỷ lệ Nợ trên Thu nhập (Debt-to-Income Ratio - DTI)
$$DTI = \frac{\text{Loan Amount}}{\text{Person Income}}$$
* **Ý nghĩa nghiệp vụ:** Đo lường tỷ lệ dư nợ của khoản vay so với thu nhập hàng năm của khách hàng. Trong ngân hàng, DTI càng thấp ($DTI \le 0.35$) thì khả năng trả nợ đúng hạn của khách hàng càng cao.

### 2. Chỉ số Gánh nặng Tín dụng (Credit Burden Index - CBI)
$$CBI = \frac{\text{Loan Amount} \times (1 + \text{Loan Interest Rate})}{\text{Person Income} \times \text{Employment Length}}$$
* **Ý nghĩa nghiệp vụ:** Đánh giá tổng nghĩa vụ phải trả (gốc + lãi) so với tổng thu nhập tích lũy theo thâm niên công tác.

### 3. Công thức Quy đổi Xác suất Vỡ nợ ($p$) sang Điểm Tín dụng FICO Score ($S$)
Dựa trên hàm Log-Odds (Logit Transformation):
$$\text{Log-Odds} = \ln\left(\frac{1 - p}{p}\right)$$
$$S = 600 + \frac{\ln\left(\frac{1 - p}{p}\right)}{\ln(2)} \times 40$$
* **Ý nghĩa nghiệp vụ:** 
  * Khi xác suất nợ xấu $p \rightarrow 0$, điểm tín dụng $S \rightarrow 850$ (Khách hàng cực kỳ uy tín).
  * Khi xác suất nợ xấu $p \rightarrow 1$, điểm tín dụng $S \rightarrow 300$ (Khách hàng rủi ro rất cao).
  * Hằng số $40$ đại diện cho giá trị "PDO" (Points to Double the Odds - Điểm số để tỷ lệ cược uy tín tăng gấp đôi).

### 4. Công thức Định giá Lãi suất theo Rủi ro (Risk-Based Pricing Model)
$$\text{Lãi suất đề xuất (\%)} = \text{Lãi suất cơ sở (8.5\%)} + \Delta_{\text{Risk}} (p \times 15\%)$$
* **Ý nghĩa nghiệp vụ:** Bù đắp rủi ro tín dụng (Risk Premium). Khách hàng có xác suất nợ xấu $p$ cao sẽ phải chịu mức lãi suất vay cao hơn để bù đắp rủi ro trích lập dự phòng của ngân hàng.

---

## 🎯 PHẦN 2: LÝ DO KHOA HỌC & KINH DOANH KHI CHỌN CÁC NGƯỠNG XÁC SUẤT ($p$)

Khi mô hình **Random Forest Classifier** tính toán ra xác suất vỡ nợ $p = P(Y=1 | X)$, dự án phân chia thành **4 Phân tầng Rủi ro (Risk Segments)** dựa trên các ngưỡng cắt (Cutoff Thresholds):

| Phân tầng Rủi ro | Ngưỡng Xác suất ($p$) | Quyết định Duyệt Vay | Lãi suất vay đề xuất |
| :--- | :---: | :--- | :---: |
| **1. Rủi ro Thấp (Low Risk)** | $p < 0.15$ (15%) | **Duyệt Tự Động 100% (Auto-Approve)** | 8.5% / năm |
| **2. Rủi ro Trung Bình (Medium Risk)** | $0.15 \le p < 0.35$ (15% - 35%) | **Duyệt Hạn Mức Tự Động 70%** | 11.5% / năm |
| **3. Rủi ro Cao (High Risk)** | $0.35 \le p < 0.60$ (35% - 60%) | **Thẩm Định Thủ Công + Bảo Đảm** | 14.5% / năm |
| **4. Rủi ro Rất Cao (Very High Risk)** | $p \ge 0.60$ (60%) | **Từ Chối Cho Vay (Auto-Reject)** | Không cấp tín dụng |

---

### 🔍 GIẢI THÍCH CHI TIẾT LÝ DO CHỌN TỪNG NGƯỠNG $p$:

#### 1. Tại sao chọn ngưỡng $p = 0.15$ (15%) cho Nhóm Rủi ro Thấp?
* **Cơ sở tiêu chuẩn quốc tế:** Theo hiệp ước **Basel II & Basel III** trong quản trị rủi ro ngân hàng, tỷ lệ nợ xấu kỳ vọng (Expected Loss - EL) cho các khoản vay tín chấp tiêu dùng nhóm an toàn thường nằm dưới 15%.
* **Phân tích Tài chính:** Chi phí rủi ro $EL = PD \times LGD \times EAD$. Khi $p < 0.15$, chi phí tổn thất kỳ vọng nhỏ hơn biên lợi nhuận thu nhập lãi ròng (Net Interest Margin - NIM). Do đó ngân hàng đảm bảo **Lợi nhuận ròng dương (Positive Return)** mà không cần tốn chi phí nhân sự thẩm định thủ công.

#### 2. Tại sao chọn ngưỡng $p = 0.35$ (35%) cho Nhóm Rủi ro Trung bình?
* **Cơ sở cân bằng rủi ro:** Khách hàng ở nhóm này có năng lực tài chính ở mức khá, nhưng xác suất xảy ra biến cố chậm trả nằm từ 15% đến 35%.
* **Chiến lược Quản trị:** Nếu từ chối nhóm này, ngân hàng sẽ bỏ lỡ cơ hội kinh doanh (Opportunity Loss). Vì vậy, chiến lược hợp lý nhất là **cho vay nhưng kiểm soát dư nợ** bằng cách cắt giảm hạn mức vay còn **70%** để đảm bảo khả năng trả nợ.

#### 3. Tại sao chọn ngưỡng $p = 0.60$ (60%) làm Ranh giới Từ chối (Auto-Reject)?
* **Tối ưu hóa Ma trận Tổn thất (Cost-Benefit / Loss Matrix Trade-off):**
  * Tổn thất khi phê duyệt sai 1 hồ sơ vỡ nợ (False Positive - Nợ xấu) gấp **4 - 5 lần** so với lợi nhuận thu được từ 1 hồ sơ trả nợ đúng hạn (True Negative).
  * Khi $p \ge 0.60$, khả năng vỡ nợ là **đa số (>60%)**. Việc giải ngân cho nhóm này chắc chắn sẽ dẫn đến tỷ lệ nợ xấu nhóm 4-5 (nợ có khả năng mất vốn), làm gia tăng chi phí trích lập dự phòng và giảm hệ số an toàn vốn CAR của ngân hàng.

---

## 📈 PHẦN 3: TỐI ƯU HÓA NGƯỠNG CẮT BẰNG CHỈ SỐ YOUDEN'S J STATISTIC

Trong thống kê học máy, ngưỡng $p^*$ tối ưu tổng thể được xác định bằng chỉ số **Youden's J Statistic** trên đường cong ROC-AUC:

$$J(p) = \text{Sensitivity}(p) + \text{Specificity}(p) - 1 = \text{TPR}(p) - \text{FPR}(p)$$

* **Điểm tối ưu $p^*$** là điểm làm cho giá trị $J(p)$ đạt cực đại ($\max J$). Trong bài toán tín dụng này, ngưỡng $p^*$ cân bằng giữa việc loại bỏ nợ xấu và giữ chân khách hàng tốt nằm trong khoảng **$p^* \approx 0.32 - 0.35$**.
