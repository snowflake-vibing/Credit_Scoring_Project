# CHƯƠNG 2: KIẾN TRÚC LUỒNG DỮ LIỆU LAKEHOUSE (MEDALLION ARCHITECTURE)

---

## 2.1. Cơ sở lý luận về Kiến trúc Dữ liệu lớn: Từ Data Warehouse, Data Lake đến Lakehouse

Trong lịch sử phát triển của các hệ thống quản trị dữ liệu doanh nghiệp, ngành ngân hàng luôn là một trong những lĩnh vực tiên phong áp dụng các giải pháp lưu trữ và xử lý dữ liệu quy mô lớn [16]. Tuy nhiên, sự phát triển bùng nổ của dữ liệu số hóa trong những năm gần đây đã bộc lộ những giới hạn cố hữu của các kiến trúc dữ liệu truyền thống:

### 2.1.1. Kiến trúc Kho dữ liệu truyền thống (Data Warehouse)
Kho dữ liệu truyền thống (Data Warehouse) được xây dựng trên nền tảng cơ sở dữ liệu quan hệ (RDBMS), hoạt động theo mô hình *Schema-on-Write* (cấu trúc dữ liệu phải được định nghĩa chặt chẽ trước khi nạp dữ liệu). Kiến trúc này rất mạnh mẽ trong việc thực thi các báo cáo phân tích kinh doanh thông minh (Business Intelligence - BI) và truy vấn SQL có cấu trúc. Tuy nhiên, nó có ba nhược điểm chí mạng:
- **Chi phí lưu trữ đắt đỏ:** Khó có thể mở rộng để lưu trữ hàng petabyte dữ liệu giao dịch lịch sử và dữ liệu thô chưa qua xử lý.
- **Không hỗ trợ dữ liệu phi cấu trúc:** Không thể xử lý trực tiếp các định dạng phi cấu trúc như hình ảnh, văn bản hợp đồng tín dụng hoặc dữ liệu chuỗi thời gian phát sinh liên tục.
- **Hạn chế đối với Trí tuệ nhân tạo và Học máy:** Các thuật toán Machine Learning hiện đại đòi hỏi quyền truy cập trực tiếp vào các tệp dữ liệu thô ở tốc độ cao, điều mà các engine xử lý của Data Warehouse không được thiết kế để tối ưu [17].

### 2.1.2. Kiến trúc Hồ dữ liệu thế hệ thứ nhất (Data Lake)
Để khắc phục bài toán chi phí và tính đa dạng của dữ liệu, kiến trúc Hồ dữ liệu (Data Lake) ra đời dựa trên hệ thống tệp phân tán (Hadoop HDFS hoặc Cloud Object Storage như AWS S3, Azure Data Lake Storage). Data Lake áp dụng cơ chế *Schema-on-Read*, cho phép nạp toàn bộ dữ liệu thô ở mọi định dạng với chi phí rất rẻ. Song, Data Lake thế hệ thứ nhất lại tạo ra những thách thức mới:
- **Thiếu tính toàn vẹn giao dịch (Lack of ACID Transactions):** Khi có nhiều tiến trình ghi và đọc dữ liệu đồng thời, hiện tượng xung đột dữ liệu, tệp bị hỏng hoặc dữ liệu đọc bẩn (dirty reads) thường xuyên xảy ra.
- **Nguy cơ biến thành "Đầm lầy dữ liệu" (Data Swamp):** Do thiếu cơ chế kiểm soát chất lượng dữ liệu (Data Quality Enforcement) và quản trị siêu dữ liệu (Metadata Management), dữ liệu trong Data Lake dễ bị phân mảnh, trùng lặp và không đáng tin cậy cho các bài toán phân tích nhạy cảm như rủi ro tín dụng [18].

### 2.1.3. Sự hội tụ tại Kiến trúc Databricks Lakehouse
Kiến trúc Hồ - Kho dữ liệu hợp nhất (Lakehouse Platform) do Databricks tiên phong phát triển nhằm kết hợp những ưu điểm vượt trội nhất của cả hai kiến trúc tiền nhiệm: tính mở, linh hoạt và chi phí thấp của Data Lake kết hợp cùng năng lực quản trị, tính toàn vẹn giao dịch ACID và hiệu năng truy vấn siêu tốc của Data Warehouse [19].

**Bảng 2.1: So sánh ưu nhược điểm giữa Data Warehouse, Data Lake và Databricks Lakehouse**

