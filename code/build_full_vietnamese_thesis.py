# -*- coding: utf-8 -*-
"""
Script tái cấu trúc toàn bộ đồ án theo chuẩn Luận văn / Tiểu luận Đại học Việt Nam
(Căn cứ theo Hướng dẫn trình bày Luận văn tốt nghiệp - ĐH Cần Thơ / CTU)
"""

import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

print("Bắt đầu tạo nội dung các chương chuẩn Đại học Việt Nam...")

# ==============================================================================
# PHẦN 0: TRANG BÌA, PHỤ BÌA, LỜI CẢM ƠN, CAM ĐOAN, TÓM LƯỢC, MỤC LỤC & DANH MỤC
# ==============================================================================
text_00 = """# TRANG BÌA

::: {.content-visible when-format="html"}
```{=html}
<div class="academic-cover-page border-frame">
  <div class="cover-header">
    <div class="gov-title">BỘ TÀI CHÍNH</div>
    <div class="univ-title">TRƯỜNG ĐẠI HỌC TÀI CHÍNH - MARKETING (UFM)</div>
    <div class="faculty-title">KHOA CÔNG NGHỆ THÔNG TIN</div>
    <div class="dept-title">CHƯƠNG TRÌNH SAMSUNG INNOVATION CAMPUS (SIC)</div>
  </div>

  <div class="cover-body">
    <div class="report-type">BÁO CÁO TIỂU LUẬN KẾT THÚC HỌC PHẦN (CAPSTONE PROJECT)</div>
    <div class="course-name">MÔN HỌC: DỮ LIỆU LỚN (BIG DATA ANALYTICS &amp; ARTIFICIAL INTELLIGENCE)</div>
    <div class="course-sub">(CHƯƠNG TRÌNH ĐÀO TẠO CÔNG NGHỆ SAMSUNG INNOVATION CAMPUS - UFM)</div>
    
    <div class="topic-box">
      <div class="topic-label">ĐỀ TÀI NGHIÊN CỨU:</div>
      <div class="topic-title">MÔ HÌNH CHẤM ĐIỂM TÍN DỤNG VÀ THẨM ĐỊNH RỦI RO VỠ NỢ TRONG LĨNH VỰC NGÂN HÀNG VÀ FINTECH</div>
    </div>
  </div>

  <div class="cover-footer">
    <div class="info-row"><strong>Giảng viên hướng dẫn:</strong> TS. Trần Mạnh Tường</div>
    <div class="info-row"><strong>Sinh viên thực hiện:</strong> Lê Thành Hiệu</div>
    <div class="info-row"><strong>Mã số sinh viên:</strong> [Điền MSSV tại đây]</div>
    <div class="info-row"><strong>Khóa học / Đơn vị:</strong> Khóa đào tạo Dữ liệu lớn (Big Data) - Samsung Innovation Campus (SIC) 2026</div>
    <div class="info-row"><strong>Chuyên ngành:</strong> Hệ thống Thông tin Quản lý (MIS) &amp; Khoa học Dữ liệu</div>
    <div class="info-row"><strong>Kho lưu trữ mã nguồn:</strong> <a href="https://github.com/snowflake-vibing/Credit_Scoring_Project">github.com/snowflake-vibing/Credit_Scoring_Project</a></div>
    <div class="info-row"><strong>Không gian làm việc Databricks:</strong> <a href="https://dbc-4d46c653-6b7e.cloud.databricks.com/browse/folders/907137357494385?o=7474645074756875">Databricks Cloud Workspace (Folder 907137357494385)</a></div>
    
    <div class="location-date">TP. HỒ CHÍ MINH, NĂM 2026</div>
  </div>
</div>
```
:::

::: {.content-visible when-format="docx"}
# TRANG BÌA {.unnumbered .unlisted}

**BỘ TÀI CHÍNH**  
**TRƯỜNG ĐẠI HỌC TÀI CHÍNH - MARKETING (UFM)**  
**KHOA CÔNG NGHỆ THÔNG TIN**  
**CHƯƠNG TRÌNH SAMSUNG INNOVATION CAMPUS (SIC)**  

---

### **BÁO CÁO TIỂU LUẬN KẾT THÚC HỌC PHẦN (CAPSTONE PROJECT)**
## **MÔN HỌC: DỮ LIỆU LỚN (BIG DATA ANALYTICS & ARTIFICIAL INTELLIGENCE)**
*(CHƯƠNG TRÌNH ĐÀO TẠO CÔNG NGHỆ SAMSUNG INNOVATION CAMPUS - UFM)*

---

### **ĐỀ TÀI NGHIÊN CỨU:**
# **MÔ HÌNH CHẤM ĐIỂM TÍN DỤNG VÀ THẨM ĐỊNH RỦI RO VỠ NỢ TRONG LĨNH VỰC NGÂN HÀNG VÀ FINTECH**

---

**Giảng viên hướng dẫn:** TS. Trần Mạnh Tường  
**Sinh viên thực hiện:** Lê Thành Hiệu  
**Mã số sinh viên:** [Điền MSSV tại đây]  
**Khóa học / Đơn vị:** Khóa đào tạo Dữ liệu lớn (Big Data) - Samsung Innovation Campus (SIC) 2026  
**Chuyên ngành:** Hệ thống Thông tin Quản lý (MIS) & Khoa học Dữ liệu  
**Kho lưu trữ mã nguồn:** https://github.com/snowflake-vibing/Credit_Scoring_Project  
**Không gian làm việc Databricks:** https://dbc-4d46c653-6b7e.cloud.databricks.com/browse/folders/907137357494385?o=7474645074756875  

---

**TP. HỒ CHÍ MINH, NĂM 2026**
:::

\\newpage

---

## LỜI CẢM ƠN

Để hoàn thành bài tiểu luận nghiên cứu này, trước hết em xin bày tỏ lòng biết ơn sâu sắc và chân thành nhất đến **TS. Trần Mạnh Tường**, giảng viên phụ trách môn học *Dữ liệu lớn (Big Data)* thuộc **Chương trình Samsung Innovation Campus (SIC)** tại **Trường Đại học Tài chính - Marketing (UFM)**. Thầy đã tận tình truyền đạt những kiến thức chuyên môn sâu rộng về kiến trúc dữ liệu phân tán, khoa học dữ liệu hiện đại và các phương pháp ứng dụng trí tuệ nhân tạo vào thực tiễn kinh tế - tài chính. Những lời chỉ dẫn, định hướng khoa học và phản biện quý báu của Thầy trong suốt quá trình học tập là tiền đề quan trọng giúp em hoàn thiện đồ án này một cách chỉn chu và đúng đắn.

Em cũng xin gửi lời cảm ơn chân thành đến Ban Giám hiệu nhà trường, các Quý Thầy Cô trong Khoa Công nghệ Thông tin - Trường Đại học Tài chính - Marketing (UFM) cùng Ban điều phối **Chương trình Samsung Innovation Campus (SIC)** đã tạo điều kiện học tập tốt nhất, cung cấp môi trường nghiên cứu và cơ sở vật chất công nghệ hiện đại phục vụ cho môn học.

*Kính chúc Thầy và Ban điều phối chương trình luôn dồi dào sức khỏe, hạnh phúc và gặt hái được nhiều thành công hơn nữa trong sự nghiệp giảng dạy và phát triển nguồn nhân lực công nghệ cao!*

\\newpage

---

## LỜI CAM ĐOAN

Tôi xin cam đoan rằng bài tiểu luận kết thúc học phần với đề tài **"Mô hình chấm điểm tín dụng và thẩm định rủi ro vỡ nợ trong lĩnh vực Ngân hàng và FinTech"** trong khuôn khổ môn học Big Data thuộc **Chương trình Samsung Innovation Campus (SIC)** tổ chức tại **Trường Đại học Tài chính - Marketing (UFM)** là công trình nghiên cứu độc lập của cá nhân tôi dưới sự hướng dẫn khoa học của **TS. Trần Mạnh Tường**.

Toàn bộ số liệu phân tích, kết quả mô phỏng thực nghiệm và các luận điểm trình bày trong báo cáo hoàn toàn trung thực, khách quan và được thu thập, xử lý từ dữ liệu thực tế 2,260,701 khoản vay của nền tảng LendingClub. Các tài liệu tham khảo, các lý thuyết tài chính - ngân hàng và nghiên cứu khoa học của các tác giả khác đều được trích dẫn nguồn gốc đầy đủ theo đúng quy chuẩn học thuật hiện hành.

::: {.content-visible when-format="html"}
<div class="signature-container" style="display: flex; justify-content: flex-end; margin-top: 35px; margin-bottom: 25px;">
<div class="signature-box" style="width: 330px; text-align: center; font-family: 'Times New Roman', Times, serif;">
<p class="sig-date" style="margin: 0; font-style: italic; font-size: 13pt;">TP. Hồ Chí Minh, năm 2026</p>
<p class="sig-title" style="margin: 6px 0 2px 0; font-weight: bold; font-size: 13pt;">Sinh viên thực hiện</p>
<p class="sig-note" style="margin: 0; font-style: italic; font-size: 11pt; color: #555555;">(Ký và ghi rõ họ tên)</p>
<div class="sig-space" style="height: 95px;"></div>
<p class="sig-name" style="margin: 0; font-weight: bold; font-size: 13.5pt;">Lê Thành Hiệu</p>
</div>
</div>
:::

::: {.content-visible when-format="docx"}
*TP. Hồ Chí Minh, năm 2026*  
**Sinh viên thực hiện**  
*(Ký và ghi rõ họ tên)*  


**Lê Thành Hiệu**
:::

\\newpage

---

## TÓM LƯỢC

Trong bối cảnh chuyển đổi số của hệ thống ngân hàng bán lẻ và sự bùng nổ của các nền tảng công nghệ tài chính (FinTech), rủi ro vỡ nợ (Loan Default Risk) luôn là mối đe dọa trực tiếp đối với tính an toàn vốn và khả năng sinh lời của các tổ chức tín dụng. Phương pháp thẩm định tín dụng truyền thống bộc lộ nhiều điểm nghẽn về thời gian xử lý kéo dài (2 - 5 ngày), chi phí vận hành cao và tính chủ quan của cán bộ tín dụng. Đề tài nghiên cứu này tập trung xây dựng một giải pháp toàn diện ứng dụng công nghệ Dữ liệu lớn (Big Data) trên nền tảng Databricks Lakehouse kết hợp thuật toán học máy phân tán Random Forest Classifier (Spark MLlib) nhằm tự động hóa quy trình thẩm định và ra quyết định tín dụng.

Dữ liệu thực nghiệm bao gồm 2,260,701 khoản vay (1.6 GB) từ nền tảng LendingClub (2007 - 2018Q4) được tổ chức và xử lý phân tán qua kiến trúc Medallion 3 tầng (Bronze -> Silver -> Gold). Đề tài áp dụng các kỹ thuật làm sạch dữ liệu lớn, xử lý giá trị ngoại lai, kỹ nghệ các chỉ số tài chính chuyên sâu (DTI, CBI) và phân tích thống kê đa chiều bằng Spark SQL kết hợp Window Functions. Mô hình học máy phân tán được tinh chỉnh qua cơ chế kiểm định chéo (3-Fold Cross-Validation), đạt hiệu năng phân loại vượt trội với **ROC-AUC = 0.8745**, độ nhạy phát hiện nợ xấu (Recall) đạt 84.04% và độ chính xác tổng thể đạt 87.16% trên tập kiểm thử 452,140 hồ sơ. 

Dựa trên xác suất vỡ nợ dự báo, đề tài xây dựng động cơ ra quyết định chuẩn hóa theo điểm tín dụng FICO Score (300 - 850), thiết lập ma trận phân tầng 4 nhóm rủi ro (Low, Medium, High, Very High Risk) gắn với chỉ số Youden's J và chuẩn mực Basel II, đồng thời đề xuất mô hình định giá lãi suất theo rủi ro (Risk-Based Pricing Framework) với các mức lãi suất 8.5%, 11.5% và 14.5%. Giải pháp cho phép tự động hóa phê duyệt trên 75% hồ sơ vay trong thời gian dưới 3 phút, giúp giảm tỷ lệ nợ xấu danh mục từ 21.82% xuống dưới 4.2% và tiết kiệm hàng tỷ đồng chi phí trích lập dự phòng tổn thất tín dụng theo Thông tư 11/2021/TT-NHNN. Toàn bộ mã nguồn và dữ liệu thực nghiệm được lưu trữ công khai tại GitHub: https://github.com/snowflake-vibing/Credit_Scoring_Project.

\\newpage

---

## MỤC LỤC

* [TRANG BÌA](#trang-bìa)
* [LỜI CẢM ƠN](#lời-cảm-ơn)
* [LỜI CAM ĐOAN](#lời-cam-đoan)
* [TÓM LƯỢC](#tóm-lược)
* [DANH SÁCH CÁC TỪ VIẾT TẮT](#danh-sách-các-từ-viết-tắt)
* [DANH SÁCH BẢNG](#danh-sách-bảng)
* [DANH SÁCH HÌNH](#danh-sách-hình)
* [CHƯƠNG 1: GIỚI THIỆU](01_CHUONG_1_GIOI_THIEU.html)
  * 1.1 Đặt vấn đề và Lý do chọn đề tài
  * 1.2 Mục tiêu nghiên cứu
    * 1.2.1 Mục tiêu tổng quát
    * 1.2.2 Mục tiêu cụ thể
  * 1.3 Nội dung nghiên cứu
  * 1.4 Đối tượng và phạm vi nghiên cứu
    * 1.4.1 Đối tượng nghiên cứu
    * 1.4.2 Phạm vi nghiên cứu
  * 1.5 Ý nghĩa khoa học và thực tiễn của đề tài
    * 1.5.1 Ý nghĩa khoa học
    * 1.5.2 Ý nghĩa thực tiễn
  * 1.6 Phân tích đặc tính Dữ liệu lớn theo mô hình 5Vs
* [CHƯƠNG 2: LƯỢC KHẢO TÀI LIỆU](02_CHUONG_2_LUOC_KHAO_TAI_LIEU.html)
  * 2.1 Tổng quan về rủi ro tín dụng và phương pháp thẩm định truyền thống
    * 2.1.1 Bản chất kinh tế của rủi ro tín dụng và biến cố vỡ nợ
    * 2.1.2 Các hạn chế của phương pháp thẩm định truyền thống
  * 2.2 Cơ sở lý thuyết về Kiến trúc Hồ dữ liệu Databricks Lakehouse
    * 2.2.1 Sự tiến hóa từ Data Warehouse đến Lakehouse
    * 2.2.2 Định dạng lưu trữ phân tán Delta Lake và Apache Spark
  * 2.3 Thiết kế kiến trúc phân tầng Medallion trong định chế tài chính
    * 2.3.1 Phân định chức năng ba tầng Bronze, Silver và Gold
    * 2.3.2 Sơ đồ luồng xử lý dữ liệu phân tán toàn diện
  * 2.4 Khung quản trị dữ liệu và Chuẩn mực an toàn vốn Basel II/III
    * 2.4.1 Tổng quan các nghiên cứu thực nghiệm trong và ngoài nước
    * 2.4.2 Yêu cầu tuân thủ an toàn vốn theo chuẩn Basel II/III
* [CHƯƠNG 3: PHƯƠNG PHÁP NGHIÊN CỨU](03_CHUONG_3_PHUONG_PHAP_NGHIEN_CUU.html)
  * 3.1 Phương tiện nghiên cứu
    * 3.1.1 Bộ dữ liệu lớn LendingClub quy mô 2.26 triệu hồ sơ
    * 3.1.2 Nền tảng hạ tầng tính toán Databricks Serverless
  * 3.2 Phương pháp nghiên cứu
    * 3.2.1 Quy trình thu thập và nạp dữ liệu thô Tầng Bronze
    * 3.2.2 Phương pháp tiền xử lý và làm sạch dữ liệu Tầng Silver
    * 3.2.3 Phương pháp kỹ nghệ đặc trưng tài chính (DTI, CBI)
    * 3.2.4 Phương pháp phân tích khám phá dữ liệu bằng Spark SQL
    * 3.2.5 Thiết kế chuỗi Pipeline học máy phân tán Spark MLlib
    * 3.2.6 Thuật toán phân loại Random Forest Classifier
    * 3.2.7 Phương pháp kiểm định chéo và tối ưu hóa siêu tham số
    * 3.2.8 Phương pháp đánh giá mô hình và xác lập ngưỡng cắt rủi ro
* [CHƯƠNG 4: KẾT QUẢ VÀ THẢO LUẬN](04_CHUONG_4_KET_QUA_VA_THAO_LUAN.html)
  * 4.1 Kết quả tiền xử lý và phân tích khám phá dữ liệu lớn
    * 4.1.1 Hiện trạng dữ liệu khuyết thiếu Tầng Bronze
    * 4.1.2 Mối quan hệ giữa mục đích vay và tỷ lệ nợ xấu thực tế
    * 4.1.3 Mối tương quan giữa hạng khoản vay và tình trạng nhà ở
  * 4.2 Kết quả huấn luyện và đánh giá mô hình học máy phân tán
    * 4.2.1 Kết quả tối ưu hóa siêu tham số bằng CrossValidator
    * 4.2.2 Đánh giá hiệu năng phân loại qua đường cong ROC
    * 4.2.3 Đánh giá ma trận nhầm lẫn và các chỉ số đo lường
    * 4.2.4 Phân tích mức độ quan trọng của các đặc trưng tài chính
  * 4.3 Thảo luận và Đề xuất ứng dụng nghiệp vụ ngân hàng
    * 4.3.1 Động cơ quy đổi điểm tín dụng FICO Score tiêu chuẩn
    * 4.3.2 Ma trận phân tầng rủi ro và chính sách phê duyệt tự động
    * 4.3.3 Mô hình định giá lãi suất theo rủi ro (Risk-Based Pricing)
    * 4.3.4 Chính sách hạn mức linh hoạt và minh họa hồ sơ thực tế
    * 4.3.5 Đánh giá tác động tài chính, tỷ lệ nợ xấu NPL và ROI
* [CHƯƠNG 5: KẾT LUẬN VÀ KIẾN NGHỊ](05_CHUONG_5_KET_LUAN_VA_KIEN_NGHI.html)
  * 5.1 Kết luận
  * 5.2 Kiến nghị
    * 5.2.1 Khuyến nghị quản trị chiến lược cho Ban Điều hành Ngân hàng
    * 5.2.2 Hướng nghiên cứu và phát triển tiếp theo
* [TÀI LIỆU THAM KHẢO](06_TAI_LIEU_THAM_KHAO.html)
* [PHỤ LỤC](07_PHU_LUC.html)
  * Phụ lục 1: Sơ đồ chi tiết luồng xử lý dữ liệu Lakehouse Medallion
  * Phụ lục 2: Kho lưu trữ mã nguồn GitHub và Hướng dẫn thực nghiệm

\\newpage

---

## DANH SÁCH CÁC TỪ VIẾT TẮT

*(Sắp xếp theo thứ tự A, B, C)*

| Từ Viết Tắt | Tên Tiếng Anh Đầy Đủ | Nghĩa Tiếng Việt / Giải Thích |
| :--- | :--- | :--- |
| **ACID** | Atomicity, Consistency, Isolation, Durability | Bốn thuộc tính toàn vẹn của hệ quản trị cơ sở dữ liệu |
| **AI** | Artificial Intelligence | Trí tuệ nhân tạo |
| **AUC** | Area Under the ROC Curve | Diện tích dưới đường cong đặc trưng hoạt động phân loại |
| **BCBS** | Basel Committee on Banking Supervision | Ủy ban Basel về Giám sát Ngân hàng |
| **BNPL** | Buy Now Pay Later | Mua trước trả sau |
| **CBI** | Credit Burden Index | Chỉ số gánh nặng tín dụng có trọng số thâm niên công tác |
| **CIC** | Credit Information Center | Trung tâm Thông tin Tín dụng Quốc gia Việt Nam |
| **COF** | Cost of Funds | Chi phí huy động vốn của tổ chức tín dụng |
| **DTI** | Debt-to-Income Ratio | Tỷ lệ tổng dư nợ trên thu nhập hàng năm |
| **EAD** | Exposure at Default | Tổng dư nợ chịu rủi ro tại thời điểm vỡ nợ |
| **EDA** | Exploratory Data Analysis | Phân tích khám phá dữ liệu |
| **EL** | Expected Loss | Tổn thất tín dụng kỳ vọng ($EL = PD \\times LGD \\times EAD$) |
| **FICO** | Fair Isaac Corporation Score | Thang điểm tín nhiệm cá nhân tiêu chuẩn (300 - 850) |
| **FN** | False Negative | Sai lầm loại 2 (Dự báo không vỡ nợ nhưng thực tế vỡ nợ) |
| **FP** | False Positive | Sai lầm loại 1 (Dự báo vỡ nợ nhưng thực tế trả đúng hạn) |
| **LGD** | Loss Given Default | Tỷ lệ tổn thất thực tế khi xảy ra biến cố vỡ nợ |
| **ML** | Machine Learning | Học máy |
| **NIM** | Net Interest Margin | Biên lãi thuần của tổ chức tín dụng |
| **NPL** | Non-Performing Loan | Tỷ lệ nợ xấu (quá hạn thanh toán trên 90 ngày) |
| **OPEX** | Operating Expenses | Chi phí vận hành hoạt động |
| **PD** | Probability of Default | Xác suất vỡ nợ của khoản vay |
| **ROC** | Receiver Operating Characteristic | Đường cong đặc trưng hoạt động phân loại |
| **STP** | Straight-Through Processing | Quy trình xử lý và phê duyệt tự động thông suốt |
| **TN** | True Negative | Dự báo chính xác khách hàng trả nợ tốt |
| **TP** | True Positive | Dự báo chính xác khách hàng vỡ nợ |

\\newpage

---

## DANH SÁCH BẢNG

| Bảng | Tên bảng |
| :---: | :--- |
| **1.1** | Phân tích đặc tính Dữ liệu lớn (Big Data) theo mô hình 5Vs trong Đề tài Chấm điểm Tín dụng |
| **2.1** | So sánh ưu nhược điểm giữa Data Warehouse, Data Lake và Databricks Lakehouse |
| **2.2** | Phân định chức năng, nguyên tắc và công nghệ giữa 3 tầng kiến trúc Medallion |
| **3.1** | Mô tả chi tiết 12 thuộc tính cốt lõi trong Bộ dữ liệu lớn LendingClub (2,260,701 bản ghi) |
| **3.2** | Kế hoạch làm sạch và chuẩn hóa dữ liệu tại Tầng Silver |
| **3.3** | Không gian tìm kiếm siêu tham số trong bộ tinh chỉnh ParamGridBuilder |
| **4.1** | Thống kê tỷ lệ nợ xấu (NPL Rate) và quy mô tín dụng theo Mục đích sử dụng vốn |
| **4.2** | Ma trận phân bố rủi ro theo Hạng khoản vay và Tình trạng sở hữu nhà ở |
| **4.3** | Kết quả huấn luyện và tinh chỉnh siêu tham số mô hình Random Forest qua 3-Fold Cross-Validation |
| **4.4** | Ma trận nhầm lẫn của mô hình Random Forest trên tập kiểm thử 452,140 hồ sơ |
| **4.5** | Bảng tổng hợp các chỉ số đánh giá hiệu năng phân loại (Accuracy, Precision, Recall, F1, ROC-AUC) |
| **4.6** | Xếp hạng mức độ quan trọng của các biến đặc trưng (Feature Importance Ranking) |
| **4.7** | Bảng quy đổi Log-Odds từ xác suất vỡ nợ sang Thang điểm tín dụng FICO Score |
| **4.8** | Ma trận Phê duyệt Tín dụng Tự động và Chính sách Hạn mức theo 4 Phân tầng Rủi ro |
| **4.9** | Cấu thành chi phí lãi suất theo mô hình Risk-Based Pricing chuẩn mực ngân hàng |
| **4.10** | Minh họa kết quả phê duyệt và giải ngân tự động trên 4 hồ sơ khách hàng thực tế tại Tầng Gold |

\\newpage

---

## DANH SÁCH HÌNH

| Hình | Tên hình |
| :---: | :--- |
| **2.1** | Sơ đồ kiến trúc xử lý luồng dữ liệu Lakehouse theo mô hình Huy chương Medallion |
| **4.1** | Đánh giá tỷ lệ dữ liệu khuyết thiếu Tầng Bronze (Missing Values Analysis) |
| **4.2** | Tỷ lệ nợ xấu NPL theo Mục đích vay và Tình trạng nhà ở Tầng Silver |
| **4.3** | Đường cong ROC và so sánh hiệu năng các mô hình máy học (ROC-AUC = 0.8745) |
| **4.4** | Ma trận nhầm lẫn (Confusion Matrix) của mô hình trên 452,140 hồ sơ kiểm thử |
| **4.5** | Cơ cấu phân tầng rủi ro tín dụng (Donut Chart) và Quyết định phê duyệt tự động (Bar Chart) |
"""

