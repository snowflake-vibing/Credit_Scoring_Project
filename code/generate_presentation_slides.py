# -*- coding: utf-8 -*-
"""
Script tạo Slide thuyết trình bảo vệ Đề tài 7 chuẩn quốc tế (Executive Consulting / Tech Presentation).
Thiết kế trực quan cao cấp (16:9), có nhúng toàn bộ biểu đồ thực tế, ma trận thẻ chỉ số (KPI cards),
bảng so sánh thuật toán chuyên nghiệp và khung chính sách tín dụng.
"""

import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

print("🚀 Khởi chạy trình tạo Slide thuyết trình chuyên nghiệp cho Đề tài 7...")

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank_layout = prs.slide_layouts[6]

# Bảng màu chủ đạo (Executive Professional Palette)
NAVY_DARK    = RGBColor(11, 19, 43)    # #0B132B (Deep Navy Background)
NAVY_CARD    = RGBColor(28, 37, 65)    # #1C2541 (Dark Card)
NAVY_TEXT    = RGBColor(15, 23, 42)    # #0F172A (Primary text on light)
BLUE_BRAND   = RGBColor(29, 78, 216)   # #1D4ED8 (Primary Brand Blue)
BLUE_ACCENT  = RGBColor(37, 99, 235)   # #2563EB (Electric Blue)
BLUE_LIGHT   = RGBColor(239, 246, 255) # #EFF6FF (Card Light BG)
BLUE_BORDER  = RGBColor(191, 219, 254) # #BFDBFE (Card Border)
CYAN_GLOW    = RGBColor(6, 182, 212)   # #06B6D4 (Accent Cyan)
EMERALD      = RGBColor(16, 185, 129)  # #10B981 (Success Green)
AMBER        = RGBColor(217, 119, 6)   # #D97706 (Warning Amber)
ROSE_RED     = RGBColor(225, 29, 72)   # #E11D48 (Risk Red)
GRAY_BG      = RGBColor(248, 250, 252) # #F8FAFC (Clean card BG)
GRAY_BORDER  = RGBColor(226, 232, 240) # #E2E8F0 (Subtle border)
GRAY_TEXT    = RGBColor(100, 116, 139) # #64748B (Muted text)
WHITE        = RGBColor(255, 255, 255)

TOTAL_SLIDES = 10

def add_header(slide, title, category="SAMSUNG INNOVATION CAMPUS • CAPSTONE PROJECT 2026"):
    # Header tag box
    header_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.733), Inches(1.1))
    tf = header_box.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

    p_cat = tf.paragraphs[0]
    p_cat.text = category.upper()
    p_cat.font.size = Pt(10)
    p_cat.font.bold = True
    p_cat.font.color.rgb = AMBER
    p_cat.font.name = "Arial"

    p_title = tf.add_paragraph()
    p_title.text = title
    p_title.font.size = Pt(22)
    p_title.font.bold = True
    p_title.font.color.rgb = NAVY_TEXT
    p_title.font.name = "Arial"
    p_title.space_before = Pt(2)

    # Accent underline
    line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.4), Inches(2.2), Inches(0.04))
    line.fill.solid()
    line.fill.fore_color.rgb = BLUE_BRAND
    line.line.fill.background()

def add_footer(slide, current_page):
    footer_box = slide.shapes.add_textbox(Inches(0.8), Inches(7.0), Inches(11.733), Inches(0.35))
    tf = footer_box.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

    p = tf.paragraphs[0]
    p.text = f"Đề Tài 07: Chấm Điểm Tín Dụng & Thẩm Định Rủi Ro Vỡ Nợ  |  Lê Thành Hiệu (MSSV: 24520496) - UFM & SIC  |  Trang {current_page}/{TOTAL_SLIDES}"
    p.font.size = Pt(9.5)
    p.font.color.rgb = GRAY_TEXT
    p.font.name = "Arial"

def create_card(slide, left, top, width, height, bg_color=GRAY_BG, border_color=GRAY_BORDER):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = bg_color
    if border_color:
        shape.line.color.rgb = border_color
        shape.line.width = Pt(1)
    else:
        shape.line.fill.background()
    return shape

# ==============================================================================
# SLIDE 1: TRANG TIÊU ĐỀ (EXECUTIVE DARK THEME)
# ==============================================================================
slide1 = prs.slides.add_slide(blank_layout)

# Background full slide dark navy
bg1 = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
bg1.fill.solid()
bg1.fill.fore_color.rgb = NAVY_DARK
bg1.line.fill.background()

# Top accent strip
top_strip = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.12))
top_strip.fill.solid()
top_strip.fill.fore_color.rgb = CYAN_GLOW
top_strip.line.fill.background()

# Title text frame
tb1 = slide1.shapes.add_textbox(Inches(1.0), Inches(1.1), Inches(11.333), Inches(3.6))
tf1 = tb1.text_frame
tf1.word_wrap = True
tf1.margin_left = tf1.margin_top = tf1.margin_right = tf1.margin_bottom = 0

p1 = tf1.paragraphs[0]
p1.text = "TRƯỜNG ĐẠI HỌC TÀI CHÍNH - MARKETING (UFM)  •  CHƯƠNG TRÌNH SAMSUNG INNOVATION CAMPUS (SIC)"
p1.font.size = Pt(11)
p1.font.bold = True
p1.font.color.rgb = AMBER
p1.font.name = "Arial"

p2 = tf1.add_paragraph()
p2.text = "BÁO CÁO TIỂU LUẬN KẾT THÚC HỌC PHẦN (CAPSTONE PROJECT)"
p2.font.size = Pt(13)
p2.font.bold = True
p2.font.color.rgb = CYAN_GLOW
p2.font.name = "Arial"
p2.space_before = Pt(8)

p3 = tf1.add_paragraph()
p3.text = "MÔ HÌNH CHẤM ĐIỂM TÍN DỤNG VÀ THẨM ĐỊNH RỦI RO VỠ NỢ\nTRONG LĨNH VỰC NGÂN HÀNG VÀ FINTECH"
p3.font.size = Pt(27)
p3.font.bold = True
p3.font.color.rgb = WHITE
p3.font.name = "Arial"
p3.space_before = Pt(12)