| Tiêu chí So sánh | Kho Dữ liệu (Data Warehouse) | Hồ Dữ liệu (Data Lake) | Nền tảng Hồ - Kho (Databricks Lakehouse) |
| :--- | :--- | :--- | :--- |
| **Định dạng dữ liệu** | Chỉ hỗ trợ dữ liệu có cấu trúc (Structured). | Đa dạng (Có cấu trúc, bán cấu trúc, phi cấu trúc). | Hỗ trợ toàn diện mọi định dạng dữ liệu trên cùng một nền tảng mở. |
| **Cơ chế nạp dữ liệu** | Schema-on-Write (nghiêm ngặt, tốn thời gian thiết kế schema). | Schema-on-Read (tự do, dễ mất kiểm soát chất lượng). | Hỗ trợ cả hai: Tiếp nhận dữ liệu thô linh hoạt kết hợp Schema Enforcement chặt chẽ. |
| **Tính toàn vẹn ACID** | Đảm bảo đầy đủ. | Không hỗ trợ hoặc hỗ trợ rất sơ sài. | Đảm bảo 100% tính toàn vẹn giao dịch ACID thông qua Delta Lake Transaction Log. |
| **Khả năng phục vụ ML/AI**| Kém, khó tích hợp với các thư viện Deep Learning/ML. | Khá tốt đối với các kỹ sư dữ liệu nhưng thiếu công cụ quản trị. | Tối ưu hóa tuyệt đối: Tích hợp trực tiếp với PySpark MLlib, MLflow và GPU Acceleration. |
| **Chi phí & Độ mở rộng** | Rất đắt đỏ khi mở rộng quy mô dữ liệu lớn. | Chi phí lưu trữ rẻ, khả năng mở rộng không giới hạn. | Chi phí lưu trữ rẻ trên Object Storage, tài nguyên tính toán tách biệt (Decoupled Compute & Storage). |

---

## 2.2. Nền tảng Apache Spark và Định dạng lưu trữ phân tán Delta Lake

Hệ thống chấm điểm tín dụng trong đề tài được vận hành trên nền tảng **Databricks Serverless Cloud Platform**, tận dụng sức mạnh cộng hưởng của công nghệ tính toán phân tán **Apache Spark** và lớp lưu trữ tối ưu **Delta Lake** [20].

### 2.2.1. Động cơ tính toán phân tán trong bộ nhớ của Apache Spark
Apache Spark là công cụ tính toán phân tán mã nguồn mở hàng đầu thế giới dành cho các bài toán xử lý dữ liệu quy mô lớn (Large-Scale Data Processing). Khác biệt hoàn toàn với mô hình MapReduce cổ điển của Hadoop (vốn phụ thuộc vào việc đọc/ghi liên tục xuống đĩa cứng I/O), Spark thực thi các phép biến đổi trực tiếp trong bộ nhớ RAM phân tán (In-Memory Computing). Cấu trúc trừu tượng hóa DataFrame của Spark kết hợp cùng bộ tối ưu hóa truy vấn **Catalyst Optimizer** và công cụ sinh mã bytecode tự động **Tungsten Engine** giúp tối ưu hóa đồ thị thực thi truy vấn (Directed Acyclic Graph - DAG), giảm thiểu chi phí xáo trộn dữ liệu qua mạng (Data Shuffling) và tăng tốc độ xử lý lên gấp 10 đến 100 lần [21].

### 2.2.2. Các đặc tính kỹ thuật cốt lõi của Delta Lake
Delta Lake là lớp lưu trữ nguồn mở được xây dựng trực tiếp trên các tệp lưu trữ cột nén chuẩn Parquet, bổ sung thêm các tính năng cấp doanh nghiệp mà Data Lake truyền thống không có:

