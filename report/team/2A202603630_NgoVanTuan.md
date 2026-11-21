# Báo cáo cá nhân — Ngô Văn Tuân — 2A202603630

## 1. Thông tin thành viên

- Họ tên: **Ngô Văn Tuân**.
- MSSV: **2A202603630**.
- Email: 26ai.tuannv3@vinuni.edu.vn.
- GitHub: [ngotuna23a](https://github.com/ngotuna23a).
- Nhóm: **3chan** · Lớp: **L3A**.
- Vai trò: **Người kiểm số**.

## 2. Phần việc phụ trách

Tôi phụ trách đối chiếu công thức, số liệu và kết luận kinh tế của Lab 13: CP1 (A1–A4), CP2 (B1–B4), cỡ mẫu và kiểm tra thiết kế CP4 (D1–D2), chỉ số và rủi ro CP5 (E1–E3). Công việc được thực hiện với hỗ trợ của Codex, dựa trên hai CSV gốc và code chung của nhóm.

Tôi phối hợp với người viết code để đối chiếu kết quả và bổ sung bằng chứng vào hồ sơ. Hai bộ nhãn CP3 do Nguyễn Đức Minh và Hồ Quốc Toản cung cấp; tôi sử dụng kết quả đồng thuận 18/20 = 90% khi kiểm tính nhất quán của hồ sơ.

## 3. Đóng góp cụ thể

- **CP1:** đối chiếu ba phép thử A1; chi phí token, tool, xem lại và làm lại ở A2; bảng theo bốn loại yêu cầu A3; phân bổ chi phí cố định A4. Khi ghép với bản của team, giữ các phần đã cập nhật và bổ sung độ chính xác, nguồn tính cùng nhãn simulated.
- **CP2:** kiểm độc lập đủ 9 kịch bản B1; quan hệ cộng tuyến tính B2; chi phí cả hệ thống với giới hạn 1/2/3 lượt ở B3; hai giả định thời gian làm lại ở B4. Sửa ký hiệu tăng/giảm, làm rõ bước làm tròn và ghi công thức để đối chiếu.
- **CP4:** tính đủ 5 câu D1, phân biệt cỡ mẫu hiệu dụng và số yêu cầu thực tế; tính tỉ lệ mở lại hiện tại. Bổ sung 5 câu D2 theo thiết kế đã ghi trong kế hoạch: đối chứng cùng thời gian, ngẫu nhiên, spillover, viết trước và số cụm.
- **CP5:** đối chiếu code E1–E2 team đã cập nhật bằng phép tính độc lập; tính thêm chi phí đúng phạm vi noi_dia + hang_nang, tối đa 2 lượt. Bổ sung đặc tả 12 event, 3 rủi ro kinh tế, timestamp và cách loại trùng; nối các trace theo request_id.
- **Hồ sơ E3:** kiểm số giữa bảng chi phí, chỉ số và pilot plan; phân biệt toàn mẫu với phạm vi pilot; đưa đề xuất xuống dòng cuối và ghi rõ lịch pilot còn cần xác nhận.

## 4. Bằng chứng

### Commit đóng góp

| Phần | Commit | Nội dung |
| --- | --- | --- |
| CP1 | [1e709a7](https://github.com/quachphucbk/K5-L3A-DAY13-3chan-LaunchEconomics/commit/1e709a7f6d831a8fde7a317acda5fde395100ce5) | Ghép và đối chiếu A1–A4, bổ sung bảng chi phí và thông tin cá nhân |
| CP2 | [d412cbb](https://github.com/quachphucbk/K5-L3A-DAY13-3chan-LaunchEconomics/commit/d412cbbb070ac55f680c1e07b9afe4d2fa0c6a5e) | Kiểm số B1–B4, làm rõ giả định và bổ sung bằng chứng cá nhân |
| CP4 — D1 | [eccc012](https://github.com/quachphucbk/K5-L3A-DAY13-3chan-LaunchEconomics/commit/eccc01270cc92d15dd806528044fc2cdb67049bd) | Tính cỡ mẫu và tỉ lệ mở lại, ghi kết quả vào chú thích YAML |
| CP4 — D2 | [7b46e87](https://github.com/quachphucbk/K5-L3A-DAY13-3chan-LaunchEconomics/commit/7b46e875d9553b2eb7181ba4b2b428d70f47d480) | Bổ sung 5 câu kiểm tra tách được tác động |
| CP5 — E1–E3 | [2915a0a](https://github.com/quachphucbk/K5-L3A-DAY13-3chan-LaunchEconomics/commit/2915a0a61fce74e01538bb9b7cce820f8ac72b8e) | Kiểm chỉ số, chi phí pilot 2 lượt, đặc tả event, rủi ro và hồ sơ launch |

### File và kết quả đối chiếu

- Code: [src/lab13.py](../../src/lab13.py).
- Bảng A–B: [bang_chi_phi.md](bang_chi_phi.md).
- Cỡ mẫu, D2: [pilot_plan.yaml](pilot_plan.yaml).
- Chỉ số, event, rủi ro: [chi_so.md](chi_so.md).
- Hồ sơ tổng hợp: [ho_so_launch_v0.md](ho_so_launch_v0.md).

| Phần | Kết quả chính |
| --- | --- |
| A1–A2 | A1 đạt **1,20 · 1,25 · 1,25**. A2 có **978 việc thành công**, CPS **4.471,97 đ/việc (simulated)** |
| A3–A4 | quoc_te thành công **27,33%**, CPS **22.515,17 đ (simulated)**. Phạm vi nội địa + hàng nặng cộng cố định: **4.599,09 đ/việc** ở 45.000 yêu cầu/tháng, **5.784,27 đ/việc** ở nửa khối lượng, đều simulated |
| B1–B2 | Làm lại gấp đôi: **6.786,90 đ/việc, +51,77% (simulated)**. Token và xem lại cùng gấp đôi: **6.543,12 đ/việc (simulated)** |
| B3–B4 | Giới hạn **2 lượt** rẻ nhất cho cả hệ thống: **6.901.220,23 đ (simulated)**. Xem lại 100%: **11.742,79 đ/việc**, hoặc **12.414,79 đ/việc** nếu làm lại 15,3 phút, đều simulated |
| D1 | MDE 5 điểm cần **1.251 yêu cầu/nhóm**. Với 75 yêu cầu/người, DE **2,48**, cần **42 người/nhóm**. MDE 6 điểm với 20 người/nhóm cần **299 yêu cầu/người**, tức **5.980 yêu cầu thực/nhóm**, DE **6,96** |
| E1 | Chính **994/1.200 = 82,83%**; bỏ qua gợi ý **48/177 = 27,12%**; mở lại **51/1.200 = 4,25%** |
| E2 | Phạm vi pilot 2 lượt: **892 việc thành công**, CPS **3.251,56 đ/việc (simulated)**. Cộng nhân viên làm thay 90 ca: **4.053,35 đ/yêu cầu (simulated)**, chưa gồm cố định |

Các phép tính dùng để đối chiếu:

- **B1:** (4.373.585,132 + 2.264.000) ÷ 978 = **6.786,90 đ/việc (simulated)** khi làm lại gấp đôi.
- **B3:** 4.093.220,23 + 234 × 12.000 = **6.901.220,23 đ (simulated)** ở giới hạn 2 lượt.
- **B4:** (224.513,274 + 948 × 5 × 2.000 + 48 × 9 × 2.000) ÷ 900 = **11.742,79 đ/việc (simulated)**.
- **D1e:** 20 × 299 ÷ [1 + (299 − 1) × 0,02] = **859,20 hiệu dụng/nhóm**. Với 298 yêu cầu/người chỉ đạt khoảng **858,79**, nên 299 là mức tối thiểu để đạt 859.
- **E2:** (2.900.391,39 + 90 × 12.000) ÷ 982 = **4.053,35 đ/yêu cầu (simulated)** trong phạm vi pilot 2 lượt.

Chạy lại từ thư mục gốc repo:

```powershell
cd src
python -X utf8 -B lab13.py
```

Kết quả kiểm tra đã thực hiện: ba phép thử A1 đạt; script chạy hết A–B–D1–E1–E2; B1–B4 và chi phí pilot khớp phép tính độc lập từ CSV; D1 được đối chiếu bằng scipy và phép tính phân số; YAML đọc được. Hồ sơ E3 có 7 mục và đề xuất ở dòng cuối.

## 5. Công cụ AI đã dùng

**Codex** hỗ trợ đọc yêu cầu, triển khai và ghép code, chạy kiểm tra, phát hiện chênh lệch và soạn báo cáo. Các phép kiểm được thực hiện bằng code trong terminal, không lấy số do AI tự suy đoán làm kết quả.

Cách đối chiếu có hỗ trợ của Codex:

1. Đọc hai CSV bằng `csv`, dùng `Decimal` tính lại chi phí, số việc thành công và các chỉ số; so với `mo_hinh()` dùng pandas.
2. Kiểm quan hệ nhân đôi/chia đôi trước làm tròn, tác động cộng tuyến tính và chi phí nhân viên làm thay. Kiểm DataFrame input không bị thay đổi sau khi gọi mô hình.
3. Đối chiếu D1 với phân vị chuẩn từ scipy và phép tính phân số; kiểm 299 là số nguyên nhỏ nhất đạt yêu cầu.
4. Đối chiếu output với bảng báo cáo, kiểm YAML và các liên kết bằng chứng. Giữ nguyên hai CSV và file starter.

Tài liệu đối chiếu: [hướng dẫn chi tiết Lab 13](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md), [dữ liệu và công thức](../../docs/du_lieu_va_cong_thuc.md), [quy định dùng AI](../../RULES.md). Các event trong báo cáo là đặc tả cần ghi khi pilot, chưa phải log của hệ thống đã triển khai.

## 6. Tự đánh giá

Phần kiểm số đã hoàn thành theo phạm vi đóng góp nêu trên, có code, bảng kết quả và commit để truy vết. Kết quả cho thấy giờ nhân viên ảnh hưởng đến chi phí lớn hơn giá token; giới hạn có CPS thấp nhất không nhất thiết rẻ nhất cho cả hệ thống.

Ba điểm cần giải thích khi bảo vệ: tử số tính mọi lần chạy nhưng mẫu số chỉ đếm việc thành công; chia theo cụm làm giảm cỡ mẫu hiệu dụng; các chỉ số mô tả mẫu thử chưa chứng minh tác động nhân quả. Chỉ số chính có 994 ca không thay cho mẫu số CPS 978 ca vì định nghĩa thành công còn xét đúng tiền.

Các kết luận chi phí còn phụ thuộc phút simulated. Khi pilot, cần đo thời gian thật, chốt lịch và kiểm các điều kiện Go có điều kiện trong hồ sơ. Nếu tác động thật chỉ 5 điểm thay vì 6 điểm, power của thiết kế hiện tại chỉ khoảng **64,18%**.

Tại thời điểm hoàn thiện báo cáo, repo chưa có kết quả duyệt chéo thực tế và báo cáo nhóm còn nội dung cần bổ sung. Báo cáo này chưa ghi điểm hội đồng hoặc phản hồi chưa được cung cấp; sẽ bổ sung khi team có bằng chứng thực tế.
