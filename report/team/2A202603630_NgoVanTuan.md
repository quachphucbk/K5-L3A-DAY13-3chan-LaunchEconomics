# Báo cáo cá nhân — Ngô Văn Tuân — 2A202603630

**Trạng thái: đã kiểm số CP1–CP2, làm D1–D2 và kiểm E1–E3 của CP5.** Còn chờ team xác nhận lịch pilot, hoàn thiện báo cáo nhóm và duyệt chéo thực tế.

## 1. Thông tin thành viên

- Họ tên: Ngô Văn Tuân.
- MSSV: 2A202603630.
- Email: 26ai.tuannv3@vinuni.edu.vn.
- Vai trong nhóm: Người kiểm số.

## 2. Phần việc phụ trách

Kiểm số CP1 (A1–A4), CP2 (B1–B4), tính cỡ mẫu và bổ sung D2 ở CP4; kiểm chỉ số E1, rủi ro E2 và tính nhất quán của hồ sơ E3. Các phép đối chiếu có hỗ trợ của Codex.

| Phần | Trạng thái hiện tại | Phần cần bổ sung |
| --- | --- | --- |
| CP1 — Mô hình chi phí | Hoàn thành A1–A4, đã push | Phản hồi đối chiếu của team nếu có |
| CP2 — Độ nhạy | Hoàn thành kiểm số B1–B4, đã push | Phản hồi đối chiếu của team nếu có |
| CP3 — Phân loại lỗi | Bảng của team đã có hai người gắn nhãn, đồng thuận 18/20 = 90% và 5 biện pháp khắc phục | Không nhận phần gắn nhãn độc lập là đóng góp cá nhân |
| CP4 — Kế hoạch pilot | Đã tính D1, bổ sung D2; team đã có thiết kế và 3 luật dừng | Team xác nhận lịch, gộp chú thích D2 lặp nếu cần |
| CP5 — Hồ sơ và duyệt chéo | Đã kiểm độc lập E1, E2 và đối chiếu hồ sơ E3 | Báo cáo nhóm, hồ sơ nhóm được chấm và phản hồi hội đồng thực tế |

## 3. Đóng góp cụ thể

- CP1: đối chiếu chi phí token, tool, xem lại/làm lại, tổng theo bốn loại yêu cầu và phân bổ chi phí cố định; bổ sung bảng A1–A4 và nhãn simulated.
- CP2: đối chiếu đủ 9 kịch bản B1, tính cộng dồn B2, chi phí hệ thống theo 3 giới hạn B3 và 2 giả định làm lại ở B4.
- Sửa ký hiệu tăng/giảm ở B2, làm rõ mức làm tròn ở B4 và bổ sung bằng chứng tính vào bảng chi phí.
- D1: tính cỡ mẫu cho cách chia theo yêu cầu, nhân viên và depot; phân biệt cỡ mẫu hiệu dụng với số yêu cầu thực tế, ghi kết quả trong chú thích `pilot_plan.yaml`.
- D2: ghi đủ 5 câu kiểm tra tách được tác động theo phương án team đã ghi trong kế hoạch.
- CP5: kiểm độc lập 3 chỉ số; bổ sung timestamp, event loại trùng và liên kết theo request_id vì một yêu cầu có nhiều trace; làm rõ mẫu số CPS khác chỉ số chính.
- E2–E3: tính thêm chi phí đúng phạm vi noi_dia + hang_nang với tối đa 2 lượt, gắn nhãn simulated, đối chiếu hồ sơ và đưa đề xuất xuống dòng cuối.

Phần kiểm số CP2 dựa trên code và bảng team đã cập nhật; đóng góp ở bước đối chiếu độc lập, bổ sung cách tính và hiệu chỉnh cách trình bày kết quả.

## 4. Bằng chứng