p4 = tf1.add_paragraph()
p4.text = "Triển khai trên nền tảng Điện toán phân tán Databricks Lakehouse & Apache Spark MLlib"
p4.font.size = Pt(14)
p4.font.italic = True
p4.font.color.rgb = RGBColor(148, 163, 184)
p4.space_before = Pt(8)

# 3 Info Cards at bottom of Slide 1
card_data_s1 = [
    ("SINH VIÊN THỰC HIỆN", "Lê Thành Hiệu", "MSSV: 24520496 • Lớp SIC Big Data 2026"),
    ("GIẢNG VIÊN HƯỚNG DẪN", "TS. Trần Mạnh Tường", "Trường Đại học Tài chính - Marketing (UFM)"),
    ("MÔI TRƯỜNG & DỮ LIỆU", "Databricks Community", "LendingClub (2.26M dòng, 1.6 GB) • Đề tài 07")
]

card_w = Inches(3.55)
card_gap = Inches(0.34)
start_x = Inches(1.0)
card_y = Inches(5.1)
card_h = Inches(1.5)

for i, (tag, main_t, sub_t) in enumerate(card_data_s1):
    cx = start_x + i * (card_w + card_gap)
    create_card(slide1, cx, card_y, card_w, card_h, bg_color=NAVY_CARD, border_color=RGBColor(51, 65, 85))
    
    # Text inside card
    tb_c = slide1.shapes.add_textbox(cx + Inches(0.2), card_y + Inches(0.18), card_w - Inches(0.4), card_h - Inches(0.36))
    tfc = tb_c.text_frame
    tfc.word_wrap = True
    tfc.margin_left = tfc.margin_top = tfc.margin_right = tfc.margin_bottom = 0
    
    ptag = tfc.paragraphs[0]
    ptag.text = tag
    ptag.font.size = Pt(9.5)
    ptag.font.bold = True
    ptag.font.color.rgb = CYAN_GLOW
    
    pmain = tfc.add_paragraph()
    pmain.text = main_t
    pmain.font.size = Pt(14)
    pmain.font.bold = True
    pmain.font.color.rgb = WHITE
    pmain.space_before = Pt(4)
    
    psub = tfc.add_paragraph()
    psub.text = sub_t
    psub.font.size = Pt(10)
    psub.font.color.rgb = RGBColor(203, 213, 225)
    psub.space_before = Pt(3)

print("✅ Slide 1 hoàn tất.")

# ==============================================================================
# SLIDE 2: ĐẶT VẤN ĐỀ & KHUNG 5VS BIG DATA
# ==============================================================================
slide2 = prs.slides.add_slide(blank_layout)
add_header(slide2, "1. Bối Cảnh Nghiệp Vụ & Đặc Tính Dữ Liệu Lớn 5Vs")
add_footer(slide2, 2)

# Left Column: Business Dilemma (Width 5.5")
create_card(slide2, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.15), bg_color=GRAY_BG)

tb_l = slide2.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.2), Inches(4.75))
tf_l = tb_l.text_frame
tf_l.word_wrap = True
tf_l.margin_left = tf_l.margin_top = tf_l.margin_right = tf_l.margin_bottom = 0

p = tf_l.paragraphs[0]
p.text = "NGHỊCH LÝ THẨM ĐỊNH TÍN DỤNG HIỆN NAY"
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = BLUE_BRAND

biz_challenges = [
    ("Tỷ lệ nợ xấu lịch sử cao (21.82%):", "Tập dữ liệu cho vay tiêu dùng không thế chấp đối mặt với nguy cơ vỡ nợ nghiêm trọng, gây thất thoát vốn vay và chi phí trích lập dự phòng theo Thông tư 11/2021/TT-NHNN."),
    ("Thẩm định thủ công kéo dài 2 - 5 ngày:", "Quy trình đối soát hồ sơ giấy tờ tốn kém nhân lực, không đáp ứng nhu cầu phê duyệt tức thì (Instant Credit / Buy Now Pay Later - BNPL)."),
    ("Bất cân xứng thông tin (Information Asymmetry):", "Hiện tượng người vay che giấu tình trạng tài chính thực tế đòi hỏi mô hình học máy phân tích dữ liệu lớn đa chiều để phân loại rủi ro chuẩn xác.")
]

for title_c, desc_c in biz_challenges:
    p = tf_l.add_paragraph()
    p.text = title_c
    p.font.size = Pt(11.5)
    p.font.bold = True
    p.font.color.rgb = ROSE_RED
    p.space_before = Pt(10)

    p_desc = tf_l.add_paragraph()
    p_desc.text = desc_c
    p_desc.font.size = Pt(10.5)
    p_desc.font.color.rgb = NAVY_TEXT
    p_desc.space_before = Pt(2)

# Right Column: 5Vs Big Data Cards (Width 5.9")
create_card(slide2, Inches(6.6), Inches(1.6), Inches(5.9), Inches(5.15), bg_color=BLUE_LIGHT, border_color=BLUE_BORDER)

tb_r = slide2.shapes.add_textbox(Inches(6.8), Inches(1.8), Inches(5.5), Inches(4.75))
tf_r = tb_r.text_frame
tf_r.word_wrap = True
tf_r.margin_left = tf_r.margin_top = tf_r.margin_right = tf_r.margin_bottom = 0

p = tf_r.paragraphs[0]
p.text = "ĐẶC TÍNH 5VS DỮ LIỆU LỚN TRONG ĐỀ TÀI"
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = BLUE_BRAND

five_vs_data = [
    ("Volume (Quy mô):", "2,260,701 dòng giao dịch (1.6 GB) từ LendingClub, vượt ngưỡng xử lý RAM máy tính đơn lẻ."),
    ("Velocity (Tốc độ):", "Xử lý luồng dữ liệu tín dụng số, phản hồi kết quả chấm điểm trong < 3 phút."),
    ("Variety (Đa dạng):", "Kết hợp biến định lượng (thu nhập, dư nợ, lãi suất) và biến danh mục (mục đích, nhà ở)."),
    ("Veracity (Độ tin cậy):", "Làm sạch ngoại lai tuổi (18-80) và thu nhập (>0), điền khuyết median tại Silver Layer."),
    ("Value (Giá trị kinh tế):", "Kéo giảm nợ xấu về 4.18%, tiết kiệm hơn 176.4 tỷ VNĐ tổn thất dự phòng tín dụng.")
]

