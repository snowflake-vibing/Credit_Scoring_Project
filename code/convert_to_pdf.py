import os
import sys

def convert_docx_to_pdf(docx_path, pdf_path):
    try:
        import win32com.client
    except ImportError:
        # fallback to comtypes or direct Word automation
        pass
    
    pass
    
    # Using python win32com
    try:
        import win32com.client
        word = win32com.client.DispatchEx("Word.Application")
        word.Visible = False
        doc = word.Documents.Open(os.path.abspath(docx_path))
        doc.SaveAs(os.path.abspath(pdf_path), FileFormat=17) # 17 = wdFormatPDF
        doc.Close()
        word.Quit()
        print(f"✅ Đã xuất thành công PDF từ Word: {pdf_path}")
        return True
    except Exception as e:
        print(f"Lỗi khi dùng win32com Word: {e}")
        return False

def convert_pptx_to_pdf(pptx_path, pdf_path):
    try:
        import win32com.client
        powerpoint = win32com.client.DispatchEx("PowerPoint.Application")
        # powerpoint.Visible = True # PowerPoint requires window or presentation open
        pres = powerpoint.Presentations.Open(os.path.abspath(pptx_path), WithWindow=False)
        pres.SaveAs(os.path.abspath(pdf_path), 32) # 32 = ppSaveAsPDF
        pres.Close()
        powerpoint.Quit()
        print(f"✅ Đã xuất thành công PDF từ PowerPoint: {pdf_path}")
        return True
    except Exception as e:
        print(f"Lỗi khi dùng win32com PowerPoint: {e}")
        return False

if __name__ == "__main__":
    convert_docx_to_pdf("qmd/BAO_CAO_TOAN_VAN.docx", "qmd/BAO_CAO_TOAN_VAN.pdf")
    convert_docx_to_pdf("qmd/BAO_CAO_TOAN_VAN.docx", "doc/BAO_CAO_TOAN_VAN.pdf")
    convert_pptx_to_pdf("slide_bao_ve_de_tai_7.pptx", "slide_bao_ve_de_tai_7.pdf")
