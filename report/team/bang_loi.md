# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Nguyễn Đức Minh · Người gắn nhãn 2: Hồ Quốc Toản (gắn trong 8 phút, không trao đổi)

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

- **Ca 13 — Giới hạn hệ thống:** Khi yêu cầu nằm ngoài phạm vi xử lý, gắn nhãn Giới hạn hệ thống. Phí bảo hiểm của đối tác nằm ngoài phạm vi trợ lý LogiX, dù trợ lý vẫn đưa ra câu trả lời chung chung về phí vận chuyển.
- **Ca 20 — Hệ thống:** Khi khách gửi lại cùng một yêu cầu và hệ thống thực hiện giao dịch lần thứ hai vì thiếu khóa chống trùng, gắn nhãn Hệ thống. Việc gửi lại kích hoạt lỗi, còn nguyên nhân hoàn tiền hai lần là thiếu cơ chế chống trùng.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Event `refund_ledger_write` có `ket_qua` = ngân hàng từ chối vì sai số tài khoản, kèm trace_id; đếm theo ngày, cảnh báo khi > 1% số lệnh hoàn | Kiểm tra độ dài, định dạng số tài khoản và hiện tên chủ tài khoản để khách xác nhận **trước khi** tạo lệnh hoàn; sai thì yêu cầu nhập lại | PM trợ lý hoàn phí |
| 2 | Hệ thống | Đối soát hằng ngày: đơn có cân nặng thuộc hàng nặng nhưng event `agent_run_completed` ghi tham số tool tra giá là hàng thường, kèm trace_id; ngưỡng 0 ca | Lấy loại hàng từ cân nặng trong dữ liệu đơn, không để LLM tự chọn; chặn lời gọi tool khi tham số không khớp cân nặng; thêm ca kiểm thử kiện 28 kg | Kỹ sư trưởng agent |
| 3 | Ngữ cảnh | Event `ticket_reopened` có `reason` = chưa thấy tiền về ngân hàng, kèm trace_id; đếm hằng tuần, cảnh báo khi > 1% số ca hoàn về ví | Hiển thị rõ "Tiền sẽ được hoàn vào ví LogiX" trước khi khách xác nhận; sau khi hoàn, gửi hướng dẫn kiểm tra số dư ví | PM trợ lý hoàn phí |
| 13 | Giới hạn hệ thống | Event `out_of_scope_detected` khi khách hỏi phí bảo hiểm, kèm trace_id; hằng tuần đọc mẫu 20 hội thoại có từ "bảo hiểm"; ngưỡng 0 ca trả lời chung chung mà không nói rõ là không xử lý được | Trợ lý nói rõ chỉ xử lý hoàn phí vận chuyển, rồi chuyển khách sang kênh hỗ trợ của đối tác bảo hiểm kèm tóm tắt | Trưởng nhóm CSKH |
| 5 | Ngầm | Event `audit_sample_checked`: hằng tuần kiểm tra mẫu 100 đơn có mã giảm giá, so số đã hoàn với số tính từ giá sau giảm, kèm trace_id; ngưỡng ≥ 1 đơn lệch thì mở sự cố | Tính hoàn theo giá thực trả sau giảm; thêm ca kiểm thử cho đơn có mã giảm giá trước mỗi lần đổi logic tính tiền | Kế toán trưởng |