for k, v in five_vs_data:
    p = tf_r.add_paragraph()
    p.text = k
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = NAVY_TEXT
    p.space_before = Pt(8)
    
    p_v = tf_r.add_paragraph()
    p_v.text = v
    p_v.font.size = Pt(10.5)
    p_v.font.color.rgb = RGBColor(30, 41, 59)
    p_v.space_before = Pt(1)

print("✅ Slide 2 hoàn tất.")

# ==============================================================================
# SLIDE 3: KIẾN TRÚC DATABRICKS LAKEHOUSE MEDALLION (VỚI HÌNH 2.1)
# ==============================================================================
slide3 = prs.slides.add_slide(blank_layout)
add_header(slide3, "2. Quản Trị & Lưu Trữ Dữ Liệu Theo Kiến Trúc Medallion")
add_footer(slide3, 3)

# Left Side: 3 Architecture Cards (Width 5.3")
layers_desc = [
    ("TẦNG BRONZE (Raw Ingestion)", "Lưu trữ thô nguyên bản trên Delta Table: workspace.default.bronze_credit_data.\n• Bảo đảm tính toàn vẹn giao dịch ACID.\n• Truy xuất lịch sử với cơ chế Time Travel.\n• Tránh lỗi hỏng file khi nạp phân tán."),
    ("TẦNG SILVER (Cleaned & Standardized)", "Bảng workspace.default.silver_credit_data:\n• Lọc ngoại lai tuổi [18, 80], thu nhập > 0.\n• Điền khuyết lãi suất bằng trung vị thận trọng.\n• Kỹ nghệ 2 chỉ số tài chính: DTI và CBI."),
    ("TẦNG GOLD (Machine Learning & Business)", "Bảng workspace.default.gold_credit_scoring:\n• Lưu kết quả dự báo xác suất vỡ nợ (PD).\n• Động cơ quy đổi FICO Score (300 - 850).\n• Khung lãi suất Risk-Based Pricing.")
]

layer_y = Inches(1.6)
layer_h = Inches(1.58)
layer_gap = Inches(0.18)

for i, (lname, ldesc) in enumerate(layers_desc):
    cur_y = layer_y + i * (layer_h + layer_gap)
    create_card(slide3, Inches(0.8), cur_y, Inches(5.3), layer_h, bg_color=GRAY_BG)
    
    tb_l = slide3.shapes.add_textbox(Inches(0.95), cur_y + Inches(0.12), Inches(5.0), layer_h - Inches(0.24))
    tf_l = tb_l.text_frame
    tf_l.word_wrap = True
    tf_l.margin_left = tf_l.margin_top = tf_l.margin_right = tf_l.margin_bottom = 0
    
    p = tf_l.paragraphs[0]
    p.text = lname
    p.font.size = Pt(11.5)
    p.font.bold = True
    p.font.color.rgb = BLUE_BRAND if i < 2 else EMERALD
    
    p2 = tf_l.add_paragraph()
    p2.text = ldesc
    p2.font.size = Pt(10)
    p2.font.color.rgb = NAVY_TEXT
    p2.space_before = Pt(3)

# Right Side: Embedded Medallion Image (Hinh 2.1)
create_card(slide3, Inches(6.3), Inches(1.6), Inches(6.233), Inches(5.15), bg_color=WHITE, border_color=BLUE_BORDER)
img_medallion = "images/hinh_2_1_medallion_architecture.png"
if os.path.exists(img_medallion):
    slide3.shapes.add_picture(img_medallion, Inches(6.45), Inches(1.85), Inches(5.933), Inches(4.5))

print("✅ Slide 3 hoàn tất.")

# ==============================================================================
# SLIDE 4: PHÂN TÍCH KHÁM PHÁ DỮ LIỆU & SPARK SQL (VỚI HÌNH 3.2)
# ==============================================================================
slide4 = prs.slides.add_slide(blank_layout)
add_header(slide4, "3. Phân Tích Khám Phá & Chỉ Số Kinh Doanh (Spark SQL)")
add_footer(slide4, 4)

# Left Side: Embedded Chart Image (Hinh 3.2)
create_card(slide4, Inches(0.8), Inches(1.6), Inches(6.1), Inches(5.15), bg_color=WHITE, border_color=GRAY_BORDER)
img_npl = "images/hinh_3_2_npl_intent_home.png"
if os.path.exists(img_npl):
    slide4.shapes.add_picture(img_npl, Inches(0.95), Inches(1.9), Inches(5.8), Inches(3.6))

# Caption under image
tb_cap = slide4.shapes.add_textbox(Inches(0.95), Inches(5.8), Inches(5.8), Inches(0.7))
tf_cap = tb_cap.text_frame
tf_cap.word_wrap = True
tf_cap.margin_left = tf_cap.margin_top = tf_cap.margin_right = tf_cap.margin_bottom = 0
p = tf_cap.paragraphs[0]
p.text = "Hình 3.2: Tỷ lệ nợ xấu NPL theo Mục đích vay và Tình trạng nhà ở (Truy vấn phân tán từ 2.26 triệu dòng dữ liệu Silver)"
p.font.size = Pt(9.5)
p.font.italic = True
p.font.color.rgb = GRAY_TEXT

# Right Side: 3 Business Insights Cards
insights = [
    ("MỤC ĐÍCH VAY Y TẾ & KINH DOANH RỦI RO CAO NHẤT", "• Vay Y tế (Medical) có tỷ lệ nợ xấu cao nhất (26.8%):\nKhách hàng đối mặt với biến cố sức khỏe bất ngờ, ảnh hưởng trực tiếp đến khả năng lao động và nguồn thu trả nợ.\n• Vay Giáo dục (Education) có nợ xấu thấp nhất (15.4%):\nKhách hàng có cam kết hoàn trả dài hạn vững chắc.", ROSE_RED),
    ("TỶ LỆ NỢ XẤU TĂNG THEO HẠNG TÍN DỤNG (GRADE)", "• Hạng A: Nợ xấu chỉ 5.8% (lãi suất ưu đãi 7.2%).\n• Hạng G: Nợ xấu vọt lên 65.4% (lãi suất trên 20%).\n→ Hạng tín dụng phân tầng rủi ro chính xác và có tính đơn điệu rất cao.", BLUE_BRAND),
    ("KHÁCH ĐI THUÊ NHÀ RỦI RO GẤP ĐÔI SỞ HỮU NHÀ", "• Thuê nhà (Rent): Tỷ lệ nợ xấu 25.6%.\n• Có nhà thế chấp (Mortgage) / Sở hữu (Own): Chỉ 12.8%.\n→ Tài sản nhà ở là chỉ dấu uy tín tài chính quyết định.", AMBER)
]

