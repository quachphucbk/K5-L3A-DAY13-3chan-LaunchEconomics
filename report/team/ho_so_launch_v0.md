# Hồ sơ Launch v0 · LogiX-VN · Gate 2a

Nhóm: 3chan · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.471,97 đ/việc [simulated]; 978 việc thành công (mẫu 1.200 yêu cầu) | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | Làm lại gấp đôi +51,77%; xem lại gấp đôi +40,70%; lương +25% làm chi phí tăng 23,12% [simulated] | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | 5.865 đ/yêu cầu cho toàn hệ thống [simulated] so với 12.000 đ/yêu cầu thủ công (0,49×) | Giả lập | PM trợ lý hoàn phí |
| 4 · Chỉ số chính, dùng, an toàn | Chỉ số trong đợt chạy thử: đóng trong 24h, không mở lại: 82,83%; bỏ qua gợi ý: 27,12%; mở lại trong 7 ngày: 4,25% (mẫu thử, chưa có đối chứng) — `chi_so.md` | Xong, có bằng chứng | PM trợ lý hoàn phí |
| 5 · Bảng lỗi và cách khắc phục | 20 ca, 5 loại; đồng thuận 90% (18/20), 2 ca không trùng đã thống nhất nhãn; 5 biện pháp khắc phục — `bang_loi.md` | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chia theo nhân viên 20/20; 5.980 yêu cầu/nhóm để phát hiện chênh 6 điểm (power 0,64 nếu tác động thật 5 điểm); 3 luật dừng có ngưỡng, thời hạn, người dừng — `pilot_plan.yaml` | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Làm lại gấp đôi: +51,77%, lên 6.786,90 đ/việc; xem lại 100%: 11.742,79 đ/việc, hoặc 12.414,79 đ nếu làm lại 15,3 phút [simulated] — `chi_so.md` | Giả lập | PM trợ lý hoàn phí |

**Đề xuất: Go có điều kiện — chỉ pilot `noi_dia` và `hang_nang`; loại `quoc_te` (22.515,17 đ/việc [simulated], 1,88× mức thủ công) và `doi_tac` (0,85× [simulated], có điều khoản riêng).**

**Lý do:** Chi phí 4.471,97 đ/việc [simulated] chưa gồm nhân viên làm thay; chi phí toàn hệ thống là 5.865 đ/yêu cầu [simulated], thấp hơn mức thủ công 12.000 đ. Tuy nhiên, xem lại 100% gần chạm mức thủ công (11.742,79 đ = 0,98× [simulated]) và kịch bản làm lại 15,3 phút vượt mức này (12.414,79 đ = 1,03× [simulated]). Các chỉ số trong đợt chạy thử là 82,83%, 27,12% và 4,25%; chúng chỉ mô tả mẫu, chưa chứng minh hiệu quả nhân quả; tỷ lệ mở lại 4,25% cần theo dõi an toàn. Nhãn lỗi đồng thuận 90%; 2 ca không trùng (13, 20) đã thống nhất và có quy tắc phân biệt. Với 40 nhân viên, thiết kế 20/20 chỉ đạt cỡ mẫu nếu chấp nhận mức chênh 6 điểm (5.980 yêu cầu/nhóm); nếu tác động thật chỉ 5 điểm, power khoảng 0,64.

**Điều kiện trước khi duyệt bắt đầu pilot:**

- Sửa và kiểm thử khóa chống hoàn trùng, đối soát sổ cái (ca 20); đạt kiểm thử không hoàn hai lần – Kỹ sư trưởng agent – 04/01/2027.
- Giám đốc vận hành phê duyệt phạm vi, cỡ mẫu 20 nhân viên mỗi nhóm và chấp nhận mức chênh phát hiện 6 điểm (power 0,64 ở mức 5 điểm); chốt đủ 3 luật dừng – Giám đốc vận hành LogiX-VN – 05/01/2027.
- Bật event có `trace_id`, so sánh tỷ lệ mở lại với nhóm đối chứng (ngưỡng chênh +2 điểm, trần 6%), và thay phút giả lập bằng thời gian đo thật sau tuần đầu; có phương án tắt trong 30 phút, chuyển khách sang luồng nhân viên – Giám đốc vận hành LogiX-VN – trước rollout đầu tiên.
- Có kế hoạch giảm xem lại theo bậc khi tỉ lệ sửa + bỏ < 15%, vì xem lại 100% gần như không tiết kiệm (0,98× [simulated]) – Trưởng nhóm CSKH – cuối bước rollout 0,25.