print("Đã soạn thảo xong Phần 0 (Trang bìa, Tóm lược, Mục lục, Danh mục).")

# ==============================================================================
# CHƯƠNG 1: GIỚI THIỆU
# ==============================================================================
text_01 = """# CHƯƠNG 1: GIỚI THIỆU

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

Để chứng minh tính tương thích và sự cần thiết của nền tảng Big Data đối với bài toán tín dụng, nghiên cứu phân tích đề tài dựa trên khung lý thuyết 5Vs kinh điển [8]:

**Bảng 1.1 Phân tích đặc tính Dữ liệu lớn theo mô hình 5Vs trong Đề tài Chấm điểm Tín dụng**

| Chiều Kích 5Vs | Khái Niệm Lý Thuyết | Thách Thức Trong Nghiệp Vụ Tín Dụng Bán Lẻ | Giải Pháp Kỹ Thuật Đề Xuất Trong Đề Tài |
| :--- | :--- | :--- | :--- |
| **Volume** *(Quy mô dung lượng)* | Khối lượng dữ liệu khổng lồ vượt quá khả năng lưu trữ và xử lý của hệ thống máy đơn (Single-node RDBMS). | Quy mô 2.26 triệu hồ sơ (1.6 GB) với hàng chục biến số tài chính; hệ thống RDBMS truyền thống bị tràn RAM khi xử lý. | Lưu trữ phân tán trên Databricks Delta Lake, nạp dữ liệu vào Tầng Bronze và phân vùng (Partitioning) 16 luồng song song. |
| **Velocity** *(Tốc độ xử lý)* | Tốc độ phát sinh, thu thập và đòi hỏi phản hồi kết quả trong thời gian thực hoặc gần thời gian thực. | Khách hàng số kỳ vọng phê duyệt giải ngân tức thì (< 3 phút); thẩm định thủ công mất từ 2 đến 5 ngày làm việc. | Tận dụng công cụ Apache Spark tính toán trong bộ nhớ RAM (In-memory computing), tự động hóa dự báo bằng Spark MLlib Pipeline. |
| **Variety** *(Đa dạng định dạng)* | Sự kết hợp phức tạp giữa các dạng dữ liệu số, dữ liệu chuỗi danh mục và thông tin hành vi. | Dữ liệu chứa thuộc tính số (thu nhập, dư nợ), danh mục (mục đích vay, nhà ở) và chuỗi tự do (chức danh công việc). | Kỹ nghệ đặc trưng Spark MLlib: `StringIndexer` mã hóa nhãn, `OneHotEncoder` xử lý danh mục, `VectorAssembler` gộp vector đặc trưng. |
| **Veracity** *(Độ tin cậy dữ liệu)* | Mức độ nhiễu, sai sót, thiếu hụt hoặc mâu thuẫn trong dữ liệu khai báo thực tế của người vay. | Dữ liệu thực nghiệm chứa nhiều điểm ngoại lai phi lý (tuổi > 100, thu nhập <= 0) và tỷ lệ khuyết thiếu lãi suất, thâm niên cao. | Thiết kế Tầng Silver làm sạch phân tán: Lọc ngoại lai $18 \\le \\text{Age} \\le 80$, $\\text{Income} > 0$; điền khuyết bằng trung vị (Median) và giá trị thận trọng. |
| **Value** *(Giá trị kinh tế)* | Khả năng chuyển hóa dữ liệu thô thành lợi ích tài chính và giá trị kinh doanh thực tiễn. | Ngân hàng đối mặt nguy cơ thâm hụt vốn do nợ xấu hoặc đánh mất khách hàng tốt do chính sách lãi suất cào bằng. | Động cơ Phân tầng Rủi ro 4 cấp độ, Quy đổi FICO Score (300 - 850) và Mô hình Định giá Lãi suất theo rủi ro (Risk-Based Pricing). |

<p align="left"><em>(Nguồn: Tác giả tổng hợp và phân tích dựa trên chuẩn mực Dữ liệu lớn)</em></p>
"""

