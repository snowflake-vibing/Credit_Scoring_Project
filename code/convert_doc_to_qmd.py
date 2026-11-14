import os
import sys
import shutil
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Định nghĩa các thư mục
doc_dir = "doc"
qmd_dir = "qmd"
os.makedirs(qmd_dir, exist_ok=True)
os.makedirs(os.path.join(qmd_dir, "images"), exist_ok=True)

# 1. Sao chép toàn bộ ảnh sang qmd/images/
doc_img_dir = os.path.join(doc_dir, "images")
qmd_img_dir = os.path.join(qmd_dir, "images")
if os.path.exists(doc_img_dir):
    for f in os.listdir(doc_img_dir):
        src = os.path.join(doc_img_dir, f)
        dst = os.path.join(qmd_img_dir, f)
        if os.path.isfile(src):
            shutil.copy2(src, dst)
print("✅ Đã sao chép toàn bộ ảnh sang qmd/images/")

# 2. Cấu hình tiêu đề cho từng chương
chapter_metadata = {
    "00_OUTLINE_VA_TRANG_BIA.md": {
        "title": "Báo Cáo Tiểu Luận Kết Thúc Học Phần",
        "subtitle": "Mô Hình Chấm Điểm Tín Dụng & Thẩm Định Rủi Ro Vỡ Nợ",
        "is_index": True
    },
    "01_CHUONG_1_GIOI_THIEU.md": {
        "title": "Chương 1: Tổng Quan Về Bài Toán & Đặt Vấn Đề",
        "subtitle": "Bối cảnh Ngân hàng số, FinTech và Mô hình 5Vs Dữ liệu lớn"
    },
    "02_CHUONG_2_KIEN_TRUC.md": {
        "title": "Chương 2: Kiến Trúc Luồng Dữ Liệu Lakehouse (Medallion Architecture)",
        "subtitle": "Apache Spark, Delta Lake và Quản trị Rủi ro Chuẩn Basel II/III"
    },
    "03_CHUONG_3_XU_LY_DU_LIEU.md": {
        "title": "Chương 3: Xử Lý & Phân Tích Dữ Liệu Lớn Với PySpark và Spark SQL",
        "subtitle": "Tiền xử lý phân tán, Kỹ nghệ đặc trưng tài chính (DTI, CBI) và Window Functions"
    },
    "04_CHUONG_4_MO_HINH_AI.md": {
        "title": "Chương 4: Xây Dựng Mô Hình Học Máy Phân Tán Với Spark MLlib",
        "subtitle": "Random Forest Pipeline, Cross-Validation và Đánh giá ROC-AUC"
    },
    "05_CHUONG_5_KHUYEN_NGHI.md": {
        "title": "Chương 5: Phân Tích Ý Nghĩa Nghiệp Vụ & Đề Xuất Chiến Lược Quản Trị",
        "subtitle": "Quy đổi FICO Score, Ma trận duyệt vay tự động, Risk-Based Pricing & ROI"
    },
    "06_TAI_LIEU_THAM_KHAO.md": {
        "title": "Tài Liệu Tham Khảo",
        "subtitle": "Quy chuẩn Văn bản pháp luật, Giáo trình, Bài báo khoa học & Kỹ thuật"
    }
}

# 3. Tạo các file .qmd
for md_name, meta in chapter_metadata.items():
    md_path = os.path.join(doc_dir, md_name)
    if not os.path.exists(md_path):
        continue
    
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Chuẩn bị YAML frontmatter
    yaml_header = f"""---
title: "{meta['title']}"
subtitle: "{meta.get('subtitle', '')}"
format:
  html:
    toc: true
    number-sections: false
  pdf:
    toc: true
    number-sections: false
---

"""
    qmd_filename = md_name.replace(".md", ".qmd")
    qmd_path = os.path.join(qmd_dir, qmd_filename)
    
    with open(qmd_path, "w", encoding="utf-8") as f:
        f.write(yaml_header + content)
    print(f"✅ Đã tạo {qmd_path}")
    
    # Nếu là trang bìa, tạo thêm index.qmd cho cấu trúc Quarto Book
    if meta.get("is_index"):
        index_path = os.path.join(qmd_dir, "index.qmd")
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(yaml_header + content)
        print(f"✅ Đã tạo {index_path} (Quarto Book landing page)")

# 4. Tạo file cấu hình _quarto.yml
quarto_yml_content = """project:
  type: book
  output-dir: _output

book:
  title: "Đề Tài 7: Mô Hình Chấm Điểm Tín Dụng & Thẩm Định Rủi Ro Vỡ Nợ"
  subtitle: "Báo Cáo Tiểu Luận Môn Học Dữ Liệu Lớn & Trí Tuệ Nhân Tạo Trong Kinh Doanh"
  author:
    - name: "Lê Thành Hiệu"
      affiliation: "Trường Đại học Tài chính - Marketing (UFM)"
  date: "2026"
  search: true
  chapters:
    - index.qmd
    - 01_CHUONG_1_GIOI_THIEU.qmd
    - 02_CHUONG_2_KIEN_TRUC.qmd
    - 03_CHUONG_3_XU_LY_DU_LIEU.qmd
    - 04_CHUONG_4_MO_HINH_AI.qmd
    - 05_CHUONG_5_KHUYEN_NGHI.qmd
    - 06_TAI_LIEU_THAM_KHAO.qmd

format:
  html:
    theme:
      light: cosmo
    toc: true
    toc-depth: 3
    number-sections: false
    code-copy: true
    code-fold: show
    highlight-style: github
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
"""

with open(os.path.join(qmd_dir, "_quarto.yml"), "w", encoding="utf-8") as f:
    f.write(quarto_yml_content)
print("✅ Đã tạo qmd/_quarto.yml")

# 5. Tạo file full_report.qmd phục vụ render tài liệu đơn nhất (Single Document Compilation)
full_report_content = """---
title: "BÁO CÁO TIỂU LUẬN KẾT THÚC HỌC PHẦN"
subtitle: "MÔ HÌNH CHẤM ĐIỂM TÍN DỤNG VÀ THẨM ĐỊNH RỦI RO VỠ NỢ TRONG LĨNH VỰC NGÂN HÀNG VÀ FINTECH"
author:
  - name: "Lê Thành Hiệu"
    affiliation: "Trường Đại học Tài chính - Marketing (UFM)"
date: "2026"
format:
  html:
    toc: true
    toc-depth: 3
    number-sections: false
    theme: cosmo
    code-copy: true
    embed-resources: true
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

{{< include 00_OUTLINE_VA_TRANG_BIA.qmd >}}

{{< include 01_CHUONG_1_GIOI_THIEU.qmd >}}

{{< include 02_CHUONG_2_KIEN_TRUC.qmd >}}

{{< include 03_CHUONG_3_XU_LY_DU_LIEU.qmd >}}

{{< include 04_CHUONG_4_MO_HINH_AI.qmd >}}

{{< include 05_CHUONG_5_KHUYEN_NGHI.qmd >}}

{{< include 06_TAI_LIEU_THAM_KHAO.qmd >}}
"""

with open(os.path.join(qmd_dir, "full_report.qmd"), "w", encoding="utf-8") as f:
    f.write(full_report_content)
print("✅ Đã tạo qmd/full_report.qmd")

print("\n🎉 HOÀN THÀNH TOÀN BỘ QUY TRÌNH CHUYỂN ĐỔI SANG THƯ MỤC QMD!")