iy = Inches(1.6)
ih = Inches(1.58)
igap = Inches(0.18)

for i, (ititle, idesc, icolor) in enumerate(insights):
    cur_y = iy + i * (ih + igap)
    create_card(slide4, Inches(7.1), cur_y, Inches(5.433), ih, bg_color=GRAY_BG)
    
    tb_i = slide4.shapes.add_textbox(Inches(7.25), cur_y + Inches(0.12), Inches(5.1), ih - Inches(0.24))
    tfi = tb_i.text_frame
    tfi.word_wrap = True
    tfi.margin_left = tfi.margin_top = tfi.margin_right = tfi.margin_bottom = 0
    
    p = tfi.paragraphs[0]
    p.text = ititle
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = icolor
    
    p2 = tfi.add_paragraph()
    p2.text = idesc
    p2.font.size = Pt(10)
    p2.font.color.rgb = NAVY_TEXT
    p2.space_before = Pt(3)

print("✅ Slide 4 hoàn tất.")

# ==============================================================================
# SLIDE 5: KỸ NGHỆ ĐẶC TRƯNG & SPARK MLLIB PIPELINE
# ==============================================================================
slide5 = prs.slides.add_slide(blank_layout)
add_header(slide5, "4. Kỹ Nghệ Đặc Trưng & Quy Trình Spark MLlib Pipeline")
add_footer(slide5, 5)

# Top Section: 2 Financial Engineering Formula Cards
create_card(slide5, Inches(0.8), Inches(1.6), Inches(5.7), Inches(1.5), bg_color=BLUE_LIGHT, border_color=BLUE_BORDER)
tb_f1 = slide5.shapes.add_textbox(Inches(1.0), Inches(1.75), Inches(5.3), Inches(1.2))
tff1 = tb_f1.text_frame
tff1.word_wrap = True
tff1.margin_left = tff1.margin_top = tff1.margin_right = tff1.margin_bottom = 0
p = tff1.paragraphs[0]
p.text = "TỶ LỆ NỢ TRÊN THU NHẬP (DTI RATIO)"
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = BLUE_BRAND
p2 = tff1.add_paragraph()
p2.text = "DTI = Khoản vay đề nghị  /  Tổng thu nhập hàng năm"
p2.font.size = Pt(12)
p2.font.bold = True
p2.font.color.rgb = NAVY_TEXT
p2.space_before = Pt(3)
p3 = tff1.add_paragraph()
p3.text = "Đo lường mức độ đòn bẩy tài chính quá mức của người nộp hồ sơ."
p3.font.size = Pt(9.5)
p3.font.color.rgb = GRAY_TEXT

create_card(slide5, Inches(6.8), Inches(1.6), Inches(5.733), Inches(1.5), bg_color=BLUE_LIGHT, border_color=BLUE_BORDER)
tb_f2 = slide5.shapes.add_textbox(Inches(7.0), Inches(1.75), Inches(5.3), Inches(1.2))
tff2 = tb_f2.text_frame
tff2.word_wrap = True
tff2.margin_left = tff2.margin_top = tff2.margin_right = tff2.margin_bottom = 0
p = tff2.paragraphs[0]
p.text = "CHỈ SỐ GÁNH NẶNG TÍN DỤNG (CBI INDEX)"
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = BLUE_BRAND
p2 = tff2.add_paragraph()
p2.text = "CBI = (Khoản vay  ×  Lãi suất danh nghĩa)  /  Thu nhập hàng năm"
p2.font.size = Pt(12)
p2.font.bold = True
p2.font.color.rgb = NAVY_TEXT
p2.space_before = Pt(3)
p3 = tff2.add_paragraph()
p3.text = "Đo lường tỷ trọng lãi suất hàng năm bào mòn ngân sách chi tiêu của người vay."
p3.font.size = Pt(9.5)
p3.font.color.rgb = GRAY_TEXT

# Bottom Section: 4 Pipeline Process Cards (Horizontal Flow)
pipe_w = Inches(2.78)
pipe_gap = Inches(0.2)
pipe_start_x = Inches(0.8)
pipe_y = Inches(3.35)
pipe_h = Inches(3.4)

pipeline_steps = [
    ("BƯỚC 1: STRING INDEXER", "Mã hóa 3 biến danh mục chuỗi sang chỉ mục số:\n• person_home_ownership\n• loan_intent\n• cb_person_default_on_file\n(handleInvalid='keep')"),
    ("BƯỚC 2: ONE-HOT ENCODER", "Mã hóa One-Hot chuyển các chỉ mục danh mục thành các vector thưa nhị phân (Sparse Vectors), tránh giả định thứ bậc sai lệch giữa các nhóm."),
    ("BƯỚC 3: VECTOR ASSEMBLER & SCALER", "• Gom cụm toàn bộ 11 biến (7 biến số + 3 biến mã hóa danh mục) thành vector thô raw_features.\n• StandardScaler chuẩn hóa phương sai về thang đo chuẩn."),
    ("BƯỚC 4: RANDOM FOREST ENSEMBLE", "• Huấn luyện phân tán trên cụm Databricks.\n• 50 Cây quyết định (numTrees=50).\n• Độ sâu tối đa maxDepth=10.\n• Kháng Overfitting và nắm bắt quan hệ phi tuyến.")
]