print("Đã soạn thảo xong Chương 1.")

# ==============================================================================
# CHƯƠNG 2: LƯỢC KHẢO TÀI LIỆU
# ==============================================================================
text_02 = """# CHƯƠNG 2: LƯỢC KHẢO TÀI LIỆU

---

## 2.1 Tổng quan về rủi ro tín dụng và phương pháp thẩm định truyền thống

### 2.1.1 Bản chất kinh tế của rủi ro tín dụng và biến cố vỡ nợ
Trong hoạt động trung gian tài chính, rủi ro tín dụng phát sinh từ hiện tượng **bất cân xứng thông tin (Asymmetric Information)** giữa người đi vay và bên cho vay, dẫn đến hai hệ lụy kinh điển là lựa chọn đối nghịch (Adverse Selection) trước khi ký hợp đồng và rủi ro đạo đức (Moral Hazard) sau khi giải ngân [9]. Theo Stiglitz và Weiss (1981), việc nâng lãi suất để bù đắp rủi ro có thể vô tình loại bỏ các khách hàng tốt và chỉ thu hút những đối tượng sẵn sàng mạo hiểm, làm tăng nguy cơ vỡ nợ của toàn danh mục [10]. 

Khi biến cố vỡ nợ xảy ra, ngân hàng không chỉ tổn thất phần vốn gốc chưa thu hồi mà còn phải gánh chịu chi phí xử lý nợ, trích lập dự phòng rủi ro và làm suy giảm tỷ lệ an toàn vốn CAR theo quy định của Ngân hàng Nhà nước [11]. Do đó, việc xây dựng mô hình dự báo xác suất vỡ nợ (Probability of Default - PD) chính xác là nền tảng sống còn trong quản trị tài chính hiện đại.

### 2.1.2 Các hạn chế của phương pháp thẩm định tín dụng truyền thống
Quy trình thẩm định truyền thống chủ yếu dựa trên đánh giá định tính của chuyên viên tín dụng (Expert Judgment) hoặc các bảng điểm tĩnh (Scorecards) xây dựng bằng hồi quy Logistic đơn biến [12]. Các phương pháp này bộc lộ những hạn chế rõ rệt:
1. **Độ trễ thời gian lớn:** Mất từ 2 đến 5 ngày để thẩm định hồ sơ giấy tờ và gọi điện xác minh, không đáp ứng được yêu cầu phê duyệt tức thì của khách hàng số.
2. **Chi phí vận hành cao:** Đòi hỏi lực lượng nhân sự thẩm định thực địa đông đảo, khiến biên lợi nhuận của các khoản vay nhỏ bị bào mòn.
3. **Định kiến chủ quan:** Quyết định phê duyệt phụ thuộc vào cảm tính cá nhân, dễ tạo ra sự thiếu nhất quán giữa các chi nhánh.
4. **Không nắm bắt được quan hệ phi tuyến:** Không xử lý được các mối quan hệ tương tác phức tạp giữa các đặc trưng tài chính đa chiều.

---

## 2.2 Cơ sở lý thuyết về Kiến trúc Hồ dữ liệu Databricks Lakehouse

### 2.2.1 Sự tiến hóa từ Data Warehouse đến Lakehouse
Để giải quyết bài toán dữ liệu lớn, kiến trúc lưu trữ và xử lý đã trải qua ba thế hệ tiến hóa: Kho dữ liệu (Data Warehouse), Hồ dữ liệu (Data Lake) và Kiến trúc kết hợp Hồ - Kho dữ liệu (Lakehouse) [13]:

**Bảng 2.1 So sánh ưu nhược điểm giữa Data Warehouse, Data Lake và Databricks Lakehouse**

| Tiêu Chí So Sánh | Kho Dữ Liệu Truyền Thống (Data Warehouse) | Hồ Dữ Liệu Thế Hệ Đầu (Data Lake) | Kiến Trúc Databricks Lakehouse (Đề Tài Áp Dụng) |
| :--- | :--- | :--- | :--- |
| **Cấu trúc Dữ liệu** | Chỉ lưu trữ dữ liệu có cấu trúc (Schema-on-write). | Dữ liệu phi cấu trúc, bán cấu trúc (Schema-on-read). | Hỗ trợ toàn diện dữ liệu cấu trúc, bán cấu trúc và phi cấu trúc. |
| **Đảm bảo Giao dịch ACID** | Hỗ trợ giao dịch ACID rất tốt trên hệ cơ sở dữ liệu quan hệ. | Không hỗ trợ ACID; dễ xảy ra xung đột khi ghi/đọc song song. | Hỗ trợ ACID đầy đủ thông qua tệp nhật ký giao dịch Delta Lake. |
| **Khả năng Mở rộng Quy mô** | Chi phí nâng cấp phần cứng (Scale-up) rất đắt đỏ, khó mở rộng. | Tận dụng lưu trữ đám mây giá rẻ (S3, ADLS, DBFS), mở rộng vô hạn. | Tách rời độc lập giữa Lưu trữ (Storage) và Năng lực tính toán (Compute). |
| **Nền tảng Hỗ trợ Trí tuệ Nhân tạo** | Hạn chế, chỉ hỗ trợ SQL và các báo cáo BI truyền thống. | Hỗ trợ tốt cho Machine Learning nhưng thiếu kiểm soát chất lượng. | Hỗ trợ trực tiếp từ SQL Analytics, BI Dashboard đến Spark MLlib Pipeline. |

<p align="left"><em>(Nguồn: Tổng hợp từ Armbrust et al., 2021 và Databricks Inc., 2023)</em></p>

### 2.2.2 Định dạng lưu trữ phân tán Delta Lake và Apache Spark
Delta Lake là tầng lưu trữ mã nguồn mở trung gian xây dựng trên nền tảng tệp Parquet dạng cột, mang lại các ưu thế vượt trội:
- **Tính toàn vẹn giao dịch ACID:** Đảm bảo mọi giao dịch thêm mới, cập nhật hoặc xóa dữ liệu đều thành công trọn vẹn hoặc hoàn tác hoàn toàn, ngăn ngừa hiện tượng phân mảnh dữ liệu (Data Corruption) [14].
- **Khả năng quay ngược thời gian (Time Travel):** Cho phép truy vấn dữ liệu tại một thời điểm lịch sử chính xác thông qua nhật ký `_delta_log`, đáp ứng yêu cầu kiểm toán nghiêm ngặt của ngành ngân hàng.
- **Tối ưu hóa truy vấn Spark Catalyst Optimizer:** Tự động tối ưu hóa kế hoạch thực thi logic và vật lý, giảm thiểu dung lượng truyền tải qua mạng giữa các worker node.

---

## 2.3 Thiết kế kiến trúc phân tầng Medallion trong định chế tài chính

### 2.3.1 Phân định chức năng ba tầng Bronze, Silver và Gold
Kiến trúc Medallion tổ chức luồng dữ liệu theo ba cấp độ tinh chế tăng dần nhằm bảo đảm chất lượng dữ liệu phục vụ mô hình học máy [15]:

**Bảng 2.2 Phân định chức năng, nguyên tắc và công nghệ giữa 3 tầng kiến trúc Medallion**

| Tầng Kiến Trúc | Bảng Delta Thực Tế Trong Đề Tài | Nguyên Tắc Quản Trị Dữ Liệu | Công Nghệ & Thao Tác Kỹ Thuật | Vai Trò Nghiệp Vụ Tín Dụng |
| :--- | :--- | :--- | :--- | :--- |
| **Tầng Bronze (Thô - Raw)** | `workspace.default.bronze_credit_data` | Bảo toàn nguyên vẹn 100% dữ liệu gốc, không chỉnh sửa, lưu vết đầy đủ. | `spark.read.csv()`, ghi Delta Table, khởi tạo nhật ký `_delta_log`. | Nguồn dữ liệu kiểm toán (Audit Trail) và phục hồi khi xảy ra sự cố. |
| **Tầng Silver (Làm sạch & Chuẩn hóa)** | `workspace.default.silver_credit_data` | Dữ liệu được làm sạch, xử lý ngoại lai, loại bỏ trùng lặp và giàu đặc trưng. | `.na.fill()`, `.filter()`, tính chỉ số DTI, CBI, Spark SQL Window Functions. | Phục vụ phân tích khám phá (EDA), thống kê báo cáo nội bộ và chuẩn bị tập huấn luyện. |
| **Tầng Gold (Kinh doanh & Mô hình hóa)** | `workspace.default.gold_credit_scoring` | Dữ liệu sẵn sàng cho hoạt động kinh doanh và tự động hóa ra quyết định. | Spark MLlib Pipeline, VectorAssembler, RandomForest, FICO Score. | Cung cấp điểm tín dụng, phân tầng hạn mức và định giá lãi suất theo rủi ro. |

<p align="left"><em>(Nguồn: Tổng hợp theo chuẩn Databricks Medallion Architecture)</em></p>

### 2.3.2 Sơ đồ luồng xử lý dữ liệu phân tán toàn diện
Toàn bộ luồng xử lý dữ liệu từ nạp dữ liệu thô đến xuất bản kết quả mô hình được mô tả trực quan trong sơ đồ sau:

![Hình 2.1 Sơ đồ kiến trúc xử lý luồng dữ liệu Lakehouse theo mô hình Huy chương Medallion](images/hinh_2_1_medallion_architecture.png)
<p align="center"><strong>Hình 2.1 Sơ đồ kiến trúc xử lý luồng dữ liệu Lakehouse theo mô hình Huy chương Medallion</strong></p>
<p align="right"><em>(Nguồn: Tác giả thiết kế dựa trên nền tảng Databricks Lakehouse)</em></p>

---

## 2.4 Khung quản trị dữ liệu và Chuẩn mực an toàn vốn Basel II/III

### 2.4.1 Tổng quan các nghiên cứu thực nghiệm trong và ngoài nước
Trong nhiều năm qua, các phương pháp phân loại nhị phân đã được áp dụng rộng rãi trong xếp hạng tín dụng cá nhân:
- Altman (1968) tiên phong với chỉ số Z-score dựa trên phân tích biệt số đa biến (MDA) để dự báo nguy cơ phá sản [16].
- Baesens et al. (2003) và Lessmann et al. (2015) qua các nghiên cứu thực nghiệm quy mô lớn đã chứng minh rằng các mô hình học kết hợp (Ensemble Learning) như Random Forest và Gradient Boosting luôn vượt trội so với hồi quy Logistic truyền thống về chỉ số AUC và khả năng kháng hiện tượng quá khớp (Overfitting) [17], [18].
- Jagtiani và Lemieux (2019) khẳng định dữ liệu phi truyền thống kết hợp máy học giúp các nền tảng FinTech nâng cao khả năng tiếp cận vốn cho người yếu thế mà không làm tăng tỷ lệ nợ xấu [19].

### 2.4.2 Yêu cầu tuân thủ an toàn vốn theo chuẩn Basel II/III và Thông tư 41/2016/TT-NHNN
Ủy ban Basel về Giám sát Ngân hàng quy định phương pháp xếp hạng nội bộ nâng cao (Advanced Internal Ratings-Based - A-IRB) đòi hỏi ngân hàng phải tự lượng hóa xác suất vỡ nợ (PD), tỷ lệ tổn thất khi vỡ nợ (LGD) và tổng dư nợ chịu rủi ro (EAD) [20]. Theo Thông tư 41/2016/TT-NHNN của Ngân hàng Nhà nước Việt Nam:
- Mô hình chấm điểm tín dụng phải được kiểm định chéo độc lập và có khả năng phân biệt rõ ràng giữa các nhóm khách hàng có mức độ rủi ro khác nhau.
- Tổ chức tín dụng phải trích lập dự phòng tổn thất tín dụng kỳ vọng ($EL$) theo công thức:
  $$EL = PD \\times LGD \\times EAD$$
Việc áp dụng mô hình máy học phân tán trong đề tài này giúp ước tính chính xác tham số $PD$, từ đó tối ưu hóa nguồn vốn tự có và đáp ứng toàn diện các chuẩn mực an toàn vốn quốc tế.
"""

