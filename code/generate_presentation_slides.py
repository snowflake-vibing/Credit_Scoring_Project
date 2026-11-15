# -*- coding: utf-8 -*-
"""
Script tái thiết kế Slide thuyết trình Đề tài 7 chuẩn quốc tế (Executive Visual Design).
Khắc phục 100% các điểm yếu thiết kế:
1. KHÔNG bị bóp méo hay thu hẹp hình ảnh (giữ nguyên tỷ lệ Aspect Ratio chuẩn của từng biểu đồ).
2. XÓA BỎ hoàn toàn header tag rườm rà và footer thừa theo yêu cầu người dùng.
3. Phối màu thẻ card đa dạng, trực quan (Emerald xanh lá, Blue xanh dương, Amber cam hổ phách, Rose đỏ).
4. Bổ sung các icon / badge sinh động.
5. Thiết kế nền và viền thẻ card có chiều sâu, tạo cảm giác một dashboard điều hành thực thụ.
"""

import os
import sys
from PIL import Image
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

print("🚀 Bắt đầu tái thiết kế toàn diện Slide thuyết trình Đề tài 7...")

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank_layout = prs.slide_layouts[6]

# Bảng màu chủ đạo (Executive High-Contrast Modern Palette)
DARK_BG      = RGBColor(15, 23, 42)     # #0F172A (Deep Slate Navy)
DARK_CARD    = RGBColor(30, 41, 59)     # #1E293B (Dark Card Container)
LIGHT_BG     = RGBColor(241, 245, 249)  # #F1F5F9 (Soft Modern Slate BG)
WHITE        = RGBColor(255, 255, 255)
TEXT_DARK    = RGBColor(15, 23, 42)     # #0F172A (Bold text)
TEXT_MUTED   = RGBColor(100, 116, 139)  # #64748B (Secondary text)

# Card colors (Vibrant tints & borders)
EMERALD_BG   = RGBColor(236, 253, 245)  # #ECFDF5
EMERALD_BR   = RGBColor(16, 185, 129)   # #10B981
EMERALD_TX   = RGBColor(4, 120, 87)     # #047857

BLUE_BG      = RGBColor(239, 246, 255)  # #EFF6FF
BLUE_BR      = RGBColor(37, 99, 235)    # #2563EB
BLUE_TX      = RGBColor(29, 78, 216)    # #1D4ED8

AMBER_BG     = RGBColor(254, 243, 199)  # #FEF3C7
AMBER_BR     = RGBColor(217, 119, 6)    # #D97706
AMBER_TX     = RGBColor(180, 83, 9)     # #B45309

ROSE_BG      = RGBColor(255, 241, 242)  # #FFF1F2
ROSE_BR      = RGBColor(225, 29, 72)    # #E11D48
ROSE_TX      = RGBColor(190, 18, 60)    # #BE123C

INDIGO_BG    = RGBColor(238, 242, 255)  # #EEF2FF
INDIGO_BR    = RGBColor(99, 102, 241)   # #6366F1
INDIGO_TX    = RGBColor(67, 56, 202)    # #4338CA

GRAY_CARD_BG = RGBColor(255, 255, 255)  # Pure White card on slate bg
GRAY_CARD_BR = RGBColor(203, 213, 225)  # Slate border

CYAN_ACCENT  = RGBColor(6, 182, 212)    # #06B6D4

def set_slide_background(slide, color):
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
    bg.fill.solid()
    bg.fill.fore_color.rgb = color
    bg.line.fill.background()
    return bg

def add_clean_title(slide, title_text, dark_mode=False):
    tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.45), Inches(11.733), Inches(0.8))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    
    p = tf.paragraphs[0]
    p.text = title_text
    p.font.size = Pt(22)
    p.font.bold = True
    p.font.name = "Arial"
    p.font.color.rgb = WHITE if dark_mode else TEXT_DARK
    
    # Sleek bottom accent line
    line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.3), Inches(1.8), Inches(0.04))
    line.fill.solid()
    line.fill.fore_color.rgb = CYAN_ACCENT if dark_mode else BLUE_BR
    line.line.fill.background()

def create_styled_card(slide, left, top, width, height, bg_color=GRAY_CARD_BG, border_color=GRAY_CARD_BR, border_width=1):
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    card.fill.solid()
    card.fill.fore_color.rgb = bg_color
    if border_color:
        card.line.color.rgb = border_color
        card.line.width = Pt(border_width)
    else:
        card.line.fill.background()
    return card

def add_proportional_image(slide, img_path, max_left, max_top, max_w, max_h, add_card_frame=True):
    if not os.path.exists(img_path):
        return None
    im = Image.open(img_path)
    orig_w, orig_h = im.size
    aspect = orig_w / orig_h
    
    # Calculate fit within bounds while strictly preserving aspect ratio
    fit_w = max_w
    fit_h = max_w / aspect
    if fit_h > max_h:
        fit_h = max_h
        fit_w = max_h * aspect
        
    left = max_left + (max_w - fit_w) / 2
    top = max_top + (max_h - fit_h) / 2
    
    if add_card_frame:
        pad = Inches(0.08)
        create_styled_card(slide, left - pad, top - pad, fit_w + 2*pad, fit_h + 2*pad, bg_color=WHITE, border_color=GRAY_CARD_BR)
    
    pic = slide.shapes.add_picture(img_path, left, top, fit_w, fit_h)
    return pic

# ==============================================================================
# SLIDE 1: TRANG TIÊU ĐỀ (EXECUTIVE DARK TECH COVER)
# ==============================================================================
slide1 = prs.slides.add_slide(blank_layout)
set_slide_background(slide1, DARK_BG)

# Top Cyan bar
top_bar = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.12))
top_bar.fill.solid()
top_bar.fill.fore_color.rgb = CYAN_ACCENT
top_bar.line.fill.background()