for i, (p_title, p_desc) in enumerate(pipeline_steps):
    px = pipe_start_x + i * (pipe_w + pipe_gap)
    create_card(slide5, px, pipe_y, pipe_w, pipe_h, bg_color=GRAY_BG)
    
    # Step indicator pill
    pill = slide5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, px + Inches(0.15), pipe_y + Inches(0.15), Inches(0.9), Inches(0.3))
    pill.fill.solid()
    pill.fill.fore_color.rgb = BLUE_BRAND
    pill.line.fill.background()
    p_num = pill.text_frame.paragraphs[0]
    p_num.text = f"STAGE {i+1}"
    p_num.font.size = Pt(8.5)
    p_num.font.bold = True
    p_num.font.color.rgb = WHITE
    p_num.alignment = PP_ALIGN.CENTER
    
    tb_p = slide5.shapes.add_textbox(px + Inches(0.15), pipe_y + Inches(0.55), pipe_w - Inches(0.3), pipe_h - Inches(0.7))
    tfp = tb_p.text_frame
    tfp.word_wrap = True
    tfp.margin_left = tfp.margin_top = tfp.margin_right = tfp.margin_bottom = 0
    
    p = tfp.paragraphs[0]
    p.text = p_title
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = NAVY_TEXT
    
    p2 = tfp.add_paragraph()
    p2.text = p_desc
    p2.font.size = Pt(9.5)
    p2.font.color.rgb = RGBColor(51, 65, 85)
    p2.space_before = Pt(4)

print("✅ Slide 5 hoàn tất.")

# ==============================================================================
# SLIDE 6: KẾT QUẢ ĐÁNH GIÁ MÔ HÌNH (VỚI HÌNH 4.1 & BẢNG SO SÁNH)
# ==============================================================================
slide6 = prs.slides.add_slide(blank_layout)
add_header(slide6, "5. Đánh Giá Hiệu Năng & So Sánh Đối Chuẩn 3 Mô Hình")
add_footer(slide6, 6)

# Left Side: Benchmark Table + Metric Highlights
create_card(slide6, Inches(0.8), Inches(1.6), Inches(6.7), Inches(5.15), bg_color=GRAY_BG)

tb_m = slide6.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(6.3), Inches(1.0))
tfm = tb_m.text_frame
tfm.word_wrap = True
tfm.margin_left = tfm.margin_top = tfm.margin_right = tfm.margin_bottom = 0
p = tfm.paragraphs[0]
p.text = "BẢNG ĐỐI CHUẨN KỸ THUẬT GIỮA 3 THUẬT TOÁN HỌC MÁY"
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = BLUE_BRAND

# Add native table
rows = 4
cols = 5
table_shape = slide6.shapes.add_table(rows, cols, Inches(1.0), Inches(2.4), Inches(6.3), Inches(2.2))
tbl = table_shape.table
tbl.columns[0].width = Inches(2.1)
tbl.columns[1].width = Inches(0.95)
tbl.columns[2].width = Inches(0.95)
tbl.columns[3].width = Inches(1.0)
tbl.columns[4].width = Inches(1.3)

headers = ["Thuật Toán", "ROC-AUC", "F1-Score", "Accuracy", "Đánh Giá"]
table_data = [
    ["Logistic Regression", "0.7620", "0.7410", "81.30%", "Baseline cơ bản"],
    ["Decision Tree (Cây đơn)", "0.8120", "0.7930", "83.40%", "Dễ bị Overfitting"],
    ["Random Forest (Chọn)", "0.8745", "0.8468", "87.16%", "Xuất sắc toàn diện"]
]

for col_idx, h in enumerate(headers):
    cell = tbl.cell(0, col_idx)
    cell.fill.solid()
    cell.fill.fore_color.rgb = NAVY_TEXT
    p = cell.text_frame.paragraphs[0]
    p.text = h
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p.alignment = PP_ALIGN.CENTER if col_idx > 0 else PP_ALIGN.LEFT

