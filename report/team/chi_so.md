# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

Số tính bằng `src/lab13.py` (mục E1–E2), kiểm độc lập bằng `csv` + `Decimal`. Các kết quả dùng phút `_simulated` ghi nhãn `simulated`.

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính | % đóng trong 24 giờ và không mở lại trong 7 ngày | Đếm yêu cầu có `dong_trong_24h == 1` và `mo_lai_trong_7_ngay == 0`, chia tổng yêu cầu | **82,83% (994/1.200)** |
| Dùng | Tỉ lệ bỏ qua gợi ý | Số yêu cầu được xem lại có quyết định `sua` hoặc `bo`, chia số yêu cầu `duoc_xem_lai == 1` | **27,12% (48/177)** |
| An toàn | Tỉ lệ mở lại trong 7 ngày, dùng làm tín hiệu lỗi lọt | Số yêu cầu có `mo_lai_trong_7_ngay == 1`, chia tổng yêu cầu | **4,25% (51/1.200)**; phạm vi noi_dia + hang_nang: **3,97% (39/982)** |
| Dùng — đề xuất | % yêu cầu nhánh trợ lý được hiển thị gợi ý | Số request_id nhánh `tro_ly` có `agent_suggestion_shown`, chia tổng request_id được gán nhánh `tro_ly` | Chưa đo; CSV không có log hiển thị gợi ý |
| An toàn — đề xuất | % đơn hoàn sai tiền trong mẫu audit hằng tuần | Số request_id được audit có số tiền hoàn khác số tiền đúng, chia số request_id được audit trong tuần | Chưa đo; CSV không có kết quả audit |

Đây là **chỉ số trong đợt chạy thử**, chưa có đối chứng nên không kết luận trợ lý đã nâng chỉ số từ baseline 70%. Mở lại chỉ là tín hiệu an toàn, không bao quát mọi lỗi sai tiền không bị phát hiện.

Chỉ số chính có 994 ca, còn `ket_qua == 'thanh_cong'` có 978 ca và thêm điều kiện đúng tiền; không dùng 994 thay mẫu số CPS ở A–B.

## Danh sách event

Đây là đặc tả event cần ghi trong pilot. Mọi event có `event_id` để loại trùng và `occurred_at` (timestamp có timezone). Gắn `staff_id`, `depot`, `arm` theo phân nhóm nhân viên; giữ nguyên nhánh trong pilot.

CSV có **1.624 trace_id cho 1.200 request_id**: một yêu cầu có nhiều trace. Nối các bước theo **request_id** và dùng **trace_id** truy vết từng lần chạy; đếm yêu cầu duy nhất, không đếm mỗi lần retry thành một yêu cầu mới.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | request_id, trace_id, created_at, loai, so_tien, staff_id, depot, arm | Khi tạo yêu cầu |
| `agent_run_completed` | Agent | request_id, trace_id, run_id, attempt, tokens_in, tokens_out, tool_calls, tham_so_tool, status, model_version, price_version | Sau mọi lần chạy, kể cả lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | request_id, trace_id, staff_id, suggestion_id, so_tien_de_xuat | Khi gợi ý được hiển thị |
| `staff_review_decision` | Nhân viên | request_id, trace_id, suggestion_id, quyet_dinh (giu/sua/bo), phut_xem_lai đo thật | Khi kết thúc xem lại |
| `staff_rework_completed` | Nhân viên | request_id, trace_id, phut_lam_lai đo thật, ly_do | Khi làm lại xong |
| `refund_ledger_write` | Dịch vụ sổ cái | request_id, trace_id, transaction_id, idempotency_key, so_tien, ket_qua | Khi ghi hoặc từ chối lệnh hoàn |
| `handoff_to_staff` | Agent | request_id, trace_id, reason, tom_tat | Khi chuyển nhân viên |
| `out_of_scope_detected` | Agent | request_id, trace_id, chu_de | Khi phát hiện ngoài phạm vi |
| `ticket_closed` | Hệ thống ticket | request_id, trace_id, closed_at | Khi đóng yêu cầu |
| `ticket_reopened` | Hệ thống ticket | request_id, trace_id, reopened_at, reason | Khi yêu cầu được mở lại |
| `audit_sample_checked` | Kế toán | request_id, trace_id, audit_id, so_tien_da_hoan, so_tien_dung, policy_version | Khi kiểm tra mẫu tuần |
| `request_outcome_finalized` | Dịch vụ đối soát | request_id, trace_id, ket_qua (thanh_cong/lam_lai/chuyen_nhan_vien), so_tien_dung, so_tien_thuc_te, policy_version | Khi đủ cửa sổ 7 ngày và hoàn tất đối soát trạng thái, số tiền |

**Kiểm tra chéo chỉ số với event:**

