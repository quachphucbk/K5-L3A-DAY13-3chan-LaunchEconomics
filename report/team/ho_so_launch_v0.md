# Hồ sơ Launch v0 · LogiX-VN · Gate 2a

Nhóm: 3chan · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.471,97 đ/việc; 978 việc thành công (mẫu 1.200 yêu cầu) | Giả lập | Người viết code |
| 2 · Ba yếu tố nhạy nhất | Làm lại gấp đôi +51,77%; xem lại gấp đôi +40,70%; lương +25% làm chi phí tăng 23,12% | Giả lập | Người kiểm số |
| 3 · So với nhân viên tự làm | 5.865 đ/yêu cầu cho toàn hệ thống so với 12.000 đ/yêu cầu thủ công | Giả lập | Người kiểm số |
| 4 · Chỉ số chính, dùng, an toàn | Đóng trong 24h, không mở lại: 82,83%; bỏ qua gợi ý: 27,12%; mở lại trong 7 ngày: 4,25% (mẫu thử, chưa có đối chứng) | Chưa | Người kiểm số |
| 5 · Bảng lỗi và cách khắc phục | 20 ca, 5 loại; đồng thuận 90% (18/20); 5 biện pháp khắc phục | Xong, có bằng chứng | Người gắn nhãn 1 và 2 |
| 6 · Pilot plan | Đề xuất chia theo nhân viên 20/20; 5.980 yêu cầu/nhóm để phát hiện chênh 6 điểm; 3 luật dừng mẫu; chưa được nhóm chốt | Chưa | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Làm lại gấp đôi: +51,77%, lên 6.786,90 đ/việc; xem lại 100%: 11.742,79 đ/việc, hoặc 12.414,79 đ nếu làm lại 15,3 phút | Giả lập | Người kiểm số |

**Đề xuất: Go có điều kiện — chỉ pilot `noi_dia` và `hang_nang`; loại `quoc_te` (22.515,17 đ/việc, 1,88× mức thủ công) và `doi_tac` (có điều khoản riêng).**

**Lý do:** Chi phí 4.471,97 đ/việc chưa gồm nhân viên làm thay; chi phí toàn hệ thống là 5.865 đ/yêu cầu, thấp hơn mức thủ công 12.000 đ. Tuy nhiên, xem lại 100% gần chạm mức thủ công và kịch bản làm lại 15,3 phút vượt mức này. Các chỉ số 82,83%, 27,12% và 4,25% chỉ mô tả mẫu, chưa chứng minh hiệu quả nhân quả; tỷ lệ mở lại 4,25% cần theo dõi an toàn. Nhãn lỗi đồng thuận 90%, còn 2/20 ca bất đồng. Với 40 nhân viên, thiết kế 20/20 chỉ đạt cỡ mẫu nếu chấp nhận mức chênh 6 điểm (5.980 yêu cầu/nhóm); nếu tác động thật chỉ 5 điểm, power khoảng 0,64. Kế hoạch pilot vẫn cần được nhóm thống nhất.

**Điều kiện trước khi duyệt bắt đầu pilot:**

- Sửa và kiểm thử khóa chống hoàn trùng, đối soát sổ cái; đạt kiểm thử không hoàn hai lần – Người viết code – 04/01/2027.
- Giám đốc vận hành phê duyệt phạm vi, cỡ mẫu 20 nhân viên mỗi nhóm và chấp nhận mức chênh phát hiện 6 điểm; chốt đủ 3 luật dừng – Giám đốc vận hành LogiX-VN – 05/01/2027.
- Bật event có `trace_id`, so sánh tỷ lệ mở lại với nhóm đối chứng (ngưỡng chênh +2 điểm, trần 6%), và thay phút giả lập bằng thời gian đo thật sau tuần đầu; có phương án tắt trong 30 phút, chuyển khách sang luồng nhân viên – Giám đốc vận hành LogiX-VN – trước rollout đầu tiên.