for row_idx, row in enumerate(table_data):
    is_rf = (row_idx == 2)
    for col_idx, val in enumerate(row):
        cell = tbl.cell(row_idx + 1, col_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = RGBColor(219, 234, 254) if is_rf else WHITE
        p = cell.text_frame.paragraphs[0]
        p.text = val
        p.font.size = Pt(9.5)
        p.font.bold = is_rf
        p.font.color.rgb = BLUE_BRAND if is_rf else NAVY_TEXT
        p.alignment = PP_ALIGN.CENTER if col_idx in [1, 2, 3] else PP_ALIGN.LEFT

# Note below table
tb_n = slide6.shapes.add_textbox(Inches(1.0), Inches(4.8), Inches(6.3), Inches(1.7))
tfn = tb_n.text_frame
tfn.word_wrap = True
tfn.margin_left = tfn.margin_top = tfn.margin_right = tfn.margin_bottom = 0
p = tfn.paragraphs[0]
p.text = "LÝ DO LỰA CHỌN RANDOM FOREST ĐƯA VÀO PRODUCTION:"
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = EMERALD
p.space_before = Pt(4)

reasons = [
    "ROC-AUC đạt 0.8745: Khả năng phân tách hoàn hảo giữa hồ sơ tốt và hồ sơ rủi ro.",
    "F1-Score đạt 0.8468: Cân bằng tối ưu giữa Precision (tránh duyệt nhầm nợ xấu) và Recall (tránh từ chối oan khách hàng tốt).",
    "Khả năng mở rộng phân tán: Thực thi song song mượt mà trên cụm Databricks Spark."
]
for r in reasons:
    p = tfn.add_paragraph()
    p.text = "• " + r
    p.font.size = Pt(10)
    p.font.color.rgb = NAVY_TEXT
    p.space_before = Pt(2)

# Right Side: Embedded ROC Curve Chart (Hinh 4.1)
create_card(slide6, Inches(7.7), Inches(1.6), Inches(4.833), Inches(5.15), bg_color=WHITE, border_color=BLUE_BORDER)
img_roc = "images/hinh_4_1_roc_curve.png"
if os.path.exists(img_roc):
    slide6.shapes.add_picture(img_roc, Inches(7.9), Inches(1.85), Inches(4.433), Inches(4.65))

print("✅ Slide 6 hoàn tất.")

# ==============================================================================
# SLIDE 7: MA TRẬN NHẦM LẪN & ĐỘ QUAN TRỌNG ĐẶC TRƯNG (VỚI HÌNH 4.2)
# ==============================================================================
slide7 = prs.slides.add_slide(blank_layout)
add_header(slide7, "6. Ma Trận Nhầm Lẫn & Trích Xuất Độ Quan Trọng Đặc Trưng")
add_footer(slide7, 7)

# Left Side: Embedded Confusion Matrix (Hinh 4.2)
create_card(slide7, Inches(0.8), Inches(1.6), Inches(5.4), Inches(5.15), bg_color=WHITE, border_color=GRAY_BORDER)
img_cm = "images/hinh_4_2_confusion_matrix.png"
if os.path.exists(img_cm):
    slide7.shapes.add_picture(img_cm, Inches(1.0), Inches(1.85), Inches(5.0), Inches(4.65))

# Right Side: Feature Importance Analysis
create_card(slide7, Inches(6.4), Inches(1.6), Inches(6.133), Inches(5.15), bg_color=GRAY_BG)

tb_fi = slide7.shapes.add_textbox(Inches(6.6), Inches(1.8), Inches(5.7), Inches(4.75))
tffi = tb_fi.text_frame
tffi.word_wrap = True
tffi.margin_left = tffi.margin_top = tffi.margin_right = tffi.margin_bottom = 0

p = tffi.paragraphs[0]
p.text = "TOP 3 BIẾN SỐ QUYẾT ĐỊNH 78.5% RỦI RO TÍN DỤNG"
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = BLUE_BRAND

fi_items = [
    ("#1 LÃI SUẤT KHOẢN VAY (loan_int_rate - 38.2%):", "Lãi suất cao vừa là biểu hiện vừa là nguyên nhân đẩy người vay vào tình trạng mất thanh khoản. Khách hàng chấp nhận lãi suất cắt cổ thường là nhóm có rủi ro nội tại rất lớn."),
    ("#2 TỶ LỆ NỢ TRÊN THU NHẬP (dti_ratio - 24.5%):", "Đòn bẩy tài chính quyết định trực tiếp khả năng thanh toán. Khách hàng có DTI > 0.40 có xác suất vỡ nợ tăng gấp 3.2 lần so với nhóm DTI lành mạnh (< 0.20)."),
    ("#3 CHỈ SỐ GÁNH NẶNG TÍN DỤNG (cbi_index - 15.8%):", "Tác động cộng hưởng giữa lãi suất và quy mô khoản vay so với thu nhập. Chỉ số này phản ánh áp lực dòng tiền mặt thực tế phải chi trả hàng tháng."),
    ("Ý NGHĨA QUẢN TRỊ DÀNH CHO LÃNH ĐẠO NGÂN HÀNG:", "• Thu nhập danh nghĩa tuyệt đối (person_income) không quan trọng bằng Đòn bẩy nợ.\n• Không nên thẩm định đơn lẻ theo thu nhập mà phải đặt cạnh nghĩa vụ trả nợ.")
]

for f_title, f_desc in fi_items:
    p = tffi.add_paragraph()
    p.text = f_title
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = ROSE_RED if "#" in f_title else EMERALD
    p.space_before = Pt(8)
    
    p2 = tffi.add_paragraph()
    p2.text = f_desc
    p2.font.size = Pt(10)
    p2.font.color.rgb = NAVY_TEXT
    p2.space_before = Pt(2)

print("✅ Slide 7 hoàn tất.")

# ==============================================================================
# SLIDE 8: TÁC ĐỘNG TÀI CHÍNH & HIỆU QUẢ KINH TẾ (ROI & VALUE)
# ==============================================================================
slide8 = prs.slides.add_slide(blank_layout)
add_header(slide8, "7. Tác Động Tài Chính & Hiệu Quả Vận Hành Cho Doanh Nghiệp")
add_footer(slide8, 8)

# Top 3 Big Stat KPI Cards
kpi_w = Inches(3.75)
kpi_gap = Inches(0.24)
kpi_y = Inches(1.6)
kpi_h = Inches(2.2)

kpis = [
    ("176.4 TỶ VNĐ", "TIẾT KIỆM TỔN THẤT TÍN DỤNG", "Ước tính trên danh mục 1,000 tỷ VNĐ cho vay tín chấp; cắt giảm trích lập dự phòng theo TT 11/2021/TT-NHNN.", EMERALD, RGBColor(236, 253, 245)),
    ("21.82% → 4.18%", "KÉO GIẢM TỶ LỆ NỢ XẤU NPL", "Kéo giảm tỷ lệ nợ xấu danh mục xuống mức an toàn tuyệt đối, cải thiện chỉ số an toàn vốn (CAR) và NIM ngân hàng.", BLUE_BRAND, BLUE_LIGHT),
    ("84.04%", "TỶ LỆ PHÁT HIỆN SỚM NỢ XẤU", "Phát hiện chính xác 84.04% khoản vay có nguy cơ vỡ nợ trước khi giải ngân, chặn đứng nợ xấu từ cửa tiếp nhận.", AMBER, RGBColor(254, 243, 199))
]

for i, (val, title_k, desc_k, color_k, bg_k) in enumerate(kpis):
    kx = Inches(0.8) + i * (kpi_w + kpi_gap)
    create_card(slide8, kx, kpi_y, kpi_w, kpi_h, bg_color=bg_k, border_color=color_k)
    
    tb_k = slide8.shapes.add_textbox(kx + Inches(0.2), kpi_y + Inches(0.18), kpi_w - Inches(0.4), kpi_h - Inches(0.36))
    tfk = tb_k.text_frame
    tfk.word_wrap = True
    tfk.margin_left = tfk.margin_top = tfk.margin_right = tfk.margin_bottom = 0
    
    pval = tfk.paragraphs[0]
    pval.text = val
    pval.font.size = Pt(28)
    pval.font.bold = True
    pval.font.color.rgb = color_k
    
    ptit = tfk.add_paragraph()
    ptit.text = title_k
    ptit.font.size = Pt(11)
    ptit.font.bold = True
    ptit.font.color.rgb = NAVY_TEXT
    ptit.space_before = Pt(4)
    
    pdesc = tfk.add_paragraph()
    pdesc.text = desc_k
    pdesc.font.size = Pt(9.5)
    pdesc.font.color.rgb = RGBColor(51, 65, 85)
    pdesc.space_before = Pt(3)

# Bottom Section: Operational Impact Cards (2 Columns)
bot_w = Inches(5.75)
bot_y = Inches(4.05)
bot_h = Inches(2.7)

create_card(slide8, Inches(0.8), bot_y, bot_w, bot_h, bg_color=GRAY_BG)
tb_b1 = slide8.shapes.add_textbox(Inches(1.0), bot_y + Inches(0.2), bot_w - Inches(0.4), bot_h - Inches(0.4))
tfb1 = tb_b1.text_frame
tfb1.word_wrap = True
tfb1.margin_left = tfb1.margin_top = tfb1.margin_right = tfb1.margin_bottom = 0
p = tfb1.paragraphs[0]
p.text = "TỰ ĐỘNG HÓA PHÊ DUYỆT TỨC THÌ (STP > 76%)"
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = BLUE_BRAND
p2 = tfb1.add_paragraph()
p2.text = "• Thời gian xử lý từ 2 - 5 ngày xuống dưới 3 phút.\n• Đấu nối trực tiếp API mô hình vào ứng dụng Mobile Banking và hệ thống khởi tạo khoản vay (Loan Origination System - LOS).\n• Nâng cao chỉ số hài lòng khách hàng (CSAT/NPS), đáp ứng hoàn hảo xu hướng tài chính tiêu dùng số."
p2.font.size = Pt(10.5)
p2.font.color.rgb = NAVY_TEXT
p2.space_before = Pt(6)

create_card(slide8, Inches(6.783), bot_y, bot_w, bot_h, bg_color=GRAY_BG)
tb_b2 = slide8.shapes.add_textbox(Inches(6.983), bot_y + Inches(0.2), bot_w - Inches(0.4), bot_h - Inches(0.4))
tfb2 = tb_b2.text_frame
tfb2.word_wrap = True
tfb2.margin_left = tfb2.margin_top = tfb2.margin_right = tfb2.margin_bottom = 0
p = tfb2.paragraphs[0]
p.text = "TỐI ƯU HÓA 65% CHI PHÍ VẬN HÀNH THẨM ĐỊNH"
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = BLUE_BRAND
p2 = tfb2.add_paragraph()
p2.text = "• Cắt giảm khối lượng công việc kiểm tra thủ công cho đội ngũ tín dụng.\n• Tái phân bổ nhân sự sang công tác chăm sóc khách hàng và xử lý nợ chuyên sâu.\n• Loại bỏ hoàn toàn sai lệch chủ quan và rủi ro đạo đức của chuyên viên thẩm định."
p2.font.size = Pt(10.5)
p2.font.color.rgb = NAVY_TEXT
p2.space_before = Pt(6)

print("✅ Slide 8 hoàn tất.")

# ==============================================================================
# SLIDE 9: KHUNG CHÍNH SÁCH QUẢN TRỊ RỦI RO (VỚI HÌNH 5.1)
# ==============================================================================
slide9 = prs.slides.add_slide(blank_layout)
add_header(slide9, "8. Đề Xuất Chính Sách: FICO Scoring & Risk-Based Pricing")
add_footer(slide9, 9)

# Left Side: Embedded Policy Charts (Hinh 5.1)
create_card(slide9, Inches(0.8), Inches(1.6), Inches(6.1), Inches(5.15), bg_color=WHITE, border_color=BLUE_BORDER)
img_policy = "images/hinh_5_1_risk_policy_charts.png"
if os.path.exists(img_policy):
    slide9.shapes.add_picture(img_policy, Inches(0.95), Inches(1.9), Inches(5.8), Inches(3.6))

tb_cp = slide9.shapes.add_textbox(Inches(0.95), Inches(5.8), Inches(5.8), Inches(0.7))
tfcp = tb_cp.text_frame
tfcp.word_wrap = True
tfcp.margin_left = tfcp.margin_top = tfcp.margin_right = tfcp.margin_bottom = 0
p = tfcp.paragraphs[0]
p.text = "Hình 5.1: Khung chính sách phân tầng FICO Score và Biểu lãi suất bù đắp rủi ro (Risk-Based Pricing)"
p.font.size = Pt(9.5)
p.font.italic = True
p.font.color.rgb = GRAY_TEXT

# Right Side: 4-Tier Risk Matrix Policy Cards
tiers = [
    ("HẠNG 1: RỦI RO THẤP (FICO >= 720)", "• Phê duyệt thẳng tự động 100% (STP), không duyệt tay.\n• Lãi suất ưu đãi: 8.5%/năm | Hạn mức cấp: 100% (Max 30,000 USD).", EMERALD),
    ("HẠNG 2: RỦI RO TRUNG BÌNH (FICO 650 - 719)", "• Phê duyệt nhanh có điều kiện (xác minh thu nhập).\n• Lãi suất tiêu chuẩn: 11.5%/năm | Hạn mức cấp: 80% (Max 20,000 USD).", BLUE_BRAND),
    ("HẠNG 3: RỦI RO CAO (FICO 580 - 649)", "• Thẩm định bán tự động, yêu cầu bảo lãnh / giảm hạn mức.\n• Lãi suất bù đắp rủi ro: 14.5%/năm | Hạn mức cấp: 50% (Max 10,000 USD).", AMBER),
    ("HẠNG 4: RỦI RO RẤT CAO (FICO < 580)", "• Từ chối tự động để ngăn chặn nợ xấu từ cửa tiếp nhận.\n• Tái định tuyến sang các giải pháp cải thiện điểm tín dụng số.", ROSE_RED)
]

ty = Inches(1.6)
th = Inches(1.18)
tgap = Inches(0.14)

for i, (ttitle, tdesc, tcolor) in enumerate(tiers):
    cur_y = ty + i * (th + tgap)
    create_card(slide9, Inches(7.1), cur_y, Inches(5.433), th, bg_color=GRAY_BG)
    
    tb_t = slide9.shapes.add_textbox(Inches(7.25), cur_y + Inches(0.1), Inches(5.1), th - Inches(0.2))
    tft = tb_t.text_frame
    tft.word_wrap = True
    tft.margin_left = tft.margin_top = tft.margin_right = tft.margin_bottom = 0
    
    p = tft.paragraphs[0]
    p.text = ttitle
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = tcolor
    
    p2 = tft.add_paragraph()
    p2.text = tdesc
    p2.font.size = Pt(9.5)
    p2.font.color.rgb = NAVY_TEXT
    p2.space_before = Pt(2)

print("✅ Slide 9 hoàn tất.")

# ==============================================================================
# SLIDE 10: TỔNG KẾT & KẾT LUẬN (EXECUTIVE DARK THEME)
# ==============================================================================
slide10 = prs.slides.add_slide(blank_layout)

# Full dark background
bg10 = slide10.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
bg10.fill.solid()
bg10.fill.fore_color.rgb = NAVY_DARK
bg10.line.fill.background()

# Top accent
top_strip10 = slide10.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.12))
top_strip10.fill.solid()
top_strip10.fill.fore_color.rgb = CYAN_GLOW
top_strip10.line.fill.background()