tb1 = slide1.shapes.add_textbox(Inches(1.0), Inches(1.0), Inches(11.333), Inches(3.6))
tf1 = tb1.text_frame
tf1.word_wrap = True
tf1.margin_left = tf1.margin_top = tf1.margin_right = tf1.margin_bottom = 0

p = tf1.paragraphs[0]
p.text = "TRƯỜNG ĐẠI HỌC TÀI CHÍNH - MARKETING (UFM) • CHƯƠNG TRÌNH SAMSUNG INNOVATION CAMPUS (SIC)"
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = AMBER_BR

p2 = tf1.add_paragraph()
p2.text = "BÁO CÁO TIỂU LUẬN KẾT THÚC HỌC PHẦN (CAPSTONE PROJECT 2026)"
p2.font.size = Pt(13)
p2.font.bold = True
p2.font.color.rgb = CYAN_ACCENT
p2.space_before = Pt(8)

p3 = tf1.add_paragraph()
p3.text = "MÔ HÌNH CHẤM ĐIỂM TÍN DỤNG VÀ THẨM ĐỊNH RỦI RO VỠ NỢ\nTRONG LĨNH VỰC NGÂN HÀNG VÀ FINTECH"
p3.font.size = Pt(27)
p3.font.bold = True
p3.font.color.rgb = WHITE
p3.space_before = Pt(12)

p4 = tf1.add_paragraph()
p4.text = "Ứng dụng Big Data Analytics & Machine Learning phân tán trên nền tảng Databricks Lakehouse"
p4.font.size = Pt(14)
p4.font.italic = True
p4.font.color.rgb = RGBColor(148, 163, 184)
p4.space_before = Pt(8)

# 3 Info Cards
info_cards = [
    ("👤 SINH VIÊN THỰC HIỆN", "Lê Thành Hiệu", "MSSV: 24520496 • Lớp SIC Big Data 2026", EMERALD_BR),
    ("👨‍🏫 GIẢNG VIÊN HƯỚNG DẪN", "TS. Trần Mạnh Tường", "Trường Đại học Tài chính - Marketing (UFM)", BLUE_BR),
    ("⚡ MÔI TRƯỜNG & TẬP DỮ LIỆU", "Databricks Community", "LendingClub (2.26 Triệu dòng, 1.6 GB) • Đề tài 07", AMBER_BR)
]

c_w = Inches(3.55)
c_gap = Inches(0.34)
c_y = Inches(5.05)
c_h = Inches(1.6)

for i, (tag, val, sub, accent) in enumerate(info_cards):
    cx = Inches(1.0) + i * (c_w + c_gap)
    create_styled_card(slide1, cx, c_y, c_w, c_h, bg_color=DARK_CARD, border_color=accent, border_width=1.5)
    
    tb = slide1.shapes.add_textbox(cx + Inches(0.2), c_y + Inches(0.18), c_w - Inches(0.4), c_h - Inches(0.36))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    
    pt = tf.paragraphs[0]
    pt.text = tag
    pt.font.size = Pt(9.5)
    pt.font.bold = True
    pt.font.color.rgb = accent
    
    pv = tf.add_paragraph()
    pv.text = val
    pv.font.size = Pt(14.5)
    pv.font.bold = True
    pv.font.color.rgb = WHITE
    pv.space_before = Pt(4)
    
    ps = tf.add_paragraph()
    ps.text = sub
    ps.font.size = Pt(10)
    ps.font.color.rgb = RGBColor(203, 213, 225)
    ps.space_before = Pt(3)

print("✅ Slide 1 hoàn tất.")

# ==============================================================================
# SLIDE 2: ĐẶT VẤN ĐỀ NGHIỆP VỤ & 5VS BIG DATA
# ==============================================================================
slide2 = prs.slides.add_slide(blank_layout)
set_slide_background(slide2, LIGHT_BG)
add_clean_title(slide2, "1. Đặt Vấn Đề Nghiệp Vụ & Mô Hình 5Vs Dữ Liệu Lớn")

# Left Column: Business Problem (3 Cards with distinct alert colors)
probs = [
    ("🔴 TỶ LỆ NỢ XẤU LỊCH SỬ CAO (21.82%)", "Các tổ chức tài chính đối mặt với tổn thất hàng trăm tỷ VNĐ vốn khó đòi trong cho vay tiêu dùng tín chấp. Buộc phải trích lập dự phòng rủi ro lớn theo Thông tư 11/2021/TT-NHNN, bào mòn nghiêm trọng lợi nhuận ròng.", ROSE_BG, ROSE_BR, ROSE_TX),
    ("⏱️ THẨM ĐỊNH THỦ CÔNG KÉO DÀI 2 - 5 NGÀY", "Quy trình đối soát hồ sơ giấy tờ cồng kềnh, tốn kém chi phí nhân sự và dễ mắc sai lầm chủ quan. Không đáp ứng được kỳ vọng phê duyệt tức thì của khách hàng số (Instant Credit / BNPL).", AMBER_BG, AMBER_BR, AMBER_TX),
    ("🎯 MỤC TIÊU CÔNG NGHỆ CỦA ĐỀ TÀI", "Xây dựng hệ thống tự động hóa chấm điểm tín dụng dữ liệu lớn trên Databricks Lakehouse: Phê duyệt tự động > 75% hồ sơ trong < 3 phút, kéo giảm tỷ lệ nợ xấu danh mục xuống dưới 4.2%.", BLUE_BG, BLUE_BR, BLUE_TX)
]

py = Inches(1.6)
ph = Inches(1.6)
pgap = Inches(0.18)

