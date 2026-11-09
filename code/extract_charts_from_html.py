import sys
import re
import urllib.parse
import base64
import json
import os

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

html_path = r"C:\Users\GIGA\Downloads\De_Tai_7_Databricks_Notebook.html"
with open(html_path, "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

m = re.search(r"var __DATABRICKS_NOTEBOOK_MODEL = '([^']+)';", text)
raw_payload = m.group(1)
data = json.loads(urllib.parse.unquote(base64.b64decode(raw_payload).decode("utf-8")))
commands = data.get("commands", [])

chart_mapping = [
    (5, "hinh_3_1_missing_values.png", "Hình 3.1: Đánh giá tỷ lệ dữ liệu khuyết thiếu Tầng Bronze"),
    (9, "hinh_3_2_npl_intent_home.png", "Hình 3.2: Tỷ lệ nợ xấu NPL theo Mục đích vay & Sở hữu nhà ở"),
    (17, "hinh_4_1_roc_curve.png", "Hình 4.1: Đường cong ROC so sánh hiệu năng các mô hình"),
    (19, "hinh_4_2_confusion_matrix.png", "Hình 4.2: Ma trận nhầm lẫn trên tập kiểm thử"),
    (21, "hinh_5_1_risk_policy_charts.png", "Hình 5.1: Phân tầng rủi ro & Chính sách phê duyệt tín dụng")
]

out_dir = r"d:\Project_SIC\final_project\doc\images"
os.makedirs(out_dir, exist_ok=True)

print("=" * 80)
print("TRÍCH XUẤT 5 BIỂU ĐỒ TỪ DATABRICKS EXPORT HTML SANG DOC/IMAGES/")
print("=" * 80)

for cell_idx, fname, title in chart_mapping:
    cmd = commands[cell_idx]
    results = cmd.get("results", {})
    data_list = results.get("data", [])
    img_b64 = None
    
    for item in data_list:
        if item.get("type") == "mimeBundle":
            bundle_data = item.get("data")
            if isinstance(bundle_data, dict):
                img_b64 = bundle_data.get("image/png")
            elif isinstance(bundle_data, str):
                m_png = re.search(r"'image/png':\s*'([A-Za-z0-9+/=\s]+)'", bundle_data)
                if m_png:
                    img_b64 = m_png.group(1).replace("\n", "").replace(" ", "")
            if img_b64:
                break
                
    if not img_b64:
        m_fallback = re.search(r"'image/png':\s*'([A-Za-z0-9+/=\s]{100,})'", str(results))
        if m_fallback:
            img_b64 = m_fallback.group(1).replace("\n", "").replace(" ", "")
            
    if img_b64:
        # clean whitespace
        img_b64 = re.sub(r'\s+', '', img_b64)
        raw_bytes = base64.b64decode(img_b64)
        save_path = os.path.join(out_dir, fname)
        with open(save_path, "wb") as f_out:
            f_out.write(raw_bytes)
        print(f"✅ Đã trích xuất & lưu: {fname:<32} ({len(raw_bytes)/1024:6.1f} KB) -> {title}")
    else:
        print(f"❌ Không tìm thấy ảnh trong Cell {cell_idx+1}: {fname}")

print("=" * 80)
print("Hoàn tất trích xuất 5 biểu đồ vào thư mục doc/images!")
