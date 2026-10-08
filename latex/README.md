# HƯỚNG DẪN CHUYỂN ĐỔI BÁO CÁO LATEX SANG FILE WORD (.DOCX)

Thư mục `latex/` chứa toàn bộ mã nguồn Báo cáo Đồ án Tiểu luận bằng ngôn ngữ LaTeX chuẩn khoa học dành cho sinh viên **Lê Thành Hiệu** (GVHD: **Trần Mạnh Tường**).

Tài liệu này hướng dẫn bạn **3 cách miễn phí và nhanh nhất** để chuyển đổi toàn bộ bộ file LaTeX (`.tex`) này thành file Microsoft Word (`.docx`) hoặc PDF để nộp bài.

---

## 🚀 CÁCH 1: DÙNG CÔNG CỤ PANDOC (KHUYÊN DÙNG - MIỄN PHÍ 100% & GIỮ NGUYÊN ĐỊNH DẠNG)

**Pandoc** là công cụ miễn phí hàng đầu thế giới giúp chuyển đổi trực tiếp từ LaTeX sang Word mà giữ nguyên tiêu đề, phân chương, bảng biểu và công thức toán.

### Bước 1: Cài đặt Pandoc
* **Windows (PowerShell):** Mở PowerShell và gõ lệnh:
  ```powershell
  winget install JohnMacFarlane.Pandoc
  ```
* Hoặc tải bộ cài đặt `.msi` tại: [pandoc.org/installing.html](https://pandoc.org/installing.html)

### Bước 2: Chuyển đổi sang file Word (.docx)
1. Mở Terminal / PowerShell tại thư mục `latex/` này.
2. Gõ câu lệnh sau để chuyển đổi toàn bộ báo cáo sang Word:

```bash
pandoc main.tex 00_trang_bia.tex 01_chuong_1_gioi_thieu.tex 02_chuong_2_kien_truc.tex 03_chuong_3_xu_ly_du_lieu.tex 04_chuong_4_mo_hinh_ai.tex 05_chuong_5_khuyen_nghi.tex 06_tai_lieu_tham_khao.tex -o Bao_Cao_Tieu_Luan_LeThanhHieu.docx --toc
```

👉 *Kết quả:* Bạn sẽ nhận được file **`Bao_Cao_Tieu_Luan_LeThanhHieu.docx`** mở được bằng Microsoft Word 2016 / 2019 / 2021 / 365!

---

## 🌐 CÁCH 2: DÙNG OVERLEAF & MỞ TRỰC TIẾP BẰNG WORD (KHÔNG CẦN CÀI ĐẶT SOFTWARE)

### Bước 1: Biên dịch ra PDF trên Overleaf
1. Truy cập trang web miễn phí: [https://www.overleaf.com/](https://www.overleaf.com/)
2. Tạo một Dự án mới (**New Project**) $\rightarrow$ Upload tất cả các file trong thư mục `latex/` này lên.
3. Nhấn **Recompile** để Overleaf biên dịch ra file **`main.pdf`**.
4. Nhấn nút **Download PDF** để tải file PDF về máy.

### Bước 2: Mở file PDF bằng Microsoft Word để thành file .docx
1. Mở ứng dụng **Microsoft Word** trên máy tính của bạn.
2. Vào menu **`File`** $\rightarrow$ Chọn **`Open`** (Mở).
3. Tìm và chọn file **`main.pdf`** vừa tải về.
4. Word sẽ hiện ra thông báo: *"Word will now convert your PDF to an editable Word document"* $\rightarrow$ Nhấn **OK**.
5. Word sẽ tự động biến toàn bộ PDF LaTeX thành file Word `.docx` cho phép chỉnh sửa văn bản, công thức và bảng biểu hoàn toàn miễn phí!

---

## 💻 CÁCH 3: DÙNG TRANG WEB CONVERTER ONLINE (VERTOPAL)

1. Truy cập trang web chuyển đổi LaTeX miễn phí: [https://www.vertopal.com/en/convert/tex-to-docx](https://www.vertopal.com/en/convert/tex-to-docx)
2. Nhấn nút **Choose File** $\rightarrow$ Chọn file `main.tex`.
3. Nhấn **Convert** và tải file `.docx` về máy.

---

## 🛠️ HƯỚNG DẪN CHÈN HÌNH ẢNH SƠ ĐỒ VÀO FILE LATEX

Trong các file `.tex` (từ Chương 1 đến Chương 5), đã được chuẩn bị sẵn các khung placeholder dạng:

```latex
\begin{figure}[h!]
\centering
\includegraphics[width=0.85\textwidth]{ten_file_anh_so_do.png}
\caption{Tên sơ đồ mô tả}
\label{fig:ma_so_do}
\end{figure}
```

**Cách chèn ảnh sơ đồ thực tế:**
1. Lưu file ảnh sơ đồ của bạn vào cùng thư mục `latex/` (ví dụ: `sodo_5vs.png`, `sodo_medallion.png`, `confusion_matrix.png`).
2. Thay dòng `\framebox[...]` bằng dòng lệnh `\includegraphics[width=0.85\textwidth]{sodo_5vs.png}`.