for i, (p_title, p_desc, bg_c, br_c, tx_c) in enumerate(probs):
    cur_y = py + i * (ph + pgap)
    create_styled_card(slide2, Inches(0.8), cur_y, Inches(5.6), ph, bg_color=bg_c, border_color=br_c, border_width=1.5)
    
    tb = slide2.shapes.add_textbox(Inches(1.0), cur_y + Inches(0.15), Inches(5.2), ph - Inches(0.3))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    
    p = tf.paragraphs[0]
    p.text = p_title
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = tx_c
    
    p2 = tf.add_paragraph()
    p2.text = p_desc
    p2.font.size = Pt(9.5)
    p2.font.color.rgb = TEXT_DARK
    p2.space_before = Pt(3)

# Right Column: 5Vs Big Data Cards
create_styled_card(slide2, Inches(6.7), Inches(1.6), Inches(5.833), Inches(5.15), bg_color=WHITE, border_color=GRAY_CARD_BR)

tb_r = slide2.shapes.add_textbox(Inches(6.9), Inches(1.8), Inches(5.4), Inches(4.75))
tf_r = tb_r.text_frame
tf_r.word_wrap = True
tf_r.margin_left = tf_r.margin_top = tf_r.margin_right = tf_r.margin_bottom = 0

p = tf_r.paragraphs[0]
p.text = "🌐 ĐẶC TÍNH 5VS DỮ LIỆU LỚN TRONG ĐỀ TÀI"
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = BLUE_TX

fives = [
    ("📦 Volume (Quy mô dữ liệu):", "2,260,701 hồ sơ vay (1.6 GB) từ LendingClub, vượt quá khả năng xử lý trong RAM máy đơn."),
    ("⚡ Velocity (Tốc độ xử lý):", "Chấm điểm thời gian thực, phản hồi quyết định phê duyệt tín dụng trong thời gian dưới 3 phút."),
    ("🗂️ Variety (Đa dạng cấu trúc):", "Kết hợp biến định lượng (thu nhập, nợ, lãi suất) và biến danh mục (mục đích vay, tình trạng nhà)."),
    ("🛡️ Veracity (Độ tin cậy dữ liệu):", "Lọc ngoại lai tuổi (18-80) và thu nhập (>0), điền khuyết median nghiêm ngặt tại Silver Layer."),
    ("💎 Value (Giá trị kinh tế):", "Kéo giảm nợ xấu về 4.18%, tiết kiệm hơn 176.4 tỷ VNĐ tổn thất dự phòng rủi ro.")
]

for k, v in fives:
    p = tf_r.add_paragraph()
    p.text = k
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = BLUE_BR
    p.space_before = Pt(8)
    
    p2 = tf_r.add_paragraph()
    p2.text = v
    p2.font.size = Pt(10)
    p2.font.color.rgb = TEXT_DARK
    p2.space_before = Pt(1)

print("✅ Slide 2 hoàn tất.")

# ==============================================================================
# SLIDE 3: KIẾN TRÚC DATABRICKS LAKEHOUSE MEDALLION (TỶ LỆ CHUẨN)
# ==============================================================================
slide3 = prs.slides.add_slide(blank_layout)
set_slide_background(slide3, LIGHT_BG)
add_clean_title(slide3, "2. Quản Trị & Lưu Trữ Dữ Liệu Theo Kiến Trúc Medallion")

# Left Side: 3 Architecture Cards with Badges
arch_cards = [
    ("🥉 TẦNG BRONZE (Raw Delta Table)", "workspace.default.bronze_credit_data:\n• Nạp thô nguyên vẹn 2.26 triệu dòng từ DBFS.\n• Đảm bảo tính toàn vẹn giao dịch ACID.\n• Truy vết lịch sử với cơ chế Time Travel Audit.", AMBER_BG, AMBER_BR, AMBER_TX),
    ("🥈 TẦNG SILVER (Cleaned & Standardized)", "workspace.default.silver_credit_data:\n• Loại bỏ bản ghi ngoại lai phi lý trong kinh doanh.\n• Điền khuyết lãi suất bằng trung vị thận trọng.\n• Kỹ nghệ 2 chỉ số tài chính cốt lõi: DTI và CBI.", BLUE_BG, BLUE_BR, BLUE_TX),
    ("🥇 TẦNG GOLD (AI Serving & Decision)", "workspace.default.gold_credit_scoring:\n• Lưu trữ kết quả dự báo xác suất vỡ nợ (PD).\n• Động cơ chấm điểm FICO Score chuẩn hóa.\n• Tích hợp biểu phí lãi suất Risk-Based Pricing.", EMERALD_BG, EMERALD_BR, EMERALD_TX)
]

ay = Inches(1.6)
ah = Inches(1.6)
agap = Inches(0.18)

for i, (atitle, adesc, bg_c, br_c, tx_c) in enumerate(arch_cards):
    cur_y = ay + i * (ah + agap)
    create_styled_card(slide3, Inches(0.8), cur_y, Inches(5.3), ah, bg_color=bg_c, border_color=br_c, border_width=1.5)
    
    tb = slide3.shapes.add_textbox(Inches(1.0), cur_y + Inches(0.12), Inches(4.9), ah - Inches(0.24))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    
    p = tf.paragraphs[0]
    p.text = atitle
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = tx_c
    
    p2 = tf.add_paragraph()
    p2.text = adesc
    p2.font.size = Pt(9.5)
    p2.font.color.rgb = TEXT_DARK
    p2.space_before = Pt(3)

# Right Side: Proportional Image (Hinh 2.1 Medallion: Aspect 1.878)
# Allocated box: width 6.2", height 5.15"
add_proportional_image(slide3, "images/hinh_2_1_medallion_architecture.png", Inches(6.3), Inches(1.6), Inches(6.233), Inches(5.15))

print("✅ Slide 3 hoàn tất.")

