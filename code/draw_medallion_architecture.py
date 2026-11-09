"""
Thiết kế lại hoàn chỉnh Sơ đồ Kiến trúc Medallion Lakehouse (Hình 2.1)
- Độ phân giải: 300 DPI
- Kích thước canvas: 18.0 x 9.5 inches
- Tuyệt đối KHÔNG đè chữ, chữ giãn đều, rõ nét, bố cục thẻ ngân hàng hiện đại
"""

import os
import sys
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

out_dir = r"d:\Project_SIC\final_project\doc\images"
os.makedirs(out_dir, exist_ok=True)
save_path = os.path.join(out_dir, "hinh_2_1_medallion_architecture.png")

# Kích thước khung vẽ: 18.0 x 9.6 inches
fig, ax = plt.subplots(figsize=(18.0, 9.6), dpi=300)
ax.set_xlim(0, 18.0)
ax.set_ylim(0, 9.6)
ax.axis('off')

# Màu nền canvas trang nhã
fig.patch.set_facecolor('#f8fafc')
ax.set_facecolor('#f8fafc')

# 1. TIÊU ĐỀ CHÍNH & PHỤ CỦA SƠ ĐỒ
ax.text(9.0, 9.15, "KIẾN TRÚC XỬ LÝ DỮ LIỆU LỚN & TRÍ TUỆ NHÂN TẠO THEO MÔ HÌNH MEDALLION LAKEHOUSE", 
        fontsize=14.5, fontweight='bold', ha='center', va='center', color='#0f172a')
ax.text(9.0, 8.78, "Hệ thống Chấm điểm Tín dụng & Thẩm định Rủi ro Vỡ nợ Phân tán từ 2.26 Triệu Hồ sơ LendingClub đến Ra Quyết định STP", 
        fontsize=10.5, fontstyle='italic', ha='center', va='center', color='#475569')

# 2. ĐỊNH NGHĨA 5 TẦNG KIẾN TRÚC
# Toạ độ X: 5 cards, width=3.0, gap=0.55
# x_coords: 0.45, 4.00, 7.55, 11.10, 14.65 (total width = 14.65 + 3.0 = 17.65, margin right = 0.35)
card_w = 3.0
gap = 0.55
start_x = 0.45

