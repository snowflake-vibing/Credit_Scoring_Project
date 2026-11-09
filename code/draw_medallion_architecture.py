"""
Tạo biểu đồ kiến trúc hệ thống Medallion Lakehouse (Hình 2.1)
Phục vụ: Báo cáo tiểu luận môn Dữ Liệu Lớn & AI Trong Kinh Doanh
Độ phân giải: 300 DPI, phong cách ngân hàng chuyên nghiệp.
"""

import os
import sys
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Cấu hình phông chữ sạch sẽ, tương thích chuẩn
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Segoe UI', 'Helvetica']
plt.rcParams['axes.edgecolor'] = '#cbd5e1'

out_dir = r"d:\Project_SIC\final_project\doc\images"
os.makedirs(out_dir, exist_ok=True)
save_path = os.path.join(out_dir, "hinh_2_1_medallion_architecture.png")

# Kích thước khung vẽ: 15.5 x 8.4 inches
fig, ax = plt.subplots(figsize=(15.5, 8.4), dpi=300)
ax.set_xlim(0, 15.5)
ax.set_ylim(0, 8.4)
ax.axis('off')

# Màu nền canvas trang nhã
fig.patch.set_facecolor('#f8fafc')
ax.set_facecolor('#f8fafc')

# Tiêu đề biểu đồ kiến trúc
ax.text(7.75, 8.0, "KIẾN TRÚC XỬ LÝ DỮ LIỆU LỚN & AI THEO MÔ HÌNH HUY CHƯƠNG MEDALLION", 
        fontsize=13.5, fontweight='bold', ha='center', va='center', color='#0f172a')
ax.text(7.75, 7.62, "Quy trình tích hợp khép kín từ 2.26 triệu hồ sơ LendingClub đến Ra quyết định Tín dụng Tự động (< 3 phút)", 
        fontsize=10.0, fontstyle='italic', ha='center', va='center', color='#475569')

# Dữ liệu 5 tầng kiến trúc
tiers = [
    {
        "x": 0.5,
        "width": 2.65,
        "title": "1. NGUỒN DỮ LIỆU",
        "sub": "Raw Data Sources",
        "color": "#1e293b",
        "accent": "#64748b",
        "items": [
            ("Hồ sơ LendingClub", True),
            ("• Quy mô: 2,260,701 hồ sơ", False),
            ("• Dung lượng: ~1.6 GB CSV", False),
            ("• 151 trường thông tin gốc", False),
            ("• Phân phối nợ xấu: ~21.8%", False),
            ("Tiếp nhận dữ liệu (Ingestion)", True),
            ("• Batch streaming phân tán", False),
            ("• Schema inference tự động", False),
            ("• Đăng ký Catalog Explorer", False),
            ("• Phân vùng nạp song song", False)
        ]
    },
    {
        "x": 3.5,
        "width": 2.65,
        "title": "2. TẦNG BRONZE",
        "sub": "Raw Delta Lakehouse",
        "color": "#9a3412",
        "accent": "#ea580c",
        "items": [
            ("Bảng bronze_credit_data", True),
            ("• Lưu trữ nguyên bản (As-is)", False),
            ("• Định dạng Delta Parquet", False),
            ("• ACID Transaction Log", False),
            ("• Quản lý tệp _delta_log v0", False),
            ("Kiểm toán & Truy vết", True),
            ("• Audit Trail không thể sửa", False),
            ("• Hỗ trợ Time Travel lịch sử", False),
            ("• Bảo toàn 100% dữ liệu gốc", False),
            ("• Khảo sát Missing Values", False)
        ]
    },
    {
        "x": 6.5,
        "width": 2.65,
        "title": "3. TẦNG SILVER",
        "sub": "Curated & Enriched",
        "color": "#1d4ed8",
        "accent": "#3b82f6",
        "items": [
            ("Làm sạch & Chuẩn hóa", True),
            ("• Lọc: 18 <= Tuổi <= 80", False),
            ("• Lọc: Thu nhập năm > 0", False),
            ("• Điền Emp_len = 0.0 năm", False),
            ("• Điền Int_rate = 11.0%", False),
            ("Kỹ nghệ đặc trưng tài chính", True),
            ("• Chỉ số DTI = Loan / Income", False),
            ("• Chỉ số CBI (Trọng số việc)", False),
            ("• Window Function ranking", False),
            ("• Bảng silver_credit_data", False)
        ]
    },
    {
        "x": 9.5,
        "width": 2.65,
        "title": "4. TẦNG GOLD",
        "sub": "AI Engine & Inference",
        "color": "#b45309",
        "accent": "#f59e0b",
        "items": [
            ("Spark MLlib Pipeline", True),
            ("• StringIndexer & OneHot", False),
            ("• VectorAssembler + Scaler", False),
            ("• Random Forest (50 Trees)", False),
            ("• ROC-AUC = 0.8745 (Test)", False),
            ("Mô hình chấm điểm rủi ro", True),
            ("• Dự báo Xác suất vỡ nợ (PD)", False),
            ("• Quy đổi FICO Score (300-850)", False),
            ("• Bảng gold_credit_scoring", False),
            ("• Phân loại chuẩn Basel II", False)
        ]
    },
    {
        "x": 12.5,
        "width": 2.5,
        "title": "5. PHÊ DUYỆT STP",
        "sub": "Decisioning & Policy",
        "color": "#15803d",
        "accent": "#22c55e",
        "items": [
            ("Động cơ ra quyết định (< 3p)", True),
            ("• Nhóm 1 (PD < 15%):", False),
            ("  -> Duyệt Tự động 100%", False),
            ("• Nhóm 2 (15% <= PD < 35%):", False),
            ("  -> Duyệt 70% hạn mức", False),
            ("• Nhóm 3 (35% <= PD < 60%):", False),
            ("  -> Thẩm định & Thế chấp", False),
            ("• Nhóm 4 (PD >= 60%):", False),
            ("  -> Auto-Reject từ chối", False),
            ("Định giá lãi suất bù rủi ro", True),
            ("• Phân dải lãi suất: 8.5% - 14.5%", False)
        ]
    }
]

