# -*- coding: utf-8 -*-
"""
Script tái cấu trúc toàn bộ đồ án theo chuẩn Luận văn / Tiểu luận Đại học Việt Nam
(Căn cứ theo Hướng dẫn trình bày Luận văn tốt nghiệp - ĐH Cần Thơ / CTU)
- Khổ giấy A4, Portrait, lề 3-2-2-2 cm
- Bố cục 5 chương: Giới thiệu -> Lược khảo tài liệu -> Phương pháp nghiên cứu -> Kết quả và thảo luận -> Kết luận và kiến nghị
- XÓA BỎ HOÀN TOÀN Abstract in English
- Giữ phần Tóm lược tiếng Việt (<= 500 từ)
- Tiêu đề chương: SIZE 14, IN HOA, ĐẬM, CANH GIỮA, KHÔNG DẤU CHẤM CUỐI
- Tiêu mục tối đa 3 cấp (1.1, 1.1.1, 1.1.2), không dấu chấm cuối
- Bảng biểu: Tên bảng ở TRÊN, in đậm size 12. Chú thích ở DƯỚI, in nghiêng size 10 canh trái.
- Hình vẽ: Tên hình ở DƯỚI, in đậm size 12 canh giữa. Chú thích/Nguồn ở DƯỚI, in nghiêng size 10 canh phải.
- Tài liệu tham khảo tách riêng Tiếng Việt và Tiếng Anh, xếp ABC.
"""

import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

print("Bắt đầu tái cấu trúc báo cáo theo chuẩn Đại học Việt Nam...")