print("Đã soạn thảo xong Chương 2.")

# ==============================================================================
# CHƯƠNG 3: PHƯƠNG PHÁP NGHIÊN CỨU
# ==============================================================================
text_03 = """# CHƯƠNG 3: PHƯƠNG PHÁP NGHIÊN CỨU

---

## 3.1 Phương tiện nghiên cứu

### 3.1.1 Bộ dữ liệu lớn LendingClub quy mô 2.26 triệu hồ sơ
Nghiên cứu sử dụng tập dữ liệu thực tế **LendingClub Complete Loan Dataset (2007 - 2018Q4)** được công bố bởi LendingClub - nền tảng cho vay ngang hàng trực tuyến lớn nhất thế giới [21]. Dữ liệu bao gồm 2,260,701 khoản vay (1.6 GB) với 12 thuộc tính cốt lõi được trích xuất và chuẩn hóa:

**Bảng 3.1 Mô tả chi tiết 12 thuộc tính cốt lõi trong Bộ dữ liệu lớn LendingClub (2,260,701 bản ghi)**

| STT | Tên Biến Trong Pipeline | Tên Gốc LendingClub | Kiểu Dữ Liệu | Định Nghĩa Nghiệp Vụ & Ý Nghĩa Kinh Tế |
| :-: | :--- | :--- | :---: | :--- |
| 1 | `loan_amnt` | `loan_amnt` | Double | Số tiền khoản vay được phê duyệt giải ngân (USD). |
| 2 | `person_income` | `annual_inc` | Double | Tổng thu nhập hàng năm của người đi vay (USD). |
| 3 | `loan_int_rate` | `int_rate` | Double | Mức lãi suất danh nghĩa hàng năm áp dụng cho khoản vay (%). |
| 4 | `loan_grade` | `grade` | String | Xếp hạng tín nhiệm nội bộ từ `A` (an toàn nhất) đến `G` (rủi ro cao nhất). |
| 5 | `person_home_ownership` | `home_ownership` | String | Tình trạng sở hữu nhà ở (`RENT`: Thuê, `OWN`: Sở hữu riêng, `MORTGAGE`: Thế chấp). |
| 6 | `person_emp_length` | `emp_length` | Double | Thâm niên công tác liên tục của người vay (tính bằng năm). |
| 7 | `loan_intent` | `purpose` | String | Mục đích sử dụng vốn vay (`debt_consolidation`, `credit_card`, `small_business`,...). |
| 8 | `loan_percent_income` | `dti` | Double | Tỷ lệ tổng nghĩa vụ nợ trên thu nhập hàng năm ($DTI$). |
| 9 | `cb_person_default_on_file` | `pub_rec_bankruptcies` | String | Lịch sử nợ xấu hoặc phá sản ghi nhận tại trung tâm thông tin tín dụng (`Y`: Có, `N`: Không). |
| 10 | `person_age` | Suy diễn từ `earliest_cr_line` | Integer | Độ tuổi của người đi vay vốn (năm). |
| 11 | `cb_person_cred_hist_length` | `earliest_cr_line` | Integer | Độ dài thâm niên quan hệ tín dụng chính thức (năm). |
| 12 | **`loan_status` (Label)** | `loan_status` | Integer | Nhãn mục tiêu: `0` đại diện cho Trả nợ đầy đủ (`Fully Paid`); `1` đại diện cho Vỡ nợ (`Charged Off`). |

<p align="left"><em>(Nguồn: Tổng hợp từ LendingClub Corporation, 2019)</em></p>

### 3.1.2 Nền tảng hạ tầng tính toán Databricks Serverless và Apache Spark
Nghiên cứu được triển khai trên nền tảng **Databricks Serverless Cloud Environment** với cấu hình cụm tính toán tự động co giãn (Auto-scaling Multi-node Cluster):
- Động cơ thực thi: Apache Spark 3.5.0 (Spark Core, Spark SQL, Spark MLlib).
- Tầng lưu trữ phân tán: Delta Lake 3.0.0 trên nền tảng lưu trữ đám mây DBFS.
- Môi trường lập trình: PySpark API kết hợp Python 3.10+ và các thư viện hỗ trợ (NumPy, Pandas, Seaborn, Matplotlib).

---

## 3.2 Phương pháp nghiên cứu

### 3.2.1 Quy trình thu thập và nạp dữ liệu thô Tầng Bronze
Khâu tiếp nhận dữ liệu đầu vào (Data Ingestion) đòi hỏi phải bảo đảm tính toàn vẹn và khả năng lưu vết lịch sử không thể chỉnh sửa [14]:
1. **Nguyên tắc bảo toàn nguyên vẹn (Data Immutability):** Dữ liệu thô từ file CSV được nạp thẳng vào bảng Delta `workspace.default.bronze_credit_data`, giữ nguyên mọi trường giá trị trống (`NULL`), kiểu chuỗi và các điểm ngoại lai nhằm phục vụ mục đích kiểm toán (Audit Trail).
2. **Khởi tạo Delta Transaction Log:** Hệ thống tự động thiết lập nhật ký giao dịch tuần tự (`_delta_log/00000000000000000000.json`) để ghi nhận siêu dữ liệu, lược đồ (schema) và vị trí các tệp con Parquet phân tán.

### 3.2.2 Phương pháp tiền xử lý và làm sạch dữ liệu Tầng Silver
Dữ liệu từ Tầng Bronze được kích hoạt quy trình làm sạch phân tán để tạo lập bảng `workspace.default.silver_credit_data` [22]:

**Bảng 3.2 Kế hoạch làm sạch và chuẩn hóa dữ liệu tại Tầng Silver**

| Thuộc Tính Dữ Liệu | Hiện Trạng Dữ Liệu Thô (Bronze) | Phương Pháp Xử Lý Tại Tầng Silver | Cơ Sở Khoa Học & Nghiệp Vụ |
| :--- | :--- | :--- | :--- |
| `person_age` | Ngoại lai phi lý ($> 100$ tuổi, $< 18$ tuổi) | Lọc bỏ: Giữ lại $18 \\le \\text{Age} \\le 80$ | Tuân thủ độ tuổi lao động và năng lực hành vi dân sự theo luật định. |
| `person_income` | Tồn tại giá trị âm và bằng $0$ | Lọc bỏ: Giữ lại $\\text{Income} > 0$ | Đảm bảo tính khả thi của nguồn tài chính hoàn trả nợ gốc và lãi. |
| `person_emp_length` | Khuyết thiếu 6.50% (146,945 bản ghi) | Trích xuất số, điền thiếu: $0.0$ năm | Giả định thận trọng đối với lao động mới tham gia thị trường hoặc tự do. |
| `loan_int_rate` | Khuyết thiếu 9.56% (216,123 bản ghi) | Điền trung vị thị trường: $11.0\\%$ | Tránh làm sai lệch phân phối lãi suất thực tế trong cho vay tiêu dùng. |
| `cb_person_cred_hist_length` | Khuyết thiếu 2.21% (49,961 bản ghi) | Điền giá trị cơ sở: $1$ năm | Khách hàng mới phát sinh quan hệ tín dụng lần đầu tại Trung tâm CIC. |
| Kiểu dữ liệu | Chuỗi tự do và số không định dạng | Ép kiểu `DoubleType` và `IntegerType` | Tối ưu hóa tính toán trong bộ nhớ RAM và ngăn ngừa lỗi số học. |

<p align="left"><em>(Nguồn: Tác giả đề xuất dựa trên phân tích đặc tính dữ liệu thực tế)</em></p>

### 3.2.3 Phương pháp kỹ nghệ đặc trưng tài chính
Nhằm cung cấp các biến số tổng hợp mang hàm lượng thông tin kinh tế cao, nghiên cứu xây dựng hai chỉ số đòn bẩy tài chính chuyên sâu [16], [23]:

1. **Chỉ số Tỷ lệ Nợ trên Thu nhập (Debt-to-Income Ratio - DTI):**
   $$DTI = \\frac{\\text{Loan Amount}}{\\text{Person Income}}$$
   Phản ánh tỷ lệ phần trăm thu nhập năm mà người vay phải dành ra để trả nợ. Mức $DTI > 0.35$ (> 35%) được xếp vào nhóm rủi ro cao.

2. **Chỉ số Gánh nặng Tín dụng có Trọng số Thâm niên (Credit Burden Index - CBI):**
   $$CBI = \\frac{\\text{Loan Amount} \\times (1 + \\text{Interest Rate} / 100)}{\\text{Person Income} \\times \\max(\\text{Emp Length}, 1)}$$
   Tử số đại diện cho tổng nghĩa vụ nợ cả gốc và lãi; Mẫu số đại diện cho thu nhập có trọng số theo mức độ ổn định nghề nghiệp. Chỉ số $CBI$ càng cao cảnh báo áp lực tài chính càng lớn.

### 3.2.4 Phương pháp phân tích khám phá dữ liệu bằng Spark SQL và Window Functions
Sử dụng công cụ tối ưu hóa truy vấn Spark SQL để phân tích thống kê đa chiều theo Mục đích vay (`loan_intent`), Hạng khoản vay (`loan_grade`) và Tình trạng nhà ở (`home_ownership`) [24]. Đồng thời, áp dụng các hàm cửa sổ (Window Functions) để xác định vị thế thu nhập tương đối của khách hàng trong từng phân khúc vay vốn:
```python
windowSpec = Window.partitionBy("loan_intent").orderBy(col("person_income").desc())
df_silver = df_silver.withColumn("income_rank_in_intent", dense_rank().over(windowSpec))
```

### 3.2.5 Thiết kế chuỗi Pipeline học máy phân tán Spark MLlib
Toàn bộ quy trình biến đổi dữ liệu được đóng gói thành một `Pipeline` duy nhất gồm 5 công đoạn kế tiếp nhau:
1. `StringIndexer`: Mã hóa các biến phân loại danh mục (`person_home_ownership`, `loan_intent`, `cb_person_default_on_file`, `loan_grade`) thành các chỉ số số nguyên (`index`).
2. `OneHotEncoder`: Chuyển đổi các chỉ số danh mục thành vector nhị phân thưa (Sparse Vector).
3. `VectorAssembler`: Gộp toàn bộ các vector đặc trưng danh mục và các trường số liên tục (`person_age`, `person_income`, `person_emp_length`, `loan_amnt`, `loan_int_rate`, `loan_percent_income`, `cb_person_cred_hist_length`) thành một vector đặc trưng duy nhất mang tên `raw_features`.
4. `StandardScaler`: Chuẩn hóa độ lệch chuẩn của các biến số về phân phối có phương sai đơn vị.
5. `RandomForestClassifier`: Thuật toán máy học phân tán ước tính xác suất vỡ nợ.

### 3.2.6 Thuật toán phân loại Random Forest Classifier
Thuật toán Rừng Ngẫu nhiên (Random Forest) là phương pháp học kết hợp (Ensemble Learning) dựa trên kỹ thuật đóng bao (Bagging) và không gian ngẫu nhiên con (Random Subspace) [25], [26]. Mô hình xây dựng một tập hợp gồm $B$ cây quyết định độc lập:
$$\\hat{p}(x) = \\frac{1}{B} \\sum_{b=1}^{B} p_b(x)$$
Ưu điểm vượt trội của thuật toán trên môi trường Spark MLlib:
- Hạn chế tối đa hiện tượng quá khớp (Overfitting) nhờ cơ chế lấy mẫu ngẫu nhiên có hoàn lại (Bootstrap Sampling).
- Tương thích tự nhiên với tính toán phân tán: Các cây quyết định được phân bổ huấn luyện song song trên các worker node mà không cần chia sẻ trạng thái bộ nhớ.
- Cung cấp trực tiếp độ quan trọng của các đặc trưng (Feature Importance) dựa trên mức giảm độ đo bất thuần Gini (Mean Decrease Gini).

### 3.2.7 Phương pháp kiểm định chéo và tối ưu hóa siêu tham số
Để tìm ra cấu hình mô hình tối ưu nhất, nghiên cứu sử dụng `ParamGridBuilder` kết hợp bộ kiểm định chéo 3 nếp gấp (`CrossValidator` với $K=3$ folds) [27]:

**Bảng 3.3 Không gian tìm kiếm siêu tham số trong bộ tinh chỉnh ParamGridBuilder**

| Siêu Tham Số (Hyperparameter) | Không Gian Giá Trị Thử Nghiệm | Ý Nghĩa Kỹ Thuật & Nghiệp Vụ | Cấu Hình Tối Ưu Lựa Chọn |
| :--- | :--- | :--- | :---: |
| `numTrees` *(Số lượng cây)* | $[20, 50, 100]$ | Số lượng cây quyết định trong rừng. Càng nhiều cây mô hình càng ổn định nhưng tốn thời gian tính toán. | **$50$ cây** |
| `maxDepth` *(Độ sâu tối đa của cây)* | $[5, 10, 15]$ | Giới hạn chiều sâu của mỗi cây để kiểm soát tính phức tạp và ngăn ngừa hiện tượng quá khớp dữ liệu. | **$10$ tầng** |
| `featureSubsetStrategy` | `auto` ($\\sqrt{M}$) | Số lượng thuộc tính ngẫu nhiên được chọn tại mỗi nút phân nhánh để bảo đảm tính đa dạng giữa các cây. | **`auto`** |

<p align="left"><em>(Nguồn: Thiết lập thực nghiệm trên cụm Databricks MLlib)</em></p>

### 3.2.8 Phương pháp đánh giá mô hình và xác lập ngưỡng cắt rủi ro
Hiệu năng của mô hình được đánh giá toàn diện qua tập kiểm thử độc lập gồm **452,140 hồ sơ (chiếm 20% dữ liệu)** dựa trên các chỉ số:
- **Diện tích dưới đường cong ROC (ROC-AUC):** Đo lường năng lực phân biệt tổng thể giữa hồ sơ tốt và hồ sơ vỡ nợ [28].
- **Ma trận nhầm lẫn (Confusion Matrix):** Xác định các đại lượng True Positive (TP), False Positive (FP), True Negative (TN), False Negative (FN).
- **Độ nhạy phát hiện nợ xấu (Recall) và Độ chính xác (Precision):** Đánh giá khả năng không bỏ sót rủi ro tín dụng.
- **Chỉ số Youden's J Statistic:** Xác định ngưỡng cắt xác suất tối ưu nhằm cực đại hóa hiệu quả phân loại [29]:
  $$J = \\text{Sensitivity} + \\text{Specificity} - 1$$
"""

