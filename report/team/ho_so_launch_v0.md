# Hồ sơ Launch v0 · LogiX-VN · Gate 2a

Nhóm: 3chan · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | Toàn mẫu: 4.471,97 đ/việc, 978 việc thành công; phạm vi pilot 2 lượt: 3.251,56 đ/việc, 892 việc thành công [simulated], chưa gồm cố định và nhân viên làm thay | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | Làm lại gấp đôi +51,77%; xem lại gấp đôi +40,70%; lương +25% làm chi phí tăng 23,12% [simulated] | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Chi phí cả hệ thống: toàn mẫu 5.864,65 đ/yêu cầu; phạm vi pilot 2 lượt 4.053,35 đ/yêu cầu [simulated], đều đã cộng nhân viên làm thay, chưa gồm cố định; baseline 12.000 đ/yêu cầu | Giả lập | PM trợ lý hoàn phí |
| 4 · Chỉ số chính, dùng, an toàn | Chỉ số trong đợt chạy thử: đóng trong 24h, không mở lại: 82,83%; bỏ qua gợi ý: 27,12%; mở lại trong 7 ngày: 4,25% (mẫu thử, chưa có đối chứng) — `chi_so.md` | Xong, có bằng chứng | PM trợ lý hoàn phí |
| 5 · Bảng lỗi và cách khắc phục | 20 ca, 5 loại; đồng thuận 90% (18/20), 2 ca không trùng đã thống nhất nhãn; 5 biện pháp khắc phục — `bang_loi.md` | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | Đã có thiết kế 20/20, 5.980 yêu cầu/nhóm, MDE 6 điểm (power 0,64 ở mức 5 điểm), 3 luật dừng — `pilot_plan.yaml`; lịch quyết định còn dự kiến, cần chốt sau thu đủ mẫu và theo dõi 7 ngày | Chưa | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Làm lại gấp đôi: +51,77%, lên 6.786,90 đ/việc; xem lại 100%: 11.742,79 đ/việc, hoặc 12.414,79 đ nếu làm lại 15,3 phút [simulated] — `chi_so.md` | Giả lập | PM trợ lý hoàn phí |

**Lý do:** Phạm vi pilot 2 lượt có CPS 3.251,56 đ/việc và chi phí cả hệ thống 4.053,35 đ/yêu cầu [simulated], chưa gồm cố định; đây là mô phỏng từ dữ liệu thử, không phải kết quả pilot thật. B4 xem lại 100% cho 11.742,79 đ = 0,98× hoặc 12.414,79 đ = 1,03× nếu làm lại 15,3 phút [simulated], theo giả định riêng của B4. Chỉ số 82,83%, 27,12%, 4,25% mô tả toàn mẫu chưa có đối chứng; không suy ra cải thiện nhân quả. Nhãn đồng thuận 90%, hai ca 13 và 20 đã thống nhất. Pilot cần chấp nhận MDE 6 điểm; nếu tác động thật 5 điểm, power chỉ khoảng 0,64.

**Điều kiện trước khi duyệt bắt đầu pilot:**

- Sửa và kiểm thử khóa chống hoàn trùng, đối soát sổ cái (ca 20); đạt kiểm thử không hoàn hai lần – Kỹ sư trưởng agent – 04/01/2027.
- Giám đốc vận hành phê duyệt phạm vi, cỡ mẫu 20 nhân viên mỗi nhóm và chấp nhận mức chênh phát hiện 6 điểm (power 0,64 ở mức 5 điểm); chốt đủ 3 luật dừng – Giám đốc vận hành LogiX-VN – 05/01/2027.
- Bật event có `trace_id`, so sánh tỷ lệ mở lại với nhóm đối chứng (ngưỡng chênh +2 điểm, trần 6%), và thay phút giả lập bằng thời gian đo thật sau tuần đầu; có phương án tắt trong 30 phút, chuyển khách sang luồng nhân viên – Giám đốc vận hành LogiX-VN – trước rollout đầu tiên.
- Có kế hoạch giảm xem lại theo bậc khi tỉ lệ sửa + bỏ < 15%, vì xem lại 100% gần như không tiết kiệm (0,98× [simulated]) – Trưởng nhóm CSKH – cuối bước rollout 0,25.

Các ngày 04–05/01/2027 ở trên là mốc dự kiến hiện có; Giám đốc vận hành phải chốt lại lịch trước rollout đầu tiên. Ngày phê duyệt bắt đầu và ngày quyết định kết quả pilot phải tách biệt; chỉ quyết định kết quả sau đủ mẫu và 7 ngày theo dõi cho ca cuối.

**Đề xuất: Go có điều kiện — chỉ pilot `noi_dia` và `hang_nang`, tối đa 2 lượt chạy; loại `quoc_te` (1,88× baseline theo A3, simulated) và `doi_tac` (0,85×, simulated; điều khoản riêng), sau khi đạt các điều kiện trên.**
