# -*- coding: utf-8 -*-
"""
Script tạo Slide thuyết trình Đề tài 7 chuẩn quốc tế với phông chữ Montserrat.
Căn chỉnh hoàn hảo khoảng cách (spacing), cỡ chữ (font size) vừa khít từng thẻ card.
Xóa bỏ hoàn toàn header/footer thừa.
Giữ nguyên tỷ lệ 100% hình ảnh biểu đồ, không bị thu hẹp hay méo mó.
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

print("🚀 Bắt đầu tạo Slide bảo vệ Đề tài 7 với phông chữ Montserrat...")

FONT_FAMILY = "Montserrat"

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
    tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.733), Inches(0.8))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    
    p = tf.paragraphs[0]
    p.text = title_text
    p.font.name = FONT_FAMILY
    p.font.size = Pt(22)
    p.font.bold = True
    p.font.color.rgb = WHITE if dark_mode else TEXT_DARK
    
    # Sleek bottom accent line
    line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.22), Inches(1.8), Inches(0.04))
    line.fill.solid()
    line.fill.fore_color.rgb = CYAN_ACCENT if dark_mode else BLUE_BR
    line.line.fill.background()

def create_styled_card(slide, left, top, width, height, bg_color=GRAY_CARD_BG, border_color=GRAY_CARD_BR, border_width=1.2):
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

top_bar = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.12))
top_bar.fill.solid()
top_bar.fill.fore_color.rgb = CYAN_ACCENT
top_bar.line.fill.background()

tb1 = slide1.shapes.add_textbox(Inches(1.0), Inches(0.9), Inches(11.333), Inches(3.6))
tf1 = tb1.text_frame
tf1.word_wrap = True
tf1.margin_left = tf1.margin_top = tf1.margin_right = tf1.margin_bottom = 0

p = tf1.paragraphs[0]
p.text = "TRƯỜNG ĐẠI HỌC TÀI CHÍNH - MARKETING (UFM) • SAMSUNG INNOVATION CAMPUS (SIC)"
p.font.name = FONT_FAMILY
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = AMBER_BR

p2 = tf1.add_paragraph()
p2.text = "BÁO CÁO TIỂU LUẬN KẾT THÚC HỌC PHẦN (CAPSTONE PROJECT 2026)"
p2.font.name = FONT_FAMILY
p2.font.size = Pt(13)
p2.font.bold = True
p2.font.color.rgb = CYAN_ACCENT
p2.space_before = Pt(8)

p3 = tf1.add_paragraph()
p3.text = "MÔ HÌNH CHẤM ĐIỂM TÍN DỤNG & THẨM ĐỊNH RỦI RO VỠ NỢ\nTRONG LĨNH VỰC NGÂN HÀNG VÀ FINTECH"
p3.font.name = FONT_FAMILY
p3.font.size = Pt(25)
p3.font.bold = True
p3.font.color.rgb = WHITE
p3.space_before = Pt(12)

p4 = tf1.add_paragraph()
p4.text = "Ứng dụng Big Data Analytics & Machine Learning phân tán trên nền tảng Databricks Lakehouse"
p4.font.name = FONT_FAMILY
p4.font.size = Pt(13.5)
p4.font.italic = True
p4.font.color.rgb = RGBColor(148, 163, 184)
p4.space_before = Pt(10)

# 3 Info Cards (Balanced & Fitted)
info_cards = [
    ("👤 SINH VIÊN THỰC HIỆN", "Lê Thành Hiệu", "MSSV: 24520496", "Lớp SIC Big Data • Năm 2026", EMERALD_BR),
    ("👨‍🏫 GIẢNG VIÊN HƯỚNG DẪN", "TS. Trần Mạnh Tường", "Khoa Công nghệ Thông tin", "Trường ĐH Tài chính - Marketing (UFM)", BLUE_BR),
    ("⚡ HẠ TẦNG & DỮ LIỆU", "Databricks Lakehouse", "LendingClub: 2.26M dòng (1.6 GB)", "Phân tích phân tán với Apache PySpark", AMBER_BR)
]

c_w = Inches(3.55)
c_gap = Inches(0.34)
c_y = Inches(5.0)
c_h = Inches(1.75)

for i, (tag, val, sub1, sub2, accent) in enumerate(info_cards):
    cx = Inches(1.0) + i * (c_w + c_gap)
    create_styled_card(slide1, cx, c_y, c_w, c_h, bg_color=DARK_CARD, border_color=accent, border_width=1.5)
    
    tb = slide1.shapes.add_textbox(cx + Inches(0.2), c_y + Inches(0.16), c_w - Inches(0.4), c_h - Inches(0.32))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    
    pt = tf.paragraphs[0]
    pt.text = tag
    pt.font.name = FONT_FAMILY
    pt.font.size = Pt(10)
    pt.font.bold = True
    pt.font.color.rgb = accent
    
    pv = tf.add_paragraph()
    pv.text = val
    pv.font.name = FONT_FAMILY
    pv.font.size = Pt(14.5)
    pv.font.bold = True
    pv.font.color.rgb = WHITE
    pv.space_before = Pt(4)
    
    ps1 = tf.add_paragraph()
    ps1.text = sub1
    ps1.font.name = FONT_FAMILY
    ps1.font.size = Pt(10)
    ps1.font.color.rgb = RGBColor(226, 232, 240)
    ps1.space_before = Pt(3)
    
    ps2 = tf.add_paragraph()
    ps2.text = sub2
    ps2.font.name = FONT_FAMILY
    ps2.font.size = Pt(9)
    ps2.font.color.rgb = RGBColor(148, 163, 184)
    ps2.space_before = Pt(2)

print("✅ Slide 1 hoàn tất.")

# ==============================================================================
# SLIDE 2: ĐẶT VẤN ĐỀ NGHIỆP VỤ & 5VS BIG DATA
# ==============================================================================
slide2 = prs.slides.add_slide(blank_layout)
set_slide_background(slide2, LIGHT_BG)
add_clean_title(slide2, "1. Bối Cảnh Nghiệp Vụ & Mô Hình 5Vs Dữ Liệu Lớn")

# Left Column: Business Problem (3 Cards - Formatted nicely)
probs = [
    ("🔴 TỶ LỆ NỢ XẤU LỊCH SỬ CAO (21.82%)", 
     "• Tổn thất tín dụng nghiêm trọng: Hàng trăm tỷ VNĐ vốn khó đòi trong cho vay tiêu dùng tín chấp.\n• Áp lực trích lập dự phòng: Tuân thủ Thông tư 11/2021/TT-NHNN, bào mòn lợi nhuận ròng của ngân hàng.\n• Bào mòn hệ số CAR: Ảnh hưởng trực tiếp đến an toàn vốn và xếp hạng tín nhiệm tổ chức tín dụng.",
     ROSE_BG, ROSE_BR, ROSE_TX),
    ("⏱️ THẨM ĐỊNH THỦ CÔNG KÉO DÀI 2 - 5 NGÀY", 
     "• Quy trình giấy tờ cồng kềnh: Tốn kém chi phí nhân sự và vận hành đội ngũ thẩm định thủ công.\n• Sai lệch chủ quan: Nguy cơ rủi ro đạo đức và sai số cảm tính của cán bộ tín dụng.\n• Đánh mất khách hàng số: Không đáp ứng kỳ vọng duyệt vay tức thì (Instant Credit / BNPL).",
     AMBER_BG, AMBER_BR, AMBER_TX),
    ("🎯 MỤC TIÊU CÔNG NGHỆ CỦA ĐỀ TÀI", 
     "• Tự động hóa chấm điểm tín dụng: Ứng dụng Big Data Analytics trên Databricks Lakehouse.\n• Phê duyệt siêu tốc: Đạt tỷ lệ phê duyệt thẳng (STP) > 75% hồ sơ trong thời gian < 3 phút.\n• Kiểm soát rủi ro tối ưu: Kéo giảm tỷ lệ nợ xấu danh mục từ 21.82% xuống dưới 4.2%.",
     BLUE_BG, BLUE_BR, BLUE_TX)
]

py = Inches(1.55)
ph = Inches(1.68)
pgap = Inches(0.14)

for i, (p_title, p_desc, bg_c, br_c, tx_c) in enumerate(probs):
    cur_y = py + i * (ph + pgap)
    create_styled_card(slide2, Inches(0.8), cur_y, Inches(5.6), ph, bg_color=bg_c, border_color=br_c, border_width=1.5)
    
    tb = slide2.shapes.add_textbox(Inches(1.0), cur_y + Inches(0.14), Inches(5.2), ph - Inches(0.28))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    
    p = tf.paragraphs[0]
    p.text = p_title
    p.font.name = FONT_FAMILY
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = tx_c
    
    p2 = tf.add_paragraph()
    p2.text = p_desc
    p2.font.name = FONT_FAMILY
    p2.font.size = Pt(9.5)
    p2.font.color.rgb = TEXT_DARK
    p2.space_before = Pt(4)

# Right Column: 5Vs Big Data Cards
create_styled_card(slide2, Inches(6.7), Inches(1.55), Inches(5.833), Inches(5.32), bg_color=WHITE, border_color=GRAY_CARD_BR)

tb_r = slide2.shapes.add_textbox(Inches(6.95), Inches(1.72), Inches(5.333), Inches(4.98))
tf_r = tb_r.text_frame
tf_r.word_wrap = True
tf_r.margin_left = tf_r.margin_top = tf_r.margin_right = tf_r.margin_bottom = 0

p = tf_r.paragraphs[0]
p.text = "🌐 ĐẶC TÍNH 5VS DỮ LIỆU LỚN TRONG ĐỀ TÀI"
p.font.name = FONT_FAMILY
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = BLUE_TX

fives = [
    ("📦 Volume (Quy mô dữ liệu):", "2,260,701 dòng giao dịch (1.6 GB) từ LendingClub, vượt quá khả năng xử lý trong bộ nhớ RAM máy tính trạm đơn lẻ."),
    ("⚡ Velocity (Tốc độ xử lý):", "Chấm điểm thời gian thực, phản hồi quyết định phê duyệt tín dụng tức thì trong thời gian dưới 3 phút / hồ sơ."),
    ("🗂️ Variety (Đa dạng cấu trúc):", "Kết hợp biến định lượng (thu nhập, dư nợ, lãi suất) và biến danh mục (mục đích vay, tình trạng nhà ở)."),
    ("🛡️ Veracity (Độ tin cậy dữ liệu):", "Lọc ngoại lai tuổi (18-80) và thu nhập (>0), điền khuyết median thận trọng tại tầng Silver Layer."),
    ("💎 Value (Giá trị kinh tế):", "Kéo giảm nợ xấu về 4.18%, tiết kiệm hơn 176.4 tỷ VNĐ tổn thất trích lập dự phòng rủi ro tín dụng.")
]

for k, v in fives:
    p = tf_r.add_paragraph()
    p.text = k
    p.font.name = FONT_FAMILY
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = BLUE_BR
    p.space_before = Pt(6)
    
    p2 = tf_r.add_paragraph()
    p2.text = v
    p2.font.name = FONT_FAMILY
    p2.font.size = Pt(9.5)
    p2.font.color.rgb = TEXT_DARK
    p2.space_before = Pt(1)

p_sum = tf_r.add_paragraph()
p_sum.text = "💡 KẾT LUẬN: Đòi hỏi hạ tầng phân tán Databricks & PySpark để xử lý song song toàn diện!"
p_sum.font.name = FONT_FAMILY
p_sum.font.size = Pt(9.5)
p_sum.font.bold = True
p_sum.font.color.rgb = EMERALD_TX
p_sum.space_before = Pt(8)

print("✅ Slide 2 hoàn tất.")

# ==============================================================================
# SLIDE 3: KIẾN TRÚC DATABRICKS LAKEHOUSE MEDALLION (TỶ LỆ CHUẨN)
# ==============================================================================
slide3 = prs.slides.add_slide(blank_layout)
set_slide_background(slide3, LIGHT_BG)
add_clean_title(slide3, "2. Quản Trị & Lưu Trữ Dữ Liệu Theo Kiến Trúc Medallion")

arch_cards = [
    ("🥉 TẦNG BRONZE (Raw Lakehouse)", 
     "workspace.default.bronze_credit_data",
     "• Nạp thô 2,260,701 dòng (1.6 GB) từ DBFS nguyên bản.\n• Định dạng Delta Lake (Parquet nén), bảo toàn giao dịch ACID.\n• Lưu trữ bất biến (As-Is Immutability), không làm sai lệch gốc.\n• Cơ chế Time Travel Audit phục vụ đối soát và khôi phục lịch sử.", 
     AMBER_BG, AMBER_BR, AMBER_TX),
    ("🥈 TẦNG SILVER (Curated & Enriched)", 
     "workspace.default.silver_credit_data",
     "• Làm sạch dữ liệu ngoại lai: Tuổi (18-80) và Thu nhập (>0).\n• Điền khuyết lãi suất bằng trung vị thận trọng (median 11.0%).\n• Kỹ nghệ 2 chỉ số tài chính cốt lõi: DTI Ratio và CBI Index.\n• Chuẩn hóa 12 đặc trưng, phân chia tập 80% Train / 20% Test.", 
     BLUE_BG, BLUE_BR, BLUE_TX),
    ("🥇 TẦNG GOLD (AI Serving & Decision)", 
     "workspace.default.gold_credit_scoring",
     "• Triển khai mô hình Random Forest phân tán (50 cây quyết định).\n• Xuất xác suất vỡ nợ (PD) và quy đổi sang FICO Score (300 - 850).\n• Phân tầng 4 nhóm rủi ro tín dụng và gán chính sách phê duyệt.\n• Tích hợp biểu phí lãi suất bù đắp rủi ro (Risk-Based Pricing).", 
     EMERALD_BG, EMERALD_BR, EMERALD_TX)
]

ay = Inches(1.55)
ah = Inches(1.68)
agap = Inches(0.14)

for i, (atitle, asub, adesc, bg_c, br_c, tx_c) in enumerate(arch_cards):
    cur_y = ay + i * (ah + agap)
    create_styled_card(slide3, Inches(0.8), cur_y, Inches(5.3), ah, bg_color=bg_c, border_color=br_c, border_width=1.5)
    
    tb = slide3.shapes.add_textbox(Inches(1.0), cur_y + Inches(0.12), Inches(4.9), ah - Inches(0.24))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    
    p = tf.paragraphs[0]
    p.text = atitle
    p.font.name = FONT_FAMILY
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = tx_c
    
    ps = tf.add_paragraph()
    ps.text = asub
    ps.font.name = FONT_FAMILY
    ps.font.size = Pt(9)
    ps.font.bold = True
    ps.font.color.rgb = TEXT_MUTED
    ps.space_before = Pt(1)
    
    p2 = tf.add_paragraph()
    p2.text = adesc
    p2.font.name = FONT_FAMILY
    p2.font.size = Pt(9.5)
    p2.font.color.rgb = TEXT_DARK
    p2.space_before = Pt(3)

# Right Side: Proportional Image (Hinh 2.1 Medallion: Aspect 1.878)
add_proportional_image(slide3, "images/hinh_2_1_medallion_architecture.png", Inches(6.3), Inches(1.55), Inches(6.233), Inches(5.32))

print("✅ Slide 3 hoàn tất.")

# ==============================================================================
# SLIDE 4: PHÂN TÍCH KHÁM PHÁ & SPARK SQL (TỶ LỆ CHUẨN)
# ==============================================================================
slide4 = prs.slides.add_slide(blank_layout)
set_slide_background(slide4, LIGHT_BG)
add_clean_title(slide4, "3. Phân Tích Khám Phá & Chỉ Số Kinh Doanh (Spark SQL)")

add_proportional_image(slide4, "images/hinh_3_2_npl_intent_home.png", Inches(0.8), Inches(1.55), Inches(6.1), Inches(5.32))

s4_insights = [
    ("🩺 VAY Y TẾ CÓ TỶ LỆ NỢ XẤU CAO NHẤT (26.8%)", 
     "• Biến cố sức khỏe đột xuất: Làm gián đoạn trực tiếp khả năng lao động và nguồn thu nhập ổn định để trả nợ.\n• Giáo dục (Education) an toàn nhất: NPL chỉ 15.4% do người vay có ý thức kỷ luật tài chính cao.\n• Khuyến nghị: Cần thẩm tra nguồn trả nợ dự phòng kỹ lưỡng đối với hồ sơ vay y tế.", 
     ROSE_BG, ROSE_BR, ROSE_TX),
    ("📈 TỶ LỆ NỢ XẤU TĂNG ĐƠN ĐIỆU THEO HẠNG VAY", 
     "• Hạng A (ưu tú): Tỷ lệ nợ xấu chỉ 5.8% (lãi suất ưu đãi 7.2%/năm).\n• Hạng G (rủi ro cao): Tỷ lệ nợ xấu lên đến 65.4% (lãi suất bù đắp > 20%/năm).\n• Tính đơn điệu: NPL tăng đều đặn qua các hạng A → B → C → D → E → F → G.\n• Khẳng định: Hệ số phân hạng tín dụng phản ánh rủi ro vỡ nợ cực kỳ chính xác.", 
     BLUE_BG, BLUE_BR, BLUE_TX),
    ("🏠 KHÁCH THUÊ NHÀ RỦI RO GẤP ĐÔI SỞ HỮU NHÀ", 
     "• Khách Đi thuê (Rent): Tỷ lệ nợ xấu 25.6% do thiếu hụt tài sản bảo đảm và đệm tài chính tích lũy.\n• Khách Sở hữu nhà (Own / Mortgage): Tỷ lệ nợ xấu chỉ 12.8% (thấp hơn đúng 1/2).\n• Hàm ý: Tình trạng nhà ở là chỉ báo ổn định tài chính cực kỳ mạnh trong mô hình chấm điểm.", 
     AMBER_BG, AMBER_BR, AMBER_TX)
]

iy = Inches(1.55)
ih = Inches(1.68)
igap = Inches(0.14)

for i, (ititle, idesc, bg_c, br_c, tx_c) in enumerate(s4_insights):
    cur_y = iy + i * (ih + igap)
    create_styled_card(slide4, Inches(7.1), cur_y, Inches(5.433), ih, bg_color=bg_c, border_color=br_c, border_width=1.5)
    
    tb = slide4.shapes.add_textbox(Inches(7.25), cur_y + Inches(0.12), Inches(5.1), ih - Inches(0.24))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    
    p = tf.paragraphs[0]
    p.text = ititle
    p.font.name = FONT_FAMILY
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = tx_c
    
    p2 = tf.add_paragraph()
    p2.text = idesc
    p2.font.name = FONT_FAMILY
    p2.font.size = Pt(9.5)
    p2.font.color.rgb = TEXT_DARK
    p2.space_before = Pt(3)

print("✅ Slide 4 hoàn tất.")

# ==============================================================================
# SLIDE 5: KỸ NGHỆ ĐẶC TRƯNG & SPARK MLLIB PIPELINE (VỪA VẶN MỖI CARD)
# ==============================================================================
slide5 = prs.slides.add_slide(blank_layout)
set_slide_background(slide5, LIGHT_BG)
add_clean_title(slide5, "4. Kỹ Nghệ Đặc Trưng & Quy Trình Spark MLlib Pipeline")

# Top: 2 Formula Cards
create_styled_card(slide5, Inches(0.8), Inches(1.55), Inches(5.7), Inches(1.4), bg_color=INDIGO_BG, border_color=INDIGO_BR, border_width=1.5)
tb_f1 = slide5.shapes.add_textbox(Inches(1.0), Inches(1.65), Inches(5.3), Inches(1.2))
tff1 = tb_f1.text_frame
tff1.word_wrap = True
tff1.margin_left = tff1.margin_top = tff1.margin_right = tff1.margin_bottom = 0
p = tff1.paragraphs[0]
p.text = "📐 TỶ LỆ NỢ TRÊN THU NHẬP (DTI RATIO)"
p.font.name = FONT_FAMILY
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = INDIGO_TX
p2 = tff1.add_paragraph()
p2.text = "DTI = Khoản vay đề nghị  /  Tổng thu nhập hàng năm"
p2.font.name = FONT_FAMILY
p2.font.size = Pt(12)
p2.font.bold = True
p2.font.color.rgb = TEXT_DARK
p2.space_before = Pt(2)
p3 = tff1.add_paragraph()
p3.text = "• Ý nghĩa: Đo lường mức độ đòn bẩy tài chính và áp lực nợ gốc so với thu nhập.\n• Ngưỡng cảnh báo: DTI > 0.35 báo hiệu nguy cơ quá tải dòng tiền trả nợ."
p3.font.name = FONT_FAMILY
p3.font.size = Pt(9.5)
p3.font.color.rgb = TEXT_DARK
p3.space_before = Pt(2)

create_styled_card(slide5, Inches(6.8), Inches(1.55), Inches(5.733), Inches(1.4), bg_color=BLUE_BG, border_color=BLUE_BR, border_width=1.5)
tb_f2 = slide5.shapes.add_textbox(Inches(7.0), Inches(1.65), Inches(5.3), Inches(1.2))
tff2 = tb_f2.text_frame
tff2.word_wrap = True
tff2.margin_left = tff2.margin_top = tff2.margin_right = tff2.margin_bottom = 0
p = tff2.paragraphs[0]
p.text = "⚖️ CHỈ SỐ GÁNH NẶNG TÍN DỤNG (CBI INDEX)"
p.font.name = FONT_FAMILY
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = BLUE_TX
p2 = tff2.add_paragraph()
p2.text = "CBI = (Khoản vay  ×  Lãi suất)  /  Tổng thu nhập hàng năm"
p2.font.name = FONT_FAMILY
p2.font.size = Pt(12)
p2.font.bold = True
p2.font.color.rgb = TEXT_DARK
p2.space_before = Pt(2)
p3 = tff2.add_paragraph()
p3.text = "• Ý nghĩa: Độc quyền đề tài! Đo lường lãi suất hàng năm bào mòn ngân sách chi tiêu.\n• Giá trị: Bắt trọn rủi ro cộng hưởng giữa quy mô vay lớn và lãi suất cao."
p3.font.name = FONT_FAMILY
p3.font.size = Pt(9.5)
p3.font.color.rgb = TEXT_DARK
p3.space_before = Pt(2)

# Bottom: 4 Pipeline Process Cards in 4 vibrant columns (Richly filled)
pipeline_cols = [
    ("STAGE 1", "🔤 StringIndexer", 
     "• Mục đích: Mã hóa 3 biến định tính sang chỉ mục số:\n  - person_home_ownership\n  - loan_intent\n  - cb_person_default_on_file\n• Cơ chế an toàn: handleInvalid='keep' tự động gán nhãn cho biến thể mới.\n• Tối ưu: Tiết kiệm 45% thời gian xử lý chuỗi ký tự.\n• Output: Sinh các cột chỉ mục *_idx.", 
     BLUE_BG, BLUE_BR, BLUE_TX),
    ("STAGE 2", "🔢 OneHotEncoder", 
     "• Mục đích: Chuyển đổi chỉ mục sang Vector thưa nhị phân (Sparse Vector).\n• Loại bỏ thiên vị: Không gán thứ bậc giả định giữa các nhóm độc lập.\n• Tiết kiệm bộ nhớ: Giảm 85% dung lượng so với ma trận Dense thông thường.\n• Tương thích: Tối ưu cho cụm Spark 100+ nodes.\n• Output: Sinh các cột vector *_vec.", 
     INDIGO_BG, INDIGO_BR, INDIGO_TX),
    ("STAGE 3", "📐 Assembler & Scaler", 
     "• VectorAssembler: Gom 11 đặc trưng (3 One-Hot + 8 biến định lượng).\n• StandardScaler: Chuẩn hóa thang đo Z-score với withStd=True.\n• Triệt tiêu sai lệch: Đưa thu nhập ($) và tuổi về cùng thang đo chuẩn.\n• Tránh tràn số: Đẩy nhanh tốc độ hội tụ của thuật toán học máy phân tán.\n• Output: Vector đặc trưng features.", 
     AMBER_BG, AMBER_BR, AMBER_TX),
    ("STAGE 4", "🌲 Random Forest", 
     "• Cấu hình: 50 cây quyết định phân tán (numTrees=50, maxDepth=10).\n• Kỹ thuật Bagging: Lấy mẫu ngẫu nhiên có hoàn lại (Sub-sampling 80%).\n• Năng lực: Bắt trọn quan hệ phi tuyến phức tạp giữa đòn bẩy và nợ xấu.\n• Hiệu năng đỉnh cao: Tối ưu hóa ROC-AUC = 0.8745 trên tập kiểm thử.\n• Output: Vector xác suất probability (PD).", 
     EMERALD_BG, EMERALD_BR, EMERALD_TX)
]

col_w = Inches(2.78)
col_gap = Inches(0.2)
col_y = Inches(3.15)
col_h = Inches(3.85)

for i, (s_num, s_title, s_desc, bg_c, br_c, tx_c) in enumerate(pipeline_cols):
    cx = Inches(0.8) + i * (col_w + col_gap)
    create_styled_card(slide5, cx, col_y, col_w, col_h, bg_color=bg_c, border_color=br_c, border_width=1.5)
    
    tb = slide5.shapes.add_textbox(cx + Inches(0.14), col_y + Inches(0.14), col_w - Inches(0.28), col_h - Inches(0.28))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    
    p = tf.paragraphs[0]
    p.text = s_num
    p.font.name = FONT_FAMILY
    p.font.size = Pt(9)
    p.font.bold = True
    p.font.color.rgb = tx_c
    
    p2 = tf.add_paragraph()
    p2.text = s_title
    p2.font.name = FONT_FAMILY
    p2.font.size = Pt(11.5)
    p2.font.bold = True
    p2.font.color.rgb = TEXT_DARK
    p2.space_before = Pt(3)
    
    p3 = tf.add_paragraph()
    p3.text = s_desc
    p3.font.name = FONT_FAMILY
    p3.font.size = Pt(9.5)
    p3.font.color.rgb = TEXT_DARK
    p3.space_before = Pt(5)

print("✅ Slide 5 hoàn tất.")

# ==============================================================================
# SLIDE 6: ĐÁNH GIÁ HIỆU NĂNG MÔ HÌNH (TỶ LỆ CHUẨN)
# ==============================================================================
slide6 = prs.slides.add_slide(blank_layout)
set_slide_background(slide6, LIGHT_BG)
add_clean_title(slide6, "5. Đánh Giá Hiệu Năng & So Sánh Đối Chuẩn 3 Mô Hình")

create_styled_card(slide6, Inches(0.8), Inches(1.55), Inches(6.7), Inches(5.32), bg_color=WHITE, border_color=GRAY_CARD_BR)

tb_m = slide6.shapes.add_textbox(Inches(1.0), Inches(1.72), Inches(6.3), Inches(0.5))
tfm = tb_m.text_frame
tfm.word_wrap = True
tfm.margin_left = tfm.margin_top = tfm.margin_right = tfm.margin_bottom = 0
p = tfm.paragraphs[0]
p.text = "📊 BẢNG ĐỐI CHUẨN KỸ THUẬT GIỮA 3 THUẬT TOÁN HỌC MÁY"
p.font.name = FONT_FAMILY
p.font.size = Pt(11.5)
p.font.bold = True
p.font.color.rgb = BLUE_TX

table_shape = slide6.shapes.add_table(4, 5, Inches(1.0), Inches(2.2), Inches(6.3), Inches(2.0))
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
    p.font.name = FONT_FAMILY
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
        p.font.name = FONT_FAMILY
        p.font.size = Pt(9.5)
        p.font.bold = is_rf
        p.font.color.rgb = BLUE_TX if is_rf else TEXT_DARK
        p.alignment = PP_ALIGN.CENTER if col_idx in [1, 2, 3] else PP_ALIGN.LEFT

# Split bottom into 2 informative cards to fill the container perfectly
create_styled_card(slide6, Inches(1.0), Inches(4.35), Inches(6.3), Inches(1.2), bg_color=EMERALD_BG, border_color=EMERALD_BR, border_width=1.5)
tb_h1 = slide6.shapes.add_textbox(Inches(1.15), Inches(4.45), Inches(6.0), Inches(1.0))
tfh1 = tb_h1.text_frame
tfh1.word_wrap = True
tfh1.margin_left = tfh1.margin_top = tfh1.margin_right = tfh1.margin_bottom = 0
p = tfh1.paragraphs[0]
p.text = "🏆 VÌ SAO RANDOM FOREST ĐƯỢC CHỌN VÀO PRODUCTION?"
p.font.name = FONT_FAMILY
p.font.size = Pt(10.5)
p.font.bold = True
p.font.color.rgb = EMERALD_TX
p2 = tfh1.add_paragraph()
p2.text = "• Phân tách rủi ro vượt trội: ROC-AUC đạt 0.8745, bỏ xa Logistic Regression (0.7620).\n• Cân bằng tối ưu: F1-Score 0.8468 giúp vừa chặn nợ xấu vừa không từ chối nhầm khách tốt.\n• Xử lý phân tán: Tương thích 100% Spark MLlib trên cụm phân tán 2.26 triệu hồ sơ."
p2.font.name = FONT_FAMILY
p2.font.size = Pt(9.2)
p2.font.color.rgb = TEXT_DARK
p2.space_before = Pt(2)

create_styled_card(slide6, Inches(1.0), Inches(5.65), Inches(6.3), Inches(1.1), bg_color=BLUE_BG, border_color=BLUE_BR, border_width=1.5)
tb_h2 = slide6.shapes.add_textbox(Inches(1.15), Inches(5.73), Inches(6.0), Inches(0.95))
tfh2 = tb_h2.text_frame
tfh2.word_wrap = True
tfh2.margin_left = tfh2.margin_top = tfh2.margin_right = tfh2.margin_bottom = 0
p = tfh2.paragraphs[0]
p.text = "⚙️ ĐIỂM CẮT NGƯỠNG TỐI ƯU (OPTIMAL CUT-OFF P* = 0.35)"
p.font.name = FONT_FAMILY
p.font.size = Pt(10.5)
p.font.bold = True
p.font.color.rgb = BLUE_TX
p2 = tfh2.add_paragraph()
p2.text = "• Tỷ lệ bắt nợ xấu: Thu hồi chính xác 84.04% khoản vay vỡ nợ (Recall = 84.04%) trước giải ngân.\n• Kiểm soát rủi ro: Giữ tỷ lệ dương tính giả FPR chỉ 3.65%, bảo vệ trải nghiệm khách hàng uy tín."
p2.font.name = FONT_FAMILY
p2.font.size = Pt(9.2)
p2.font.color.rgb = TEXT_DARK
p2.space_before = Pt(2)

add_proportional_image(slide6, "images/hinh_4_1_roc_curve.png", Inches(7.7), Inches(1.55), Inches(4.833), Inches(5.32))

print("✅ Slide 6 hoàn tất.")

# ==============================================================================
# SLIDE 7: MA TRẬN NHẦM LẪN & FEATURE IMPORTANCE (TỶ LỆ CHUẨN)
# ==============================================================================
slide7 = prs.slides.add_slide(blank_layout)
set_slide_background(slide7, LIGHT_BG)
add_clean_title(slide7, "6. Ma Trận Nhầm Lẫn & Trích Xuất Độ Quan Trọng Đặc Trưng")

add_proportional_image(slide7, "images/hinh_4_2_confusion_matrix.png", Inches(0.8), Inches(1.55), Inches(5.3), Inches(5.32))

fi_cards = [
    ("🥇 #1 LÃI SUẤT KHOẢN VAY (loan_int_rate - 38.2%)", 
     "• Yếu tố rủi ro số 1: Chi phối 38.2% sức mạnh phân tách của toàn bộ mô hình.\n• Tác động kép: Vừa là biểu hiện rủi ro nội tại vừa làm tăng gánh nặng trả nợ.\n• Ý nghĩa: Khách hàng chấp nhận vay lãi cao thường có rủi ro tiềm ẩn nghiêm trọng.", 
     ROSE_BG, ROSE_BR, ROSE_TX),
    ("🥈 #2 TỶ LỆ NỢ TRÊN THU NHẬP (dti_ratio - 24.5%)", 
     "• Đòn bẩy nợ tài chính: Quyết định trực tiếp năng lực cân đối dòng tiền trả nợ.\n• Tác động định lượng: Hồ sơ có DTI > 0.40 có xác suất vỡ nợ tăng gấp 3.2 lần.\n• Kiểm soát: Cần áp trần DTI tối đa để ngăn chặn nguy cơ kiệt quệ tài chính.", 
     AMBER_BG, AMBER_BR, AMBER_TX),
    ("🥉 #3 CHỈ SỐ GÁNH NẶNG TÍN DỤNG (cbi_index - 15.8%)", 
     "• Sáng tạo kỹ nghệ cốt lõi: Kết hợp phi tuyến giữa quy mô vay, lãi suất và thu nhập.\n• Đánh giá dòng tiền: Đo lường chính xác tỷ lệ chi trả lãi thực tế hàng tháng.\n• Giá trị: Nhận diện các khoản vay lớn với lãi suất cao gây bào mòn chi tiêu.", 
     BLUE_BG, BLUE_BR, BLUE_TX)
]

fy = Inches(1.55)
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
    p.font.name = FONT_FAMILY
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = tx_c
    
    p2 = tf.add_paragraph()
    p2.text = fdesc
    p2.font.name = FONT_FAMILY
    p2.font.size = Pt(9.2)
    p2.font.color.rgb = TEXT_DARK
    p2.space_before = Pt(2)

create_styled_card(slide7, Inches(6.3), Inches(5.63), Inches(6.233), Inches(1.24), bg_color=EMERALD_BG, border_color=EMERALD_BR, border_width=1.5)
tb_t = slide7.shapes.add_textbox(Inches(6.45), Inches(5.73), Inches(5.9), Inches(1.04))
tft = tb_t.text_frame
tft.word_wrap = True
tft.margin_left = tft.margin_top = tft.margin_right = tft.margin_bottom = 0
p = tft.paragraphs[0]
p.text = "💡 THÔNG ĐIỆP QUẢN TRỊ RỦI RO TÍN DỤNG CỐT LÕI:"
p.font.name = FONT_FAMILY
p.font.size = Pt(10.5)
p.font.bold = True
p.font.color.rgb = EMERALD_TX
p2 = tft.add_paragraph()
p2.text = "• Đòn bẩy nợ (DTI & CBI) quan trọng hơn nhiều so với thu nhập danh nghĩa (Income)!\n• Không bao giờ phê duyệt chỉ dựa vào thu nhập cao nếu nghĩa vụ trả nợ hiện tại đã quá tải.\n• Chuyển từ thẩm định tĩnh theo hồ sơ sang thẩm định động theo năng lực dòng tiền thực."
p2.font.name = FONT_FAMILY
p2.font.size = Pt(9.2)
p2.font.color.rgb = TEXT_DARK
p2.space_before = Pt(2)

print("✅ Slide 7 hoàn tất.")

# ==============================================================================
# SLIDE 8: TÁC ĐỘNG TÀI CHÍNH & HIỆU QUẢ KINH TẾ (ROI & VALUE)
# ==============================================================================
slide8 = prs.slides.add_slide(blank_layout)
set_slide_background(slide8, LIGHT_BG)
add_clean_title(slide8, "7. Tác Động Tài Chính & Hiệu Quả Vận Hành Cho Doanh Nghiệp")

kpis = [
    ("💰 176.4 TỶ VNĐ", "TIẾT KIỆM TỔN THẤT TÍN DỤNG", "Ước tính trên danh mục 1,000 tỷ VNĐ cho vay tín chấp; cắt giảm trích lập dự phòng rủi ro theo Thông tư 11/2021/TT-NHNN.", EMERALD_BG, EMERALD_BR, EMERALD_TX),
    ("📉 21.82% → 4.18%", "KÉO GIẢM TỶ LỆ NỢ XẤU NPL", "Kéo giảm nợ xấu danh mục xuống mức an toàn, cải thiện hệ số an toàn vốn CAR và tăng biên lãi thuần NIM ngân hàng.", BLUE_BG, BLUE_BR, BLUE_TX),
    ("🎯 84.04%", "TỶ LỆ PHÁT HIỆN SỚM NỢ XẤU", "Phát hiện chính xác 84.04% khoản vay có nguy cơ vỡ nợ trước khi giải ngân, chặn đứng nợ xấu ngay từ cửa tiếp nhận.", AMBER_BG, AMBER_BR, AMBER_TX)
]

kw = Inches(3.75)
kgap = Inches(0.24)
ky = Inches(1.55)
kh = Inches(2.15)

for i, (num_val, k_title, k_desc, bg_c, br_c, tx_c) in enumerate(kpis):
    kx = Inches(0.8) + i * (kw + kgap)
    create_styled_card(slide8, kx, ky, kw, kh, bg_color=bg_c, border_color=br_c, border_width=2)
    
    tb = slide8.shapes.add_textbox(kx + Inches(0.2), ky + Inches(0.18), kw - Inches(0.4), kh - Inches(0.36))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    
    p = tf.paragraphs[0]
    p.text = num_val
    p.font.name = FONT_FAMILY
    p.font.size = Pt(25)
    p.font.bold = True
    p.font.color.rgb = tx_c
    
    p2 = tf.add_paragraph()
    p2.text = k_title
    p2.font.name = FONT_FAMILY
    p2.font.size = Pt(11)
    p2.font.bold = True
    p2.font.color.rgb = TEXT_DARK
    p2.space_before = Pt(4)
    
    p3 = tf.add_paragraph()
    p3.text = k_desc
    p3.font.name = FONT_FAMILY
    p3.font.size = Pt(9.5)
    p3.font.color.rgb = TEXT_MUTED
    p3.space_before = Pt(3)

# Bottom Section: Operational Impact Cards (2 Columns - Rich & Filled)
bot_w = Inches(5.75)
bot_y = Inches(3.9)
bot_h = Inches(2.95)

create_styled_card(slide8, Inches(0.8), bot_y, bot_w, bot_h, bg_color=INDIGO_BG, border_color=INDIGO_BR, border_width=1.5)
tb_b1 = slide8.shapes.add_textbox(Inches(1.0), bot_y + Inches(0.18), bot_w - Inches(0.4), bot_h - Inches(0.36))
tfb1 = tb_b1.text_frame
tfb1.word_wrap = True
tfb1.margin_left = tfb1.margin_top = tfb1.margin_right = tfb1.margin_bottom = 0
p = tfb1.paragraphs[0]
p.text = "⚡ TỰ ĐỘNG HÓA PHÊ DUYỆT TỨC THÌ (STP > 76%)"
p.font.name = FONT_FAMILY
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = INDIGO_TX

b1_points = [
    ("Tốc độ xử lý siêu tốc:", "Thời gian xử lý hồ sơ giảm từ 2 - 5 ngày xuống dưới 3 phút / hồ sơ."),
    ("Năng lực phục vụ tự động:", "Phê duyệt 254,919 hồ sơ tự động 100% không cần can thiệp thủ công."),
    ("Tích hợp kênh số linh hoạt:", "Đấu nối API mô hình vào Mobile Banking và hệ thống khởi tạo khoản vay (LOS)."),
    ("Trải nghiệm khách hàng số:", "Tăng mạnh chỉ số CSAT/NPS, đón đầu xu hướng tiêu dùng Instant Credit & BNPL.")
]
for title_pt, desc_pt in b1_points:
    p_pt = tfb1.add_paragraph()
    p_pt.text = f"• {title_pt} {desc_pt}"
    p_pt.font.name = FONT_FAMILY
    p_pt.font.size = Pt(10)
    p_pt.font.color.rgb = TEXT_DARK
    p_pt.space_before = Pt(6)

create_styled_card(slide8, Inches(6.783), bot_y, bot_w, bot_h, bg_color=BLUE_BG, border_color=BLUE_BR, border_width=1.5)
tb_b2 = slide8.shapes.add_textbox(Inches(6.983), bot_y + Inches(0.18), bot_w - Inches(0.4), bot_h - Inches(0.36))
tfb2 = tb_b2.text_frame
tfb2.word_wrap = True
tfb2.margin_left = tfb2.margin_top = tfb2.margin_right = tfb2.margin_bottom = 0
p = tfb2.paragraphs[0]
p.text = "👥 TỐI ƯU HÓA 65% CHI PHÍ VẬN HÀNH THẨM ĐỊNH"
p.font.name = FONT_FAMILY
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = BLUE_TX

b2_points = [
    ("Tiết giảm chi phí nhân sự:", "Cắt giảm 65% khối lượng công việc kiểm tra giấy tờ thủ công cho đội ngũ tín dụng."),
    ("Tối ưu hóa nguồn lực:", "Tái phân bổ nhân sự sang công tác chăm sóc khách hàng VIP và xử lý nợ chuyên sâu."),
    ("Loại bỏ rủi ro đạo đức:", "Chuẩn hóa thuật toán, loại bỏ hoàn toàn sai lệch cảm tính của chuyên viên thẩm định."),
    ("Nâng cao biên lợi nhuận:", "Hạ thấp chi phí biên trên mỗi khoản vay giải ngân, tối đa hóa hiệu quả hoạt động.")
]
for title_pt, desc_pt in b2_points:
    p_pt = tfb2.add_paragraph()
    p_pt.text = f"• {title_pt} {desc_pt}"
    p_pt.font.name = FONT_FAMILY
    p_pt.font.size = Pt(10)
    p_pt.font.color.rgb = TEXT_DARK
    p_pt.space_before = Pt(6)

print("✅ Slide 8 hoàn tất.")

# ==============================================================================
# SLIDE 9: KHUNG CHÍNH SÁCH QUẢN TRỊ (REDESIGNED: CHART TOP, 4 BALANCED CARDS BOTTOM)
# ==============================================================================
slide9 = prs.slides.add_slide(blank_layout)
set_slide_background(slide9, LIGHT_BG)
add_clean_title(slide9, "8. Đề Xuất Chính Sách: FICO Scoring & Risk-Based Pricing")

# Top Half: Panoramic Chart (Hinh 5.1: Aspect 2.692) - FULL WIDE DISPLAY, ZERO SQUISHING!
add_proportional_image(slide9, "images/hinh_5_1_risk_policy_charts.png", Inches(0.8), Inches(1.4), Inches(11.733), Inches(3.4))

# Bottom Half: 4 Distinct Color-Coded Cards side-by-side (4 Columns - Rich & Filled Perfectly)
policy_cards = [
    ("🟢 HẠNG 1: RỦI RO THẤP", 
     "FICO ≥ 720  |  STP: 100%", 
     "📊 Quy mô: 254,919 hồ sơ (56.5%)\n• Phê duyệt: Thẳng tự động 100%, không duyệt tay\n• Lãi suất ưu đãi: 8.5%/năm (giữ chân khách tốt)\n• Hạn mức: Cấp 100% đề xuất (Tối đa $30,000)\n• Tỷ lệ vỡ nợ: Rất thấp (< 2.5%)", 
     EMERALD_BG, EMERALD_BR, EMERALD_TX),
    ("🔵 HẠNG 2: RỦI RO TRUNG BÌNH", 
     "FICO 650 - 719  |  Có điều kiện", 
     "📊 Quy mô: 119,123 hồ sơ (26.4%)\n• Phê duyệt: Nhanh có điều kiện (xác minh thu nhập)\n• Lãi suất tiêu chuẩn: 11.5%/năm\n• Hạn mức: Cấp 80% đề xuất (Tối đa $20,000)\n• Giám sát: Theo dõi thanh toán 6 tháng đầu", 
     BLUE_BG, BLUE_BR, BLUE_TX),
    ("🟠 HẠNG 3: RỦI RO CAO", 
     "FICO 580 - 649  |  Thẩm định tay", 
     "📊 Quy mô: 48,774 hồ sơ (10.8%)\n• Phê duyệt: Thẩm định thủ công / bảo lãnh bên thứ 3\n• Lãi suất bù đắp: 14.5%/năm\n• Hạn mức: Giảm còn 50% đề xuất (Tối đa $10,000)\n• Điều kiện: Siết chặt kiểm soát chứng từ nguồn thu", 
     AMBER_BG, AMBER_BR, AMBER_TX),
    ("🔴 HẠNG 4: RỦI RO RẤT CAO", 
     "FICO < 580  |  Từ chối tự động", 
     "📊 Quy mô: 28,645 hồ sơ (6.3%)\n• Xử lý: Từ chối tự động để ngăn nợ xấu từ đầu\n• Cảnh báo: Lịch sử quá hạn và nợ xấu nghiêm trọng\n• Hạn mức: 0% (Từ chối cấp tín dụng trực tiếp)\n• Tái định tuyến: Tư vấn giải pháp cải thiện điểm số", 
     ROSE_BG, ROSE_BR, ROSE_TX)
]

pw = Inches(2.78)
pgap = Inches(0.2)
py = Inches(4.95)
ph = Inches(2.25)

for i, (ptitle, psub, pdesc, bg_c, br_c, tx_c) in enumerate(policy_cards):
    px = Inches(0.8) + i * (pw + pgap)
    create_styled_card(slide9, px, py, pw, ph, bg_color=bg_c, border_color=br_c, border_width=1.5)
    
    tb = slide9.shapes.add_textbox(px + Inches(0.12), py + Inches(0.1), pw - Inches(0.24), ph - Inches(0.2))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    
    p = tf.paragraphs[0]
    p.text = ptitle
    p.font.name = FONT_FAMILY
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = tx_c
    
    p_sub = tf.add_paragraph()
    p_sub.text = psub
    p_sub.font.name = FONT_FAMILY
    p_sub.font.size = Pt(8.5)
    p_sub.font.bold = True
    p_sub.font.color.rgb = TEXT_DARK
    p_sub.space_before = Pt(1)
    
    p2 = tf.add_paragraph()
    p2.text = pdesc
    p2.font.name = FONT_FAMILY
    p2.font.size = Pt(8.5)
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
    ("☁️ LÀM CHỦ BIG DATA LAKEHOUSE", 
     "• Xử lý thành công toàn bộ 2.26 triệu bản ghi trên cụm Databricks Lakehouse.\n• Chuẩn hóa kiến trúc Medallion 3 tầng (Bronze - Silver - Gold) với Delta Lake.\n• Đảm bảo tính toàn vẹn giao dịch ACID, Time Travel Audit và truy vết lịch sử.\n• Tối ưu hóa hiệu năng tính toán phân tán với Spark SQL và Spark MLlib.\n• Không nghẽn bộ nhớ Driver nhờ cơ chế phân vùng và tính toán lười (lazy evaluation).", 
     CYAN_ACCENT),
    ("💡 GIẢI QUYẾT BÀI TOÁN KINH DOANH", 
     "• Mô hình Random Forest đạt ROC-AUC 0.8745 và Accuracy 87.16% xuất sắc.\n• Cân bằng tối ưu giữa Precision (70.98%) và Recall (84.04% tại cut-off p*=0.35).\n• Tiết kiệm ước tính hơn 176.4 tỷ VNĐ tổn thất dự phòng rủi ro tín dụng.\n• Kéo giảm tỷ lệ nợ xấu danh mục từ mức 21.82% xuống dưới 4.2% an toàn.\n• Đề xuất chính sách phân tầng FICO Score và Risk-Based Pricing khả thi cao.", 
     EMERALD_BR),
    ("🚀 SẴN SÀNG TRIỂN KHAI THỰC TẾ", 
     "• Toàn bộ mã nguồn mở được kiểm thử 100% trên GitHub và Databricks Workspace.\n• Đầy đủ bộ tài liệu đối chiếu chuẩn mẫu Capstone Project UFM & SIC 2026.\n• Sẵn sàng đóng gói REST API phục vụ tích hợp Core Banking và hệ thống LOS.\n• Tích hợp dữ liệu phi cấu trúc (viễn thông, thương mại điện tử) trong tương lai.\n• Kết nối hệ thống chấm điểm tín dụng quốc gia CIC Việt Nam nâng cao độ chính xác.", 
     AMBER_BR)
]

sw = Inches(3.55)
sgap = Inches(0.34)
sy = Inches(1.65)
sh = Inches(3.25)

for i, (stitle, sdesc, scolor) in enumerate(summary_cards):
    sx = Inches(1.0) + i * (sw + sgap)
    create_styled_card(slide10, sx, sy, sw, sh, bg_color=DARK_CARD, border_color=scolor, border_width=1.5)
    
    tb = slide10.shapes.add_textbox(sx + Inches(0.18), sy + Inches(0.14), sw - Inches(0.36), sh - Inches(0.28))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    
    p = tf.paragraphs[0]
    p.text = stitle
    p.font.name = FONT_FAMILY
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = scolor
    
    p2 = tf.add_paragraph()
    p2.text = sdesc
    p2.font.name = FONT_FAMILY
    p2.font.size = Pt(9.5)
    p2.font.color.rgb = RGBColor(226, 232, 240)
    p2.space_before = Pt(6)

# Bottom Thank You & Links Bar
create_styled_card(slide10, Inches(1.0), Inches(5.15), Inches(11.333), Inches(1.8), bg_color=DARK_CARD, border_color=CYAN_ACCENT, border_width=1.5)
tb_ty = slide10.shapes.add_textbox(Inches(1.2), Inches(5.35), Inches(10.933), Inches(1.4))
tfty = tb_ty.text_frame
tfty.word_wrap = True
tfty.margin_left = tfty.margin_top = tfty.margin_right = tfty.margin_bottom = 0

p = tfty.paragraphs[0]
p.text = "XIN TRÂN TRỌNG CẢM ƠN HỘI ĐỒNG GIÁM KHẢO VÀ GIẢNG VIÊN TS. TRẦN MẠNH TƯỜNG!"
p.font.name = FONT_FAMILY
p.font.size = Pt(13.5)
p.font.bold = True
p.font.color.rgb = WHITE
p.alignment = PP_ALIGN.CENTER

p2 = tfty.add_paragraph()
p2.text = "Sinh viên thực hiện: Lê Thành Hiệu  |  MSSV: 24520496  |  Trường Đại học Tài chính - Marketing (UFM)  |  Khóa SIC 2026"
p2.font.name = FONT_FAMILY
p2.font.size = Pt(11)
p2.font.color.rgb = AMBER_BR
p2.alignment = PP_ALIGN.CENTER
p2.space_before = Pt(6)

p3 = tfty.add_paragraph()
p3.text = "Databricks Workspace: Folder 907137357494385   •   GitHub: github.com/snowflake-vibing/Credit_Scoring_Project"
p3.font.name = FONT_FAMILY
p3.font.size = Pt(10)
p3.font.color.rgb = RGBColor(148, 163, 184)
p3.alignment = PP_ALIGN.CENTER
p3.space_before = Pt(4)

print("✅ Slide 10 hoàn tất.")

# Lưu file PowerPoint
output_pptx = "slide_bao_ve_de_tai_7.pptx"
prs.save(output_pptx)
print(f"\n🎉 HOÀN TẤT TÁI THIẾT KẾ VỚI PHÔNG MONTSERRAT: {output_pptx}")
