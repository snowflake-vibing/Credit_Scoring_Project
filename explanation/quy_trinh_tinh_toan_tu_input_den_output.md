# QUY TRÌNH TÍNH TOÁN TOÀN DIỆN TỪ INPUT ĐẾN OUTPUT TRONG MÔ HÌNH CREDIT SCORING

> **Đề tài:** Mô Hình Chấm Điểm Tín Dụng & Thẩm Định Rủi Ro Vỡ Nợ (Loan Default & Credit Scoring)  
> **Kiến trúc:** Medallion Lakehouse (Bronze $\rightarrow$ Silver $\rightarrow$ Gold) trên nền tảng **Databricks Serverless / PySpark MLlib**

---

## 📌 1. SƠ ĐỒ TỔNG THỂ LUỒNG XỬ LÝ (END-TO-END WORKFLOW)

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                GIAI ĐOẠN 1: INPUT ĐẦU VÀO                              │
│  Hồ sơ vay khách hàng: Nhân khẩu học (Age, Income, Home), Khoản vay (Amnt, Intent,    │
│  Grade), Lịch sử tín dụng (Default on file, Cred hist length, Emp length)             │
└───────────────────────────────────────────┬────────────────────────────────────────────┘
                                            │
                                            ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                   GIAI ĐOẠN 2: LƯU TRỮ & LÀM SẠCH (BRONZE & SILVER)                    │
│  • Bronze Layer: Lưu nguyên bản bảng Delta thô (ACID Transactions)                     │
│  • Silver Layer: Filter outliers (18 <= Age <= 80), Impute giá trị thiếu (Emp, Rate),  │
│    Cast kiểu dữ liệu chuẩn (Double, Integer)                                           │
└───────────────────────────────────────────┬────────────────────────────────────────────┘
                                            │
                                            ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│               GIAI ĐOẠN 3: PHÂN TÍCH KPIS & WINDOW FUNCTIONS (SPARK SQL)                │
│  • Tính tỷ lệ nợ trên thu nhập: DTI = Loan_Amnt / Person_Income                        │
│  • Tính gánh nặng tín dụng: CBI = Loan_Amnt * (1 + Rate) / (Income * Emp_Length)       │
│  • Xếp hạng thu nhập phân vùng: Window.partitionBy("loan_intent").orderBy(Income)      │
└───────────────────────────────────────────┬────────────────────────────────────────────┘
                                            │
                                            ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│           GIAI ĐOẠN 4: CHUỖI FEATURE ENGINEERING & MÔ HÌNH HÓA (SPARK MLLIB)           │
│  • StringIndexer: Chuyển chuỗi danh mục sang số nguyên                                 │
│  • OneHotEncoder: Mã hóa Vector thưa cho biến danh mục đa lớp                          │
│  • VectorAssembler: Gom toàn bộ 11 biến vào 1 Vector 'raw_features'                    │
│  • StandardScaler: Chuẩn hóa Z-Score Vector về cùng thang đo                           │
│  • RandomForestClassifier: Huấn luyện phân tán 50 cây quyết định                       │
│  • CrossValidator (3-Folds): Tối ưu hóa siêu tham số (maxDepth, numTrees)              │
└───────────────────────────────────────────┬────────────────────────────────────────────┘
                                            │
                                            ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│           GIAI ĐOẠN 5: ĐỘNG CƠ PHÂN TẦNG RỦI RO & ĐỊNH GIÁ (DECISION ENGINE)           │
│  • Trích xuất Vector xác suất: p = P(Default = 1 | Features)                           │
│  • Quy đổi điểm FICO Score: S = 600 + (ln((1-p)/p) / ln(2)) * 40                       │
│  • Phân tầng 4 nhóm rủi ro: [p < 15%], [15% <= p < 35%], [35% <= p < 60%], [p >= 60%]  │
│  • Định giá Risk-Based Pricing: Lãi suất = 8.5% + (p * 15%)                            │
└───────────────────────────────────────────┬────────────────────────────────────────────┘
                                            │
                                            ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                            GIAI ĐOẠN 6: OUTPUT KẾT QUẢ CUỐI CÙNG                       │
│  Bảng Delta Gold (`gold_credit_scoring`): Nhãn dự báo (0/1), Xác suất vỡ nợ (p),       │
│  Điểm tín dụng, Phân tầng rủi ro, Quyết định duyệt vay, Hạn mức cấp, Lãi suất đề xuất  │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 📥 2. CHI TIẾT GIAI ĐOẠN 1: INPUT DỮ LIỆU ĐẦU VÀO

