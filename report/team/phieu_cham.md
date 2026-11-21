# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): 3chan
- Nhóm được chấm: ABC
- link repo :https://github.com/nhvtmanh/K5-L3A-DAY13-NhomABC-LaunchEconomics.git


| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | Chi phí trung bình cho mỗi công việc thành công là 4.472 đồng, thấp hơn so với phương án thủ công 12.000 đồng/yêu cầu. Tuy nhiên, khi số ca phải làm lại tăng gấp đôi, chi phí tăng 51,8%. Đây là rủi ro cần được xem xét trước khi triển khai. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Nhóm sử dụng bộ dữ liệu giả lập gồm 1.200 yêu cầu và 1.624 lượt chạy Agent. Phạm vi thử nghiệm được giới hạn ở 40 nhân viên, chia đều thành hai nhóm thử nghiệm và đối chứng, mỗi nhóm 20 người. |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Kế hoạch Pilot gồm hai nhóm, mỗi nhóm 20 nhân viên, với mục tiêu phát hiện mức chênh lệch 6 điểm phần trăm. Nhóm đã đề xuất theo dõi tỷ lệ mở lại, với ngưỡng chênh lệch tối đa 2 điểm phần trăm so với nhóm đối chứng và tỷ lệ mở lại không vượt quá 6%. |
| **Tổng** | | | | **30/ 30** | |

**Quyết định của hội đồng:** Go · Go có điều kiện · No-go (giữ một)

**Lý do:**
Chi phí xử lý bằng Agent trung bình là 5.865 đồng/yêu cầu, thấp hơn mức 12.000 đồng khi xử lý thủ công. Tuy nhiên, khi số ca làm lại tăng gấp đôi, chi phí tăng 51,8%. Vì vậy, nhóm cần triển khai Pilot có kiểm soát, theo dõi các chỉ số an toàn và hoàn thiện biện pháp xử lý rủi ro trước khi mở rộng.
**Một câu hỏi cho đội trình:** ...Nếu tỷ lệ yêu cầu bị mở lại tăng cao hoặc Agent thực hiện hoàn tiền trùng lặp trong quá trình Pilot, nhóm sẽ xử lý như thế nào?

**Câu trả lời của đội trình (ghi lại tại buổi):** ...Nếu tỷ lệ yêu cầu bị mở lại vượt 6% hoặc cao hơn nhóm đối chứng trên 2 điểm phần trăm, nhóm sẽ tạm dừng Pilot để kiểm tra nguyên nhân. Trường hợp phát hiện hoàn tiền trùng lặp, hệ thống sẽ ngừng chức năng hoàn tiền tự động ngay lập tức, chuyển các yêu cầu sang nhân viên xử lý và đối soát giao dịch. Nhóm chỉ tiếp tục thử nghiệm sau khi khắc phục lỗi, kiểm thử lại và được người phụ trách phê duyệt.