# ==============================================================================
# SLIDE 4: PHÂN TÍCH KHÁM PHÁ & SPARK SQL (TỶ LỆ CHUẨN)
# ==============================================================================
slide4 = prs.slides.add_slide(blank_layout)
set_slide_background(slide4, LIGHT_BG)
add_clean_title(slide4, "3. Phân Tích Khám Phá & Chỉ Số Kinh Doanh (Spark SQL)")

# Left Side: Image Hinh 3.2 (Aspect 2.204) - Allocate full suitable box
add_proportional_image(slide4, "images/hinh_3_2_npl_intent_home.png", Inches(0.8), Inches(1.6), Inches(6.1), Inches(5.15))

# Right Side: 3 Business Insights Cards
s4_insights = [
    ("🩺 VAY Y TẾ CÓ TỶ LỆ NỢ XẤU CAO NHẤT (26.8%)", "Khách hàng vay y tế thường gặp biến cố sức khỏe bất ngờ, suy giảm trực tiếp khả năng lao động và nguồn thu nhập ổn định để trả nợ. Ngược lại, vay Giáo dục (Education) an toàn nhất với NPL chỉ 15.4%.", ROSE_BG, ROSE_BR, ROSE_TX),
    ("📈 TỶ LỆ NỢ XẤU TĂNG ĐƠN ĐIỆU THEO HẠNG VAY", "• Khoản vay Hạng A: Tỷ lệ nợ xấu chỉ 5.8% (lãi suất 7.2%).\n• Khoản vay Hạng G: Tỷ lệ nợ xấu lên đến 65.4% (lãi suất trên 20%).\n→ Chứng minh hạng tín dụng là nhân tố phân loại rủi ro cực kỳ hiệu quả.", BLUE_BG, BLUE_BR, BLUE_TX),
    ("🏠 KHÁCH THUÊ NHÀ RỦI RO GẤP ĐÔI SỞ HỮU NHÀ", "Khách hàng Đi thuê (Rent) có tỷ lệ nợ xấu 25.6%, trong khi khách có Nhà thế chấp (Mortgage) hoặc Sở hữu riêng (Own) chỉ 12.8% do có tài sản tích lũy bảo đảm và ý thức tài chính cao hơn.", AMBER_BG, AMBER_BR, AMBER_TX)
]

iy = Inches(1.6)
ih = Inches(1.6)
igap = Inches(0.18)

for i, (ititle, idesc, bg_c, br_c, tx_c) in enumerate(s4_insights):
    cur_y = iy + i * (ih + igap)
    create_styled_card(slide4, Inches(7.1), cur_y, Inches(5.433), ih, bg_color=bg_c, border_color=br_c, border_width=1.5)
    
    tb = slide4.shapes.add_textbox(Inches(7.25), cur_y + Inches(0.12), Inches(5.1), ih - Inches(0.24))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    
    p = tf.paragraphs[0]
    p.text = ititle
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = tx_c
    
    p2 = tf.add_paragraph()
    p2.text = idesc
    p2.font.size = Pt(9.5)
    p2.font.color.rgb = TEXT_DARK
    p2.space_before = Pt(3)

print("✅ Slide 4 hoàn tất.")

# ==============================================================================
# SLIDE 5: KỸ NGHỆ ĐẶC TRƯNG & SPARK MLLIB PIPELINE
# ==============================================================================
slide5 = prs.slides.add_slide(blank_layout)
set_slide_background(slide5, LIGHT_BG)
add_clean_title(slide5, "4. Kỹ Nghệ Đặc Trưng & Quy Trình Spark MLlib Pipeline")

# Top: 2 Formula Cards
create_styled_card(slide5, Inches(0.8), Inches(1.6), Inches(5.7), Inches(1.5), bg_color=INDIGO_BG, border_color=INDIGO_BR, border_width=1.5)
tb_f1 = slide5.shapes.add_textbox(Inches(1.0), Inches(1.72), Inches(5.3), Inches(1.25))
tff1 = tb_f1.text_frame
tff1.word_wrap = True
tff1.margin_left = tff1.margin_top = tff1.margin_right = tff1.margin_bottom = 0
p = tff1.paragraphs[0]
p.text = "📐 TỶ LỆ NỢ TRÊN THU NHẬP (DTI RATIO)"
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = INDIGO_TX
p2 = tff1.add_paragraph()
p2.text = "DTI = Khoản vay đề nghị  /  Tổng thu nhập hàng năm"
p2.font.size = Pt(12)
p2.font.bold = True
p2.font.color.rgb = TEXT_DARK
p2.space_before = Pt(2)
p3 = tff1.add_paragraph()
p3.text = "Đo lường mức độ đòn bẩy tài chính và nguy cơ quá tải trả nợ của người vay."
p3.font.size = Pt(9.5)
p3.font.color.rgb = TEXT_MUTED

create_styled_card(slide5, Inches(6.8), Inches(1.6), Inches(5.733), Inches(1.5), bg_color=BLUE_BG, border_color=BLUE_BR, border_width=1.5)
tb_f2 = slide5.shapes.add_textbox(Inches(7.0), Inches(1.72), Inches(5.3), Inches(1.25))
tff2 = tb_f2.text_frame
tff2.word_wrap = True
tff2.margin_left = tff2.margin_top = tff2.margin_right = tff2.margin_bottom = 0
p = tff2.paragraphs[0]
p.text = "⚖️ CHỈ SỐ GÁNH NẶNG TÍN DỤNG (CBI INDEX)"
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = BLUE_TX
p2 = tff2.add_paragraph()
p2.text = "CBI = (Khoản vay  ×  Lãi suất)  /  Tổng thu nhập hàng năm"
p2.font.size = Pt(12)
p2.font.bold = True
p2.font.color.rgb = TEXT_DARK
p2.space_before = Pt(2)
p3 = tff2.add_paragraph()
p3.text = "Đo lường tỷ trọng lãi suất hàng năm bào mòn trực tiếp ngân sách chi tiêu của người vay."
p3.font.size = Pt(9.5)
p3.font.color.rgb = TEXT_MUTED

