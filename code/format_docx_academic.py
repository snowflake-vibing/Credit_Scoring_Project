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

target_docx_paths = [
    os.path.join("qmd", "_output", "Đề-Tài-7--Mô-Hình-Chấm-Điểm-Tín-Dụng---Thẩm-Định-Rủi-Ro-Vỡ-Nợ.docx"),
    os.path.join("qmd", "BAO_CAO_TOAN_VAN.docx")
]

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
        
        # Thiết lập Header
        header = section.header
        header_p = header.paragraphs[0] if header.paragraphs else header.add_paragraph()
        header_p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        header_p.text = ""
        run_h = header_p.add_run("TRƯỜNG ĐH KINH TẾ - ĐHQG • BÁO CÁO TIỂU LUẬN DỮ LIỆU LỚN & AI")
        run_h.font.name = "Times New Roman"
        run_h.font.size = Pt(10)
        run_h.font.italic = True
        run_h.font.color.rgb = RGBColor(100, 116, 139)
        
        # Thiết lập Footer (Đánh số trang ở giữa trang, cỡ chữ 13pt)
        footer = section.footer
        footer_p = footer.paragraphs[0] if footer.paragraphs else footer.add_paragraph()
        footer_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        footer_p.text = ""
        
        # Thêm text chân trang và số trang
        run_f1 = footer_p.add_run("— ")
        run_f1.font.name = "Times New Roman"
        run_f1.font.size = Pt(13)
        
        fldSimple = OxmlElement('w:fldSimple')
        fldSimple.set(qn('w:instr'), 'PAGE')
        footer_p._p.append(fldSimple)
        
        run_f2 = footer_p.add_run(" —")
        run_f2.font.name = "Times New Roman"
        run_f2.font.size = Pt(13)

    # 2. Chuẩn hóa font và paragraph spacing cho toàn bộ văn bản
    for p in doc.paragraphs:
        p.paragraph_format.line_spacing = 1.2
        p.paragraph_format.space_before = Pt(6)
        p.paragraph_format.space_after = Pt(6)
        for r in p.runs:
            if not r.font.name:
                r.font.name = "Times New Roman"

    doc.save(path)
    print(f"✅ Đã chuẩn hóa thành công: {path} (Header 1.27cm, Footer 1.27cm số trang giữa, Margin 3-2-2-2cm, Font 13pt)")

for p in target_docx_paths:
    format_document(p)

print("\n🎉 HOÀN TẤT CHUẨN HÓA TOÀN BỘ FILE WORD THEO QUY CHUẨN ĐẠI HỌC VIỆT NAM!")
