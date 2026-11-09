import os
import sys
import glob
import json
import re
import py_compile

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

print("=" * 80)
print("🔍 KIỂM TRA TOÀN DIỆN DỰ ÁN TRƯỚC KHI ĐÁNH GIÁ TRÊN GITHUB")
print("=" * 80)

# 1. Kiểm tra cấu trúc thư mục và tệp
root_files = os.listdir('.')
print(f"📂 Thư mục gốc gồm có: {root_files}")

# 2. Kiểm tra tính hợp lệ của tất cả file Python (.py)
print("\n--- 1. KIỂM TRA CÚ PHÁP CÁC FILE PYTHON (.py) ---")
py_files = glob.glob('code/*.py')
py_errors = []
for f in py_files:
    try:
        py_compile.compile(f, doraise=True)
        print(f"  ✅ {f:<40} : Cú pháp hợp lệ (Syntax OK)")
    except Exception as e:
        print(f"  ❌ {f:<40} : Lỗi cú pháp! {e}")
        py_errors.append((f, str(e)))

# 3. Kiểm tra tính hợp lệ của file Jupyter Notebook (.ipynb)
print("\n--- 2. KIỂM TRA FILE NOTEBOOK (.ipynb) ---")
nb_files = glob.glob('code/*.ipynb')
nb_errors = []
for nb in nb_files:
    try:
        with open(nb, 'r', encoding='utf-8') as f:
            data = json.load(f)
        cells = data.get('cells', [])
        nbformat = data.get('nbformat')
        print(f"  ✅ {nb:<40} : JSON hợp lệ, nbformat v{nbformat}, gồm {len(cells)} cells")
        # Kiểm tra cell types
        code_cells = sum(1 for c in cells if c.get('cell_type') == 'code')
        md_cells = sum(1 for c in cells if c.get('cell_type') == 'markdown')
        print(f"     -> {code_cells} code cells, {md_cells} markdown cells")
    except Exception as e:
        print(f"  ❌ {nb:<40} : Lỗi notebook! {e}")
        nb_errors.append((nb, str(e)))

# 4. Kiểm tra các ảnh trong doc/images/
print("\n--- 3. KIỂM TRA CÁC BIỂU ĐỒ ẢNH TRONG doc/images/ ---")
expected_images = [
    'hinh_2_1_medallion_architecture.png',
    'hinh_3_1_missing_values.png',
    'hinh_3_2_npl_intent_home.png',
    'hinh_4_1_roc_curve.png',
    'hinh_4_2_confusion_matrix.png',
    'hinh_5_1_risk_policy_charts.png'
]
img_errors = []
for img in expected_images:
    p = os.path.join('doc', 'images', img)
    if os.path.exists(p):
        sz = os.path.getsize(p) / 1024
        print(f"  ✅ {img:<35} : Tồn tại ({sz:.1f} KB)")
    else:
        print(f"  ❌ {img:<35} : KHÔNG TỒN TẠI!")
        img_errors.append(img)

# 5. Kiểm tra các file Markdown (.md): Math KaTeX, link ảnh, liên kết nội bộ
print("\n--- 4. KIỂM TRA CÔNG THỨC TOÁN (KATEX) & LINK ẢNH TRONG CÁC FILE .md ---")
md_files = glob.glob('**/*.md', recursive=True)
math_errors = []
link_errors = []

for md in sorted(md_files):
    if '.git' in md:
        continue
    with open(md, 'r', encoding='utf-8') as f:
        content = f.read()

    # Kiểm tra ký tự % trong khối math $...$ hoặc $$...$$
    # Regex tìm các khối math
    inline_math = re.findall(r'(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)', content, re.DOTALL)
    block_math = re.findall(r'\$\$(.+?)\$\$', content, re.DOTALL)
    
    file_math_issues = 0
    for m in inline_math + block_math:
        # Nếu có ký tự % mà không phải \%
        if '%' in m and r'\%' not in m:
            file_math_issues += 1
            math_errors.append((md, m.strip()))

    # Kiểm tra link ảnh ![...](...)
    img_refs = re.findall(r'!\[.*?\]\((.*?)\)', content)
    file_img_issues = 0
    md_dir = os.path.dirname(md)
    for ref in img_refs:
        # Bỏ qua link web http
        if ref.startswith('http') or ref.startswith('#'):
            continue
        # Đường dẫn tương đối từ vị trí file md
        target = os.path.normpath(os.path.join(md_dir, ref))
        if not os.path.exists(target):
            file_img_issues += 1
            link_errors.append((md, ref, target))

    status_str = f"Toán: {file_math_issues} lỗi % | Link ảnh: {file_img_issues} lỗi"
    if file_math_issues == 0 and file_img_issues == 0:
        print(f"  ✅ {md:<50} : Hoàn hảo ({status_str})")
    else:
        print(f"  ⚠️ {md:<50} : CẦN CHÚ Ý ({status_str})")

# 6. Kiểm tra các liên kết nội bộ trong TẤT CẢ các file .md
print("\n--- 5. KIỂM TRA TẤT CẢ CÁC LIÊN KẾT TỆP NỘI BỘ TRONG DỰ ÁN ---")
broken_links = []
unclosed_math = []

for md in sorted(md_files):
    if '.git' in md:
        continue
    with open(md, 'r', encoding='utf-8') as f:
        content = f.read()

    md_dir = os.path.dirname(md)
    # Tìm link [text](path)
    links = re.findall(r'(?<!!)\[.*?\]\((.*?)\)', content)
    for l in links:
        if l.startswith('http') or l.startswith('#') or l.startswith('mailto:') or l.startswith('javascript:'):
            continue
        # Bỏ query hoặc anchor
        clean_path = l.split('#')[0].split('?')[0].strip()
        if not clean_path:
            continue
        # Check target relative to current md
        target = os.path.normpath(os.path.join(md_dir, clean_path))
        # Cũng check nếu target relative to project root
        target_root = os.path.normpath(clean_path)
        if not os.path.exists(target) and not os.path.exists(target_root):
            broken_links.append((md, l, target))

    # Kiểm tra số lượng dấu $ có bị lẻ không (chỉ đếm dấu $ không bị escape bằng backslash)
    raw_dollars = re.findall(r'(?<!\\)\$', content)
    if len(raw_dollars) % 2 != 0:
        unclosed_math.append((md, len(raw_dollars)))

if broken_links:
    for src, l, cl in broken_links:
        print(f"  ❌ File [{src}] có link hỏng: [{l}] trỏ đến [{cl}] không tồn tại!")
else:
    print(f"  ✅ Tất cả liên kết tệp nội bộ trong toàn bộ các file .md đều tồn tại chính xác!")

if unclosed_math:
    for src, cnt in unclosed_math:
        print(f"  ❌ File [{src}] có số lượng dấu $ lẻ ({cnt}), có thể bị unclosed math block!")
else:
    print(f"  ✅ Tất cả các file .md đều có các khối math $...$ đóng mở hoàn toàn cân đối!")

# 7. Tổng kết
print("\n" + "=" * 80)
total_issues = len(py_errors) + len(nb_errors) + len(img_errors) + len(math_errors) + len(link_errors) + len(broken_links) + len(unclosed_math)
if total_issues == 0:
    print("🎉 KẾT QUẢ: 100% CÁC FILE ĐỀU HOÀN HẢO, SẠCH SẼ, SẴN SÀNG TRÊN GITHUB!")
else:
    print(f"⚠️ KẾT QUẢ: PHÁT HIỆN {total_issues} ĐIỂM CẦN XỬ LÝ.")
print("=" * 80)