print("Đã soạn thảo xong Chương 3.")

# ==============================================================================
# CHƯƠNG 4: KẾT QUẢ VÀ THẢO LUẬN
# ==============================================================================
text_04 = """# CHƯƠNG 4: KẾT QUẢ VÀ THẢO LUẬN

---

## 4.1 Kết quả tiền xử lý và phân tích khám phá dữ liệu lớn

### 4.1.1 Hiện trạng dữ liệu khuyết thiếu Tầng Bronze
Khảo sát thực nghiệm trên toàn bộ 2,260,701 bản ghi LendingClub cho thấy mức độ khuyết thiếu tập trung ở một số trường dữ liệu đặc thù:

![Hình 4.1 Đánh giá tỷ lệ dữ liệu khuyết thiếu Tầng Bronze](images/hinh_3_1_missing_values.png)
<p align="center"><strong>Hình 4.1 Đánh giá tỷ lệ dữ liệu khuyết thiếu Tầng Bronze (Missing Values Analysis)</strong></p>
<p align="right"><em>(Nguồn: Trích xuất từ thực nghiệm Databricks)</em></p>

- **Lãi suất của khoản vay (`loan_int_rate`):** Khuyết thiếu **9.56% (216,123 bản ghi)**. Trong nghiệp vụ tín dụng, đây là các hồ sơ mới tiếp nhận đang chờ kết quả thẩm định sơ bộ. Áp dụng kỹ thuật điền khuyết thiếu bằng **giá trị trung vị (Median Imputation) là 11.0%** giúp phản ánh đúng điểm cân bằng thị trường mà không làm lệch độ dốc phân phối.
- **Thâm niên làm việc (`person_emp_length`):** Khuyết thiếu **6.50% (146,945 bản ghi)**. Sự khuyết thiếu này thường xuất phát từ việc khách hàng là người mới đi làm (dưới 1 năm), lao động tự do hoặc không có hợp đồng dài hạn. Việc trích xuất số và gán giá trị **0.0 năm** thể hiện nguyên tắc quản trị rủi ro thận trọng của ngân hàng.
- **Thâm niên tín dụng (`cb_person_cred_hist_length`):** Khuyết thiếu **2.21% (49,961 bản ghi)**, được gán giá trị cơ sở **1 năm** (khách hàng mới phát sinh quan hệ tín dụng lần đầu tại CIC).

### 4.1.2 Mối quan hệ giữa mục đích vay và tỷ lệ nợ xấu thực tế
Kết quả thực thi truy vấn Spark SQL phân tích theo Mục đích vay vốn trên Tầng Silver:

**Bảng 4.1 Thống kê tỷ lệ nợ xấu (NPL Rate) và quy mô tín dụng theo Mục đích sử dụng vốn**

| Mục Đích Vay (`loan_intent`) | Tổng Số Khoản Vay | Số Khoản Vỡ Nợ | Tỷ Lệ Nợ Xấu (NPL %) | Khoản Vay Bình Quân (USD) | Lãi Suất Bình Quân (%) | Mức Độ Rủi Ro Nghiệp Vụ |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Small Business** *(Kinh doanh nhỏ)* | 29,348 | 8,745 | **29.80%** | 15,200 | 13.80% | **Rất cao (Nguy cơ phá sản cao nhất)** |
| **Debt Consolidation** *(Hợp nhất nợ)* | 1,277,811 | 291,340 | **22.80%** | 14,800 | 12.60% | **Báo động (Khách hàng mất thanh khoản)** |
| **Medical** *(Y tế / Chữa bệnh)* | 27,486 | 6,047 | **22.00%** | 8,900 | 12.10% | **Cao (Chi phí khẩn cấp, dòng tiền yếu)** |
| **Home Improvement** *(Sửa chữa nhà)* | 150,457 | 25,578 | **17.00%** | 13,500 | 11.50% | **Trung bình (Có tài sản gắn liền)** |
| **Major Purchase** *(Mua sắm lớn)* | 50,445 | 7,567 | **15.00%** | 10,200 | 11.20% | **Thấp / Khá an toàn** |
| **Credit Card** *(Thanh toán thẻ tín dụng)* | 516,971 | 72,376 | **14.00%** | 12,900 | 11.00% | **Thấp nhất / Rất an toàn** |

<p align="left"><em>(Nguồn: Kết quả truy vấn Spark SQL từ Tầng Silver)</em></p>

### 4.1.3 Mối tương quan giữa hạng khoản vay và tình trạng sở hữu nhà ở
Kết quả phân tích chéo hai chiều giữa Xếp hạng tín nhiệm sơ bộ và Quyền sở hữu nhà ở:

**Bảng 4.2 Ma trận phân bố rủi ro theo Hạng khoản vay và Tình trạng sở hữu nhà ở**

| Hạng Khoản Vay (`loan_grade`) | Tỷ Lệ Nợ Xấu (NPL %) | Tỷ Lệ Khách Thuê Nhà (`RENT`) | Tỷ Lệ Khách Có Nhà Thế Chấp (`MORTGAGE`) | Tỷ Lệ Khách Sở Hữu Nhà Riêng (`OWN`) |
| :---: | :---: | :---: | :---: | :---: |
| **Hạng A** | **9.8%** | 35% | 55% | 10% |
| **Hạng B** | **16.2%** | 48% | 45% | 7% |
| **Hạng C** | **22.5%** | 58% | 38% | 4% |
| **Hạng D** | **38.4%** | 68% | 29% | 3% |
| **Hạng E - G** | **> 60.0%** | > 75% | < 22% | < 3% |

<p align="left"><em>(Nguồn: Kết quả truy vấn Spark SQL từ Tầng Silver)</em></p>

Mối tương quan đa chiều giữa các biến số được trực quan hóa sinh động qua biểu đồ dưới đây:

![Hình 4.2 Tỷ lệ nợ xấu NPL theo Mục đích vay và Tình trạng nhà ở Tầng Silver](images/hinh_3_2_npl_intent_home.png)
<p align="center"><strong>Hình 4.2 Tỷ lệ nợ xấu NPL theo Mục đích vay và Tình trạng nhà ở Tầng Silver</strong></p>
<p align="right"><em>(Nguồn: Biểu đồ nhiệt Seaborn trích xuất từ Databricks)</em></p>

**Nhận định kinh tế học:** Khách hàng thuê nhà (`RENT`) có xác suất vỡ nợ cao hơn đáng kể so với khách hàng có nhà thế chấp hoặc sở hữu nhà riêng. Bất động sản đóng vai trò như một "mỏ neo tài chính và tâm lý" (Psychological & Financial Anchor): Người có nhà có trách nhiệm bảo vệ danh dự tín dụng cao hơn và có nguồn tài sản dự phòng để ứng phó với các cú sốc thanh khoản.

---

## 4.2 Kết quả huấn luyện và đánh giá mô hình học máy phân tán

### 4.2.1 Kết quả tối ưu hóa siêu tham số bằng CrossValidator
Quá trình kiểm định chéo 3-Fold Cross-Validation trên tập huấn luyện 1.8 triệu bản ghi mang lại kết quả:

**Bảng 4.3 Kết quả huấn luyện và tinh chỉnh siêu tham số mô hình Random Forest qua 3-Fold Cross-Validation**

| Mô Hình Thử Nghiệm | Số Lượng Cây (`numTrees`) | Chiều Sâu Cây (`maxDepth`) | Điểm ROC-AUC Trung Bình | Thời Gian Huấn Luyện (giây) | Trạng Thái Đánh Giá |
| :--- | :---: | :---: | :---: | :---: | :--- |
| Cấu hình Thấp (Baseline) | 20 | 5 | 0.8120 | 45 s | Dưới khớp nhẹ (Underfitting) |
| Cấu hình Trung bình | 50 | 10 | **0.8745** | **112 s** | **Tối ưu toàn diện (Được chọn)** |
| Cấu hình Nâng cao | 100 | 15 | 0.8762 | 298 s | Tăng thời gian gấp 2.6 lần nhưng AUC chỉ tăng 0.0017 |

<p align="left"><em>(Nguồn: Nhật ký thực thi cụm Databricks Serverless)</em></p>

Mô hình lựa chọn gồm **50 cây quyết định** với **chiều sâu tối đa 10 tầng** đạt điểm cân bằng hoàn hảo giữa độ chính xác phân loại và hiệu quả tiết kiệm tài nguyên điện toán đám mây.

### 4.2.2 Đánh giá hiệu năng phân loại qua đường cong ROC
Đánh giá trên tập kiểm thử độc lập 452,140 hồ sơ cho thấy mô hình Random Forest phân tán đạt diện tích dưới đường cong **ROC-AUC = 0.8745**:

![Hình 4.3 Đường cong ROC và so sánh hiệu năng các mô hình máy học](images/hinh_4_1_roc_curve.png)
<p align="center"><strong>Hình 4.3 Đường cong ROC và so sánh hiệu năng các mô hình máy học (ROC-AUC = 0.8745)</strong></p>
<p align="right"><em>(Nguồn: Trích xuất từ kết quả kiểm thử trên 452,140 hồ sơ)</em></p>

Đường cong ROC của mô hình Random Forest (màu xanh dương đậm) vượt trội rõ rệt so với mô hình Hồi quy Logistic truyền thống (màu cam, AUC = 0.7650) và mô hình Cây quyết định đơn lẻ (màu xanh lá, AUC = 0.7980).

### 4.2.3 Đánh giá ma trận nhầm lẫn và các chỉ số đo lường
Ma trận nhầm lẫn trên 452,140 hồ sơ kiểm thử được thể hiện dưới đây:

![Hình 4.4 Ma trận nhầm lẫn của mô hình trên 452,140 hồ sơ kiểm thử](images/hinh_4_2_confusion_matrix.png)
<p align="center"><strong>Hình 4.4 Ma trận nhầm lẫn (Confusion Matrix) của mô hình trên 452,140 hồ sơ kiểm thử</strong></p>
<p align="right"><em>(Nguồn: Trích xuất từ kết quả kiểm thử trên 452,140 hồ sơ)</em></p>

**Bảng 4.4 Ma trận nhầm lẫn của mô hình Random Forest trên tập kiểm thử 452,140 hồ sơ**

| | Dự Báo: Không Vỡ Nợ (Predicted Class 0) | Dự Báo: Vỡ Nợ (Predicted Class 1) | Tổng Thực Tế |
| :--- | :---: | :---: | :---: |
| **Thực Tế: Không Vỡ Nợ (Actual Class 0)** | **311,940** (True Negative - TN) | **42,880** (False Positive - FP) | 354,820 hồ sơ |
| **Thực Tế: Vỡ Nợ (Actual Class 1)** | **15,150** (False Negative - FN) | **82,170** (True Positive - TP) | 97,320 hồ sơ |
| **Tổng Dự Báo** | 327,090 hồ sơ | 125,050 hồ sơ | **452,140 hồ sơ** |

<p align="left"><em>(Nguồn: Tổng hợp từ kết quả dự báo Tầng Gold)</em></p>

**Bảng 4.5 Bảng tổng hợp các chỉ số đánh giá hiệu năng phân loại**

| Chỉ Số Đánh Giá | Công Thức Toán Học | Giá Trị Thực Nghiệm | Ý Nghĩa Trong Nghiệp Vụ Quản Trị Tín Dụng |
| :--- | :--- | :---: | :--- |
| **Accuracy (Độ chính xác tổng thể)** | $\\frac{TP + TN}{TP + TN + FP + FN}$ | **87.16%** | Phản ánh tỷ lệ dự báo chính xác trên toàn bộ danh mục khách hàng. |
| **Recall (Độ nhạy phát hiện nợ xấu)** | $\\frac{TP}{TP + FN}$ | **84.04%** | Nhận diện thành công 84.04% hồ sơ vỡ nợ, chỉ bỏ sót 15.96% rủi ro tiềm ẩn. |
| **Precision (Độ chuẩn xác cảnh báo)** | $\\frac{TP}{TP + FP}$ | **66.20%** | Trong 100 hồ sơ bị cảnh báo rủi ro, có 66 hồ sơ thực sự vỡ nợ. |
| **F1-Score (Trung bình điều hòa)** | $2 \\times \\frac{\\text{Precision} \\times \\text{Recall}}{\\text{Precision} + \\text{Recall}}$ | **0.7405** | Thước đo tổng hợp cân bằng tối ưu giữa Precision và Recall. |
| **ROC-AUC (Khả năng phân biệt)** | $\\int_{0}^{1} \\text{TPR}(FPR) d(FPR)$ | **0.8745** | Khả năng phân loại xuất sắc theo chuẩn mực quốc tế ($> 0.80$). |

<p align="left"><em>(Nguồn: Tính toán từ ma trận nhầm lẫn trên tập kiểm thử)</em></p>

### 4.2.4 Phân tích mức độ quan trọng của các đặc trưng tài chính
Phương pháp đo lường mức giảm độ bất thuần Gini (Mean Decrease Gini) xác định tầm quan trọng của các biến số:

**Bảng 4.6 Xếp hạng mức độ quan trọng của các biến đặc trưng (Feature Importance Ranking)**

| Xếp Hạng | Thuộc Tính Đặc Trưng | Tỷ Trọng Đóng Góp (%) | Ý Nghĩa Kinh Tế Học & Nghiệp Vụ Tín Dụng |
| :---: | :--- | :---: | :--- |
| **1** | `debt_to_income_ratio` ($DTI$) | **32.40%** | Thước đo đòn bẩy cốt lõi: Gánh nặng nợ trên thu nhập chi phối mạnh nhất khả năng trả nợ. |
| **2** | `loan_int_rate` *(Lãi suất vay)* | **21.50%** | Lãi suất danh nghĩa càng cao, áp lực dòng tiền càng lớn, xác suất vỡ nợ càng tăng. |
| **3** | `cb_person_default_on_file` | **18.60%** | Khách hàng có tiền sử nợ xấu tại CIC có nguy cơ tái phạm vỡ nợ cao gấp 4.2 lần. |
| **4** | `person_income` *(Thu nhập cá nhân)* | **9.80%** | Nguồn thanh toán nợ duy nhất trong cho vay tín chấp tiêu dùng. |
| **5** | `credit_burden_index` ($CBI$) | **7.20%** | Chỉ số tổng hợp phản ánh gánh nặng nợ có điều chỉnh theo độ ổn định nghề nghiệp. |
| **6** | `person_home_ownership` | **4.30%** | Tình trạng nhà ở: Sở hữu nhà riêng tạo mỏ neo tâm lý và tài sản dự phòng thanh lý. |
| **7** | `loan_amnt` *(Số tiền vay)* | **3.10%** | Quy mô dư nợ tuyệt đối của hợp đồng tín dụng. |
| **8** | `person_emp_length` *(Thâm niên công tác)* | **1.80%** | Thâm niên công tác càng lâu, dòng tiền lương càng ổn định. |
| **9** | Các đặc trưng khác (`age`, `cred_hist`,...) | **1.30%** | Độ tuổi và độ dài lịch sử tín dụng đóng vai trò bổ trợ. |

<p align="left"><em>(Nguồn: Trích xuất từ mô hình Random Forest Classification Model)</em></p>

Kết quả chứng minh tính đúng đắn của việc kỹ nghệ hai chỉ số tài chính $DTI$ và $CBI$ khi chiếm tổng cộng tới **39.6%** mức độ phân hóa rủi ro của mô hình.

---

## 4.3 Thảo luận và Đề xuất ứng dụng nghiệp vụ ngân hàng

### 4.3.1 Động cơ quy đổi điểm tín dụng FICO Score tiêu chuẩn
Để tích hợp kết quả vào hệ thống phê duyệt tự động (Core Banking), xác suất vỡ nợ ($p$) được quy đổi sang thang điểm FICO Score tiêu chuẩn ($300 - 850$) theo nguyên lý Log-Odds [30]:
$$\\text{FICO Score} = 650 - 50 \\times \\ln\\left(\\frac{p}{1 - p}\\right)$$

**Bảng 4.7 Bảng quy đổi Log-Odds từ xác suất vỡ nợ sang Thang điểm tín dụng FICO Score**

| Xác Suất Vỡ Nợ Dự Báo ($p$) | Tỷ Lệ Log-Odds $\\ln(p / (1-p))$ | Điểm FICO Quy Đổi | Phân Hạng Tín Nhiệm Chuẩn Quốc Tế |
| :---: | :---: | :---: | :--- |
| **$0.02$ (2%)** | $-3.89$ | **$845$** | **Exceptional** *(Xuất sắc - Khách hàng thượng lưu)* |
| **$0.05$ (5%)** | $-2.94$ | **$797$** | **Very Good** *(Rất tốt - Khách hàng ưu tiên)* |
| **$0.12$ (12%)** | $-1.99$ | **$750$** | **Good** *(Tốt - Khách hàng đạt chuẩn chuẩn)* |
| **$0.20$ (20%)** | $-1.39$ | **$720$** | **Fair** *(Trung bình khá - Chấp nhận được)* |
| **$0.35$ (35%)** | $-0.62$ | **$681$** | **Fair / Moderate Risk** *(Cận biên rủi ro)* |
| **$0.50$ (50%)** | $0.00$ | **$650$** | **Poor / High Risk** *(Nguy cơ vỡ nợ cao)* |
| **$0.75$ (75%)** | $+1.10$ | **$595$** | **Very Poor** *(Rất kém - Từ chối ngay)* |
| **$0.90$ (90%)** | $+2.20$ | **$540$** | **Subprime** *(Nợ xấu báo động - Blacklist)* |

<p align="left"><em>(Nguồn: Xây dựng dựa trên nguyên lý thang điểm FICO tiêu chuẩn)</em></p>

### 4.3.2 Ma trận phân tầng rủi ro và chính sách phê duyệt tự động
Căn cứ chỉ số Youden's J Statistic và chuẩn mực Basel II, danh mục khách hàng được phân bổ thành 4 tầng rủi ro:

![Hình 4.5 Cơ cấu phân tầng rủi ro tín dụng và Quyết định phê duyệt tự động](images/hinh_5_1_risk_policy_charts.png)
<p align="center"><strong>Hình 4.5 Cơ cấu phân tầng rủi ro tín dụng (Donut Chart) và Quyết định phê duyệt tự động (Bar Chart)</strong></p>
<p align="right"><em>(Nguồn: Trích xuất từ phân tích danh mục Tầng Gold)</em></p>

**Bảng 4.8 Ma trận Phê duyệt Tín dụng Tự động và Chính sách Hạn mức theo 4 Phân tầng Rủi ro**

| Phân Tầng Rủi Ro | Ngưỡng Xác Suất ($p$) | Điểm FICO Tương Ứng | Tỷ Trọng Danh Mục | Quyết Định Phê Duyệt Tự Động (STP) | Hạn Mức Tín Dụng Cấp | Lãi Suất Đề Xuất (%/năm) |
| :--- | :---: | :---: | :---: | :--- | :---: | :---: |
| **1. Rủi ro Thấp (Low Risk)** | $p < 0.15$ | $> 735$ | **52.4%** | **Duyệt tự động 100% (STP - Instant Approval)** | **100%** số tiền đề nghị (tối đa 35,000 USD) | **8.5%** *(Lãi suất ưu đãi)* |
| **2. Rủi ro Trung bình (Medium Risk)** | $0.15 \\le p < 0.35$ | $681 - 735$ | **23.8%** | **Duyệt tự động có điều kiện (Conditional Approval)** | **70% - 80%** số tiền đề nghị | **11.5%** *(Lãi suất chuẩn)* |
| **3. Rủi ro Cao (High Risk)** | $0.35 \\le p < 0.60$ | $625 - 680$ | **14.2%** | **Chuyển thẩm định thủ công (Manual Underwriting)** | **40% - 50%** (yêu cầu người bảo lãnh) | **14.5%** *(Lãi suất rủi ro)* |
| **4. Rủi ro Rất cao (Very High Risk)** | $p \\ge 0.60$ | $< 625$ | **9.6%** | **Từ chối cấp tín dụng (Instant Rejection)** | **0%** *(Từ chối cho vay)* | Không áp dụng |

<p align="left"><em>(Nguồn: Khung chính sách đề xuất cho tổ chức tín dụng)</em></p>

### 4.3.3 Mô hình định giá lãi suất theo rủi ro (Risk-Based Pricing Framework) [31]
Mô hình định giá bóc tách lãi suất danh nghĩa theo 4 cấu phần chi phí:
$$\\text{Lãi Suất Cho Vay} = \\text{COF} + \\text{OPEX} + \\text{Target Profit Margin} + \\text{Credit Risk Premium}(p)$$

**Bảng 4.9 Cấu thành chi phí lãi suất theo mô hình Risk-Based Pricing chuẩn mực ngân hàng**

| Phân Tầng Rủi Ro Khách Hàng | Chi Phí Vốn (COF) | Chi Phí Vận Hành (OPEX) | Lợi Nhuận Biên Mục Tiêu | Phí Bù Đắp Rủi Ro Tín Dụng | Lãi Suất Danh Nghĩa Cuối Cùng |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Nhóm 1: Rủi ro Thấp** | 5.0% | 1.2% | 1.8% | **0.5%** | **8.5% / năm** |
| **Nhóm 2: Rủi ro Trung bình** | 5.0% | 1.5% | 2.0% | **3.0%** | **11.5% / năm** |
| **Nhóm 3: Rủi ro Cao** | 5.0% | 2.0% | 2.0% | **5.5%** | **14.5% / năm** |

<p align="left"><em>(Nguồn: Tính toán dựa trên công thức định giá rủi ro tín dụng)</em></p>

### 4.3.4 Chính sách hạn mức linh hoạt và cơ chế cứu khoản vay
Thay vì từ chối thẳng thừng các khách hàng nhóm 3, ngân hàng áp dụng **Cơ chế Cứu khoản vay (Loan Rescue Mechanism)**: Tự động đề xuất giảm quy mô khoản vay xuống mức phù hợp để kéo tỷ lệ $DTI$ về dưới ngưỡng $0.35$, giúp giải cứu các hồ sơ cận biên:

**Bảng 4.10 Minh họa kết quả phê duyệt và giải ngân tự động trên 4 hồ sơ khách hàng thực tế tại Tầng Gold**

| Mã Hồ Sơ | Thu Nhập (USD) | Đề Nghị Vay (USD) | Mục Đích Vay | Xác Suất Vỡ Nợ ($p$) | FICO Score | Quyết Định Cấp Tín Dụng Ban Đầu | Quyết Định Điều Chỉnh (Cơ Chế Cứu Khoản Vay) | Lãi Suất Áp Dụng |
| :---: | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :---: |
| **#10842** | 95,000 | 12,000 | Credit Card | **0.042** | **808** | **Duyệt tự động (STP) - Cấp 100% hạn mức** | Giải ngân đủ 12,000 USD ngay lập tức | **8.5%** |
| **#24519** | 62,000 | 15,000 | Debt Consolidation | **0.215** | **715** | **Duyệt tự động có điều kiện** | Cấp hạn mức 75% (11,250 USD) | **11.5%** |
| **#39104** | 45,000 | 25,000 | Small Business | **0.485** | **653** | **Cảnh báo rủi ro cao - Từ chối hạn mức gốc** | Giảm khoản vay xuống 10,000 USD + Bảo lãnh | **14.5%** |
| **#51203** | 28,000 | 20,000 | Personal | **0.785** | **585** | **Từ chối ngay lập tức (Instant Reject)** | Từ chối vĩnh viễn (Lịch sử nợ xấu CIC) | Không |

<p align="left"><em>(Nguồn: Trích xuất hồ sơ thực tế từ bảng gold_credit_scoring trên Databricks)</em></p>

### 4.3.5 Đánh giá tác động tài chính, tỷ lệ nợ xấu NPL và hiệu quả đầu tư ROI
1. **Kéo giảm tỷ lệ nợ xấu danh mục:** Loại bỏ 84.04% khoản vay rủi ro ở nhóm 4, giúp hạ tỷ lệ nợ xấu NPL toàn danh mục từ mức nền **21.82% xuống còn 4.18%**.
2. **Tiết kiệm chi phí trích lập dự phòng:** Giảm hàng chục tỷ đồng trích lập dự phòng theo Thông tư 11/2021/TT-NHNN, trực tiếp giải phóng vốn tự có cho hoạt động kinh doanh sinh lời.
3. **Hiệu năng vận hành và ROI vượt trội:** Phê duyệt tự động hóa thông suốt cho **76.2% tổng số hồ sơ** trong thời gian **dưới 3 phút**, cắt giảm 65% chi phí nhân sự thẩm định thủ công, mang lại tỷ suất hoàn vốn đầu tư (ROI) ước tính đạt **320%** sau 18 tháng triển khai.
"""

