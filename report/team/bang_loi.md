# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: ... · Người gắn nhãn 2: ... (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | 1 | Do người dùng |
| 2 | Hệ thống | Hệ thống | 1 | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | 1 | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | 1 | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | 1 | Ngầm |
| 6 | Do người dùng | Do người dùng | 1 | Do người dùng |
| 7 | Hệ thống | Hệ thống | 1 | Hệ thống |
| 8 | Hệ thống | Hệ thống | 1 | Hệ thống |
| 9 | Do người dùng | Do người dùng | 1 | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | 1 | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | 1 | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | 1 | Ngầm |
| 13 | Ngữ cảnh | Giới hạn hệ thống | 0 | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | 1 | Do người dùng |
| 15 | Hệ thống | Hệ thống | 1 | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | 1 | Ngữ cảnh |
| 17 | Ngầm | Ngầm | 1 | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | 1 | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | 1 | Giới hạn hệ thống |
| 20 | Ngầm | Hệ thống | 0 | Hệ thống |

**Tỉ lệ đồng thuận:** 90% (18/20 ca).

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- ...

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | người dùng thao tác sai | yêu cầu người dùng xác nhận lại | người gán nhãn 2 |
| 2 | Hệ thống | llm gọi sai tool cho ra kết quả sai | thêm ngữ cảnh cho llm  | người gán nhãn 2 |
| ... | Ngữ cảnh | ... | ... | ... |
| ... | Giới hạn hệ thống | ... | ... | ... |
| ... | Ngầm | ... | ... | ... |
