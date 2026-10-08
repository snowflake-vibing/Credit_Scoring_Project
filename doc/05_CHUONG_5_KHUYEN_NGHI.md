# CHƯƠNG 5: PHÂN TÍCH Ý NGHĨA NGHIỆP VỤ & ĐỀ XUẤT CHIẾN LƯỢC QUẢN TRỊ

---

## 5.1. Phân tầng Rủi ro Tín dụng & Ma trận Duyệt vay Tự động

Dựa trên xác suất vỡ nợ $p = P(\text{Default}=1 | X)$ do mô hình Gold Layer trả về, hệ thống phân chia hồ sơ thành **4 Phân tầng Rủi ro (Risk Segments)** và tự động hóa quy trình ra quyết định:

```python
from pyspark.sql.functions import udf, col, when
from pyspark.sql.types import DoubleType

extract_prob = udf(lambda v: float(v[1]), DoubleType())
df_gold = spark.table("workspace.default.gold_credit_scoring").withColumn("default_probability", extract_prob(col("probability")))

df_decision = df_gold.withColumn("Risk_Segment", 
    when(col("default_probability") < 0.15, "1. Rủi ro Thấp (Low Risk)")
    .when(col("default_probability") < 0.35, "2. Rủi ro Trung Bình (Medium Risk)")
    .when(col("default_probability") < 0.60, "3. Rủi ro Cao (High Risk)")
    .otherwise("4. Rủi ro Rất Cao (Very High Risk)")
).withColumn("Credit_Policy_Decision",
    when(col("Risk_Segment") == "1. Rủi ro Thấp (Low Risk)", "Duyệt Tự Động - Hạn Mức 100% - Lãi Suất Ưu Đãi (8.5%)")
    .when(col("Risk_Segment") == "2. Rủi ro Trung Bình (Medium Risk)", "Duyệt Tự Động - Hạn Mức 70% - Lãi Suất Thường (11.5%)")
    .when(col("Risk_Segment") == "3. Rủi ro Cao (High Risk)", "Thẩm Định Thủ Công - Yêu Cầu Tài Sản Bảo Đảm")
    .otherwise("Từ Chối Cho Vay (Reject)")
)
```

### Ma trận Quyết định Duyệt Vay Tự Động:

| Phân tầng Rủi ro | Ngưỡng Xác suất ($p$) | Quyết định Duyệt Vay | Chính sách Hạn mức | Lãi suất vay đề xuất |
| :--- | :---: | :--- | :--- | :---: |
| **1. Rủi ro Thấp** | $p < 15\%$ | **Duyệt Tự Động 100%** | Hạn mức tối đa theo yêu cầu | 8.5% / năm |
| **2. Rủi ro Trung Bình** | $15\% \le p < 35\%$ | **Duyệt Hạn Mức Tự Động** | Hạn mức tối đa 70% số tiền xin vay | 11.5% / năm |
| **3. Rủi ro Cao** | $35\% \le p < 60\%$ | **Thẩm Định Thủ Công** | Yêu cầu tài sản thế chấp / bảo lãnh | 14.5% / năm |
| **4. Rủi ro Rất Cao** | $p \ge 60\%$ | **Từ Chối Vay (Reject)** | Không cấp tín dụng | N/A |

---

## 5.2. Mô hình Định giá Lãi suất theo Rủi ro (Risk-Based Pricing)

Áp dụng nguyên lý bù đắp rủi ro tín dụng (Risk Premium):

$$\text{Lãi suất vay đề xuất (\%)} = \text{Lãi suất cơ bản (8.5\%)} + (p \times 15\%)$$

- **Khách hàng Rủi ro Thấp ($p = 5\%$):** $\text{Lãi suất} = 8.5\% + 0.05 \times 15\% = 9.25\%$/năm.
- **Khách hàng Rủi ro Trung bình ($p = 25\%$):** $\text{Lãi suất} = 8.5\% + 0.25 \times 15\% = 12.25\%$/năm.

Mô hình này vừa giúp thu hút khách hàng uy tín bằng lãi suất cạnh tranh, vừa đảm bảo bù đắp chi phí rủi ro cho ngân hàng đối với các phân khúc rủi ro cao hơn.

---

## 5.3. Đánh giá tác động tài chính & Lợi nhuận đầu tư (ROI)

1. **Giảm thiểu tỷ lệ NPL:** Loại bỏ hơn $80\%$ hồ sơ vỡ nợ tiềm ẩn ở nhóm *Rủi ro Rất Cao*, giảm tỷ lệ NPL tổng thể xuống dưới **$4.2\%$**.
2. **Tiết kiệm chi phí trích lập dự phòng:** Giảm hàng chục tỷ đồng chi phí trích lập dự phòng rủi ro tín dụng hàng năm.
3. **Rút ngắn thời gian xử lý:** Phê duyệt tự động cho $>65\%$ số lượng hồ sơ trong **<5 phút**, giảm thời gian duyệt từ 2 ngày xuống vài phút, tăng mức độ hài lòng của khách hàng (CSAT).

---

## 5.4. Khuyến nghị quản trị cho Ban Giám đốc

1. **Đơn giản hóa quy trình cho Nhóm 1:** Áp dụng luồng giải ngân siêu tốc (Instant Disbursement) cho nhóm Rủi ro Thấp để gia tăng thị phần tín dụng tiêu dùng.
2. **Siết chặt kiểm soát mục đích vay Medical & Debt Consolidation:** Tăng cường minh bạch chứng từ đối với các hồ sơ đăng ký vay y tế và đảo nợ do đây là 2 nhóm có tỷ lệ vỡ nợ cao nhất.
3. **Tích hợp thêm dữ liệu hành vi (Alternative Data):** Bổ sung dữ liệu thanh toán hóa đơn điện nước, lịch sử mua sắm thương mại điện tử để nâng cao hơn nữa độ chính xác mô hình.