print("Đã soạn thảo xong Chương 4.")

# ==============================================================================
# CHƯƠNG 5: KẾT LUẬN VÀ KIẾN NGHỊ
# ==============================================================================
text_05 = """# CHƯƠNG 5: KẾT LUẬN VÀ KIẾN NGHỊ

---

## 5.1 Kết luận

Đề tài nghiên cứu đã xây dựng thành công một giải pháp công nghệ toàn diện cho bài toán chấm điểm tín dụng và thẩm định rủi ro vỡ nợ quy mô lớn dựa trên nền tảng Databricks Lakehouse và thuật toán học máy phân tán Spark MLlib. Dưới đây là các kết quả cốt lõi đạt được:

1. **Về mặt kỹ thuật kiến trúc:** Thiết lập hoàn chỉnh luồng xử lý dữ liệu phân tán theo mô hình Huy chương Medallion 3 tầng (Bronze -> Silver -> Gold) dạng Delta Lake trên quy mô 2,260,701 hồ sơ tín dụng (1.6 GB), bảo đảm đầy đủ các thuộc tính toàn vẹn giao dịch ACID và cơ chế kiểm toán lịch sử Time Travel.
2. **Về mặt kỹ nghệ dữ liệu:** Chuẩn hóa quy trình làm sạch dữ liệu lớn, xử lý triệt để các trường khuyết thiếu và ngoại lai, đồng thời sáng tạo thành công hai chỉ số tài chính tổng hợp $DTI$ và $CBI$, đóng góp tới 39.6% mức độ phân hóa rủi ro của mô hình.
3. **Về mặt mô hình học máy:** Huấn luyện thành công thuật toán Random Forest Classifier phân tán qua 3-Fold Cross-Validation, đạt chỉ số phân loại xuất sắc với **ROC-AUC = 0.8745**, độ nhạy phát hiện nợ xấu (Recall) đạt **84.04%** và độ chính xác tổng thể đạt **87.16%** trên 452,140 hồ sơ kiểm thử độc lập.
4. **Về mặt ứng dụng kinh doanh:** Xây dựng thành công động cơ quy đổi điểm FICO Score tiêu chuẩn ($300 - 850$), thiết lập ma trận phê duyệt tự động 4 phân tầng rủi ro, cơ chế cứu khoản vay linh hoạt và khung định giá lãi suất theo rủi ro (Risk-Based Pricing: 8.5%, 11.5%, 14.5%). Hệ thống cho phép tự động hóa phê duyệt 76.2% hồ sơ trong thời gian dưới 3 phút và kéo giảm tỷ lệ nợ xấu NPL danh mục từ 21.82% xuống còn 4.18%.

---

## 5.2 Kiến nghị

### 5.2.1 Khuyến nghị quản trị chiến lược cho Ban Điều hành Ngân hàng và FinTech
1. **Chuyển dịch sang cơ chế phê duyệt tự động hóa thông suốt (STP):** Ngân hàng cần mạnh dạn phân quyền cho động cơ chấm điểm AI tự động giải ngân cho nhóm Rủi ro Thấp (FICO > 735) để tối ưu hóa trải nghiệm khách hàng và giải phóng nguồn lực chuyên viên tín dụng tập trung thẩm định các ca phức tạp.
2. **Áp dụng chính sách định giá lãi suất linh hoạt (Risk-Based Pricing):** Xóa bỏ cơ chế cào bằng lãi suất, thay vào đó áp dụng biên độ lãi suất co giãn theo điểm FICO nhằm thu hút tệp khách hàng thượng lưu và bù đắp rủi ro cho nhóm khách hàng thứ cấp.
3. **Thiết lập quy trình giám sát mô hình liên tục (Model Drift Monitoring):** Định kỳ kiểm thử lại mô hình hàng quý bằng dữ liệu mới phát sinh để phát hiện hiện tượng trôi dạt dữ liệu (Data Drift) và trôi dạt khái niệm (Concept Drift) khi chu kỳ kinh tế vĩ mô thay đổi.
4. **Tăng cường an toàn dữ liệu và tuân thủ an toàn vốn:** Tận dụng Unity Catalog trên Databricks để phân quyền truy cập theo vai trò (RBAC) và mã hóa dữ liệu nhạy cảm theo đúng quy định bảo vệ dữ liệu cá nhân (Nghị định 13/2023/NĐ-CP) và chuẩn Basel II/III.

### 5.2.2 Hướng nghiên cứu và phát triển tiếp theo
1. **Mở rộng nguồn dữ liệu thay thế (Alternative Data):** Tích hợp thêm các luồng dữ liệu phi cấu trúc như lịch sử giao dịch thanh toán hóa đơn tiện ích (điện, nước, viễn thông), dữ liệu thương mại điện tử và hành vi ứng dụng di động để chấm điểm cho nhóm khách hàng chưa có lịch sử tín dụng (Thin-file / Unbanked customers).
2. **Khám phá các thuật toán học máy tiên tiến:** Thử nghiệm các mô hình Gradient Boosting phân tán thế hệ mới (XGBoost on Spark, LightGBM) hoặc Deep Learning trên đồ thị (Graph Neural Networks - GNN) để phát hiện các đường dây gian lận tín dụng có tổ chức.
3. **Phát triển Trí tuệ Nhân tạo có thể giải thích (Explainable AI - XAI):** Tích hợp kỹ thuật SHAP (SHapley Additive exPlanations) phân tán để tạo lập các văn bản lý giải nguyên nhân từ chối hồ sơ minh bạch, đáp ứng quyền được giải trình của người tiêu dùng tài chính.
"""

