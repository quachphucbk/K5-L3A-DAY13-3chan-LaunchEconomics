# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: 3chan
- Lớp: L3A
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Dựng hồ sơ launch v0 cho trợ lý hoàn phí LogiX-VN để hội đồng Gate 2a quyết định có cho chạy pilot hay không, trả lời bốn câu: có đáng chạy không, nhân viên có dùng không, khi hỏng thì sao, pilot thiết kế thế nào để ra được quyết định.

Cách tiếp cận: mọi con số tính bằng `src/lab13.py` từ hai file CSV (1.200 yêu cầu, 1.624 lần chạy), đối chiếu với số tham khảo sau mỗi checkpoint (lệch dưới 2%); người kiểm số tính độc lập để đối chiếu. Số từ cột `_simulated` đều ghi nhãn simulated. Nhiệm vụ sau dùng lại số của nhiệm vụ trước để hồ sơ nhất quán.

## 3. Giải pháp

| Nhiệm vụ | Cách làm | File |
| --- | --- | --- |
| A · Chi phí | Ba hàm A1 (qua 1,20 · 1,25 · 1,25); `mo_hinh()` cộng token + tool trên mọi lần chạy, cộng phút xem lại + làm lại, chia cho số việc thành công; tách theo loại; cộng chi phí cố định 40 triệu đ/tháng | [`bang_chi_phi.md`](bang_chi_phi.md), `src/lab13.py` |
| B · Độ nhạy | Gọi lại `mo_hinh()` cho 9 kịch bản, 1 cặp, 3 giới hạn số lần chạy (tính cả chi phí cả hệ thống), kịch bản xem lại 100% | [`bang_chi_phi.md`](bang_chi_phi.md) |
| C · Bảng lỗi | Hai người gắn nhãn độc lập 20 ca theo 5 loại Google PAIR, so nhãn, viết quy tắc cho ca không trùng; bảng khắc phục 5 ca có event, ngưỡng, tần suất, vai trò phụ trách | [`bang_loi.md`](bang_loi.md) |
| D · Pilot | Tính 5 câu D1 trước khi chọn cách chia; chọn chia theo nhân viên 20 + 20 và chấp nhận mức chênh 6 điểm; 3 luật dừng NẾU – TRONG – THÌ – KHÔNG THÌ; ngưỡng an toàn đặt theo tỉ lệ mở lại hiện tại | [`pilot_plan.yaml`](pilot_plan.yaml) |
| E · Chỉ số, hồ sơ | Tính thử 3 chỉ số, đề xuất thêm 2 chỉ số; 11 event có `trace_id` và kiểm tra chéo; 3 dòng rủi ro kinh tế; hồ sơ một trang 7 mục | [`chi_so.md`](chi_so.md), [`ho_so_launch_v0.md`](ho_so_launch_v0.md) |
| Duyệt chéo | Nhóm 3chan làm hội đồng chấm nhóm ABC theo 3 tiêu chí | [`phieu_cham.md`](phieu_cham.md) |

## 4. Kết quả

**Con số chính:**

- Chi phí mỗi việc thành công: **4.472 đ** [simulated], gấp 16,3 lần hoá đơn token chia số yêu cầu; giờ nhân viên chiếm 92,5% tổng chi phí [simulated].
- So với nhân viên tự làm (12.000 đ): chi phí cả hệ thống **5.865 đ/yêu cầu = 0,49×** [simulated]; phạm vi pilot noi_dia + hang_nang, tối đa 2 lượt chạy: 4.053 đ/yêu cầu [simulated], chưa gồm chi phí cố định.
- Theo loại: noi_dia 0,22×, hang_nang 0,69×, quoc_te **1,88×**, doi_tac 0,85× [simulated]; với quoc_te, chạy lại không giúp (ok 30,0% → 11,4% → 2,2%).
- Ba yếu tố nhạy nhất: số ca làm lại (+51,8% khi gấp đôi), tỉ lệ xem lại (+40,7%), lương nhân viên (+23,1% khi tăng 25%) [simulated]; giá token chỉ +5,6%.
- Con số bất lợi: xem lại 100% đẩy chi phí lên **11.743 đ = 0,98×**, hoặc 12.415 đ = 1,03× nếu làm lại 15,3 phút như dữ liệu [simulated].
- Chỉ số trong đợt chạy thử (chưa có đối chứng): chính 82,83%, dùng (bỏ qua gợi ý) 27,12%, an toàn (mở lại trong 7 ngày) 4,25%.
- Bảng lỗi: đồng thuận 18/20 = 90%.
- Pilot: chia theo nhân viên 20 + 20, cần 299 yêu cầu mỗi nhân viên (5.980 mỗi nhóm) để thấy mức chênh 6 điểm; nếu tác động thật là 5 điểm thì power chỉ khoảng 0,64.