tiers_data = [
    {
        "stage": "BƯỚC 1",
        "title": "NGUỒN DỮ LIỆU",
        "sub": "Raw Data Sources",
        "header_bg": "#1e293b",
        "badge_bg": "#f1f5f9",
        "badge_text": "#0f172a",
        "sections": [
            {
                "title": "HỒ SƠ TÍN DỤNG GỐC",
                "color": "#334155",
                "bullets": [
                    "Dữ liệu: LendingClub (2007 - 2018Q4)",
                    "Quy mô: 2,260,701 hồ sơ vay thực tế",
                    "Dung lượng tệp: ~1.6 GB định dạng CSV",
                    "Thuộc tính: 151 trường thông tin gốc",
                    "Tỷ lệ nợ xấu nền tảng: ~21.82%"
                ]
            },
            {
                "title": "CƠ CHẾ NẠP TIẾP NHẬN",
                "color": "#475569",
                "bullets": [
                    "Giao thức: Batch Ingestion phân tán",
                    "Động cơ: PySpark DataFrame Reader",
                    "Quản trị: Catalog Explorer Databricks",
                    "Phân vùng: 16 partitions song song",
                    "Đảm bảo: Không nghẽn bộ nhớ Driver"
                ]
            }
        ],
        "footer_badge": "Dung lượng thô: 1.6 GB (2.26M rows)",
        "footer_bg": "#e2e8f0",
        "footer_fg": "#1e293b"
    },
    {
        "stage": "BƯỚC 2",
        "title": "TẦNG BRONZE",
        "sub": "Raw Lakehouse Layer",
        "header_bg": "#854d0e",
        "badge_bg": "#fef9c3",
        "badge_text": "#713f12",
        "sections": [
            {
                "title": "LƯU TRỮ DELTA THÔ",
                "color": "#854d0e",
                "bullets": [
                    "Bảng: bronze_credit_data",
                    "Định dạng: Delta Lake (Parquet nền)",
                    "Nguyên tắc: Bất biến (As-Is Immutability)",
                    "Bảo toàn 100% dữ liệu gốc ban đầu",
                    "Lưu vết: _delta_log phiên bản v0"
                ]
            },
            {
                "title": "KIỂM TOÁN CHẤT LƯỢNG",
                "color": "#9a3412",
                "bullets": [
                    "Audit Trail lịch sử không thể sửa",
                    "Hỗ trợ Time Travel phục hồi dữ liệu",
                    "Khảo sát khuyết thiếu (Missing Values):",
                    " • loan_int_rate khuyết 9.56%",
                    " • person_emp_length khuyết 6.50%"
                ]
            }
        ],
        "footer_badge": "Độ toàn vẹn dữ liệu: 100% Acid Log",
        "footer_bg": "#fef3c7",
        "footer_fg": "#92400e"
    },
    {
        "stage": "BƯỚC 3",
        "title": "TẦNG SILVER",
        "sub": "Curated & Enriched Layer",
        "header_bg": "#1d4ed8",
        "badge_bg": "#dbeafe",
        "badge_text": "#1e40af",
        "sections": [
            {
                "title": "TIỀN XỬ LÝ & LÀM SẠCH",
                "color": "#1d4ed8",
                "bullets": [
                    "Lọc tuổi hợp pháp: 18 <= Tuổi <= 80",
                    "Lọc nguồn trả nợ: Thu nhập năm > 0",
                    "Điền thâm niên thiếu: 0.0 năm (thận trọng)",
                    "Điền lãi suất thiếu: 11.0% (trung vị)",
                    "Bảng Delta: silver_credit_data"
                ]
            },
            {
                "title": "KỸ NGHỆ ĐẶC TRƯNG TÀI CHÍNH",
                "color": "#2563eb",
                "bullets": [
                    "Chỉ số DTI = Khoản vay / Thu nhập",
                    "Chỉ số CBI = Gánh nặng nợ có trọng số",
                    "Phân tích Spark SQL & Window Function:",
                    " • dense_rank() theo mục đích vay",
                    " • Thống kê NPL theo sở hữu nhà"
                ]
            }
        ],
        "footer_badge": "Dữ liệu sạch: Chuẩn hóa 12 Features",
        "footer_bg": "#e0e7ff",
        "footer_fg": "#3730a3"
    },
    {
        "stage": "BƯỚC 4",
        "title": "TẦNG GOLD",
        "sub": "AI Engine & Scoring Model",
        "header_bg": "#b45309",
        "badge_bg": "#fef3c7",
        "badge_text": "#92400e",
        "sections": [
            {
                "title": "PIPELINE MÁY HỌC PHÂN TÁN",
                "color": "#b45309",
                "bullets": [
                    "Mã hóa: StringIndexer + OneHotEncoder",
                    "Đóng gói: VectorAssembler phân tán",
                    "Chuẩn hóa: StandardScaler (z-score)",
                    "Thuật toán: Random Forest (50 Trees)",
                    "Phân chia: 80% Train / 20% Test"
                ]
            },
            {
                "title": "HIỆU NĂNG & ĐIỂM FICO",
                "color": "#c2410c",
                "bullets": [
                    "Chỉ số ROC-AUC: 0.8745 (Xuất sắc)",
                    "Độ chính xác Accuracy: 82.07%",
                    "Quy đổi xác suất vỡ nợ PD sang:",
                    " • Điểm FICO Score (300 - 850)",
                    "Bảng Delta: gold_credit_scoring"
                ]
            }
        ],
        "footer_badge": "Hiệu năng: ROC-AUC = 0.8745 (Test)",
        "footer_bg": "#ffedd5",
        "footer_fg": "#9a3412"
    },
    {
        "stage": "BƯỚC 5",
        "title": "RA QUYẾT ĐỊNH STP",
        "sub": "Automated Policy Engine",
        "header_bg": "#15803d",
        "badge_bg": "#dcfce7",
        "badge_text": "#166534",
        "sections": [
            {
                "title": "PHÂN TẦNG RỦI RO (4 NHÓM)",
                "color": "#15803d",
                "bullets": [
                    "G1 (PD < 15%): Duyệt tự động 100%",
                    "G2 (15% <= PD < 35%): Duyệt 70% hạn mức",
                    "G3 (35% <= PD < 60%): Thẩm định thủ công",
                    "G4 (PD >= 60%): Từ chối cấp tín dụng",
                    "Thời gian xử lý: Dưới 3 phút / hồ sơ"
                ]
            },
            {
                "title": "ĐỊNH GIÁ LÃI SUẤT BÙ RỦI RO",
                "color": "#166534",
                "bullets": [
                    "Nhóm 1 (Rủi ro Thấp): Lãi suất 8.5%",
                    "Nhóm 2 (Rủi ro Trung bình): Lãi suất 11.5%",
                    "Nhóm 3 (Rủi ro Cao): Lãi suất 14.5%",
                    "Tuân thủ tỷ lệ an toàn vốn CAR",
                    "Đáp ứng khuyến nghị Basel II / Basel III"
                ]
            }
        ],
        "footer_badge": "Tự động hóa STP: > 80% hồ sơ",
        "footer_bg": "#dcfce7",
        "footer_fg": "#14532d"
    }
]