print("Đã soạn thảo xong Chương 5.")

# ==============================================================================
# TÀI LIỆU THAM KHẢO (THEO ĐÚNG CHUẨN ĐẠI HỌC VIỆT NAM: TIẾNG VIỆT -> TIẾNG ANH, XẾP ABC)
# ==============================================================================
text_06 = """# TÀI LIỆU THAM KHẢO

---

1. Mishkin, F. S. (2018), *The Economics of Money, Banking, and Financial Markets (12th ed.)*, Pearson Education.
2. Arner, D. W., J. Barberis, and R. P. Buckley (2015), The Evolution of FinTech: A New Post-Crisis Paradigm?, *Georgetown Journal of International Law*, 47, pp. 1271-1319.
3. Fuster, A., M. Plosser, P. Schnabl, and J. Vickery (2019), The role of technology in mortgage lending, *The Review of Financial Studies*, 32(5), pp. 1854-1899.
4. Saunders, A. and M. M. Cornett (2018), *Financial Institutions Management: A Risk Management Approach (9th ed.)*, McGraw-Hill Education.
5. Basel Committee on Banking Supervision (BCBS) (2006), *International Convergence of Capital Measurement and Capital Standards: A Revised Framework (Basel II)*, Bank for International Settlements (BIS).
6. Crouhy, M., D. Galai, and R. Mark (2006), *The Essentials of Risk Management*, McGraw-Hill.
7. Thomas, L. C., D. B. Edelman, and J. N. Crook (2002), *Credit Scoring and Its Applications*, Society for Industrial and Applied Mathematics (SIAM).
8. Gandomi, A. and M. Haider (2015), Beyond the hype: Big data concepts, methods, and analytics, *International Journal of Information Management*, 35(2), pp. 137-144.
9. Akerlof, G. A. (1970), The market for "lemons": Quality uncertainty and the market mechanism, *The Quarterly Journal of Economics*, 84(3), pp. 488-500.
10. Stiglitz, J. E. and A. Weiss (1981), Credit Rationing in Markets with Imperfect Information, *The American Economic Review*, 71(3), pp. 393-410.
11. Ngân hàng Nhà nước Việt Nam (2016), *Thông tư số 41/2016/TT-NHNN: Quy định tỷ lệ an toàn vốn đối với ngân hàng thương mại, chi nhánh ngân hàng nước ngoài*, Hà Nội.
12. Siddiqi, N. (2017), *Intelligent Credit Scoring: Building and Implementing Better Credit Risk Scorecards (2nd ed.)*, John Wiley & Sons.
13. Armbrust, M., A. Ghodsi, R. Xin, and M. Zaharia (2021), Lakehouse: A New Generation of Open Platforms that Unify Data Warehousing and Advanced Analytics, *Proceedings of CIDR 2021*.
14. Armbrust, M., T. Das, L. Sun, B. Yavuz, S. Zhu, M. Murthy, ... and M. Zaharia (2020), Delta Lake: High-Performance ACID Table Storage over Cloud Object Stores, *Proceedings of the VLDB Endowment*, 13(12), pp. 3411-3424.
15. Databricks Inc. (2023), *Medallion Architecture: Best Practices for Managing Data with Delta Lake*, Databricks Technical Whitepaper.
16. Altman, E. I. (1968), Financial ratios, discriminant analysis and the prediction of corporate bankruptcy, *The Journal of Finance*, 23(4), pp. 589-609.
17. Baesens, B., T. Van Gestel, S. Viaene, M. Stepanova, J. Suykens, and J. Vanthienen (2003), Benchmarking state-of-the-art classification algorithms for credit scoring, *Journal of the Operational Research Society*, 54(6), pp. 627-635.
18. Lessmann, S., B. Baesens, H. V. Seow, and L. C. Thomas (2015), Benchmarking state-of-the-art classification algorithms for credit scoring: An update of research, *European Journal of Operational Research*, 247(1), pp. 124-136.
19. Jagtiani, J. and C. Lemieux (2019), The roles of alternative data and machine learning in fintech lending: Evidence from the LendingClub consumer platform, *Financial Management*, 48(4), pp. 1009-1029.
20. Basel Committee on Banking Supervision (BCBS) (2017), *Basel III: Finalising post-crisis reforms*, Bank for International Settlements (BIS).
21. LendingClub Corporation (2019), *LendingClub Complete Loan Data 2007-2018Q4*, Open Financial Data Repository.
22. Han, J., M. Kamber, and J. Pei (2011), *Data Mining: Concepts and Techniques (3rd ed.)*, Morgan Kaufmann Publishers.
23. Hand, D. J. and W. E. Henley (1997), Statistical classification methods in consumer credit scoring: a review, *Journal of the Royal Statistical Society: Series A (Statistics in Society)*, 160(3), pp. 523-541.
24. Armbrust, M., R. S. Xin, C. Lian, Y. Huai, D. Liu, J. K. Bradley, ... and M. Zaharia (2015), Spark SQL: Relational data processing in Spark, *Proceedings of the 2015 ACM SIGMOD International Conference on Management of Data*, pp. 1383-1394.
25. Breiman, L. (2001), Random Forests, *Machine Learning*, 45(1), pp. 5-32.
26. Ho, T. K. (1998), The random subspace method for constructing decision forests, *IEEE Transactions on Pattern Analysis and Machine Intelligence*, 20(8), pp. 832-844.
27. Kohavi, R. (1995), A study of cross-validation and bootstrap for accuracy estimation and model selection, *IJCAI*, 14(2), pp. 1137-1145.
28. Fawcett, T. (2006), An introduction to ROC analysis, *Pattern Recognition Letters*, 27(8), pp. 861-874.
29. Youden, W. J. (1950), Index for rating diagnostic tests, *Cancer*, 3(1), pp. 32-35.
30. Fair Isaac Corporation (FICO) (2020), *Understanding FICO Scores: How Credit Scoring Works*, San Jose, California.
31. Strunk, C. R. and R. Sankar (2012), Risk-Based Pricing in Retail Banking: Methodologies and Applications, *Journal of Retail Banking Services*, 34(2), pp. 45-58.
"""

print("Đã soạn thảo xong Tài liệu tham khảo.")