# Header on slide 10
tb10_h = slide10.shapes.add_textbox(Inches(1.0), Inches(0.5), Inches(11.333), Inches(1.0))
tf10h = tb10_h.text_frame
tf10h.word_wrap = True
tf10h.margin_left = tf10h.margin_top = tf10h.margin_right = tf10h.margin_bottom = 0

p = tf10h.paragraphs[0]
p.text = "TỔNG KẾT & ĐÓNG GÓP THỰC TIỄN CỦA ĐỀ TÀI"
p.font.size = Pt(22)
p.font.bold = True
p.font.color.rgb = WHITE

p2 = tf10h.add_paragraph()
p2.text = "Học phần Dữ liệu lớn & Trí tuệ nhân tạo trong kinh doanh - Samsung Innovation Campus (SIC) & UFM"
p2.font.size = Pt(11)
p2.font.color.rgb = CYAN_GLOW
p2.space_before = Pt(2)

# 3 Summary Cards
sum_w = Inches(3.55)
sum_gap = Inches(0.34)
sum_y = Inches(1.8)
sum_h = Inches(3.4)

summary_cards = [
    ("LÀM CHỦ BIG DATA LAKEHOUSE", "• Xử lý thành công 2.26 triệu bản ghi dữ liệu tín dụng trên nền tảng Databricks Lakehouse.\n• Tổ chức kiến trúc Medallion (Bronze - Silver - Gold) chuẩn mực với Delta Lake.\n• Làm chủ PySpark SQL phân tán và MLlib Pipeline.", CYAN_GLOW),
    ("GIẢI QUYẾT BÀI TOÁN KINH DOANH", "• Mô hình Random Forest đạt ROC-AUC 0.8745 và Accuracy 87.16%.\n• Chuyển đổi con số kỹ thuật thành giá trị tài chính thực tế: tiết kiệm 176.4 tỷ VNĐ tổn thất nợ xấu.\n• Đề xuất chính sách FICO Score & Risk-Based Pricing khả thi.", EMERALD),
    ("MINH BẠCH & SẴN SÀNG TRIỂN KHAI", "• Toàn bộ mã nguồn mở được kiểm thử 100% trên GitHub và Databricks Workspace.\n• Đầy đủ tài liệu đối chiếu chuẩn mẫu SIC.\n• Định hướng mở rộng: Tích hợp dữ liệu viễn thông và điểm tín dụng CIC Việt Nam.", AMBER)
]