- CP1: [commit 1e709a7 — CP1](https://github.com/quachphucbk/K5-L3A-DAY13-3chan-LaunchEconomics/commit/1e709a7f6d831a8fde7a317acda5fde395100ce5).
- CP2: [commit d412cbb — CP2](https://github.com/quachphucbk/K5-L3A-DAY13-3chan-LaunchEconomics/commit/d412cbbb070ac55f680c1e07b9afe4d2fa0c6a5e).
- CP4: commit `eccc012` bổ sung D1 và commit `7b46e87` bổ sung D2.
- Code và cách chạy: `cd src`, rồi `python -X utf8 -B lab13.py`.
- Bảng số và công thức đối chiếu: [bang_chi_phi.md](bang_chi_phi.md).
- A1: ba phép thử đạt **1,20 · 1,25 · 1,25**; A2 có **978 việc thành công**, chi phí **4.471,97 đ/việc (simulated)**.
- A3: quoc_te chỉ thành công **27,33%**, chi phí **22.515,17 đ/việc (simulated)**; A4 trong phạm vi noi_dia + hang_nang là **4.599,09 đ/việc** ở 45.000 yêu cầu/tháng và **5.784,27 đ/việc** ở nửa khối lượng, đều **simulated** và đã cộng chi phí cố định.
- B1, làm lại gấp đôi: (4.373.585,132 + 2.264.000) ÷ 978 = **6.786,90 đ/việc**, tăng **51,77% (simulated)**.
- B2, token và xem lại gấp đôi: (4.373.585,132 + 245.585,132 + 1.780.000) ÷ 978 = **6.543,12 đ/việc (simulated)**.
- B3, tối đa 2 lần chạy: 4.093.220,23 + 234 × 12.000 = **6.901.220,23 đ cho cả hệ thống (simulated)**; rẻ nhất trong 3 giới hạn đã xét.
- B4: (224.513,274 + 948 × 5 × 2.000 + 48 × 9 × 2.000) ÷ 900 = **11.742,79 đ/việc (simulated)**. Thay 9 bằng 15,3 phút làm lại cho **12.414,79 đ/việc (simulated)**.
- D1: cần **1.251 yêu cầu/nhóm** cho mức chênh 5 điểm; với 75 yêu cầu/người, DE = **2,48**, cần **42 người/nhóm**, vượt tổng 40 người hiện có. Chia 20 người/nhóm có trần hiệu dụng **1.000**, chia 6 depot/nhóm có trần **300**.
- D1e: thiết kế team đã ghi chọn mức chênh 6 điểm, cần **859 hiệu dụng/nhóm**; với 20 người/nhóm cần **299 yêu cầu/người**, DE = **6,96**, tương ứng **5.980 yêu cầu thực tế/nhóm**; lịch và phê duyệt bắt đầu vẫn cần xác nhận.
- Tỉ lệ mở lại hiện tại: toàn mẫu **51/1.200 = 4,25%**; phạm vi noi_dia + hang_nang **39/982 = 3,97%**, làm cơ sở đối chiếu ngưỡng an toàn.
- E1: chỉ số chính **994/1.200 = 82,83%**; bỏ qua gợi ý **48/177 = 27,12%**; mở lại **51/1.200 = 4,25%**. Đây là số mô tả đợt chạy thử, không phải bằng chứng tác động nhân quả.
- E2: phạm vi pilot 2 lượt có **892 việc thành công**, CPS **3.251,56 đ/việc (simulated)**. Làm lại gấp đôi cho **4.854,70 đ**, xem lại gấp đôi cho **4.659,63 đ/việc (simulated)**. Cộng 90 ca nhân viên làm thay cho **4.053,35 đ/yêu cầu (simulated)**, chưa gồm cố định.
- Event và rủi ro được đặc tả trong [chi_so.md](chi_so.md); bằng chứng được đối chiếu với [ho_so_launch_v0.md](ho_so_launch_v0.md). Đây là thiết kế event cần bật trong pilot, không phải hệ thống đã được triển khai.

Kết quả kiểm tra: script chạy hết phần A–B; ba phép thử A1 đạt; B1 đủ 9 kịch bản, B2 cộng tuyến tính, B3 đủ 3 giới hạn và B4 đủ 2 giả định đều khớp phép kiểm độc lập. Hai DataFrame input được kiểm tra không bị thay đổi sau khi gọi mô hình.

## 5. Công cụ AI đã dùng

Codex hỗ trợ đọc yêu cầu, triển khai/ghép code, chạy kiểm tra và soạn bảng. Phép kiểm độc lập chạy trong terminal, dùng `csv` và `Decimal` tính lại từ hai CSV, rồi so với `mo_hinh()` dùng pandas; kiểm quan hệ nhân đôi/chia đôi, cộng tuyến tính và việc giữ nguyên input.

Số liệu là giả lập của lab; các kết quả dùng phút `_simulated` đều ghi nhãn simulated. Không gọi model qua API và không sửa hai CSV.

## 6. Tự đánh giá

Phần kiểm số đã có phép tính để đối chiếu từ CP1 đến E1–E3. Các kết luận chi phí phụ thuộc phút simulated; cần đo thời gian thật trong pilot. Chưa có kết quả duyệt chéo thực tế và lịch pilot cuối cùng.

Điểm cần nắm để giải thích: tử số tính mọi lần chạy còn mẫu số chỉ đếm việc thành công; phương án có CPS thấp nhất có thể không rẻ nhất cho cả hệ thống; xem lại 100% có thể làm mất lợi ích chi phí.

Việc tiếp theo: team xác nhận lịch pilot, hoàn thiện báo cáo nhóm và thực hiện duyệt chéo; bổ sung báo cáo cá nhân bằng phản hồi thực tế sau buổi duyệt.
