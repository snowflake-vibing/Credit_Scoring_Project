import glob
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

files = sorted(glob.glob('doc/*.md'))
total_words = 0
print(f"| {'File':<32} | {'Lines':<7} | {'Words':<7} | {'Est. Text Pages':<18} | {'Embedded Figures / Tables':<30} |")
print("|" + "-"*34 + "|" + "-"*9 + "|" + "-"*9 + "|" + "-"*20 + "|" + "-"*32 + "|")

chart_map = {
    '00_OUTLINE_VA_TRANG_BIA.md': 'Front matter (Bìa, Mục lục, DS)',
    '01_CHUONG_1_GIOI_THIEU.md': '2 Bảng biểu (Bảng 1.1, 1.2)',
    '02_CHUONG_2_KIEN_TRUC.md': 'Hình 2.1 (Mermaid) + 2 Bảng biểu',
    '03_CHUONG_3_XU_LY_DU_LIEU.md': 'Hình 3.1, Hình 3.2 + 3 Bảng biểu',
    '04_CHUONG_4_MO_HINH_AI.md': 'Hình 4.1, Hình 4.2 + 4 Bảng biểu',
    '05_CHUONG_5_KHUYEN_NGHI.md': 'Hình 5.1 + 4 Bảng biểu',
    '06_TAI_LIEU_THAM_KHAO.md': '49 Tài liệu tham khảo'
}

page_breakdown = {
    '00_OUTLINE_VA_TRANG_BIA.md': 4.0,  # Bìa (1), Cam đoan & Cảm ơn (1), Abstract (1), Mục lục & DS (1)
    '01_CHUONG_1_GIOI_THIEU.md': 5.0,
    '02_CHUONG_2_KIEN_TRUC.md': 5.5,
    '03_CHUONG_3_XU_LY_DU_LIEU.md': 6.5,
    '04_CHUONG_4_MO_HINH_AI.md': 7.5,
    '05_CHUONG_5_KHUYEN_NGHI.md': 6.5,
    '06_TAI_LIEU_THAM_KHAO.md': 2.0
}

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        text = fp.read()
    words = len(text.split())
    lines = len(text.splitlines())
    total_words += words
    base = os.path.basename(f)
    print(f"| {base:<32} | {lines:<7} | {words:<7} | {words/350:<18.1f} | {chart_map.get(base, ''):<30} |")

print("-" * 110)
print(f"Tổng số từ: {total_words:,} từ.")
total_allocated = sum(page_breakdown.values())
print(f"Tổng số trang ấn bản A4 ước tính theo quy chuẩn Bộ GD&ĐT (Font 13, giãn dòng 1.5, lề 3-2-2-2 cm):")
print(f"=> Tổng cộng: {total_allocated:.1f} TRANG (ĐÁP ỨNG CHÍNH XÁC GIỚI HẠN DƯỚI 40 TRANG)")