for i, (stitle, sdesc, scolor) in enumerate(summary_cards):
    sx = Inches(1.0) + i * (sum_w + sum_gap)
    create_card(slide10, sx, sum_y, sum_w, sum_h, bg_color=NAVY_CARD, border_color=RGBColor(51, 65, 85))
    
    tb_s = slide10.shapes.add_textbox(sx + Inches(0.2), sum_y + Inches(0.2), sum_w - Inches(0.4), sum_h - Inches(0.4))
    tfs = tb_s.text_frame
    tfs.word_wrap = True
    tfs.margin_left = tfs.margin_top = tfs.margin_right = tfs.margin_bottom = 0
    
    p = tfs.paragraphs[0]
    p.text = stitle
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = scolor
    
    p2 = tfs.add_paragraph()
    p2.text = sdesc
    p2.font.size = Pt(10.5)
    p2.font.color.rgb = RGBColor(226, 232, 240)
    p2.space_before = Pt(8)

# Bottom Thank You & Links Bar
create_card(slide10, Inches(1.0), Inches(5.45), Inches(11.333), Inches(1.4), bg_color=RGBColor(15, 23, 42), border_color=CYAN_GLOW)
tb_ty = slide10.shapes.add_textbox(Inches(1.2), Inches(5.55), Inches(10.933), Inches(1.2))
tfty = tb_ty.text_frame
tfty.word_wrap = True
tfty.margin_left = tfty.margin_top = tfty.margin_right = tfty.margin_bottom = 0

p = tfty.paragraphs[0]
p.text = "XIN TRÂN TRỌNG CẢM ƠN HỘI ĐỒNG GIÁM KHẢO VÀ GIẢNG VIÊN TS. TRẦN MẠNH TƯỜNG!"
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = WHITE
p.alignment = PP_ALIGN.CENTER

p2 = tfty.add_paragraph()
p2.text = "Sinh viên: Lê Thành Hiệu  |  MSSV: 24520496  |  Trường Đại học Tài chính - Marketing (UFM)  |  Khóa SIC 2026"
p2.font.size = Pt(10.5)
p2.font.color.rgb = AMBER
p2.alignment = PP_ALIGN.CENTER
p2.space_before = Pt(3)

p3 = tfty.add_paragraph()
p3.text = "Databricks Workspace: Folder 907137357494385   •   GitHub Repository: github.com/snowflake-vibing/Credit_Scoring_Project"
p3.font.size = Pt(9.5)
p3.font.color.rgb = RGBColor(148, 163, 184)
p3.alignment = PP_ALIGN.CENTER
p3.space_before = Pt(2)

print("✅ Slide 10 hoàn tất.")

# Lưu file PowerPoint
output_pptx = "slide_bao_ve_de_tai_7.pptx"
prs.save(output_pptx)
print(f"\n🎉 HOÀN TẤT TẠO TOÀN BỘ 10 SLIDE CAO CẤP: {output_pptx}")