1. **Đảm bảo tính toàn vẹn giao dịch ACID (ACID Transactions):** Delta Lake sử dụng cơ chế ghi nhật ký giao dịch tuần tự có thứ tự (Delta Transaction Log hay `_delta_log`). Mọi thao tác thêm mới (Append), cập nhật (Update), xóa (Delete) hoặc hợp nhất (Merge) đều được ghi nhận như một giao dịch đơn vị nguyên tử (Atomicity). Nếu một tác vụ phân tán bị lỗi giữa chừng trên một worker node, toàn bộ trạng thái sẽ tự động quay về điểm an toàn trước đó, đảm bảo không bao giờ xuất hiện dữ liệu bị hỏng trong kho dữ liệu ngân hàng [22].
2. **Khả năng truy vết lịch sử và kiểm toán tín dụng (Time Travel / Data Versioning):** Mỗi thay đổi dữ liệu trong Delta Lake đều tạo ra một phiên bản phiên bản mới (Commit Version). Tính năng này cho phép các kiểm toán viên ngân hàng hoặc cơ quan quản lý thanh tra có thể truy vấn lại chính xác trạng thái dữ liệu của một khách hàng tại thời điểm 6 tháng hoặc 1 năm trước:
   - Giúp tái lập chính xác môi trường dữ liệu đầu vào đã dùng để đưa ra quyết định duyệt vay tại thời điểm phê duyệt trong quá khứ.
   - Đáp ứng nghiêm ngặt các quy định về tính minh bạch và khả năng giải trình quyết định tín dụng của Ngân hàng Nhà nước và Hiệp ước Basel II [23].
3. **Kiểm soát và tiến hóa cấu trúc dữ liệu (Schema Enforcement & Schema Evolution):** Delta Lake tự động ngăn chặn các tệp dữ liệu rác hoặc dữ liệu có định dạng sai lệch bị ghi vào bảng (Schema Enforcement). Đồng thời, khi nghiệp vụ ngân hàng cần bổ sung các trường thông tin tín dụng mới trong tương lai, hệ thống cho phép cấu trúc bảng tự động tiến hóa an toàn (Schema Evolution) mà không làm gián đoạn các luồng dữ liệu đang hoạt động.
4. **Tối ưu hóa hiệu năng truy vấn phân tán:** Delta Lake tự động tổ chức lại các tệp dữ liệu phân tán thông qua các kỹ thuật nén tệp nhỏ (Compaction / Bin-packing), bỏ qua dữ liệu không liên quan dựa trên siêu dữ liệu tối thiểu/tối đa (Data Skipping), và sắp xếp chỉ mục đa chiều (Z-Ordering), giúp các truy vấn Spark SQL đạt tốc độ phản hồi gần như tức thì [24].

---

## 2.3. Thiết kế Kiến trúc Huy chương Medallion 3 tầng (Bronze - Silver - Gold)

Kiến trúc Huy chương Medallion (Medallion Architecture) là một mô hình thiết kế chuẩn mực dữ liệu được khuyến nghị bởi Databricks nhằm nâng cao dần chất lượng và cấu trúc dữ liệu qua từng tầng xử lý, tạo nên một đường ống dẫn dữ liệu phân tán (Data Pipeline) có tính kiểm soát cao [25].

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                          NGUỒN DỮ LIỆU ĐẦU VÀO (DATA INGESTION)                        │
│            Dữ liệu Hồ sơ Đăng ký vay Trực tuyến / Dữ liệu Lịch sử CIC (CSV)            │
└───────────────────────────────────────────┬────────────────────────────────────────────┘
                                            │
                                            ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        TẦNG BRONZE: DỮ LIỆU NGUYÊN BẢN (RAW LAYER)                     │
│  • Bảng Delta: workspace.default.bronze_credit_data                                    │
│  • Nguyên tắc: Lưu trữ nguyên trạng (As-is), bảo toàn mọi thuộc tính thô              │
│  • Vai trò: Phục vụ lưu vết lịch sử (Audit Trail), sao lưu và tái lập dữ liệu         │
└───────────────────────────────────────────┬────────────────────────────────────────────┘
                                            │
                                            ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                   TẦNG SILVER: DỮ LIỆU LÀM SẠCH VÀ GIÀU THÔNG TIN (CURATED)            │
│  • Bảng Delta: workspace.default.silver_credit_data                                    │
│  • Xử lý: Lọc ngoại lai phi lý, điền khuyết thiếu, chuẩn hóa kiểu dữ liệu              │
│  • Kỹ nghệ đặc trưng: Tính toán DTI, CBI, Window Functions xếp hạng thu nhập          │
│  • Vai trò: Cung cấp nguồn dữ liệu chuẩn mực cho phân tích Spark SQL và Feature Store  │
└───────────────────────────────────────────┬────────────────────────────────────────────┘
                                            │
                                            ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                  TẦNG GOLD: DỮ LIỆU RA QUYẾT ĐỊNH & MÔ HÌNH HÓA AI (BUSINESS)          │