# KÍCH THƯỚC CHUẨN CỦA CÁC THẺ
card_y = 0.68
card_h = 7.70
header_h = 1.30

for i, tier in enumerate(tiers_data):
    x = start_x + i * (card_w + gap)
    
    # 1. Shadow card mềm mại
    shadow = FancyBboxPatch((x + 0.04, card_y - 0.04), card_w, card_h,
                            boxstyle="round,pad=0.04,rounding_size=0.14",
                            facecolor='#e2e8f0', edgecolor='none', zorder=1)
    ax.add_patch(shadow)
    
    # 2. Main card body nền trắng viền xám nhạt
    card = FancyBboxPatch((x, card_y), card_w, card_h,
                          boxstyle="round,pad=0.04,rounding_size=0.14",
                          facecolor='white', edgecolor='#cbd5e1', linewidth=1.2, zorder=2)
    ax.add_patch(card)
    
    # 3. Header box ở đỉnh thẻ
    header_y = card_y + card_h - header_h
    header = FancyBboxPatch((x, header_y), card_w, header_h,
                            boxstyle="round,pad=0.04,rounding_size=0.14",
                            facecolor=tier["header_bg"], edgecolor='none', zorder=3)
    ax.add_patch(header)
    
    # Khối vuông che góc tròn dưới của header
    sq_h = FancyBboxPatch((x, header_y), card_w, 0.45,
                          boxstyle="square,pad=0",
                          facecolor=tier["header_bg"], edgecolor='none', zorder=4)
    ax.add_patch(sq_h)
    
    # Nhãn Bước (Stage pill)
    pill_w = 0.85
    pill_h = 0.26
    pill_x = x + (card_w - pill_w) / 2
    pill_y = header_y + 0.90
    pill = FancyBboxPatch((pill_x, pill_y), pill_w, pill_h,
                          boxstyle="round,pad=0.02,rounding_size=0.08",
                          facecolor=tier["badge_bg"], edgecolor='none', zorder=5)
    ax.add_patch(pill)
    ax.text(pill_x + pill_w/2, pill_y + pill_h/2, tier["stage"],
            fontsize=7.8, fontweight='bold', ha='center', va='center', color=tier["badge_text"], zorder=6)
    
    # Tiêu đề thẻ chính
    ax.text(x + card_w/2, header_y + 0.56, tier["title"],
            fontsize=10.8, fontweight='bold', ha='center', va='center', color='white', zorder=5)
    ax.text(x + card_w/2, header_y + 0.24, tier["sub"],
            fontsize=8.5, ha='center', va='center', color='#cbd5e1', zorder=5)
    
    # Đường kẻ viền màu phân tách dưới header
    ax.plot([x + 0.15, x + card_w - 0.15], [header_y - 0.02, header_y - 0.02],
            color=tier["header_bg"], linewidth=2.0, zorder=6)
    
    # 4. Nội dung chi tiết trong Card Body
    curr_y = header_y - 0.35
    for sec in tier["sections"]:
        # Tiêu đề mục con có nền pill nhẹ
        sec_title = sec["title"]
        ax.text(x + 0.16, curr_y, sec_title,
                fontsize=8.8, fontweight='bold', ha='left', va='center', color=sec["color"], zorder=5)
        # Đường gạch chân tiêu đề mục con
        ax.plot([x + 0.16, x + card_w - 0.20], [curr_y - 0.12, curr_y - 0.12],
                color='#e2e8f0', linewidth=1.0, zorder=5)
        
        curr_y -= 0.32
        for bullet in sec["bullets"]:
            ax.text(x + 0.18, curr_y, bullet,
                    fontsize=7.9, ha='left', va='center', color='#334155', zorder=5)
            curr_y -= 0.28
        
        curr_y -= 0.22  # Khoảng cách giữa 2 section con
    
    # 5. Footer Badge ở đáy thẻ
    footer_w = card_w - 0.36
    footer_h = 0.38
    footer_x = x + 0.18
    footer_y = card_y + 0.18
    footer_box = FancyBboxPatch((footer_x, footer_y), footer_w, footer_h,
                                boxstyle="round,pad=0.02,rounding_size=0.08",
                                facecolor=tier["footer_bg"], edgecolor='none', zorder=5)
    ax.add_patch(footer_box)
    ax.text(footer_x + footer_w/2, footer_y + footer_h/2, tier["footer_badge"],
            fontsize=8.0, fontweight='bold', ha='center', va='center', color=tier["footer_fg"], zorder=6)

