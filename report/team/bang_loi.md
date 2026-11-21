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

**Tỉ lệ đồng thuận:** 100% (20/20 ca).

## Quy tắc phân biệt cho các ca không trùng

- **Ca 13 — Giới hạn hệ thống:** Khi yêu cầu nằm ngoài phạm vi xử lý, gắn nhãn Giới hạn hệ thống. Phí bảo hiểm của đối tác nằm ngoài phạm vi trợ lý LogiX, dù trợ lý vẫn đưa ra câu trả lời chung chung về phí vận chuyển.
- **Ca 20 — Hệ thống:** Khi khách gửi lại cùng một yêu cầu và hệ thống thực hiện giao dịch lần thứ hai vì thiếu khóa chống trùng, gắn nhãn Hệ thống. Việc gửi lại kích hoạt lỗi, còn nguyên nhân hoàn tiền hai lần là thiếu cơ chế chống trùng.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | người dùng thao tác sai | yêu cầu người dùng xác nhận lại | người gán nhãn 2 |
| 2 | Hệ thống | llm gọi sai tool cho ra kết quả sai | thêm ngữ cảnh cho llm  | người gán nhãn 2 |
| 3 | Ngữ cảnh | Ghi nhận lý do khi khách mở lại yêu cầu vì chờ tiền về ngân hàng; đếm số ca có lý do này mỗi tuần. | Hiển thị rõ **“Tiền sẽ được hoàn vào ví LogiX”** trước khi khách xác nhận. Sau khi hoàn, gửi hướng dẫn kiểm tra số dư ví. | Người gắn nhãn 1 |
| 13 | Giới hạn hệ thống | Ghi sự kiện `out_of_scope_detected` khi khách yêu cầu hoàn phí bảo hiểm của đối tác. Hằng tuần, kiểm tra các ca có sự kiện này nhưng thiếu hướng dẫn chuyển kênh. | Nêu rõ trợ lý chỉ xử lý hoàn phí vận chuyển. Hướng dẫn khách liên hệ kênh hỗ trợ của đối tác bảo hiểm để xử lý yêu cầu. | Người gắn nhãn 1 |
| 5 | Ngầm | Hằng tuần, đối soát tiền đã hoàn với số tiền phải hoàn tính từ **giá sau giảm**; đánh dấu mọi đơn có chênh lệch. | Dùng giá thực trả sau giảm làm cơ sở tính hoàn. Bổ sung kiểm thử cho đơn có mã giảm giá trước khi triển khai thay đổi. | Người gắn nhãn 1 |
