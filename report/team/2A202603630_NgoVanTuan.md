# Báo cáo cá nhân — Ngô Văn Tuân — 2A202603630

## 1. Thông tin thành viên

- Họ tên: Ngô Văn Tuân.
- MSSV: 2A202603630.
- Email: 26ai.tuannv3@vinuni.edu.vn.
- Vai trong nhóm: Người kiểm số.

## 2. Phần việc phụ trách

Kiểm số CP1 (A1–A4) và CP2 (B1–B4), đối chiếu kết quả code với phép tính độc lập từ dữ liệu gốc, có hỗ trợ của Codex.

## 3. Đóng góp cụ thể

- CP1: đối chiếu chi phí token, tool, xem lại/làm lại, tổng theo bốn loại yêu cầu và phân bổ chi phí cố định; bổ sung bảng A1–A4 và nhãn simulated.
- CP2: đối chiếu đủ 9 kịch bản B1, tính cộng dồn B2, chi phí hệ thống theo 3 giới hạn B3 và 2 giả định làm lại ở B4.
- Sửa ký hiệu tăng/giảm ở B2, làm rõ mức làm tròn ở B4 và bổ sung bằng chứng tính vào bảng chi phí.

## 4. Bằng chứng

- CP1: commit `1e709a7` (`CP1`).
- Code và cách chạy: `cd src`, rồi `python -X utf8 -B lab13.py`.
- Bảng số và công thức đối chiếu: [bang_chi_phi.md](bang_chi_phi.md).
- B1, làm lại gấp đôi: (4.373.585,132 + 2.264.000) ÷ 978 = **6.786,90 đ/việc**, tăng **51,77% (simulated)**.
- B2, token và xem lại gấp đôi: (4.373.585,132 + 245.585,132 + 1.780.000) ÷ 978 = **6.543,12 đ/việc (simulated)**.
- B3, tối đa 2 lần chạy: 4.093.220,23 + 234 × 12.000 = **6.901.220,23 đ cho cả hệ thống (simulated)**; rẻ nhất trong 3 giới hạn đã xét.
- B4: (224.513,274 + 948 × 5 × 2.000 + 48 × 9 × 2.000) ÷ 900 = **11.742,79 đ/việc (simulated)**. Thay 9 bằng 15,3 phút làm lại cho **12.414,79 đ/việc (simulated)**.

## 5. Công cụ AI đã dùng

Codex hỗ trợ đọc yêu cầu, triển khai/ghép code, chạy kiểm tra và soạn bảng. Phép kiểm độc lập chạy trong terminal, dùng `csv` và `Decimal` tính lại từ hai CSV, rồi so với `mo_hinh()` dùng pandas; kiểm quan hệ nhân đôi/chia đôi, cộng tuyến tính và việc giữ nguyên input.

Số liệu là giả lập của lab; các kết quả dùng phút `_simulated` đều ghi nhãn simulated. Không gọi model qua API và không sửa hai CSV.

## 6. Tự đánh giá

CP1–CP2 đã có phép tính và kết quả kiểm tra để đối chiếu. Các kết luận chi phí phụ thuộc phút simulated; cần đo thời gian thật trong pilot. Chưa ghi nhận đóng góp hoặc kết quả duyệt chéo CP3–CP5.