# 3. VẼ CÁC MŨI TÊN LIÊN KẾT GIỮA CÁC THẺ (ĐẶT Ở VÙNG KHOẢNG TRỐNG HEADER, KHÔNG ĐÈ CHỮ)
arrow_y = card_y + card_h - header_h / 2
connectors = [
    (start_x + card_w, start_x + card_w + gap, "PySpark\nIngest"),
    (start_x + 2*card_w + gap, start_x + 2*card_w + 2*gap, "Clean &\nEnrich"),
    (start_x + 3*card_w + 2*gap, start_x + 3*card_w + 3*gap, "Spark MLlib\nTrain/Test"),
    (start_x + 4*card_w + 3*gap, start_x + 4*card_w + 4*gap, "Decision\nRules")
]

for x1, x2, label in connectors:
    # Mũi tên kết nối màu xanh nổi bật trong khoảng trống giữa 2 header
    arrow = patches.FancyArrowPatch(
        (x1 + 0.04, arrow_y), (x2 - 0.04, arrow_y),
        arrowstyle="-|>", mutation_scale=18,
        linewidth=2.4, color='#0284c7', zorder=10
    )
    ax.add_patch(arrow)
    
    # Nhãn mô tả luồng đặt ngay phía trên mũi tên (không chạm vào card)
    mid_x = (x1 + x2) / 2
    ax.text(mid_x, arrow_y + 0.44, label,
            fontsize=7.8, fontweight='bold', ha='center', va='center',
            color='#0369a1', zorder=11,
            bbox=dict(boxstyle="round,pad=0.20", facecolor='#e0f2fe', edgecolor='#38bdf8', linewidth=0.8))

# 4. CHÂN TRANG GHI CHÚ
ax.text(9.0, 0.24, "Mô hình kiến trúc Medallion Lakehouse - Đề tài 7: Credit Scoring & Loan Default Risk Engine (TS. Trần Mạnh Tường hướng dẫn)",
        fontsize=8.8, ha='center', va='center', color='#64748b')

plt.tight_layout()
fig.savefig(save_path, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches='tight')
plt.close(fig)
print(f"✅ ĐÃ XUẤT THÀNH CÔNG BIỂU ĐỒ KIẾN TRÚC MỚI KHÔNG ĐÈ CHỮ: {save_path}")