**Đề xuất cuối của hồ sơ:** **Go có điều kiện**, chỉ pilot noi_dia + hang_nang, tối đa 2 lượt chạy; loại quoc_te và doi_tac. Điều kiện: sửa khoá chống hoàn trùng (ca 20), Giám đốc vận hành chấp nhận mức chênh 6 điểm, bật đủ event có `trace_id` và đo phút thật, giảm xem lại theo bậc.

**Kết quả duyệt chéo nhóm nhận được từ hội đồng:** chưa nhận được phiếu chấm của nhóm hội đồng tại thời điểm nộp; sẽ bổ sung bằng commit mới khi có.

## 5. Khó khăn và cách xử lý

- **Đổi người viết code sau giải lao:** người viết code CP1–CP2 chuyển sang vai người gắn nhãn 1 (hoàn thiện bảng khắc phục, theo dõi điều kiện "Xong khi"); ghi lại việc đổi vai trong `TEAM.md`.
- **Hai ca gắn nhãn không trùng (13, 20):** thống nhất theo nguyên nhân gốc và viết quy tắc phân biệt; không sửa hai bộ nhãn độc lập sau khi so.
- **Không cách chia theo cụm nào đủ mẫu cho mức chênh 5 điểm** (20 nhân viên tối đa 1.000 < 1.251): chấp nhận mức chênh 6 điểm, ghi rõ power 0,64 trong `pilot_plan.yaml` và hồ sơ.
- **Ngưỡng an toàn:** tỉ lệ mở lại hiện tại 4,25% nên ngưỡng tuyệt đối 3% sẽ dừng pilot ngay tuần đầu; chuyển sang so với đối chứng (+2 điểm) kèm trần 6%.
- **Đồng bộ Git khi nhiều người cùng sửa:** push bị từ chối (non-fast-forward) vì nhánh trên GitHub có commit mới; xử lý bằng cách commit hoặc stash phần đang sửa, `git pull` rồi mới push.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

- Chi phí xem lại và làm lại dựa trên phút giả lập; pilot phải thay bằng phút đo thật qua event `staff_review_decision`, `staff_rework_completed` sau tuần đầu.
- Đợt chạy thử không có nhóm đối chứng nên 82,83% chỉ mô tả mẫu, chưa chứng minh tác động của trợ lý.
- Pilot chỉ đủ power cho mức chênh 6 điểm; nếu tác động thật nhỏ hơn thì dễ kết luận nhầm là không có tác động.
- Mốc phê duyệt bắt đầu pilot và ngày ra quyết định đang cùng là 05/01/2027; Giám đốc vận hành cần chốt lại lịch, tách hai mốc trước rollout đầu tiên.
- Ngưỡng của luật dừng chi phí (8.000 đ/việc) và chỉ số tự đề xuất chưa được tính thử trên dữ liệu.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, [arxiv.org/abs/2504.13359](https://arxiv.org/abs/2504.13359).
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure", [pair.withgoogle.com](https://pair.withgoogle.com).
- Tài liệu statsmodels, lớp `NormalIndPower` (mục `stats.power`).
- Tài liệu của lab: `docs/du_lieu_va_cong_thuc.md`, `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`.