# Bottom: 4 Pipeline Process Cards in 4 vibrant columns
pipeline_cols = [
    ("STAGE 1", "🔤 StringIndexer", "• Mã hóa 3 biến phân loại danh mục:\n  - person_home_ownership\n  - loan_intent\n  - cb_person_default_on_file\n• handleInvalid='keep': Tự động gán nhãn an toàn cho giá trị mới.\n• Output: các cột *_idx.", BLUE_BG, BLUE_BR, BLUE_TX),
    ("STAGE 2", "🔢 OneHotEncoder", "• Chuyển đổi các chỉ mục sang định dạng Vector thưa nhị phân (Sparse Vector).\n• Tránh áp đặt thứ tự sai lệch giữa các nhóm danh mục độc lập.\n• Tối ưu hóa lưu trữ phân tán.\n• Output: các cột *_vec.", INDIGO_BG, INDIGO_BR, INDIGO_TX),
    ("STAGE 3", "📐 Assembler & Scaler", "• VectorAssembler gom 11 đặc trưng (3 biến One-Hot + 8 biến định lượng).\n• StandardScaler chuẩn hóa thang đo độ lệch chuẩn (withStd=True).\n• Triệt tiêu sai lệch độ lớn giữa thu nhập ($) và độ tuổi.", AMBER_BG, AMBER_BR, AMBER_TX),
    ("STAGE 4", "🌲 Random Forest", "• Khởi tạo 50 cây quyết định phân tán (numTrees=50, maxDepth=10).\n• Bắt trọn quan hệ phi tuyến phức tạp giữa đòn bẩy và vỡ nợ.\n• Tối ưu hóa ROC-AUC = 0.8745.\n• Kháng triệt để hiện tượng Overfitting.", EMERALD_BG, EMERALD_BR, EMERALD_TX)
]

col_w = Inches(2.78)
col_gap = Inches(0.2)
col_y = Inches(3.35)
col_h = Inches(3.4)

for i, (s_num, s_title, s_desc, bg_c, br_c, tx_c) in enumerate(pipeline_cols):
    cx = Inches(0.8) + i * (col_w + col_gap)
    create_styled_card(slide5, cx, col_y, col_w, col_h, bg_color=bg_c, border_color=br_c, border_width=1.5)
    
    tb = slide5.shapes.add_textbox(cx + Inches(0.15), col_y + Inches(0.18), col_w - Inches(0.3), col_h - Inches(0.36))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    
    p = tf.paragraphs[0]
    p.text = s_num
    p.font.size = Pt(9)
    p.font.bold = True
    p.font.color.rgb = tx_c
    
    p2 = tf.add_paragraph()
    p2.text = s_title
    p2.font.size = Pt(11)
    p2.font.bold = True
    p2.font.color.rgb = TEXT_DARK
    p2.space_before = Pt(2)
    
    p3 = tf.add_paragraph()
    p3.text = s_desc
    p3.font.size = Pt(9.5)
    p3.font.color.rgb = TEXT_DARK
    p3.space_before = Pt(6)

print("✅ Slide 5 hoàn tất.")

# ==============================================================================
# SLIDE 6: ĐÁNH GIÁ HIỆU NĂNG MÔ HÌNH (TỶ LỆ CHUẨN)
# ==============================================================================
slide6 = prs.slides.add_slide(blank_layout)
set_slide_background(slide6, LIGHT_BG)
add_clean_title(slide6, "5. Đánh Giá Hiệu Năng & So Sánh Đối Chuẩn 3 Mô Hình")

# Left Side: Table & Metric Summary
create_styled_card(slide6, Inches(0.8), Inches(1.6), Inches(6.7), Inches(5.15), bg_color=WHITE, border_color=GRAY_CARD_BR)

tb_m = slide6.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(6.3), Inches(0.6))
tfm = tb_m.text_frame
tfm.word_wrap = True
tfm.margin_left = tfm.margin_top = tfm.margin_right = tfm.margin_bottom = 0
p = tfm.paragraphs[0]
p.text = "📊 BẢNG ĐỐI CHUẨN KỸ THUẬT GIỮA 3 THUẬT TOÁN HỌC MÁY"
p.font.size = Pt(11.5)
p.font.bold = True
p.font.color.rgb = BLUE_TX

# Table
table_shape = slide6.shapes.add_table(4, 5, Inches(1.0), Inches(2.35), Inches(6.3), Inches(2.2))
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
    cell.fill.fore_color.rgb = TEXT_DARK
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
        p.font.color.rgb = BLUE_TX if is_rf else TEXT_DARK
        p.alignment = PP_ALIGN.CENTER if col_idx in [1, 2, 3] else PP_ALIGN.LEFT

# Highlight box below table
create_styled_card(slide6, Inches(1.0), Inches(4.8), Inches(6.3), Inches(1.75), bg_color=EMERALD_BG, border_color=EMERALD_BR, border_width=1.5)
tb_h = slide6.shapes.add_textbox(Inches(1.15), Inches(4.92), Inches(6.0), Inches(1.5))
tfh = tb_h.text_frame
tfh.word_wrap = True
tfh.margin_left = tfh.margin_top = tfh.margin_right = tfh.margin_bottom = 0

p = tfh.paragraphs[0]
p.text = "🏆 VÌ SAO RANDOM FOREST ĐƯỢC CHỌN VÀO PRODUCTION?"
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = EMERALD_TX

