import os
import sys
import docx
from docx import Document
from docx.shared import Inches, Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_SECTION, WD_ORIENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

print("Bắt đầu chuẩn hóa file Word (.docx) theo Quy định Luận văn / Tiểu luận ĐH Việt Nam (ĐH Cần Thơ)...")

import glob

target_docx_paths = glob.glob("qmd/**/*.docx", recursive=True) + glob.glob("qmd/*.docx")
target_docx_paths = list(set([os.path.normpath(p) for p in target_docx_paths]))
print(f"Tìm thấy các file docx cần chuẩn hóa: {target_docx_paths}")

def add_page_number_to_section(footer, align=WD_ALIGN_PARAGRAPH.CENTER):
    p = footer.paragraphs[0] if footer.paragraphs else footer.add_paragraph()
    p.alignment = align
    run = p.add_run("Trang ")
    run.font.name = "Times New Roman"
    run.font.size = Pt(13)
    
    # Thêm trường PAGE động trong Word XML
    fldSimple = OxmlElement('w:fldSimple')
    fldSimple.set(qn('w:instr'), 'PAGE')
    p._p.append(fldSimple)

def format_document(path):
    if not os.path.exists(path):
        print(f"Bỏ qua vì không tìm thấy: {path}")
        return
    
    doc = Document(path)
    
    # 1. Cấu hình Margins & Header/Footer cho tất cả các Section
    for idx, section in enumerate(doc.sections):
        # Lề: Top 2cm, Bottom 2cm, Left 3cm, Right 2cm
        section.top_margin = Cm(2.0)
        section.bottom_margin = Cm(2.0)
        section.left_margin = Cm(3.0)
        section.right_margin = Cm(2.0)
        
        # Header & Footer cách mép giấy 1.27 cm
        section.header_distance = Cm(1.27)
        section.footer_distance = Cm(1.27)
        
        # Xóa hoàn toàn Header và Footer theo yêu cầu người dùng ("khỏi header, footer đi")
        section.different_first_page_header_footer = False
        
        header = section.header
        header.is_linked_to_previous = False
        for hp in header.paragraphs:
            hp.text = ""
            
        footer = section.footer
        footer.is_linked_to_previous = False
        for fp in footer.paragraphs:
            fp.text = ""

    # 2. Chuẩn hóa font, căn lề và khoảng cách cho từng đoạn văn
    prev_was_sig_note = False
    in_cover_page = True
    
    for p in doc.paragraphs:
        txt = p.text.strip()
        
        # Thiết lập font Times New Roman mặc định
        for r in p.runs:
            if not r.font.name:
                r.font.name = "Times New Roman"

        # Nhận diện kết thúc trang bìa khi gặp LỜI CẢM ƠN
        if "LỜI CẢM ƠN" in txt:
            in_cover_page = False

        if in_cover_page:
            # Định dạng trang trọng cho Trang Bìa UFM & Samsung Innovation Campus (SIC)
            if any(term in txt for term in ["BỘ TÀI CHÍNH", "TRƯỜNG ĐẠI HỌC TÀI CHÍNH - MARKETING", "KHOA CÔNG NGHỆ THÔNG TIN", "CHƯƠNG TRÌNH SAMSUNG INNOVATION CAMPUS", "BỘ MÔN HỆ THỐNG THÔNG TIN QUẢN LÝ"]):
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.paragraph_format.space_before = Pt(2)
                p.paragraph_format.space_after = Pt(2)
                for r in p.runs:
                    r.font.name = "Times New Roman"
                    r.font.bold = True
                    r.font.size = Pt(12)
            elif "BÁO CÁO TIỂU LUẬN" in txt or "CAPSTONE PROJECT" in txt:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.paragraph_format.space_before = Pt(24)
                p.paragraph_format.space_after = Pt(4)
                for r in p.runs:
                    r.font.name = "Times New Roman"
                    r.font.bold = True
                    r.font.size = Pt(13)
            elif "DỮ LIỆU LỚN" in txt or "BIG DATA" in txt:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.paragraph_format.space_before = Pt(4)
                p.paragraph_format.space_after = Pt(2)
                for r in p.runs:
                    r.font.name = "Times New Roman"
                    r.font.bold = True
                    r.font.size = Pt(15)
            elif any(sub in txt for sub in ["PHỐI HỢP ĐÀO TẠO", "SAMSUNG INNOVATION CAMPUS - UFM", "BIG DATA ANALYTICS & ARTIFICIAL INTELLIGENCE IN BUSINESS"]):
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.paragraph_format.space_before = Pt(2)
                p.paragraph_format.space_after = Pt(20)
                for r in p.runs:
                    r.font.name = "Times New Roman"
                    r.font.italic = True
                    r.font.size = Pt(11)
            elif "ĐỀ TÀI NGHIÊN CỨU:" in txt:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.paragraph_format.space_before = Pt(16)
                p.paragraph_format.space_after = Pt(4)
                for r in p.runs:
                    r.font.name = "Times New Roman"
                    r.font.bold = True
                    r.font.size = Pt(13)
            elif "MÔ HÌNH CHẤM ĐIỂM TÍN DỤNG VÀ THẨM ĐỊNH RỦI RO VỠ NỢ" in txt:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.paragraph_format.space_before = Pt(4)
                p.paragraph_format.space_after = Pt(24)
                for r in p.runs:
                    r.font.name = "Times New Roman"
                    r.font.bold = True
                    r.font.size = Pt(16)
            elif any(txt.startswith(prefix) for prefix in ["Giảng viên hướng dẫn:", "Sinh viên thực hiện:", "Mã số sinh viên:", "Lớp / Khóa học:", "Khóa học / Đơn vị:", "Chuyên ngành:", "Kho lưu trữ mã nguồn:", "Không gian làm việc Databricks:"]):
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                p.paragraph_format.left_indent = Cm(1.5)
                p.paragraph_format.space_before = Pt(3)
                p.paragraph_format.space_after = Pt(3)
                p.paragraph_format.line_spacing = 1.15
                for r in p.runs:
                    r.font.name = "Times New Roman"
                    r.font.size = Pt(12)
            elif "TP. HỒ CHÍ MINH, NĂM 2026" in txt:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.paragraph_format.space_before = Pt(30)
                p.paragraph_format.space_after = Pt(6)
                for r in p.runs:
                    r.font.name = "Times New Roman"
                    r.font.bold = True
                    r.font.size = Pt(13)
            continue

        # Đoạn văn phần nội dung (sau trang bìa)
        p.paragraph_format.line_spacing = 1.2
        p.paragraph_format.space_before = Pt(6)
        p.paragraph_format.space_after = Pt(6)

        # Căn phải và chừa khoảng trống chữ ký theo đúng Hình 3 (Image 3)
        if "TP. Hồ Chí Minh" in txt and "Sinh viên thực hiện" in txt:
            p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
            p.paragraph_format.space_before = Pt(24)
            p.paragraph_format.space_after = Pt(72) # Chừa ~2.5cm để ký tên
            for r in p.runs:
                r.font.name = "Times New Roman"
            prev_was_sig_note = True
            continue
        elif "TP. Hồ Chí Minh" in txt and ("năm" in txt or "tháng" in txt or "2026" in txt):
            p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
            p.paragraph_format.space_before = Pt(24)
            p.paragraph_format.space_after = Pt(2)
            for r in p.runs:
                r.font.name = "Times New Roman"
                r.font.italic = True
        elif txt in ["Sinh viên thực hiện", "Sinh viên cam đoan"]:
            p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            for r in p.runs:
                r.font.name = "Times New Roman"
                r.font.bold = True
        elif "(Ký và ghi rõ họ tên)" in txt:
            p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(72) # Chừa ~2.5cm để ký tên
            for r in p.runs:
                r.font.name = "Times New Roman"
                r.font.italic = True
            prev_was_sig_note = True
            continue
        elif txt == "Lê Thành Hiệu" or (prev_was_sig_note and "Lê Thành Hiệu" in txt):
            p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(12)
            for r in p.runs:
                r.font.name = "Times New Roman"
                r.font.bold = True
            prev_was_sig_note = False
            continue

    try:
        doc.save(path)
        print(f"✅ Đã chuẩn hóa thành công: {path} (Header 1.27cm, Footer 1.27cm số trang giữa, Margin 3-2-2-2cm, Font 13pt)")
    except PermissionError:
        print(f"⚠️ Cảnh báo: Tệp {path} đang được mở trong Microsoft Word hoặc ứng dụng khác. Vui lòng đóng tệp để cập nhật.")
    except Exception as e:
        print(f"❌ Lỗi khi lưu {path}: {e}")

for p in target_docx_paths:
    format_document(p)

print("\n🎉 HOÀN TẤT CHUẨN HÓA TOÀN BỘ FILE WORD THEO QUY CHUẨN ĐẠI HỌC VIỆT NAM!")