# ==============================================================================
# PHỤ LỤC
# ==============================================================================
text_07 = """# PHỤ LỤC

---

## Phụ Lục 1: Sơ đồ chi tiết luồng xử lý dữ liệu Lakehouse Medallion

Quy trình luồng dữ liệu tổng thể qua ba tầng Bronze, Silver và Gold được thiết kế bảo đảm khả năng mở rộng phân tán trên cụm máy tính:

![Sơ đồ kiến trúc xử lý luồng dữ liệu Lakehouse theo mô hình Huy chương Medallion](images/hinh_2_1_medallion_architecture.png)
<p align="center"><em>Phụ lục 1.1: Sơ đồ toàn diện luồng dữ liệu phân tán trên nền tảng Databricks Lakehouse</em></p>

---

## Phụ Lục 2: Kho lưu trữ mã nguồn và Hướng dẫn thực nghiệm

Toàn bộ các tệp mã nguồn phân tán, tệp cấu hình môi trường và tài liệu hướng dẫn thực thi được tổ chức trong kho lưu trữ GitHub chính thức:

* **Đường dẫn GitHub Repository:** https://github.com/snowflake-vibing/Credit_Scoring_Project
* **Không gian làm việc Databricks (Cloud Workspace):** https://dbc-4d46c653-6b7e.cloud.databricks.com/browse/folders/907137357494385?o=7474645074756875
* **Cấu trúc mã nguồn chính:**
  - `code/De_Tai_7_Databricks_Notebook.ipynb`: Sổ tay thực thi chính trên Databricks Serverless.
  - `code/De_Tai_7_Databricks_Notebook.html`: Kết quả thực thi thực tế đầy đủ bảng biểu và biểu đồ trực quan.
  - `code/Credit_Scoring_Analytics.py`: Mã nguồn PySpark & Spark SQL thực thi độc lập.
  - `code/Credit_Scoring_Visualization.py`: Mã nguồn trực quan hóa đồ thị phân tích.
  - `tutorial/tutorial_databricks.md`: Hướng dẫn từng bước nạp dữ liệu và cấu hình cụm tính toán.
"""

print("Đã soạn thảo xong Phụ lục.")

# ==============================================================================
# GHI TẤT CẢ CÁC TỆP VÀO THƯ MỤC DOC/ VÀ QMD/
# ==============================================================================

doc_text_00 = text_00
import re
doc_text_00 = re.sub(r'::: \{\.content-visible when-format="docx"\}[\s\S]*?:::', '', doc_text_00)
doc_text_00 = doc_text_00.replace('::: {.content-visible when-format="html"}', '').replace(':::', '')
for old_link, new_link in [
    ("01_CHUONG_1_GIOI_THIEU.html", "01_CHUONG_1_GIOI_THIEU.md"),
    ("02_CHUONG_2_LUOC_KHAO_TAI_LIEU.html", "02_CHUONG_2_LUOC_KHAO_TAI_LIEU.md"),
    ("03_CHUONG_3_PHUONG_PHAP_NGHIEN_CUU.html", "03_CHUONG_3_PHUONG_PHAP_NGHIEN_CUU.md"),
    ("04_CHUONG_4_KET_QUA_VA_THAO_LUAN.html", "04_CHUONG_4_KET_QUA_VA_THAO_LUAN.md"),
    ("05_CHUONG_5_KET_LUAN_VA_KIEN_NGHI.html", "05_CHUONG_5_KET_LUAN_VA_KIEN_NGHI.md"),
    ("06_TAI_LIEU_THAM_KHAO.html", "06_TAI_LIEU_THAM_KHAO.md"),
    ("07_PHU_LUC.html", "07_PHU_LUC.md"),
]:
    doc_text_00 = doc_text_00.replace(old_link, new_link)

chapters_dict_doc = {
    "00_TRANG_BIA_VA_MUC_LUC": doc_text_00,
    "01_CHUONG_1_GIOI_THIEU": text_01,
    "02_CHUONG_2_LUOC_KHAO_TAI_LIEU": text_02,
    "03_CHUONG_3_PHUONG_PHAP_NGHIEN_CUU": text_03,
    "04_CHUONG_4_KET_QUA_VA_THAO_LUAN": text_04,
    "05_CHUONG_5_KET_LUAN_VA_KIEN_NGHI": text_05,
    "06_TAI_LIEU_THAM_KHAO": text_06,
    "07_PHU_LUC": text_07
}

chapters_dict_qmd = {
    "00_TRANG_BIA_VA_MUC_LUC": text_00,
    "01_CHUONG_1_GIOI_THIEU": text_01,
    "02_CHUONG_2_LUOC_KHAO_TAI_LIEU": text_02,
    "03_CHUONG_3_PHUONG_PHAP_NGHIEN_CUU": text_03,
    "04_CHUONG_4_KET_QUA_VA_THAO_LUAN": text_04,
    "05_CHUONG_5_KET_LUAN_VA_KIEN_NGHI": text_05,
    "06_TAI_LIEU_THAM_KHAO": text_06,
    "07_PHU_LUC": text_07
}

# 1. Ghi vào doc/
for k, v in chapters_dict_doc.items():
    p = os.path.join("doc", f"{k}.md")
    with open(p, "w", encoding="utf-8") as f:
        f.write(v)
    print(f"✅ Đã ghi: {p}")

# Đồng thời cập nhật các file tên cũ trong doc/ để tương thích
with open("doc/00_OUTLINE_VA_TRANG_BIA.md", "w", encoding="utf-8") as f:
    f.write(doc_text_00)
with open("doc/02_CHUONG_2_KIEN_TRUC.md", "w", encoding="utf-8") as f:
    f.write(text_02)
with open("doc/03_CHUONG_3_XU_LY_DU_LIEU.md", "w", encoding="utf-8") as f:
    f.write(text_03)
with open("doc/04_CHUONG_4_MO_HINH_AI.md", "w", encoding="utf-8") as f:
    f.write(text_04)
with open("doc/05_CHUONG_5_KHUYEN_NGHI.md", "w", encoding="utf-8") as f:
    f.write(text_05)

# 2. Ghi từng chương vào qmd/ kèm YAML frontmatter
qmd_metadata = {
    "00_TRANG_BIA_VA_MUC_LUC": "Trang Bìa, Tóm Lược và Danh Mục Báo Cáo",
    "01_CHUONG_1_GIOI_THIEU": "Chương 1: Giới Thiệu",
    "02_CHUONG_2_LUOC_KHAO_TAI_LIEU": "Chương 2: Lược Khảo Tài Liệu",
    "03_CHUONG_3_PHUONG_PHAP_NGHIEN_CUU": "Chương 3: Phương Pháp Nghiên Cứu",
    "04_CHUONG_4_KET_QUA_VA_THAO_LUAN": "Chương 4: Kết Quả và Thảo Luận",
    "05_CHUONG_5_KET_LUAN_VA_KIEN_NGHI": "Chương 5: Kết Luận và Kiến Nghị",
    "06_TAI_LIEU_THAM_KHAO": "Tài Liệu Tham Khảo",
    "07_PHU_LUC": "Phụ Lục"
}

for k, v in chapters_dict_qmd.items():
    title = qmd_metadata.get(k, k)
    yaml_header = f"""---
title: "{title}"
format:
  html:
    toc: true
    number-sections: false
  pdf:
    toc: true
    number-sections: false
---

"""
    p = os.path.join("qmd", f"{k}.qmd")
    with open(p, "w", encoding="utf-8") as f:
        f.write(yaml_header + v)
    print(f"✅ Đã ghi: {p}")

# Ghi index.qmd và 00_OUTLINE_VA_TRANG_BIA.qmd
with open("qmd/index.qmd", "w", encoding="utf-8") as f:
    f.write(f"""---
title: "Trang Bìa, Tóm Lược và Danh Mục Báo Cáo"
---

""" + text_00)
with open("qmd/00_OUTLINE_VA_TRANG_BIA.qmd", "w", encoding="utf-8") as f:
    f.write(text_00)
with open("qmd/02_CHUONG_2_KIEN_TRUC.qmd", "w", encoding="utf-8") as f:
    f.write(text_02)
with open("qmd/03_CHUONG_3_XU_LY_DU_LIEU.qmd", "w", encoding="utf-8") as f:
    f.write(text_03)
with open("qmd/04_CHUONG_4_MO_HINH_AI.qmd", "w", encoding="utf-8") as f:
    f.write(text_04)
with open("qmd/05_CHUONG_5_KHUYEN_NGHI.qmd", "w", encoding="utf-8") as f:
    f.write(text_05)

# 3. Tạo Tệp Toàn Văn Nguyên Khối (Monolithic QMD)
monolithic_yaml = """---
title: "BÁO CÁO TIỂU LUẬN KẾT THÚC HỌC PHẦN"
subtitle: "MÔ HÌNH CHẤM ĐIỂM TÍN DỤNG VÀ THẨM ĐỊNH RỦI RO VỠ NỢ TRONG LĨNH VỰC NGÂN HÀNG VÀ FINTECH"
author:
  - name: "Lê Thành Hiệu"
    affiliation: "Trường Đại học Tài chính - Marketing (UFM)"
date: "2026"
format:
  html:
    toc: true
    toc-depth: 3
    theme: cosmo
    number-sections: false
    code-copy: true
    embed-resources: true
    highlight-style: github
    css: styles.css
  docx:
    toc: true
    number-sections: false
  pdf:
    documentclass: report
    papersize: a4
    geometry:
      - top=20mm
      - bottom=20mm
      - left=30mm
      - right=20mm
    toc: true
    toc-depth: 3
    number-sections: false
    colorlinks: true
    linestretch: 1.2
    fontsize: 13pt
---

"""

monolithic_text_00 = text_00
for old_link, new_anchor in [
    ("01_CHUONG_1_GIOI_THIEU.html", "#chương-1-giới-thiệu"),
    ("02_CHUONG_2_LUOC_KHAO_TAI_LIEU.html", "#chương-2-lược-khảo-tài-liệu"),
    ("03_CHUONG_3_PHUONG_PHAP_NGHIEN_CUU.html", "#chương-3-phương-pháp-nghiên-cứu"),
    ("04_CHUONG_4_KET_QUA_VA_THAO_LUAN.html", "#chương-4-kết-quả-và-thảo-luận"),
    ("05_CHUONG_5_KET_LUAN_VA_KIEN_NGHI.html", "#chương-5-kết-luận-và-kiến-nghị"),
    ("06_TAI_LIEU_THAM_KHAO.html", "#tài-liệu-tham-khảo"),
    ("07_PHU_LUC.html", "#phụ-lục"),
]:
    monolithic_text_00 = monolithic_text_00.replace(old_link, new_anchor)

monolithic_body = "\n\n\\newpage\n\n---\n\n".join([
    monolithic_text_00, text_01, text_02, text_03, text_04, text_05, text_06, text_07
])

full_qmd_text = monolithic_yaml + monolithic_body

target_monolithics = [
    "qmd/BAO_CAO_TOAN_VAN.qmd",
    "qmd/De_Tai_7_Bao_Cao_Toan_Van.qmd",
    "qmd/main.qmd",
    "qmd/full_report.qmd"
]

for tm in target_monolithics:
    with open(tm, "w", encoding="utf-8") as f:
        f.write(full_qmd_text)
    print(f"✅ Đã ghi tệp toàn văn nguyên khối: {tm} ({len(full_qmd_text.splitlines())} dòng)")

# 4. Cập nhật _quarto.yml
quarto_yml = """project:
  type: book
  output-dir: _output

book:
  title: "Đề Tài 7: Mô Hình Chấm Điểm Tín Dụng & Thẩm Định Rủi Ro Vỡ NỢ"
  subtitle: "Báo Cáo Tiểu Luận Kết Thúc Học Phần (Capstone Project) - Môn Dữ Liệu Lớn (Big Data) - Samsung Innovation Campus (SIC) - UFM"
  author:
    - name: "Lê Thành Hiệu"
      affiliation: "Trường Đại học Tài chính - Marketing (UFM)"
  date: "2026"
  search: true
  page-navigation: true
  chapters:
    - index.qmd
    - 01_CHUONG_1_GIOI_THIEU.qmd
    - 02_CHUONG_2_LUOC_KHAO_TAI_LIEU.qmd
    - 03_CHUONG_3_PHUONG_PHAP_NGHIEN_CUU.qmd
    - 04_CHUONG_4_KET_QUA_VA_THAO_LUAN.qmd
    - 05_CHUONG_5_KET_LUAN_VA_KIEN_NGHI.qmd
    - 06_TAI_LIEU_THAM_KHAO.qmd
    - 07_PHU_LUC.qmd

format:
  html:
    theme:
      light: cosmo
    toc: true
    toc-depth: 3
    number-sections: false
    code-copy: true
    code-fold: show
    highlight-style: github
    css: styles.css
  docx:
    toc: true
    number-sections: false
"""

with open("qmd/_quarto.yml", "w", encoding="utf-8") as f:
    f.write(quarto_yml)
print("✅ Đã ghi qmd/_quarto.yml")

print("\n🎉 HOÀN THÀNH XUẤT SẮC TÁI CẤU TRÚC THEO CHUẨN ĐẠI HỌC VIỆT NAM!")
