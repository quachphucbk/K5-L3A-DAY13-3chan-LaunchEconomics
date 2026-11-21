# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

Số tính bằng `src/lab13.py` (mục E1). Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`.

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | **82,83%** (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | **27,12%** (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | **4,25%** (51/1.200); trong phạm vi noi_dia + hang_nang 3,97% (39/982) |
| Dùng | Nhóm tự đề xuất: % yêu cầu của nhóm trợ lý được nhân viên mở bằng trợ lý | Số `refund_request_created` có `arm` = tro_ly và có `agent_suggestion_shown` cùng trace_id, chia số `refund_request_created` có `arm` = tro_ly | Không cần tính |
| An toàn | Nhóm tự đề xuất: % đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần (bắt lỗi ngầm như ca 5, 17) | Số `audit_sample_checked` có `so_tien_da_hoan` khác `so_tien_dung`, chia số đơn được kiểm tra mẫu trong tuần | Không cần tính |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng. Chỉ số chính trong đợt chạy thử là 82,83%; con số này chưa so được với baseline 0,70 của nhân viên tự làm.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | request_id, loai, so_tien, depot, staff_id, arm, trace_id | Khi khách gửi yêu cầu |
| `agent_run_completed` | Agent | attempt, tokens_in, tokens_out, tool_calls, tham số tool, status, trace_id | Sau mỗi lần chạy, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | staff_id, so_tien_de_xuat, trace_id | Khi gợi ý hiện ra cho nhân viên |
| `staff_review_decision` | Nhân viên | quyet_dinh (giu / sua / bo), phut_xem_lai đo thật, trace_id | Khi nhân viên bấm gửi, sửa hoặc bỏ |
| `staff_rework_completed` | Nhân viên | phut_lam_lai đo thật, ly_do, trace_id | Khi làm lại xong |
| `refund_ledger_write` | Dịch vụ sổ cái | idempotency_key, so_tien, ket_qua, trace_id | Khi ghi lệnh hoàn vào sổ cái |
| `handoff_to_staff` | Agent | reason (thieu_du_lieu, ngoai_pham_vi, het_lan_chay), tom_tat, trace_id | Khi chuyển yêu cầu cho nhân viên |
| `out_of_scope_detected` | Agent | chu_de, trace_id | Khi nhận ra yêu cầu ngoài phạm vi |
| `ticket_closed` | Hệ thống ticket | closed_at, trace_id | Khi yêu cầu được đóng |
| `ticket_reopened` | Khách | reopened_at, reason, trace_id | Khi khách mở lại yêu cầu |
| `audit_sample_checked` | Kế toán | so_tien_da_hoan, so_tien_dung, trace_id | Hằng tuần, kiểm tra mẫu |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- **Chính:** `refund_request_created` (mẫu số) + `ticket_closed` (đóng trong 24 giờ, so `closed_at` với lúc tạo) + `ticket_reopened` (không mở lại trong 7 ngày). Tính được.
- **Dùng · bỏ qua gợi ý:** `staff_review_decision` (đếm sua + bo, chia tổng số quyết định xem lại). Tính được.
- **An toàn · lỗi lọt đến khách:** `ticket_reopened` trong 7 ngày sau `ticket_closed`, chia `refund_request_created`. Tính được.
- **Dùng · tự đề xuất:** `refund_request_created` (lọc `arm` = tro_ly) + `agent_suggestion_shown` cùng trace_id. Tính được.
- **An toàn · tự đề xuất:** `audit_sample_checked` (so `so_tien_da_hoan` với `so_tien_dung`). Tính được.
- **Chi phí mỗi việc thành công (luật dừng chi phí):** `agent_run_completed` (token, tool) + `staff_review_decision` và `staff_rework_completed` (phút đo thật thay cột simulated) + `ticket_closed`, `ticket_reopened` (đếm việc thành công). Tính được.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | Chi phí mỗi việc thành công +51,8%, từ 4.472 lên 6.787 đ [simulated] (B1, yếu tố nhạy nhất) | Tỉ lệ `staff_rework_completed` / yêu cầu theo tuần > 7% (đợt chạy thử: 4,9% trong phạm vi noi_dia + hang_nang) | Thu hẹp về noi_dia, rà 20 trace làm lại gần nhất để tìm nguyên nhân | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | 11.743 đ = 0,98× của 12.000 đ [simulated]; 12.415 đ = 1,03× nếu làm lại 15,3 phút như dữ liệu [simulated] (B4) | % yêu cầu có `staff_review_decision` còn > 50% ở cuối bước rollout 0,25; hoặc `phut_xem_lai` đo thật trung bình > 5 phút (hoà vốn 5,1 phút) | Giảm xem lại theo bậc khi tỉ lệ sửa + bo < 15%; rút gọn màn hình xem lại để mỗi lần dưới 5 phút | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | Chi phí cố định 40 triệu đ/tháng: +1.185 đ/việc ở 45.000 yêu cầu/tháng, +2.370 đ/việc nếu chỉ còn một nửa (5.784 đ = 0,48×) [simulated] (A4) | Số việc thành công theo tuần < 50% kế hoạch | Không mở rộng pilot; xem lại hợp đồng chi phí cố định | PM trợ lý hoàn phí |
