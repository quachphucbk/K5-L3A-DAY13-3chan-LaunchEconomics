# Báo cáo cá nhân — HoVaTen-MSSV

Copy file này và đổi tên theo quy tắc `MSSV_HoTen.md`. Giữ nguyên file mẫu.

Ví dụ: `20241234_NguyenVanAn.md`.

## 1. Thông tin thành viên

- Họ tên: Nguyễn Đức Minh
- MSSV: 2A202603633
- Email: Jiji.Minh@gmail.com
- Lớp và nhóm: L3A · 3chan
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): người gắn nhãn 1 ở CP3, người viết code ở CP4

## 2. Phần việc phụ trách

Ở CP3, mình gắn nhãn 20 ca lỗi, đối chiếu kết quả với Người gắn nhãn 2 và đề xuất cách khắc phục cho ba loại lỗi. Ở CP4–D1, mình bổ sung phần tính cỡ mẫu pilot vào `src/lab13.py` và chạy lại chương trình để kiểm tra kết quả.


## 3. Đóng góp cụ thể

- **CP3:** Hai bộ nhãn trùng 18/20 ca, đạt 90%. Ở ca 13, nhóm thống nhất nhãn Giới hạn hệ thống vì bảo hiểm đối tác nằm ngoài phạm vi trợ lý. Ở ca 20, nhóm thống nhất nhãn Hệ thống vì thiếu khóa chống trùng dẫn đến hoàn tiền hai lần. Mình đề xuất ba dòng khắc phục cho ca 3 (Ngữ cảnh), ca 13 (Giới hạn hệ thống) và ca 5 (Ngầm).
- **CP4–D1:** Mình bổ sung công thức tính cỡ mẫu cho hai tỷ lệ và tính hệ số thiết kế cho phương án chia theo nhân viên. Với mức tăng từ 70% lên 75%, phương án chia theo yêu cầu cần 1.251 yêu cầu mỗi nhánh. Với 20 nhân viên mỗi nhánh và mục tiêu phát hiện mức tăng 6 điểm phần trăm, cần 299 yêu cầu mỗi nhân viên, tương đương 5.980 yêu cầu thực mỗi nhánh để đạt ít nhất 859 yêu cầu hiệu dụng. Nếu mức tăng thực tế là 5 điểm phần trăm, power ước tính còn 64,18%.
## 4. Bằng chứng

- [Bảng lỗi CP3](bang_loi.md), gồm hai bộ nhãn, tỷ lệ đồng thuận 90% và ba dòng khắc phục do tôi phụ trách.
- Commit `0d604c2` — `Implement CP4 D1 sample size and add run evidence`, chứa phần triển khai D1 và output kiểm tra.
- [Mã nguồn tính cỡ mẫu](../../src/lab13.py). Khi chạy `python .\lab13.py` từ thư mục `src`, cả ba phép thử A1 đều đạt và chương trình in đầy đủ kết quả D1. Tỷ lệ mở lại trong 7 ngày trên dữ liệu lab là 51/1.200 (4,25%) toàn mẫu và 39/982 (3,97%) trong phạm vi nội địa và hàng nặng.


## 5. Công cụ AI đã dùng

Mình dùng ChatGPT để tham khảo cách phân biệt các loại lỗi, soạn đề xuất khắc phục, hỗ trợ triển khai công thức D1 và xử lý lỗi môi trường Python. Mình đối chiếu các nhãn với tình huống trong đề và kiểm tra tỷ lệ đồng thuận từ hai cột nhãn. Với D1, mình chạy mã trên máy, đối chiếu đầu ra với công thức và mốc kiểm tra trong tài liệu lab.

## 6. Tự đánh giá

Qua CP3, mình hiểu rõ hơn cách phân biệt lỗi theo nguyên nhân gốc và cách biến một đề xuất khắc phục thành tiêu chí có thể theo dõi. Qua CP4, mình phân biệt được số yêu cầu thực với cỡ mẫu hiệu dụng khi chia theo cụm. 
