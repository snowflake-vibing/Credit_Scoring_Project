import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

yaml_frontmatter = """---
title: "BÁO CÁO TIỂU LUẬN KẾT THÚC HỌC PHẦN"
subtitle: "MÔ HÌNH CHẤM ĐIỂM TÍN DỤNG VÀ THẨM ĐỊNH RỦI RO VỠ NỢ TRONG LĨNH VỰC NGÂN HÀNG VÀ FINTECH"
author:
  - name: "Lê Thành Hiệu"
    affiliation: "Trường Đại học Kinh tế - Đại học Quốc gia"
date: "2026"
format:
  html:
    toc: true
    toc-depth: 3
    theme: cosmo
    number-sections: false
    code-copy: true
    embed-resources: true
    highlight-style: github
  docx:
    toc: true
    number-sections: false
  pdf:
    documentclass: report
    papersize: a4
    geometry:
      - top=20mm
      - bottom=20mm
      - left=30mm
      - right=20mm
    toc: true
    toc-depth: 3
    number-sections: false
    colorlinks: true
    linestretch: 1.5
    fontsize: 13pt
---

"""

doc_files = [
    "doc/00_OUTLINE_VA_TRANG_BIA.md",
    "doc/01_CHUONG_1_GIOI_THIEU.md",
    "doc/02_CHUONG_2_KIEN_TRUC.md",
    "doc/03_CHUONG_3_XU_LY_DU_LIEU.md",
    "doc/04_CHUONG_4_MO_HINH_AI.md",
    "doc/05_CHUONG_5_KHUYEN_NGHI.md",
    "doc/06_TAI_LIEU_THAM_KHAO.md"
]

sections = []
for file_path in doc_files:
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read().strip()
            sections.append(content)
        print(f"📖 Đã đọc: {file_path}")
    else:
        print(f"❌ Không tìm thấy: {file_path}")

# Nối các chương lại với nhau bằng phân trang chuẩn LaTeX và gạch ngang Markdown
full_content = yaml_frontmatter + "\n\n\\newpage\n\n---\n\n".join(sections)

# Ghi ra 2 tệp: BAO_CAO_TOAN_VAN.qmd và full_report.qmd
target_files = [
    "qmd/BAO_CAO_TOAN_VAN.qmd",
    "qmd/full_report.qmd"
]

for target in target_files:
    with open(target, "w", encoding="utf-8") as f:
        f.write(full_content)
    print(f"✅ Đã tạo thành công tệp nguyên khối: {target} ({len(full_content.splitlines())} dòng, {len(full_content)} ký tự)")