reasons = [
    "ROC-AUC đạt 0.8745: Phân tách rủi ro vượt trội so với baseline (0.7620).",
    "F1-Score đạt 0.8468: Cân bằng tối ưu giữa Precision (chặn nợ xấu) và Recall (không từ chối oan khách tốt).",
    "Khả năng mở rộng phân tán: Xử lý song song mượt mà trên 2.26 triệu hồ sơ Databricks."
]
for r in reasons:
    p = tfh.add_paragraph()
    p.text = "• " + r
    p.font.size = Pt(9.5)
    p.font.color.rgb = TEXT_DARK
    p.space_before = Pt(2)

# Right Side: Image Hinh 4.1 ROC Curve (Aspect 1.339) - Proportional fit!
add_proportional_image(slide6, "images/hinh_4_1_roc_curve.png", Inches(7.7), Inches(1.6), Inches(4.833), Inches(5.15))

print("✅ Slide 6 hoàn tất.")

# ==============================================================================
# SLIDE 7: MA TRẬN NHẦM LẪN & FEATURE IMPORTANCE (TỶ LỆ CHUẨN)
# ==============================================================================
slide7 = prs.slides.add_slide(blank_layout)
set_slide_background(slide7, LIGHT_BG)
add_clean_title(slide7, "6. Ma Trận Nhầm Lẫn & Trích Xuất Độ Quan Trọng Đặc Trưng")

# Left Side: Confusion Matrix (Aspect 1.213) - Proportional fit!
add_proportional_image(slide7, "images/hinh_4_2_confusion_matrix.png", Inches(0.8), Inches(1.6), Inches(5.3), Inches(5.15))

# Right Side: Feature Importance Analysis (3 Cards with distinct colors)
fi_cards = [
    ("🥇 #1 LÃI SUẤT KHOẢN VAY (loan_int_rate - 38.2%)", "Lãi suất cao vừa là biểu hiện vừa là nguyên nhân đẩy người vay vào tình trạng mất thanh khoản. Khách hàng chấp nhận vay lãi cao thường có rủi ro nội tại nghiêm trọng.", ROSE_BG, ROSE_BR, ROSE_TX),
    ("🥈 #2 TỶ LỆ NỢ TRÊN THU NHẬP (dti_ratio - 24.5%)", "Đòn bẩy nợ quyết định trực tiếp khả năng thanh toán. Khách hàng có DTI > 0.40 có xác suất vỡ nợ tăng gấp 3.2 lần so với nhóm DTI lành mạnh (< 0.20).", AMBER_BG, AMBER_BR, AMBER_TX),
    ("🥉 #3 CHỈ SỐ GÁNH NẶNG TÍN DỤNG (cbi_index - 15.8%)", "Tác động cộng hưởng giữa lãi suất và quy mô khoản vay so với thu nhập. Phản ánh áp lực dòng tiền mặt thực tế phải chi trả hàng tháng.", BLUE_BG, BLUE_BR, BLUE_TX)
]

fy = Inches(1.6)
fh = Inches(1.22)
fgap = Inches(0.14)

for i, (ftitle, fdesc, bg_c, br_c, tx_c) in enumerate(fi_cards):
    cur_y = fy + i * (fh + fgap)
    create_styled_card(slide7, Inches(6.3), cur_y, Inches(6.233), fh, bg_color=bg_c, border_color=br_c, border_width=1.5)
    
    tb = slide7.shapes.add_textbox(Inches(6.45), cur_y + Inches(0.1), Inches(5.9), fh - Inches(0.2))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    
    p = tf.paragraphs[0]
    p.text = ftitle
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = tx_c
    
    p2 = tf.add_paragraph()
    p2.text = fdesc
    p2.font.size = Pt(9.5)
    p2.font.color.rgb = TEXT_DARK
    p2.space_before = Pt(2)

# Bottom Takeaway Card
create_styled_card(slide7, Inches(6.3), Inches(5.6), Inches(6.233), Inches(1.15), bg_color=EMERALD_BG, border_color=EMERALD_BR, border_width=1.5)
tb_t = slide7.shapes.add_textbox(Inches(6.45), Inches(5.7), Inches(5.9), Inches(0.95))
tft = tb_t.text_frame
tft.word_wrap = True
tft.margin_left = tft.margin_top = tft.margin_right = tft.margin_bottom = 0
p = tft.paragraphs[0]
p.text = "💡 THÔNG ĐIỆP QUẢN TRỊ RỦI RO:"
p.font.size = Pt(10.5)
p.font.bold = True
p.font.color.rgb = EMERALD_TX
p2 = tft.add_paragraph()
p2.text = "Thu nhập danh nghĩa (income) không quan trọng bằng Đòn bẩy nợ (DTI & CBI). Không nên phê duyệt chỉ dựa vào thu nhập cao mà phải xét kèm nghĩa vụ trả nợ hiện tại!"
p2.font.size = Pt(9.5)
p2.font.color.rgb = TEXT_DARK
p2.space_before = Pt(2)

print("✅ Slide 7 hoàn tất.")

# ==============================================================================
# SLIDE 8: TÁC ĐỘNG TÀI CHÍNH & HIỆU QUẢ KINH TẾ (ROI & VALUE)
# ==============================================================================
slide8 = prs.slides.add_slide(blank_layout)
set_slide_background(slide8, LIGHT_BG)
add_clean_title(slide8, "7. Tác Động Tài Chính & Hiệu Quả Vận Hành Cho Doanh Nghiệp")

