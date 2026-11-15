# -*- coding: utf-8 -*-
"""
Script tạo Slide thuyết trình Đề tài 7 chuẩn quốc tế với phông chữ Montserrat.
- Giãn dòng chuẩn 1.5 (line_spacing = 1.5) trên toàn bộ slide, cực kỳ thoáng đãng, dễ đọc.
- Tinh giản tối đa câu từ, chỉ giữ thông tin trọng tâm và số liệu đắt giá nhất.
- Giữ nguyên 100% tỷ lệ gốc biểu đồ (không co bóp, méo mó).
- Màu sắc thẻ card phong phú, hiện đại, có icon nhận diện trực quan.
- Loại bỏ hoàn toàn header/footer thừa.
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

print("🚀 Bắt đầu tạo Slide bảo vệ Đề tài 7: Montserrat, Spacing 1.5, Tinh giản nội dung...")

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
p3.line_spacing = 1.3
p3.space_before = Pt(12)

p4 = tf1.add_paragraph()
p4.text = "Phân tích Big Data & Machine Learning phân tán trên nền tảng Databricks Lakehouse"
p4.font.name = FONT_FAMILY
p4.font.size = Pt(13.5)
p4.font.italic = True
p4.font.color.rgb = RGBColor(148, 163, 184)
p4.space_before = Pt(10)

# 3 Info Cards (Concise, Spacing 1.5)
info_cards = [
    ("👤 SINH VIÊN THỰC HIỆN", "Lê Thành Hiệu", "MSSV: 24520496", "Lớp SIC Big Data 2026", EMERALD_BR),
    ("👨‍🏫 GIẢNG VIÊN HƯỚNG DẪN", "TS. Trần Mạnh Tường", "Khoa Công nghệ Thông tin", "Đại học Tài chính - Marketing", BLUE_BR),
    ("⚡ HẠ TẦNG & DỮ LIỆU", "Databricks Lakehouse", "LendingClub: 2.26 triệu dòng", "Apache PySpark phân tán", AMBER_BR)
]

c_w = Inches(3.55)
c_gap = Inches(0.34)
c_y = Inches(5.0)
c_h = Inches(1.8)

for i, (tag, val, sub1, sub2, accent) in enumerate(info_cards):
    cx = Inches(1.0) + i * (c_w + c_gap)
    create_styled_card(slide1, cx, c_y, c_w, c_h, bg_color=DARK_CARD, border_color=accent, border_width=1.5)
    
    tb = slide1.shapes.add_textbox(cx + Inches(0.2), c_y + Inches(0.18), c_w - Inches(0.4), c_h - Inches(0.36))
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
    pv.font.size = Pt(15)
    pv.font.bold = True
    pv.font.color.rgb = WHITE
    pv.space_before = Pt(4)
    
    ps1 = tf.add_paragraph()
    ps1.text = sub1
    ps1.font.name = FONT_FAMILY
    ps1.font.size = Pt(10)
    ps1.font.color.rgb = RGBColor(226, 232, 240)
    ps1.line_spacing = 1.5
    ps1.space_before = Pt(5)
    
    ps2 = tf.add_paragraph()
    ps2.text = sub2
    ps2.font.name = FONT_FAMILY
    ps2.font.size = Pt(9)
    ps2.font.color.rgb = RGBColor(148, 163, 184)
    ps2.line_spacing = 1.5
    ps2.space_before = Pt(2)

print("✅ Slide 1 hoàn tất.")

# ==============================================================================
# SLIDE 2: ĐẶT VẤN ĐỀ NGHIỆP VỤ & 5VS BIG DATA (CONCISE & SPACING 1.5)
# ==============================================================================
slide2 = prs.slides.add_slide(blank_layout)
set_slide_background(slide2, LIGHT_BG)
add_clean_title(slide2, "1. Bối Cảnh Nghiệp Vụ & Mô Hình 5Vs Dữ Liệu Lớn")

probs = [
    ("🔴 NỢ XẤU LỊCH SỬ CAO (21.82%)", 
     [("Tổn thất tín dụng lớn:", "Gây rủi ro thất thoát vốn nghiêm trọng cho ngân hàng."),
      ("Áp lực trích lập dự phòng:", "Bào mòn lợi nhuận ròng theo Thông tư 11/2021/TT-NHNN.")],
     ROSE_BG, ROSE_BR, ROSE_TX),
    ("⏱️ THẨM ĐỊNH THỦ CÔNG (2 - 5 NGÀY)", 
     [("Tốn kém chi phí vận hành:", "Thẩm tra giấy tờ thủ công, dễ mắc sai lầm cảm tính."),
      ("Đánh mất khách hàng số:", "Không đáp ứng nhu cầu vay tức thì (Instant Credit / BNPL).")],
     AMBER_BG, AMBER_BR, AMBER_TX),
    ("🎯 MỤC TIÊU DỰ ÁN", 
     [("Phê duyệt tự động siêu tốc:", "Đạt tỷ lệ STP > 75% trong thời gian dưới 3 phút."),
      ("Kiểm soát rủi ro danh mục:", "Kéo giảm tỷ lệ nợ xấu từ 21.82% xuống dưới 4.2%.")],
     BLUE_BG, BLUE_BR, BLUE_TX)
]

py = Inches(1.55)
ph = Inches(1.68)
pgap = Inches(0.14)

for i, (p_title, p_bullets, bg_c, br_c, tx_c) in enumerate(probs):
    cur_y = py + i * (ph + pgap)
    create_styled_card(slide2, Inches(0.8), cur_y, Inches(5.6), ph, bg_color=bg_c, border_color=br_c, border_width=1.5)
    
    tb = slide2.shapes.add_textbox(Inches(1.0), cur_y + Inches(0.16), Inches(5.2), ph - Inches(0.32))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    
    p = tf.paragraphs[0]
    p.text = p_title
    p.font.name = FONT_FAMILY
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = tx_c
    
    for lead, desc in p_bullets:
        p_b = tf.add_paragraph()
        p_b.text = f"• {lead} {desc}"
        p_b.font.name = FONT_FAMILY
        p_b.font.size = Pt(10.5)
        p_b.font.color.rgb = TEXT_DARK
        p_b.line_spacing = 1.5
        p_b.space_before = Pt(8)

# Right Column: 5Vs Big Data Card (Sharp, Concise, Spacing 1.5)
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
    ("📦 Volume (Quy mô):", "2,260,701 dòng (1.6 GB) — Vượt giới hạn RAM máy tính trạm."),
    ("⚡ Velocity (Tốc độ):", "Chấm điểm thời gian thực, ra quyết định dưới 3 phút / hồ sơ."),
    ("🗂️ Variety (Đa dạng):", "Kết hợp biến định lượng, biến danh mục và lịch sử tín dụng."),
    ("🛡️ Veracity (Tin cậy):", "Lọc ngoại lai, điền khuyết trung vị thận trọng tại Silver Layer."),
    ("💎 Value (Giá trị):", "Giảm nợ xấu về 4.18%, tiết kiệm hơn 176.4 tỷ VNĐ tổn thất.")
]

for k, v in fives:
    p_v = tf_r.add_paragraph()
    p_v.text = f"• {k} {v}"
    p_v.font.name = FONT_FAMILY
    p_v.font.size = Pt(10.5)
    p_v.font.color.rgb = TEXT_DARK
    p_v.line_spacing = 1.5
    p_v.space_before = Pt(10)

p_sum = tf_r.add_paragraph()
p_sum.text = "💡 KẾT LUẬN: Đòi hỏi hạ tầng phân tán Databricks & PySpark xử lý toàn diện!"
p_sum.font.name = FONT_FAMILY
p_sum.font.size = Pt(10)
p_sum.font.bold = True
p_sum.font.color.rgb = EMERALD_TX
p_sum.line_spacing = 1.5
p_sum.space_before = Pt(14)

print("✅ Slide 2 hoàn tất.")

# ==============================================================================
# SLIDE 3: KIẾN TRÚC DATABRICKS LAKEHOUSE MEDALLION (NATIVE VECTOR DIAGRAM & KEYWORDS)
# ==============================================================================
slide3 = prs.slides.add_slide(blank_layout)
set_slide_background(slide3, LIGHT_BG)
add_clean_title(slide3, "2. Quản Trị & Lưu Trữ Dữ Liệu Theo Kiến Trúc Medallion")

tiers = [
    {
        "step": "BƯỚC 1",
        "title": "NGUỒN DỮ LIỆU",
        "sub": "Raw Data Sources",
        "badge": "LendingClub Dataset",
        "header_bg": RGBColor(30, 41, 59),
        "border_c": RGBColor(71, 85, 105),
        "pill_bg": RGBColor(241, 245, 249),
        "pill_tx": RGBColor(30, 41, 59),
        "pill_title": "TẬP DỮ LIỆU GỐC",
        "pill_sub": "1.6 GB • 2.26M dòng",
        "keywords": [
            ("Quy mô:", "2,260,701 hồ sơ vay"),
            ("Định dạng:", "Tệp nén CSV (1.6 GB)"),
            ("Thuộc tính:", "151 trường thông tin"),
            ("Nợ xấu nền:", "21.82% toàn danh mục"),
            ("Tiếp nhận:", "PySpark Batch Ingest")
        ]
    },
    {
        "step": "BƯỚC 2",
        "title": "TẦNG BRONZE",
        "sub": "Raw Lakehouse Layer",
        "badge": "workspace.bronze",
        "header_bg": RGBColor(180, 83, 9),
        "border_c": RGBColor(217, 119, 6),
        "pill_bg": RGBColor(254, 243, 199),
        "pill_tx": RGBColor(180, 83, 9),
        "pill_title": "TOÀN VẸN GIAO DỊCH",
        "pill_sub": "100% ACID Log Audit",
        "keywords": [
            ("Bảng Delta:", "bronze_credit_data"),
            ("Lưu trữ:", "Delta Lake (Parquet)"),
            ("Nguyên tắc:", "Bất biến (As-Is Data)"),
            ("Bảo toàn:", "100% dữ liệu nguyên bản"),
            ("Kiểm toán:", "Time Travel v0 Audit")
        ]
    },
    {
        "step": "BƯỚC 3",
        "title": "TẦNG SILVER",
        "sub": "Curated & Enriched",
        "badge": "workspace.silver",
        "header_bg": RGBColor(29, 78, 216),
        "border_c": RGBColor(37, 99, 235),
        "pill_bg": RGBColor(239, 246, 255),
        "pill_tx": RGBColor(29, 78, 216),
        "pill_title": "DỮ LIỆU SẠCH & CHUẨN",
        "pill_sub": "12 Features Đầu Vào",
        "keywords": [
            ("Bảng Delta:", "silver_credit_data"),
            ("Lọc logic:", "Tuổi (18-80) & Thu nhập"),
            ("Điền khuyết:", "Median lãi suất 11%"),
            ("Kỹ nghệ:", "DTI Ratio & CBI Index"),
            ("Phân chia:", "80% Train / 20% Test")
        ]
    },
    {
        "step": "BƯỚC 4",
        "title": "TẦNG GOLD",
        "sub": "AI Engine & Scoring",
        "badge": "workspace.gold",
        "header_bg": RGBColor(4, 120, 87),
        "border_c": RGBColor(16, 185, 129),
        "pill_bg": RGBColor(236, 253, 245),
        "pill_tx": RGBColor(4, 120, 87),
        "pill_title": "MÔ HÌNH HỌC MÁY",
        "pill_sub": "ROC-AUC = 0.8745",
        "keywords": [
            ("Bảng Delta:", "gold_credit_scoring"),
            ("Thuật toán:", "Random Forest (50 cây)"),
            ("Dự báo:", "Xác suất vỡ nợ (PD)"),
            ("Chấm điểm:", "FICO Score (300-850)"),
            ("Độ chính xác:", "Accuracy 87.16%")
        ]
    },
    {
        "step": "BƯỚC 5",
        "title": "QUYẾT ĐỊNH STP",
        "sub": "Automated Policy",
        "badge": "Core Banking / LOS",
        "header_bg": RGBColor(67, 56, 202),
        "border_c": RGBColor(99, 102, 241),
        "pill_bg": RGBColor(238, 242, 255),
        "pill_tx": RGBColor(67, 56, 202),
        "pill_title": "TỰ ĐỘNG HÓA CAO",
        "pill_sub": "Duyệt STP > 76% Hồ Sơ",
        "keywords": [
            ("Phân tầng:", "4 nhóm rủi ro tín dụng"),
            ("Định giá:", "Risk-Based Pricing"),
            ("Phê duyệt:", "STP 100% nhóm tốt"),
            ("Thời gian:", "Dưới 3 phút / hồ sơ"),
            ("Giá trị:", "Tiết kiệm 176.4 tỷ VNĐ")
        ]
    }
]

c_w = Inches(2.18)
c_gap = Inches(0.20)
c_y = Inches(1.55)
c_h = Inches(5.35)

for i, t in enumerate(tiers):
    cx = Inches(0.8) + i * (c_w + c_gap)
    
    # Outer card container
    card = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, c_y, c_w, c_h)
    card.fill.solid()
    card.fill.fore_color.rgb = WHITE
    card.line.color.rgb = t["border_c"]
    card.line.width = Pt(1.5)
    
    # Header shape
    head = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, c_y, c_w, Inches(1.08))
    head.fill.solid()
    head.fill.fore_color.rgb = t["header_bg"]
    head.line.fill.background()
    
    # Header text
    tb_h = slide3.shapes.add_textbox(cx, c_y + Inches(0.08), c_w, Inches(0.92))
    tf_h = tb_h.text_frame
    tf_h.word_wrap = True
    tf_h.margin_left = tf_h.margin_right = tf_h.margin_top = tf_h.margin_bottom = 0
    
    p = tf_h.paragraphs[0]
    p.text = t["step"]
    p.font.name = FONT_FAMILY
    p.font.size = Pt(8.5)
    p.font.bold = True
    p.font.color.rgb = RGBColor(226, 232, 240)
    p.alignment = PP_ALIGN.CENTER
    
    p2 = tf_h.add_paragraph()
    p2.text = t["title"]
    p2.font.name = FONT_FAMILY
    p2.font.size = Pt(10.5)
    p2.font.bold = True
    p2.font.color.rgb = WHITE
    p2.alignment = PP_ALIGN.CENTER
    p2.space_before = Pt(1)
    
    p3 = tf_h.add_paragraph()
    p3.text = t["sub"]
    p3.font.name = FONT_FAMILY
    p3.font.size = Pt(8.2)
    p3.font.italic = True
    p3.font.color.rgb = RGBColor(203, 213, 225)
    p3.alignment = PP_ALIGN.CENTER
    p3.space_before = Pt(1)
    
    # Body keywords textbox
    tb_b = slide3.shapes.add_textbox(cx + Inches(0.12), c_y + Inches(1.18), c_w - Inches(0.24), Inches(3.3))
    tf_b = tb_b.text_frame
    tf_b.word_wrap = True
    tf_b.margin_left = tf_b.margin_right = tf_b.margin_top = tf_b.margin_bottom = 0
    
    # Sub badge
    p_sub = tf_b.paragraphs[0]
    p_sub.text = f"🏷️ {t['badge']}"
    p_sub.font.name = FONT_FAMILY
    p_sub.font.size = Pt(8.5)
    p_sub.font.bold = True
    p_sub.font.color.rgb = t["header_bg"]
    
    for lead, val in t["keywords"]:
        pb = tf_b.add_paragraph()
        pb.text = f"• {lead} {val}"
        pb.font.name = FONT_FAMILY
        pb.font.size = Pt(9.2)
        pb.font.color.rgb = TEXT_DARK
        pb.line_spacing = 1.5
        pb.space_before = Pt(6)
        
    # Bottom KPI Box
    pill_h = Inches(0.68)
    pill_y = c_y + c_h - pill_h - Inches(0.12)
    pill = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx + Inches(0.1), pill_y, c_w - Inches(0.2), pill_h)
    pill.fill.solid()
    pill.fill.fore_color.rgb = t["pill_bg"]
    pill.line.color.rgb = t["border_c"]
    pill.line.width = Pt(1.2)
    
    tb_pill = slide3.shapes.add_textbox(cx + Inches(0.12), pill_y + Inches(0.08), c_w - Inches(0.24), pill_h - Inches(0.16))
    tf_pill = tb_pill.text_frame
    tf_pill.word_wrap = True
    tf_pill.margin_left = tf_pill.margin_right = tf_pill.margin_top = tf_pill.margin_bottom = 0
    
    p_pt = tf_pill.paragraphs[0]
    p_pt.text = t["pill_title"]
    p_pt.font.name = FONT_FAMILY
    p_pt.font.size = Pt(8)
    p_pt.font.bold = True
    p_pt.font.color.rgb = t["pill_tx"]
    p_pt.alignment = PP_ALIGN.CENTER
    
    p_ps = tf_pill.add_paragraph()
    p_ps.text = t["pill_sub"]
    p_ps.font.name = FONT_FAMILY
    p_ps.font.size = Pt(9.5)
    p_ps.font.bold = True
    p_ps.font.color.rgb = t["pill_tx"]
    p_ps.alignment = PP_ALIGN.CENTER
    p_ps.space_before = Pt(1)

    # Connector arrow to next stage
    if i < len(tiers) - 1:
        arr_x = cx + c_w
        arr_y = c_y + Inches(0.35)
        tb_arr = slide3.shapes.add_textbox(arr_x, arr_y, c_gap, Inches(0.4))
        tfa = tb_arr.text_frame
        tfa.margin_left = tfa.margin_right = tfa.margin_top = tfa.margin_bottom = 0
        pa = tfa.paragraphs[0]
        pa.text = "➔"
        pa.font.name = FONT_FAMILY
        pa.font.size = Pt(14)
        pa.font.bold = True
        pa.font.color.rgb = RGBColor(148, 163, 184)
        pa.alignment = PP_ALIGN.CENTER

print("✅ Slide 3 hoàn tất.")

# ==============================================================================
# SLIDE 4: PHÂN TÍCH KHÁM PHÁ & SPARK SQL (CONCISE & SPACING 1.5)
# ==============================================================================
slide4 = prs.slides.add_slide(blank_layout)
set_slide_background(slide4, LIGHT_BG)
add_clean_title(slide4, "3. Phân Tích Khám Phá & Chỉ Số Kinh Doanh (Spark SQL)")

add_proportional_image(slide4, "images/hinh_3_2_npl_intent_home.png", Inches(0.8), Inches(1.55), Inches(6.1), Inches(5.32))

s4_insights = [
    ("🩺 VAY Y TẾ: RỦI RO CAO NHẤT (26.8%)", 
     ["Biến cố sức khỏe đột xuất làm gián đoạn trực tiếp nguồn thu nhập trả nợ.",
      "Vay Giáo dục (Education) an toàn nhất với tỷ lệ nợ xấu chỉ 15.4%."], 
     ROSE_BG, ROSE_BR, ROSE_TX),
    ("📈 NỢ XẤU TĂNG ĐƠN ĐIỆU THEO HẠNG VAY", 
     ["Hạng A (ưu tú): Nợ xấu chỉ 5.8% (lãi suất ưu đãi 7.2%/năm).",
      "Hạng G (rủi ro cao): Nợ xấu lên tới 65.4% (lãi suất bù đắp > 20%/năm)."], 
     BLUE_BG, BLUE_BR, BLUE_TX),
    ("🏠 THUÊ NHÀ RỦI RO GẤP ĐÔI SỞ HỮU NHÀ", 
     ["Khách Đi thuê (Rent): Nợ xấu 25.6% do thiếu hụt tài sản bảo đảm.",
      "Sở hữu nhà (Mortgage / Own): Nợ xấu chỉ 12.8% (thấp hơn đúng một nửa)."], 
     AMBER_BG, AMBER_BR, AMBER_TX)
]

iy = Inches(1.55)
ih = Inches(1.68)
igap = Inches(0.14)

for i, (ititle, ibullets, bg_c, br_c, tx_c) in enumerate(s4_insights):
    cur_y = iy + i * (ih + igap)
    create_styled_card(slide4, Inches(7.1), cur_y, Inches(5.433), ih, bg_color=bg_c, border_color=br_c, border_width=1.5)
    
    tb = slide4.shapes.add_textbox(Inches(7.3), cur_y + Inches(0.16), Inches(5.0), ih - Inches(0.32))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    
    p = tf.paragraphs[0]
    p.text = ititle
    p.font.name = FONT_FAMILY
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = tx_c
    
    for b_item in ibullets:
        pb = tf.add_paragraph()
        pb.text = f"• {b_item}"
        pb.font.name = FONT_FAMILY
        pb.font.size = Pt(10.5)
        pb.font.color.rgb = TEXT_DARK
        pb.line_spacing = 1.5
        pb.space_before = Pt(8)

print("✅ Slide 4 hoàn tất.")

# ==============================================================================
# SLIDE 5: KỸ NGHỆ ĐẶC TRƯNG & SPARK MLLIB PIPELINE (CONCISE & SPACING 1.5)
# ==============================================================================
slide5 = prs.slides.add_slide(blank_layout)
set_slide_background(slide5, LIGHT_BG)
add_clean_title(slide5, "4. Kỹ Nghệ Đặc Trưng & Quy Trình Spark MLlib Pipeline")

# Top: 2 Formula Cards
create_styled_card(slide5, Inches(0.8), Inches(1.55), Inches(5.7), Inches(1.4), bg_color=INDIGO_BG, border_color=INDIGO_BR, border_width=1.5)
tb_f1 = slide5.shapes.add_textbox(Inches(1.0), Inches(1.68), Inches(5.3), Inches(1.15))
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
p3.text = "• Đo lường mức độ đòn bẩy tài chính; ngưỡng cảnh báo rủi ro khi DTI > 0.35."
p3.font.name = FONT_FAMILY
p3.font.size = Pt(10)
p3.font.color.rgb = TEXT_DARK
p3.line_spacing = 1.5
p3.space_before = Pt(4)

create_styled_card(slide5, Inches(6.8), Inches(1.55), Inches(5.733), Inches(1.4), bg_color=BLUE_BG, border_color=BLUE_BR, border_width=1.5)
tb_f2 = slide5.shapes.add_textbox(Inches(7.0), Inches(1.68), Inches(5.3), Inches(1.15))
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
p3.text = "• Độc quyền đề tài: Đo lường lãi suất hàng năm bào mòn ngân sách chi tiêu."
p3.font.name = FONT_FAMILY
p3.font.size = Pt(10)
p3.font.color.rgb = TEXT_DARK
p3.line_spacing = 1.5
p3.space_before = Pt(4)

# Bottom: 4 Pipeline Process Cards (Fitted, Spacing 1.5)
pipeline_cols = [
    ("STAGE 1", "🔤 StringIndexer", 
     ["Mã hóa 3 biến danh mục sang chỉ số (*_idx).",
      "handleInvalid='keep': Tự gán nhãn an toàn.",
      "Tối ưu hóa tốc độ xử lý phân tán."], 
     BLUE_BG, BLUE_BR, BLUE_TX),
    ("STAGE 2", "🔢 OneHotEncoder", 
     ["Chuyển chỉ số sang Sparse Vector (*_vec).",
      "Tránh áp đặt thứ tự giả định sai lệch.",
      "Tiết kiệm 85% bộ nhớ RAM tính toán."], 
     INDIGO_BG, INDIGO_BR, INDIGO_TX),
    ("STAGE 3", "📐 Assembler & Scaler", 
     ["VectorAssembler: Gom 11 đặc trưng.",
      "StandardScaler: Chuẩn hóa thang đo Z-score.",
      "Triệt tiêu sai lệch thứ nguyên thu nhập và tuổi."], 
     AMBER_BG, AMBER_BR, AMBER_TX),
    ("STAGE 4", "🌲 Random Forest", 
     ["50 cây quyết định phân tán (maxDepth=10).",
      "Bắt trọn quan hệ phi tuyến giữa đòn bẩy và nợ.",
      "Tối ưu hóa ROC-AUC = 0.8745 trên tập kiểm thử."], 
     EMERALD_BG, EMERALD_BR, EMERALD_TX)
]

col_w = Inches(2.78)
col_gap = Inches(0.2)
col_y = Inches(3.2)
col_h = Inches(3.65)

for i, (s_num, s_title, s_bullets, bg_c, br_c, tx_c) in enumerate(pipeline_cols):
    cx = Inches(0.8) + i * (col_w + col_gap)
    create_styled_card(slide5, cx, col_y, col_w, col_h, bg_color=bg_c, border_color=br_c, border_width=1.5)
    
    tb = slide5.shapes.add_textbox(cx + Inches(0.14), col_y + Inches(0.18), col_w - Inches(0.28), col_h - Inches(0.36))
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
    
    for b_item in s_bullets:
        pb = tf.add_paragraph()
        pb.text = f"• {b_item}"
        pb.font.name = FONT_FAMILY
        pb.font.size = Pt(10)
        pb.font.color.rgb = TEXT_DARK
        pb.line_spacing = 1.5
        pb.space_before = Pt(8)

print("✅ Slide 5 hoàn tất.")

# ==============================================================================
# SLIDE 6: ĐÁNH GIÁ HIỆU NĂNG MÔ HÌNH (CONCISE & SPACING 1.5)
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

# Split bottom into 2 concise cards with Spacing 1.5
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
p2.text = "• ROC-AUC đạt 0.8745: Phân tách rủi ro vượt trội hoàn toàn so với baseline.\n• Cân bằng tối ưu: F1-Score 0.8468 giúp vừa chặn nợ xấu vừa không từ chối nhầm khách tốt."
p2.font.name = FONT_FAMILY
p2.font.size = Pt(9.5)
p2.font.color.rgb = TEXT_DARK
p2.line_spacing = 1.5
p2.space_before = Pt(3)

create_styled_card(slide6, Inches(1.0), Inches(5.65), Inches(6.3), Inches(1.15), bg_color=BLUE_BG, border_color=BLUE_BR, border_width=1.5)
tb_h2 = slide6.shapes.add_textbox(Inches(1.15), Inches(5.72), Inches(6.0), Inches(1.0))
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
p2.text = "• Bắt trọn 84.04% khoản vay vỡ nợ (Recall = 84.04%) trước khi giải ngân.\n• Giữ FPR chỉ 3.65%, bảo vệ tối đa trải nghiệm khách hàng uy tín."
p2.font.name = FONT_FAMILY
p2.font.size = Pt(9.5)
p2.font.color.rgb = TEXT_DARK
p2.line_spacing = 1.5
p2.space_before = Pt(3)

add_proportional_image(slide6, "images/hinh_4_1_roc_curve.png", Inches(7.7), Inches(1.55), Inches(4.833), Inches(5.32))

print("✅ Slide 6 hoàn tất.")

# ==============================================================================
# SLIDE 7: MA TRẬN NHẦM LẪN & FEATURE IMPORTANCE (CONCISE & SPACING 1.5)
# ==============================================================================
slide7 = prs.slides.add_slide(blank_layout)
set_slide_background(slide7, LIGHT_BG)
add_clean_title(slide7, "6. Ma Trận Nhầm Lẫn & Trích Xuất Độ Quan Trọng Đặc Trưng")

add_proportional_image(slide7, "images/hinh_4_2_confusion_matrix.png", Inches(0.8), Inches(1.55), Inches(5.3), Inches(5.32))

fi_cards = [
    ("🥇 #1 LÃI SUẤT KHOẢN VAY (loan_int_rate - 38.2%)", 
     [("Chi phối 38.2% sức mạnh mô hình; là nhân tố phân tách rủi ro hàng đầu."),
      ("Người vay chấp nhận lãi suất cao thường có rủi ro nội tại nghiêm trọng.")], 
     ROSE_BG, ROSE_BR, ROSE_TX),
    ("🥈 #2 TỶ LỆ NỢ TRÊN THU NHẬP (dti_ratio - 24.5%)", 
     [("Quyết định trực tiếp năng lực cân đối dòng tiền trả nợ hàng tháng."),
      ("Nhóm có DTI > 0.40 có xác suất vỡ nợ tăng gấp 3.2 lần bình thường.")], 
     AMBER_BG, AMBER_BR, AMBER_TX),
    ("🥉 #3 CHỈ SỐ GÁNH NẶNG TÍN DỤNG (cbi_index - 15.8%)", 
     [("Chỉ số độc quyền kết hợp giữa quy mô vay, lãi suất và thu nhập."),
      ("Phản ánh áp lực dòng tiền mặt thực tế phải chi trả lãi suất hàng tháng.")], 
     BLUE_BG, BLUE_BR, BLUE_TX)
]

fy = Inches(1.55)
fh = Inches(1.22)
fgap = Inches(0.14)

for i, (ftitle, fbullets, bg_c, br_c, tx_c) in enumerate(fi_cards):
    cur_y = fy + i * (fh + fgap)
    create_styled_card(slide7, Inches(6.3), cur_y, Inches(6.233), fh, bg_color=bg_c, border_color=br_c, border_width=1.5)
    
    tb = slide7.shapes.add_textbox(Inches(6.45), cur_y + Inches(0.12), Inches(5.9), fh - Inches(0.24))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    
    p = tf.paragraphs[0]
    p.text = ftitle
    p.font.name = FONT_FAMILY
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = tx_c
    
    for b_item in fbullets:
        pb = tf.add_paragraph()
        pb.text = f"• {b_item}"
        pb.font.name = FONT_FAMILY
        pb.font.size = Pt(9.5)
        pb.font.color.rgb = TEXT_DARK
        pb.line_spacing = 1.5
        pb.space_before = Pt(3)

create_styled_card(slide7, Inches(6.3), Inches(5.63), Inches(6.233), Inches(1.24), bg_color=EMERALD_BG, border_color=EMERALD_BR, border_width=1.5)
tb_t = slide7.shapes.add_textbox(Inches(6.45), Inches(5.75), Inches(5.9), Inches(1.0))
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
p2.text = "• Đòn bẩy nợ (DTI & CBI) quan trọng hơn nhiều so với thu nhập danh nghĩa!\n• Tuyệt đối không phê duyệt chỉ dựa vào thu nhập cao nếu nghĩa vụ trả nợ hiện tại đã quá tải."
p2.font.name = FONT_FAMILY
p2.font.size = Pt(9.5)
p2.font.color.rgb = TEXT_DARK
p2.line_spacing = 1.5
p2.space_before = Pt(3)

print("✅ Slide 7 hoàn tất.")

# ==============================================================================
# SLIDE 8: TÁC ĐỘNG TÀI CHÍNH & HIỆU QUẢ KINH TẾ (CONCISE & SPACING 1.5)
# ==============================================================================
slide8 = prs.slides.add_slide(blank_layout)
set_slide_background(slide8, LIGHT_BG)
add_clean_title(slide8, "7. Tác Động Tài Chính & Hiệu Quả Vận Hành Cho Doanh Nghiệp")

kpis = [
    ("💰 176.4 TỶ VNĐ", "TIẾT KIỆM TỔN THẤT TÍN DỤNG", "Ước tính trên danh mục 1,000 tỷ VNĐ cho vay tín chấp; cắt giảm dự phòng theo Thông tư 11/2021/TT-NHNN.", EMERALD_BG, EMERALD_BR, EMERALD_TX),
    ("📉 21.82% → 4.18%", "KÉO GIẢM TỶ LỆ NỢ XẤU NPL", "Kéo giảm nợ xấu danh mục về mức an toàn cao, cải thiện hệ số an toàn vốn CAR và tăng biên lãi NIM.", BLUE_BG, BLUE_BR, BLUE_TX),
    ("🎯 84.04%", "PHÁT HIỆN SỚM NỢ XẤU", "Phát hiện chính xác 84.04% khoản vay có nguy cơ vỡ nợ trước khi giải ngân, chặn đứng nợ xấu từ đầu.", AMBER_BG, AMBER_BR, AMBER_TX)
]

kw = Inches(3.75)
kgap = Inches(0.24)
ky = Inches(1.55)
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
    p3.line_spacing = 1.4
    p3.space_before = Pt(4)

# Bottom Section: Operational Impact Cards (Concise, Spacing 1.5)
bot_w = Inches(5.75)
bot_y = Inches(4.0)
bot_h = Inches(2.8)

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
    ("Tốc độ xử lý siêu tốc:", "Thời gian duyệt hồ sơ giảm từ 2 - 5 ngày xuống dưới 3 phút."),
    ("Tự động hóa toàn diện:", "Phê duyệt 254,919 hồ sơ (56.5%) giải ngân thẳng không duyệt tay."),
    ("Tích hợp kênh số linh hoạt:", "Đấu nối API mô hình vào Mobile Banking và hệ thống LOS ngân hàng.")
]
for title_pt, desc_pt in b1_points:
    p_pt = tfb1.add_paragraph()
    p_pt.text = f"• {title_pt} {desc_pt}"
    p_pt.font.name = FONT_FAMILY
    p_pt.font.size = Pt(10.5)
    p_pt.font.color.rgb = TEXT_DARK
    p_pt.line_spacing = 1.5
    p_pt.space_before = Pt(8)

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
    ("Tiết giảm chi phí nhân sự:", "Cắt giảm 65% khối lượng kiểm tra giấy tờ thủ công cho đội ngũ tín dụng."),
    ("Tối ưu hóa nguồn lực:", "Tái phân bổ nhân sự sang chăm sóc khách hàng VIP và xử lý nợ chuyên sâu."),
    ("Loại bỏ rủi ro đạo đức:", "Chuẩn hóa thuật toán, loại bỏ hoàn toàn sai lệch cảm tính của chuyên viên.")
]
for title_pt, desc_pt in b2_points:
    p_pt = tfb2.add_paragraph()
    p_pt.text = f"• {title_pt} {desc_pt}"
    p_pt.font.name = FONT_FAMILY
    p_pt.font.size = Pt(10.5)
    p_pt.font.color.rgb = TEXT_DARK
    p_pt.line_spacing = 1.5
    p_pt.space_before = Pt(8)

print("✅ Slide 8 hoàn tất.")

# ==============================================================================
# SLIDE 9: KHUNG CHÍNH SÁCH QUẢN TRỊ (CONCISE & SPACING 1.5)
# ==============================================================================
slide9 = prs.slides.add_slide(blank_layout)
set_slide_background(slide9, LIGHT_BG)
add_clean_title(slide9, "8. Đề Xuất Chính Sách: FICO Scoring & Risk-Based Pricing")

# Top Half: Panoramic Chart (Hinh 5.1: Aspect 2.692) - FULL WIDE DISPLAY, ZERO SQUISHING!
add_proportional_image(slide9, "images/hinh_5_1_risk_policy_charts.png", Inches(0.8), Inches(1.35), Inches(11.733), Inches(3.6))

# Bottom Half: 4 Distinct Color-Coded Cards side-by-side (Concise, Key Facts, Spacing 1.5)
policy_cards = [
    ("🟢 HẠNG 1: RỦI RO THẤP", 
     "FICO ≥ 720  |  254,919 hồ sơ (56.5%)", 
     ["Phê duyệt: Thẳng tự động 100% (STP)",
      "Lãi suất ưu đãi: 8.5%/năm",
      "Hạn mức: 100% đề xuất (Max $30,000)"], 
     EMERALD_BG, EMERALD_BR, EMERALD_TX),
    ("🔵 HẠNG 2: RỦI RO TRUNG BÌNH", 
     "FICO 650 - 719  |  119,123 hồ sơ (26.4%)", 
     ["Phê duyệt: Nhanh có điều kiện thu nhập",
      "Lãi suất tiêu chuẩn: 11.5%/năm",
      "Hạn mức: 80% đề xuất (Max $20,000)"], 
     BLUE_BG, BLUE_BR, BLUE_TX),
    ("🟠 HẠNG 3: RỦI RO CAO", 
     "FICO 580 - 649  |  48,774 hồ sơ (10.8%)", 
     ["Phê duyệt: Thẩm định thủ công / bảo lãnh",
      "Lãi suất bù đắp: 14.5%/năm",
      "Hạn mức: 50% đề xuất (Max $10,000)"], 
     AMBER_BG, AMBER_BR, AMBER_TX),
    ("🔴 HẠNG 4: RỦI RO RẤT CAO", 
     "FICO < 580  |  28,645 hồ sơ (6.3%)", 
     ["Xử lý: Từ chối tự động để ngăn nợ xấu",
      "Hạn mức: 0% (Từ chối cấp tín dụng)",
      "Hướng dẫn: Tư vấn cải thiện điểm số"], 
     ROSE_BG, ROSE_BR, ROSE_TX)
]

pw = Inches(2.78)
pgap = Inches(0.2)
py = Inches(5.2)
ph = Inches(1.9)

for i, (ptitle, psub, pbullets, bg_c, br_c, tx_c) in enumerate(policy_cards):
    px = Inches(0.8) + i * (pw + pgap)
    create_styled_card(slide9, px, py, pw, ph, bg_color=bg_c, border_color=br_c, border_width=1.5)
    
    tb = slide9.shapes.add_textbox(px + Inches(0.14), py + Inches(0.12), pw - Inches(0.28), ph - Inches(0.24))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    
    p = tf.paragraphs[0]
    p.text = ptitle
    p.font.name = FONT_FAMILY
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = tx_c
    
    p_sub = tf.add_paragraph()
    p_sub.text = psub
    p_sub.font.name = FONT_FAMILY
    p_sub.font.size = Pt(8.5)
    p_sub.font.bold = True
    p_sub.font.color.rgb = TEXT_DARK
    p_sub.space_before = Pt(2)
    
    for b_item in pbullets:
        pb = tf.add_paragraph()
        pb.text = f"• {b_item}"
        pb.font.name = FONT_FAMILY
        pb.font.size = Pt(9.2)
        pb.font.color.rgb = TEXT_DARK
        pb.line_spacing = 1.5
        pb.space_before = Pt(4)

print("✅ Slide 9 hoàn tất.")

# ==============================================================================
# SLIDE 10: TỔNG KẾT & KẾT LUẬN (CONCISE & SPACING 1.5)
# ==============================================================================
slide10 = prs.slides.add_slide(blank_layout)
set_slide_background(slide10, DARK_BG)
add_clean_title(slide10, "9. Tổng Kết & Đóng Góp Thực Tiễn Của Đề Tài", dark_mode=True)

summary_cards = [
    ("☁️ LÀM CHỦ BIG DATA LAKEHOUSE", 
     ["Xử lý trọn vẹn 2.26 triệu bản ghi trên Databricks Lakehouse.",
      "Kiến trúc Medallion 3 tầng chuẩn mực với Delta Lake và ACID.",
      "Tối ưu hóa hiệu năng tính toán phân tán với PySpark SQL & MLlib."], 
     CYAN_ACCENT),
    ("💡 HIỆU QUẢ CHO DOANH NGHIỆP", 
     ["Mô hình Random Forest đạt ROC-AUC 0.8745 và Accuracy 87.16%.",
      "Tiết kiệm hơn 176.4 tỷ VNĐ tổn thất dự phòng rủi ro tín dụng.",
      "Thiết lập chính sách phân tầng FICO Score và Risk-Based Pricing khả thi."], 
     EMERALD_BR),
    ("🚀 SẴN SÀNG TRIỂN KHAI THỰC TẾ", 
     ["Mã nguồn mở kiểm thử 100% trên GitHub và Databricks Workspace.",
      "Sẵn sàng đóng gói REST API phục vụ tích hợp Core Banking và LOS.",
      "Định hướng mở rộng: Tích hợp dữ liệu viễn thông và điểm tín dụng CIC."], 
     AMBER_BR)
]

sw = Inches(3.55)
sgap = Inches(0.34)
sy = Inches(1.8)
sh = Inches(2.9)

for i, (stitle, sbullets, scolor) in enumerate(summary_cards):
    sx = Inches(1.0) + i * (sw + sgap)
    create_styled_card(slide10, sx, sy, sw, sh, bg_color=DARK_CARD, border_color=scolor, border_width=1.5)
    
    tb = slide10.shapes.add_textbox(sx + Inches(0.2), sy + Inches(0.18), sw - Inches(0.4), sh - Inches(0.36))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    
    p = tf.paragraphs[0]
    p.text = stitle
    p.font.name = FONT_FAMILY
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = scolor
    
    for b_item in sbullets:
        pb = tf.add_paragraph()
        pb.text = f"• {b_item}"
        pb.font.name = FONT_FAMILY
        pb.font.size = Pt(10)
        pb.font.color.rgb = RGBColor(226, 232, 240)
        pb.line_spacing = 1.5
        pb.space_before = Pt(10)

# Bottom Thank You & Links Bar
create_styled_card(slide10, Inches(1.0), Inches(4.95), Inches(11.333), Inches(2.05), bg_color=DARK_CARD, border_color=CYAN_ACCENT, border_width=1.5)
tb_ty = slide10.shapes.add_textbox(Inches(1.2), Inches(5.2), Inches(10.933), Inches(1.6))
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
p2.line_spacing = 1.5
p2.space_before = Pt(8)

p3 = tfty.add_paragraph()
p3.text = "Databricks Workspace: Folder 907137357494385   •   GitHub: github.com/snowflake-vibing/Credit_Scoring_Project"
p3.font.name = FONT_FAMILY
p3.font.size = Pt(10)
p3.font.color.rgb = RGBColor(148, 163, 184)
p3.alignment = PP_ALIGN.CENTER
p3.line_spacing = 1.5
p3.space_before = Pt(6)

print("✅ Slide 10 hoàn tất.")

# Lưu file PowerPoint
output_pptx = "slide_bao_ve_de_tai_7.pptx"
prs.save(output_pptx)
print(f"\n🎉 HOÀN TẤT TÁI THIẾT KẾ VỚI SPACING 1.5 & TINH GIẢN NỘI DUNG: {output_pptx}")