│  • Bảng Delta: workspace.default.gold_credit_scoring                                   │
│  • Tích hợp Spark MLlib: VectorAssembler, StandardScaler, Random Forest Classifier     │
│  • Động cơ Quyết định: Vector xác suất p, Điểm FICO Score, Phân tầng rủi ro 4 nhóm,   │
│    Định giá Lãi suất theo Rủi ro (Risk-Based Pricing), Hạn mức giải ngân               │
│  • Vai trò: Xuất kết quả phê duyệt tự động ra ứng dụng ngân hàng và Dashboard điều hành│
└────────────────────────────────────────────────────────────────────────────────────────┘
```

**Bảng 2.2: Phân định chức năng, nguyên tắc và công nghệ giữa 3 tầng kiến trúc Medallion**

| Tầng Dữ liệu | Bảng Lưu Trữ Delta | Mục Đích Nghiệp Vụ & Kỹ Thuật | Tiêu Chuẩn Chất Lượng & Quản Trị |
| :--- | :--- | :--- | :--- |
| **BRONZE** *(Dữ liệu Thô)* | `workspace.default.bronze_credit_data` | Tiếp nhận và nạp nguyên vẹn toàn bộ các bản ghi đăng ký vay từ tệp thô vào kho Delta Lake. Bảo toàn 100% dữ liệu gốc không chỉnh sửa. | Bất biến (Immutable), cho phép truy vết nguồn gốc (Data Lineage) và phục vụ kiểm toán toàn diện. |
| **SILVER** *(Dữ liệu Làm Sạch)* | `workspace.default.silver_credit_data` | Áp dụng các quy tắc kiểm định dữ liệu ngân hàng: lọc bỏ các dòng có tuổi ngoại lai hoặc thu nhập phi thực tế; điền giá trị thiếu cho thâm niên làm việc và lãi suất; tính toán chỉ số tài chính nghiệp vụ (DTI, CBI). | Dữ liệu sạch, nhất quán về kiểu dữ liệu (Schema-conformed), loại bỏ trùng lặp và sẵn sàng cho phân tích. |
| **GOLD** *(Dữ liệu Kinh Doanh & AI)* | `workspace.default.gold_credit_scoring` | Tích hợp đầu ra từ mô hình học máy phân tán Random Forest: lưu trữ nhãn dự báo, véc-tơ xác suất vỡ nợ, điểm tín dụng FICO Score, phân loại nhóm rủi ro, chính sách hạn mức và mức lãi suất đề xuất. | Dữ liệu tổng hợp cấp cao nhất, phục vụ trực tiếp cho API phê duyệt tự động của ngân hàng và Dashboard quản trị. |

---

## 2.4. Sơ đồ luồng dữ liệu phân tán toàn diện (Data Pipeline Workflow)

*[Ghi chú: Thêm Sơ đồ kiến trúc Medallion Lakehouse tại đây]*

Quy trình vận hành luồng dữ liệu phân tán trong đề tài được thiết kế theo một chu trình tự động hóa khép kín gồm 6 giai đoạn logic:

1. **Giai đoạn 1 - Thu thập và Tiếp nhận (Data Ingestion):** Dữ liệu hồ sơ vay vốn từ cổng tiếp nhận trực tuyến được nạp vào Catalog lưu trữ của Databricks dưới dạng các tệp dữ liệu phân tán.
2. **Giai đoạn 2 - Đóng gói Tầng Bronze:** Động cơ PySpark đọc dữ liệu và chuyển đổi sang bảng định dạng Delta Lake thô (`bronze_credit_data`). Toàn bộ cấu trúc gốc và lịch sử giao dịch được khởi tạo với phiên bản Version 0 trong Delta Log.
3. **Giai đoạn 3 - Tiền xử lý và Làm giàu dữ liệu Tầng Silver:** Cụm phân tán thực thi đồng thời các phép lọc dữ liệu ngoại lai phi logic, điền giá trị khuyết thiếu theo nguyên tắc trung vị thị trường, chuyển đổi kiểu dữ liệu chuẩn và tính toán các chỉ số đòn bẩy tài chính (DTI, CBI). Dữ liệu sau xử lý được ghi đè an toàn vào bảng Delta `silver_credit_data`.
4. **Giai đoạn 4 - Phân tích Thống kê Phân tán (Spark SQL Analytics):** Sử dụng ngôn ngữ Spark SQL tối ưu hóa để truy vấn tổng hợp tỷ lệ nợ xấu, phân tích ma trận tương quan giữa mục đích vay, hạng tín dụng và rủi ro chậm trả, đồng thời ứng dụng hàm cửa sổ phân vùng Window Functions để xếp hạng vị thế tài chính khách hàng.
5. **Giai đoạn 5 - Huấn luyện Pipeline Học máy Phân tán (Spark MLlib Training):** Các thuộc tính được chuẩn hóa và đóng gói qua chuỗi công đoạn `StringIndexer`, `OneHotEncoder`, `VectorAssembler` và `StandardScaler`. Mô hình `RandomForestClassifier` được huấn luyện song song trên các worker nodes với bộ tinh chỉnh siêu tham số `CrossValidator` (3-Folds) để tìm ra mô hình tối ưu nhất.
6. **Giai đoạn 6 - Xuất bản Tầng Gold và Ra quyết định Tự động (Gold Publication & Decisioning):** Kết quả dự báo xác suất vỡ nợ được đưa qua Động cơ Quyết định (Decision Engine) để quy đổi ra điểm FICO Score, gán phân tầng rủi ro, áp chính sách hạn mức và tính lãi suất cho vay theo rủi ro. Toàn bộ thông tin được lưu vĩnh viễn vào bảng Delta `gold_credit_scoring` sẵn sàng phục vụ các kênh giao dịch trực tuyến.

---

## 2.5. Quản trị dữ liệu (Data Governance) và Tuân thủ an toàn vốn theo chuẩn Basel II/III

Đối với các hệ thống công nghệ thông tin trong ngành ngân hàng, việc xây dựng mô hình AI không thể tách rời yêu cầu tuân thủ các quy định về quản trị dữ liệu (Data Governance) và chuẩn mực an toàn vốn quốc tế [26]:

### 2.5.1. Quản trị và Bảo mật Dữ liệu trên Databricks Unity Catalog
- **Phân quyền truy cập dựa trên vai trò (Role-Based Access Control - RBAC):** Hệ thống thiết lập các chính sách phân quyền chi tiết đến từng cấp độ bảng (Table-level) và cấp độ cột (Column-level). Chuyên viên phân tích chỉ được quyền truy cập vào các trường dữ liệu ẩn danh tại Tầng Silver, trong khi các quyết định phê duyệt tại Tầng Gold được phân quyền cho cấp quản lý tín dụng.
- **Truy xuất nguồn gốc dữ liệu (Data Lineage):** Tính năng Data Lineage tự động ghi nhận đường đi của dữ liệu từ bảng thô ban đầu đến các cột tính toán trong bảng Gold, giúp các đoàn kiểm tra kiểm toán dễ dàng xác minh công thức tính toán và nguồn gốc của từng biến số [27].

### 2.5.2. Tuân thủ Hiệp ước An toàn Vốn Basel II và Basel III
Hiệp ước Basel II và Basel III đưa ra các nguyên tắc nghiêm ngặt đối với Phương pháp Tiếp cận Dựa trên Xếp hạng Nội bộ (Internal Ratings-Based - IRB Approach) [28]:
- **Tính ổn định và Khả năng giải trình của Mô hình (Model Explainability):** Các quy định của Ủy ban Basel nghiêm cấm việc sử dụng các mô hình "hộp đen" hoàn toàn không thể giải thích. Việc đề tài lựa chọn thuật toán Random Forest kết hợp phân tích Tầm quan trọng của thuộc tính (Feature Importance) và hàm Log-Odds quy đổi điểm FICO đảm bảo mọi quyết định từ chối hoặc duyệt vay đều có cơ sở định lượng rõ ràng, sẵn sàng giải trình trước cơ quan thanh tra giám sát ngân hàng.
- **Ước lượng Tổn thất Kỳ vọng (Expected Loss - EL):** Dữ liệu xác suất vỡ nợ ($PD$) do Tầng Gold cung cấp là đầu vào trực tiếp cho công thức tính toán trích lập dự phòng tổn thất tín dụng theo chuẩn quốc tế:
  $$EL = PD \times LGD \times EAD$$
  Trong đó $LGD$ (Tỷ lệ tổn thất khi vỡ nợ) và $EAD$ (Tổng dư nợ chịu rủi ro) được kiểm soát chặt chẽ thông qua chính sách quản trị hạn mức và yêu cầu tài sản thế chấp ở các phân tầng rủi ro cao.