# Top 3 Big Stat KPI Cards (Vibrant Colors & Big Numbers)
kpis = [
    ("💰 176.4 TỶ VNĐ", "TIẾT KIỆM TỔN THẤT TÍN DỤNG", "Ước tính trên danh mục 1,000 tỷ VNĐ cho vay tín chấp; cắt giảm trích lập dự phòng theo TT 11/2021/TT-NHNN.", EMERALD_BG, EMERALD_BR, EMERALD_TX),
    ("📉 21.82% → 4.18%", "KÉO GIẢM TỶ LỆ NỢ XẤU NPL", "Kéo giảm nợ xấu danh mục xuống mức an toàn, cải thiện hệ số an toàn vốn CAR và tăng biên lãi thuần NIM.", BLUE_BG, BLUE_BR, BLUE_TX),
    ("🎯 84.04%", "TỶ LỆ PHÁT HIỆN SỚM NỢ XẤU", "Phát hiện chính xác 84.04% khoản vay có nguy cơ vỡ nợ trước khi giải ngân, chặn đứng nợ xấu từ cửa tiếp nhận.", AMBER_BG, AMBER_BR, AMBER_TX)
]

kw = Inches(3.75)
kgap = Inches(0.24)
ky = Inches(1.6)
kh = Inches(2.2)

for i, (num_val, k_title, k_desc, bg_c, br_c, tx_c) in enumerate(kpis):
    kx = Inches(0.8) + i * (kw + kgap)
    create_styled_card(slide8, kx, ky, kw, kh, bg_color=bg_c, border_color=br_c, border_width=2)
    
    tb = slide8.shapes.add_textbox(kx + Inches(0.2), ky + Inches(0.18), kw - Inches(0.4), kh - Inches(0.36))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    
    p = tf.paragraphs[0]
    p.text = num_val
    p.font.size = Pt(26)
    p.font.bold = True
    p.font.color.rgb = tx_c
    
    p2 = tf.add_paragraph()
    p2.text = k_title
    p2.font.size = Pt(11)
    p2.font.bold = True
    p2.font.color.rgb = TEXT_DARK
    p2.space_before = Pt(4)
    
    p3 = tf.add_paragraph()
    p3.text = k_desc
    p3.font.size = Pt(9.5)
    p3.font.color.rgb = TEXT_MUTED
    p3.space_before = Pt(3)

# Bottom Section: Operational Impact Cards (2 Columns)
bot_w = Inches(5.75)
bot_y = Inches(4.05)
bot_h = Inches(2.7)

create_styled_card(slide8, Inches(0.8), bot_y, bot_w, bot_h, bg_color=INDIGO_BG, border_color=INDIGO_BR, border_width=1.5)
tb_b1 = slide8.shapes.add_textbox(Inches(1.0), bot_y + Inches(0.2), bot_w - Inches(0.4), bot_h - Inches(0.4))
tfb1 = tb_b1.text_frame
tfb1.word_wrap = True
tfb1.margin_left = tfb1.margin_top = tfb1.margin_right = tfb1.margin_bottom = 0
p = tfb1.paragraphs[0]
p.text = "⚡ TỰ ĐỘNG HÓA PHÊ DUYỆT TỨC THÌ (STP > 76%)"
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = INDIGO_TX
p2 = tfb1.add_paragraph()
p2.text = "• Thời gian xử lý hồ sơ giảm từ 2 - 5 ngày xuống dưới 3 phút.\n• Đấu nối trực tiếp API mô hình vào ứng dụng Mobile Banking và hệ thống khởi tạo khoản vay (LOS).\n• Nâng cao trải nghiệm khách hàng (CSAT/NPS), đáp ứng hoàn hảo xu hướng tài chính tiêu dùng số."
p2.font.size = Pt(10.5)
p2.font.color.rgb = TEXT_DARK
p2.space_before = Pt(6)

create_styled_card(slide8, Inches(6.783), bot_y, bot_w, bot_h, bg_color=BLUE_BG, border_color=BLUE_BR, border_width=1.5)
tb_b2 = slide8.shapes.add_textbox(Inches(6.983), bot_y + Inches(0.2), bot_w - Inches(0.4), bot_h - Inches(0.4))
tfb2 = tb_b2.text_frame
tfb2.word_wrap = True
tfb2.margin_left = tfb2.margin_top = tfb2.margin_right = tfb2.margin_bottom = 0
p = tfb2.paragraphs[0]
p.text = "👥 TỐI ƯU HÓA 65% CHI PHÍ VẬN HÀNH THẨM ĐỊNH"
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = BLUE_TX
p2 = tfb2.add_paragraph()
p2.text = "• Cắt giảm khối lượng công việc kiểm tra thủ công cho đội ngũ tín dụng.\n• Tái phân bổ nhân sự sang công tác chăm sóc khách hàng và xử lý nợ chuyên sâu.\n• Loại bỏ hoàn toàn sai lệch chủ quan và rủi ro đạo đức của chuyên viên thẩm định."
p2.font.size = Pt(10.5)
p2.font.color.rgb = TEXT_DARK
p2.space_before = Pt(6)

print("✅ Slide 8 hoàn tất.")

# ==============================================================================
# SLIDE 9: KHUNG CHÍNH SÁCH QUẢN TRỊ (REDESIGNED: CHART ON TOP, 4 CARDS BELOW!)
# ==============================================================================
slide9 = prs.slides.add_slide(blank_layout)
set_slide_background(slide9, LIGHT_BG)
add_clean_title(slide9, "8. Đề Xuất Chính Sách: FICO Scoring & Risk-Based Pricing")

# Top Half: Panoramic Chart (Hinh 5.1: Aspect 2.692) - FULL WIDE DISPLAY, ZERO SQUISHING!
# Native aspect is 2.692. Giving it width 9.6" -> Height 3.56"
add_proportional_image(slide9, "images/hinh_5_1_risk_policy_charts.png", Inches(0.8), Inches(1.45), Inches(11.733), Inches(3.45))