Hệ thống tiếp nhận thông tin từ hồ sơ đăng ký vay trực tuyến của khách hàng thông qua bảng `credit_risk_dataset.csv`. Bảng dữ liệu bao gồm **11 biến giải thích (Features)** và **1 biến mục tiêu (Label)**:

| Tên Cột (Column) | Kiểu Dữ Liệu | Nhóm Thuộc Tính | Ý Nghĩa Kinh Doanh | Ví Dụ Mẫu |
| :--- | :---: | :--- | :--- | :---: |
| `person_age` | Integer | Nhân khẩu học | Tuổi của người nộp đơn | $25$ |
| `person_income` | Double | Năng lực tài chính | Thu nhập hàng năm của khách hàng (USD/VND) | $60,000$ |
| `person_home_ownership` | String | Tài sản tích lũy | Tình trạng nhà ở (`RENT`, `OWN`, `MORTGAGE`, `OTHER`) | `RENT` |
| `person_emp_length` | Double | Độ ổn định nghề nghiệp | Số năm làm việc tại cơ quan hiện tại (thâm niên) | $3.0$ |
| `loan_intent` | String | Mục đích sử dụng vốn | Mục đích vay (`EDUCATION`, `MEDICAL`, `VENTURE`,...) | `EDUCATION` |
| `loan_grade` | String | Xếp hạng nội bộ | Hạng tín dụng sơ bộ theo tiêu chuẩn (`A` đến `G`) | `B` |
| `loan_amnt` | Double | Quy mô khoản vay | Số tiền khách hàng đề nghị vay | $10,000$ |
| `loan_int_rate` | Double | Lãi suất quá khứ/hiện tại | Mức lãi suất của khoản vay đề nghị (%) | $11.14\%$ |
| `loan_percent_income` | Double | Đòn bẩy tài chính | Tỷ lệ số tiền vay so với thu nhập hàng năm | $0.17$ |
| `cb_person_default_on_file` | String | Lịch sử CIC | Đã từng có nợ xấu ghi nhận trên hệ thống tín dụng chưa? (`Y`/`N`) | `N` |
| `cb_person_cred_hist_length` | Integer | Lịch sử tín dụng | Số năm có lịch sử giao dịch tín dụng | $3$ |
| **`loan_status` (Label)** | Integer | **Biến Mục Tiêu** | `0`: Trả nợ đúng hạn; `1`: Vỡ nợ (chậm trả $>90$ ngày) | `0` hoặc `1` |

---

## ⚙️ 3. CHI TIẾT GIAI ĐOẠN 2 & 3: XỬ LÝ LÀM SẠCH VÀ TÍNH TOÁN CHỈ SỐ

### 3.1. Tầng Bronze: Tiếp nhận dữ liệu thô
Dữ liệu thô từ CSV được nạp vào bảng Delta `workspace.default.bronze_credit_data` để bảo toàn nguyên trạng dữ liệu gốc, phục vụ truy vết lịch sử (Time Travel) và kiểm toán.

### 3.2. Tầng Silver: Xử lý chất lượng dữ liệu phân tán (Data Preprocessing)
Thực hiện các thao tác biến đổi PySpark trên toàn bộ cụm:
1. **Lọc dữ liệu ngoại lai phi lý (Outlier Filtering):**
   - Lọc bỏ các dòng có độ tuổi không nằm trong độ tuổi lao động hợp pháp: $18 \le \text{person\_age} \le 80$.
   - Lọc bỏ các dòng có thu nhập không dương: $\text{person\_income} > 0$.
2. **Điền giá trị khuyết thiếu (Missing Value Imputation):**
   - `person_emp_length`: Nếu `NULL`, điền $0.0$ (giả định lao động mới bắt đầu đi làm).
   - `loan_int_rate`: Nếu `NULL`, điền giá trị trung vị thị trường là $11.0\%$.
   - `cb_person_cred_hist_length`: Nếu `NULL`, điền $1$ năm.
3. Lưu kết quả làm sạch vào Delta Table `workspace.default.silver_credit_data`.

### 3.3. Tính toán các chỉ số tài chính nâng cao (Spark SQL & Window Functions)
Trong tầng Silver, hệ thống tính toán thêm các biến phái sinh mang tính nghiệp vụ cao:
* **Tỷ lệ Nợ trên Thu nhập (Debt-to-Income - DTI):**
  $$DTI = \frac{\text{loan\_amnt}}{\text{person\_income}}$$