- **Chính:** `refund_request_created.created_at` + `ticket_closed.closed_at` + `ticket_reopened.reopened_at`; kiểm đóng trong 24 giờ và không mở lại trong 7 ngày sau đóng. Chỉ dùng cohort đủ thời gian theo dõi; ca không đóng trong 24 giờ không đạt.
- **Bỏ qua gợi ý:** lấy quyết định cuối của mỗi request_id được xem lại trong `staff_review_decision`; đếm sua + bo, chia tất cả ca được xem lại, gồm cả giu.
- **Mở lại:** đếm request_id có `ticket_reopened` trong 7 ngày sau `ticket_closed`; chia tổng yêu cầu của cohort đã đủ theo dõi. Chưa đóng thì không tự coi là một ca đã qua đủ 7 ngày sau đóng.
- **Hiển thị gợi ý:** `refund_request_created` lọc arm = tro_ly + `agent_suggestion_shown`, nối theo request_id. Chỉ số này đo mức tiếp cận gợi ý, chưa chứng minh nhân viên chấp nhận.
- **Sai tiền trong mẫu audit:** `audit_sample_checked`, loại bản ghi trùng và dùng kết quả audit cuối cho mỗi yêu cầu trong tuần. Không suy ra tỉ lệ sai tiền toàn bộ từ một mẫu chọn thiên lệch.
- **CPS và luật dừng chi phí:** cộng token/tool từ mọi `agent_run_completed` theo bảng giá có phiên bản, phút thật từ `staff_review_decision` và `staff_rework_completed`; mẫu số lấy `request_outcome_finalized.ket_qua == thanh_cong`, sau khi kiểm tra cả số tiền. Chỉ đóng ticket và không mở lại chưa đủ để chứng minh đúng tiền.

## E2 · Rủi ro kinh tế

B1 là **toàn mẫu, tối đa 3 lượt**; B4 và A4 là phạm vi noi_dia + hang_nang theo giả định riêng. Không dùng các số này làm chi phí đã đo của pilot 2 lượt.

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Làm lại tăng gấp đôi | B1 toàn mẫu: từ 4.471,97 lên 6.786,90 đ/việc, +51,77% (simulated). Trong phạm vi pilot 2 lượt: từ 3.251,56 lên 4.854,70 đ, +49,30% (simulated) | Số request_id có staff_rework_completed / yêu cầu trong phạm vi > 7%/tuần; baseline mẫu là 48/982 = 4,89%, chưa áp giới hạn 2 lượt | PM rà 20 trace làm lại; đối chiếu luật dừng 8.000 đ/việc trong 2 tuần trước khi quyết định thu hẹp phạm vi | PM trợ lý hoàn phí |
| Xem lại 100% kéo dài | B4: 11.742,79 đ/việc với 9 phút làm lại; 12.414,79 đ nếu 15,3 phút (simulated). Hoà vốn xem lại lần lượt 5,12 và 4,80 phút (simulated), chưa gồm cố định | Tỉ lệ yêu cầu được xem lại > 50% cuối bước 0,25; đo phút thật và audit sai tiền hằng tuần | Chỉ đề xuất giảm xem lại theo bậc khi sửa + bo < 15%, audit an toàn đạt và người phụ trách phê duyệt | Trưởng nhóm CSKH |
| Khối lượng thấp | A4: cố định thêm 1.185,19 đ/việc ở tổng 45.000 yêu cầu/tháng; 2.370,37 đ ở 22.500 yêu cầu/tháng; CPS gồm cố định 4.599,09 và 5.784,27 đ (simulated), giả định A4 chưa áp giới hạn 2 lượt | Số việc thành công/tuần < 50% kế hoạch; tính lại cố định trên số việc thành công trong phạm vi | Không tăng rollout; tính lại chi phí và hợp đồng vận hành trước khi mở rộng | PM trợ lý hoàn phí |

### Đối chiếu bổ sung đúng phương án pilot

Dùng `mo_hinh(runs, reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])], max_lan_chay=2)` và đổi hệ số xem lại/làm lại cho từng kịch bản: giữ 982 yêu cầu, có **892 việc thành công**. Chi phí dùng phút simulated; không phải kết quả đo pilot thật, chưa gồm cố định hoặc phần nhân viên làm thay.

| Kịch bản | CPS (đ, simulated) | Thay đổi (simulated) |
| --- | ---: | ---: |
| Gốc, tối đa 2 lượt | 3.251,56 | 0,00% |
| Làm lại gấp đôi | 4.854,70 | +49,30% |
| Xem lại gấp đôi | 4.659,63 | +43,30% |

Cộng nhân viên làm thay 90 ca chưa thành công: (2.900.391,39 + 90 × 12.000) ÷ 982 = **4.053,35 đ/yêu cầu (simulated)**, chưa gồm chi phí cố định.