# Bottom Half: 4 Distinct Color-Coded Cards side-by-side (4 Columns)
policy_cards = [
    ("🟢 HẠNG 1: RỦI RO THẤP\n(FICO ≥ 720)", "• Phê duyệt thẳng tự động 100% (STP).\n• Lãi suất ưu đãi: 8.5%/năm.\n• Hạn mức: 100% (Max $30,000).", EMERALD_BG, EMERALD_BR, EMERALD_TX),
    ("🔵 HẠNG 2: RỦI RO TRUNG BÌNH\n(FICO 650 - 719)", "• Phê duyệt nhanh có điều kiện thu nhập.\n• Lãi suất tiêu chuẩn: 11.5%/năm.\n• Hạn mức: 80% (Max $20,000).", BLUE_BG, BLUE_BR, BLUE_TX),
    ("🟠 HẠNG 3: RỦI RO CAO\n(FICO 580 - 649)", "• Thẩm định bán tự động / bảo lãnh.\n• Lãi suất bù đắp: 14.5%/năm.\n• Hạn mức: 50% (Max $10,000).", AMBER_BG, AMBER_BR, AMBER_TX),
    ("🔴 HẠNG 4: RỦI RO RẤT CAO\n(FICO < 580)", "• Từ chối tự động để ngăn nợ xấu.\n• Tái định tuyến sang giải pháp cải thiện FICO.", ROSE_BG, ROSE_BR, ROSE_TX)
]

pw = Inches(2.78)
pgap = Inches(0.2)
py = Inches(5.05)
ph = Inches(1.95)

for i, (ptitle, pdesc, bg_c, br_c, tx_c) in enumerate(policy_cards):
    px = Inches(0.8) + i * (pw + pgap)
    create_styled_card(slide9, px, py, pw, ph, bg_color=bg_c, border_color=br_c, border_width=1.5)
    
    tb = slide9.shapes.add_textbox(px + Inches(0.15), py + Inches(0.12), pw - Inches(0.3), ph - Inches(0.24))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    
    p = tf.paragraphs[0]
    p.text = ptitle
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = tx_c
    
    p2 = tf.add_paragraph()
    p2.text = pdesc
    p2.font.size = Pt(9)
    p2.font.color.rgb = TEXT_DARK
    p2.space_before = Pt(3)

print("✅ Slide 9 hoàn tất.")

# ==============================================================================
# SLIDE 10: TỔNG KẾT & KẾT LUẬN (EXECUTIVE DARK THEME)
# ==============================================================================
slide10 = prs.slides.add_slide(blank_layout)
set_slide_background(slide10, DARK_BG)
add_clean_title(slide10, "9. Tổng Kết & Đóng Góp Thực Tiễn Của Đề Tài", dark_mode=True)

# 3 Summary Cards
summary_cards = [
    ("☁️ LÀM CHỦ BIG DATA LAKEHOUSE", "• Xử lý thành công 2.26 triệu bản ghi trên nền tảng Databricks Lakehouse.\n• Tổ chức kiến trúc Medallion (Bronze - Silver - Gold) chuẩn mực với Delta Lake.\n• Làm chủ PySpark SQL phân tán và MLlib Pipeline.", CYAN_ACCENT),
    ("💡 GIẢI QUYẾT BÀI TOÁN KINH DOANH", "• Mô hình Random Forest đạt ROC-AUC 0.8745 và Accuracy 87.16%.\n• Chuyển đổi con số kỹ thuật thành giá trị tài chính thực tế: tiết kiệm 176.4 tỷ VNĐ tổn thất nợ xấu.\n• Đề xuất chính sách FICO Score & Risk-Based Pricing khả thi.", EMERALD_BR),
    ("🚀 SẴN SÀNG TRIỂN KHAI THỰC TẾ", "• Toàn bộ mã nguồn mở được kiểm thử 100% trên GitHub và Databricks Workspace.\n• Đầy đủ tài liệu đối chiếu chuẩn mẫu SIC.\n• Định hướng mở rộng: Tích hợp dữ liệu viễn thông và điểm tín dụng CIC Việt Nam.", AMBER_BR)
]

sw = Inches(3.55)
sgap = Inches(0.34)
sy = Inches(1.8)
sh = Inches(3.4)

for i, (stitle, sdesc, scolor) in enumerate(summary_cards):
    sx = Inches(1.0) + i * (sw + sgap)
    create_styled_card(slide10, sx, sy, sw, sh, bg_color=DARK_CARD, border_color=scolor, border_width=1.5)
    
    tb = slide10.shapes.add_textbox(sx + Inches(0.2), sy + Inches(0.2), sw - Inches(0.4), sh - Inches(0.4))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    
    p = tf.paragraphs[0]
    p.text = stitle
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = scolor
    
    p2 = tf.add_paragraph()
    p2.text = sdesc
    p2.font.size = Pt(10.5)
    p2.font.color.rgb = RGBColor(226, 232, 240)
    p2.space_before = Pt(8)

# Bottom Thank You & Links Bar
create_styled_card(slide10, Inches(1.0), Inches(5.45), Inches(11.333), Inches(1.4), bg_color=DARK_CARD, border_color=CYAN_ACCENT, border_width=1.5)
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
p2.font.color.rgb = AMBER_BR
p2.alignment = PP_ALIGN.CENTER
p2.space_before = Pt(3)

p3 = tfty.add_paragraph()
p3.text = "Databricks Workspace: Folder 907137357494385   •   GitHub: github.com/snowflake-vibing/Credit_Scoring_Project"
p3.font.size = Pt(9.5)
p3.font.color.rgb = RGBColor(148, 163, 184)
p3.alignment = PP_ALIGN.CENTER
p3.space_before = Pt(2)

print("✅ Slide 10 hoàn tất.")

# Lưu file PowerPoint
output_pptx = "slide_bao_ve_de_tai_7.pptx"
prs.save(output_pptx)
print(f"\n🎉 HOÀN TẤT TÁI THIẾT KẾ 100% BỘ SLIDE CAO CẤP: {output_pptx}")