* **Chỉ số Gánh nặng Tín dụng (Credit Burden Index - CBI):**
  $$CBI = \frac{\text{loan\_amnt} \times (1 + \text{loan\_int\_rate} / 100)}{\text{person\_income} \times \max(\text{person\_emp\_length}, 1)}$$
* **Xếp hạng thu nhập phân vùng (Income Rank):**
  Sử dụng Window Function phân vùng theo mục đích vay (`loan_intent`) và xếp hạng thu nhập giảm dần để đánh giá vị thế tài chính tương đối của khách hàng trong cùng nhóm vay.

---

## 🤖 4. CHI TIẾT GIAI ĐOẠN 4: PIPELINE HỌC MÁY PHÂN TÁN (SPARK MLLIB)

Để đưa dữ liệu vào thuật toán học máy phân tán, dữ liệu phải trải qua một chuỗi biến đổi hình học (Pipeline Transformers):

```
Dữ liệu Thô (Silver) 
   │
   ├─► [StringIndexer] ────► Mã hóa cột chuỗi thành chỉ số nguyên (0, 1, 2,...)
   │
   ├─► [OneHotEncoder] ────► Biến chỉ số nguyên thành Vector nhị phân thưa (Sparse Vector)
   │
   ├─► [VectorAssembler] ──► Gom tất cả biến danh mục + số học thành 1 Vector 'raw_features'
   │
   ├─► [StandardScaler] ───► Chuẩn hóa độ lệch chuẩn: z = (x - mean) / std
   │
   └─► [RandomForest] ─────► Rừng cây quyết định phân tán (50 cây, maxDepth = 10)
```

### Các bước toán học cụ thể:
1. **Mã hóa One-Hot:** 3 biến danh mục (`person_home_ownership`, `loan_intent`, `cb_person_default_on_file`) được chuyển thành các véc-tơ chỉ báo nhị phân để mô hình không gán thứ tự ưu tiên giả định.
2. **Gom véc-tơ (Vector Assembler):** Tập hợp $11$ biến đặc trưng thành một véc-tơ đa chiều:
   $$\vec{X} = [x_1, x_2, \dots, x_k]^T \in \mathbb{R}^{K}$$
3. **Chuẩn hóa StandardScaler:** Đưa các biến có độ lệch lớn như thu nhập ($60,000$) và tuổi ($25$) về cùng thang đo đơn vị phương sai.
4. **Mô hình Random Forest Classifier:** 
   - Tập hợp 50 cây quyết định độc lập (Bootstrap Aggregating).
   - Mỗi cây được huấn luyện trên một tập con ngẫu nhiên của dữ liệu và thuộc tính.
   - Kết quả dự báo của từng cây là xác suất vỡ nợ: $h_t(\vec{X}) \in \{0, 1\}$.
   - Xác suất tổng hợp là trung bình trọng số của tất cả các cây:
     $$p = P(\text{Default}=1 | \vec{X}) = \frac{1}{T} \sum_{t=1}^{T} P_t(\text{Default}=1 | \vec{X})$$
5. **Đánh giá & Tinh chỉnh siêu tham số:** Dùng `CrossValidator` (3-Folds) thử nghiệm các tổ hợp `maxDepth` $\in \{5, 10\}$ và `numTrees` $\in \{20, 50\}$, tối ưu theo hàm mục tiêu diện tích dưới đường cong **ROC-AUC (đạt $0.8745$)**.

---

## 🧮 5. CHI TIẾT GIAI ĐOẠN 5: ĐỘNG CƠ PHÂN TẦNG RỦI RO & ĐỊNH GIÁ LÃI SUẤT (DECISION ENGINE)

Sau khi mô hình trả về véc-tơ xác suất $\vec{P} = [P_0, P_1] = [1 - p, p]$, Động cơ Ra quyết định (Decision Engine) thực hiện 3 bước tính toán nghiệp vụ:

### Bước 1: Quy đổi xác suất sang Điểm Tín dụng FICO Score ($S$)
Sử dụng hàm Log-Odds (Logit Transformation) chuẩn hóa về thang điểm $300 - 850$:
$$S = 600 + \frac{\ln\left(\frac{1 - p}{p}\right)}{\ln(2)} \times 40$$
* Khi $p = 0.05 \Rightarrow S \approx 770$ điểm (Hạng Xuất sắc).
* Khi $p = 0.20 \Rightarrow S \approx 680$ điểm (Hạng Khá).
* Khi $p = 0.40 \Rightarrow S \approx 623$ điểm (Hạng Trung bình).
* Khi $p = 0.65 \Rightarrow S \approx 564$ điểm (Hạng Kém).

### Bước 2: Phân tầng Rủi ro theo Ngưỡng cắt ($p$)
Áp dụng hàm điều kiện đa tầng:
```python
Risk_Segment = (
    "1. Rủi ro Thấp"      if p < 0.15 else
    "2. Rủi ro Trung Bình" if p < 0.35 else
    "3. Rủi ro Cao"       if p < 0.60 else
    "4. Rủi ro Rất Cao"
)
```

### Bước 3: Định giá Lãi suất theo Rủi ro (Risk-Based Pricing Model)
Tính mức lãi suất đề xuất dựa trên chi phí vốn và biên bù đắp rủi ro:
$$R_{\text{loan}}(\%) = R_{\text{base}} (8.5\%) + \Delta_{\text{Risk}}(p)$$
Trong đó:
$$\Delta_{\text{Risk}}(p) = p \times 15\%$$

---

## 📤 6. CHI TIẾT GIAI ĐOẠN 6: OUTPUT ĐẦU RA VÀ HÀNH ĐỘNG HỆ THỐNG

Kết quả được ghi vào Delta Table **`workspace.default.gold_credit_scoring`** và xuất ra màn hình phê duyệt của ngân hàng với các trường thông tin đầy đủ:

### Bảng Minh Họa Output Thực Tế Cho 4 Hồ Sơ Khách Hàng Tiêu Biểu:

| Mã Hồ Sơ | Tuổi / Thu nhập | Số Tiền Xin Vay | Xác Suất Nợ Xấu ($p$) | Điểm FICO ($S$) | Phân Tầng Rủi Ro | Quyết Định Duyệt Vay | Hạn Mức Giải Ngân | Lãi Suất Đề Xuất | Hành Động Vận Hành |
| :---: | :---: | :---: | :---: | :---: | :--- | :--- | :---: | :---: | :--- |
| **HS-01** | 29 tuổi / 85tr | 100 triệu | **$4.2\%$** | **780** | **1. Rủi ro Thấp** | **Duyệt Tự Động (Auto-Approve)** | **100 triệu** (100%) | **8.5% / năm** | Giải ngân tài khoản trong 3 phút |
| **HS-02** | 24 tuổi / 45tr | 80 triệu | **$22.5\%$** | **672** | **2. Rủi ro Trung Bình** | **Duyệt Hạn Mức Tự Động** | **56 triệu** (70%) | **11.5% / năm** | Gửi thông báo phê duyệt hạn mức 70% |
| **HS-03** | 35 tuổi / 30tr | 120 triệu | **$48.0\%$** | **605** | **3. Rủi ro Cao** | **Thẩm Định Thủ Công** | Theo tài sản | **14.5% / năm** | Chuyển chuyên viên tín dụng thẩm định thực địa & thế chấp |
| **HS-04** | 22 tuổi / 20tr | 90 triệu | **$73.5\%$** | **541** | **4. Rủi ro Rất Cao** | **Từ Chối Vay (Auto-Reject)** | **0 đồng** (0%) | **N/A** | Gửi SMS từ chối do điểm rủi ro vượt ngưỡng |

---

## 💡 7. TỔNG KẾT Ý NGHĨA KINH TẾ CỦA QUY TRÌNH
1. **Tốc độ xử lý siêu tốc:** Giúp phê duyệt tự động $>75\%$ hồ sơ (Nhóm 1 + Nhóm 2 + Nhóm 4) trong vòng **$< 3$ phút**, không cần con người can thiệp.
2. **Cân bằng Lợi nhuận & Rủi ro:** Vừa kích cầu tăng trưởng tín dụng cho khách hàng tốt bằng lãi suất rẻ ($8.5\%$), vừa bảo toàn vốn ngân hàng bằng cách từ chối sớm các ca nợ xấu ($p \ge 60\%$).
3. **Tuân thủ quy chuẩn quốc tế:** Đáp ứng đầy đủ các yêu cầu kiểm định mô hình nội bộ của hiệp ước **Basel II & Basel III**.