# Vẽ các card tầng
card_y = 0.70
card_h = 6.45

for tier in tiers:
    x = tier["x"]
    w = tier["width"]
    
    # 1. Shadow card
    shadow = FancyBboxPatch((x + 0.05, card_y - 0.05), w, card_h,
                            boxstyle="round,pad=0.06,rounding_size=0.16",
                            facecolor='#e2e8f0', edgecolor='none', zorder=1)
    ax.add_patch(shadow)
    
    # 2. Main card body
    card = FancyBboxPatch((x, card_y), w, card_h,
                          boxstyle="round,pad=0.06,rounding_size=0.16",
                          facecolor='white', edgecolor='#cbd5e1', linewidth=1.2, zorder=2)
    ax.add_patch(card)
    
    # 3. Header box
    header_h = 1.05
    header_y = card_y + card_h - header_h
    header = FancyBboxPatch((x, header_y), w, header_h,
                            boxstyle="round,pad=0.06,rounding_size=0.16",
                            facecolor=tier["color"], edgecolor='none', zorder=3)
    ax.add_patch(header)
    
    # Square out bottom corners of header
    sq_h = FancyBboxPatch((x, header_y), w, 0.4,
                          boxstyle="square,pad=0",
                          facecolor=tier["color"], edgecolor='none', zorder=4)
    ax.add_patch(sq_h)
    
    # Header text
    ax.text(x + w/2, header_y + 0.65, tier["title"],
            fontsize=10.2, fontweight='bold', ha='center', va='center', color='white', zorder=5)
    ax.text(x + w/2, header_y + 0.28, tier["sub"],
            fontsize=8.2, ha='center', va='center', color='#cbd5e1', zorder=5)
    
    # Accent indicator bar
    ax.plot([x + 0.18, x + w - 0.18], [header_y - 0.03, header_y - 0.03],
            color=tier["accent"], linewidth=2.8, zorder=6)
    
    # Content text
    curr_y = header_y - 0.38
    for text, is_header in tier["items"]:
        if is_header:
            curr_y -= 0.10
            ax.text(x + 0.14, curr_y, text, fontsize=8.8, fontweight='bold', color=tier["color"], zorder=5)
            curr_y -= 0.32
        else:
            ax.text(x + 0.20, curr_y, text, fontsize=7.9, color='#334155', zorder=5)
            curr_y -= 0.26

# Vẽ 4 mũi tên liên kết giữa các tầng
arrow_y = card_y + card_h / 2
connectors = [
    (0.5 + 2.65, 3.5, "PySpark\nIngest"),
    (3.5 + 2.65, 6.5, "Clean &\nEnrich"),
    (6.5 + 2.65, 9.5, "Spark MLlib\nTrain/Test"),
    (9.5 + 2.65, 12.5, "Decision\nRules")
]

for x1, x2, label in connectors:
    # Mũi tên chính
    arrow = patches.FancyArrowPatch(
        (x1 + 0.04, arrow_y), (x2 - 0.04, arrow_y),
        arrowstyle="-|>", mutation_scale=16,
        linewidth=2.2, color='#0284c7', zorder=10
    )
    ax.add_patch(arrow)
    
    # Nhãn mũi tên (badge)
    mid_x = (x1 + x2) / 2
    ax.text(mid_x, arrow_y + 0.42, label,
            fontsize=7.5, fontweight='bold', ha='center', va='center',
            color='#0369a1', zorder=11,
            bbox=dict(boxstyle="round,pad=0.22", facecolor='#e0f2fe', edgecolor='#38bdf8', linewidth=0.8))

# Chân trang ghi chú
ax.text(7.75, 0.24, "Mô hình kiến trúc Medallion Lakehouse - Đề tài 7: Credit Scoring & Loan Default Risk Engine (TS. Trần Mạnh Tường hướng dẫn)",
        fontsize=8.5, ha='center', va='center', color='#64748b')

plt.tight_layout()
fig.savefig(save_path, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches='tight')
plt.close(fig)
print(f"SAVED: {save_path}")
