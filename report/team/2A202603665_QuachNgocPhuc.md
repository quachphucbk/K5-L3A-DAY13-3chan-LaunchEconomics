# Báo cáo cá nhân — Quách Ngọc Phúc — 2A202603665

**Trạng thái: bản tạm.** Đã xong CP1–CP2 (code), bảng khắc phục CP3 và sửa CP4; CP5 đang chờ nhóm phân việc.

## 1. Thông tin thành viên

- Họ tên: Quách Ngọc Phúc.
- MSSV: 2A202603665.
- Email: quachphucbk@gmail.com.
- Vai trong nhóm: Người viết code (CP1–CP2); sau giải lao đổi sang Người gắn nhãn 1 (từ CP3: hoàn thiện bảng khắc phục, theo dõi điều kiện "Xong khi").

## 2. Phần việc phụ trách

| Phần | Việc | Trạng thái |
| --- | --- | --- |
| CP1 — Mô hình chi phí | Viết A1, `mo_hinh()` (A2), A3, A4 trong `src/lab13.py`; điền A1–A4 trong `bang_chi_phi.md` | Xong |
| CP2 — Độ nhạy | Viết B1–B4 trong `src/lab13.py`; điền B1–B4 trong `bang_chi_phi.md` | Xong |
| CP3 — Bảng lỗi | Không gắn nhãn (hai bộ nhãn độc lập do Minh và Toản gắn); điền tên người gắn nhãn và viết lại bảng khắc phục 5 ca | Xong |
| CP4 — Pilot plan | Rà `pilot_plan.yaml` theo checklist; bổ sung D1, D2, đánh đổi, ngưỡng an toàn, sửa vế KHÔNG THÌ và scope | Xong |
| CP5 — Hồ sơ, duyệt chéo | Chờ nhóm phân việc | Chưa |

## 3. Đóng góp cụ thể

- **A1:** ba hàm kinh tế của việc chạy lại; ba phép thử in ĐẠT (1,20 · 1,25 · 1,25).
- **A2:** hàm `mo_hinh()` tính tử số trên mọi lần chạy (kể cả lần lỗi), mẫu số chỉ đếm `thanh_cong`; có tham số giá, hệ số và `max_lan_chay` để CP2 gọi lại. Kết quả: 978 việc thành công, 4.472 đ/việc [simulated], gấp 16,3 lần hoá đơn token chia số yêu cầu [simulated].
- **A3, A4:** tách theo loại (quoc_te 1,88× [simulated], tỉ lệ ok 30,0% → 11,4% → 2,2% theo lần thử); cộng chi phí cố định cho noi_dia + hang_nang: 4.599 đ = 0,38× và 5.784 đ = 0,48× khi khối lượng còn một nửa [simulated].
- **B1–B4:** 9 kịch bản độ nhạy, xếp hạng làm lại > xem lại > lương; B3 giới hạn 2 lần rẻ nhất cho cả hệ thống (6.901.220 đ [simulated]); B4 xem lại 100% là 11.743 đ = 0,98× (12.415 đ = 1,03× với 15,3 phút làm lại) [simulated].
- **CP3:** viết lại 5 dòng khắc phục (ca 1, 2, 3, 13, 5) để mỗi dòng có event, ngưỡng, tần suất và người phụ trách là vai trò trong LogiX.
- **CP4:** bổ sung kết luận cho D1 b–d, năm câu D2, đánh đổi (power 0,64 ở mức 5 điểm), ngưỡng an toàn dựa trên tỉ lệ mở lại 4,25% / 3,97%; sửa vế KHÔNG THÌ của 3 luật dừng thành việc bị cấm; thêm lý do bằng số cho `scope`.

## 4. Bằng chứng

- CP1, CP2 (code): [commit d2a520d — CP1, CP2](https://github.com/quachphucbk/K5-L3A-DAY13-3chan-LaunchEconomics/commit/d2a520d219b0ff25a3a6c61834fea825659562c7) — `src/lab13.py`.
- CP1, CP2 (bảng): [commit 466dc7d — CP1, CP2](https://github.com/quachphucbk/K5-L3A-DAY13-3chan-LaunchEconomics/commit/466dc7dde5e5811712cdc72cb6a74f26e95423e7) — `report/team/bang_chi_phi.md`.
- CP3, CP4: [commit 62480b8 — edit cp4](https://github.com/quachphucbk/K5-L3A-DAY13-3chan-LaunchEconomics/commit/62480b821adf36a1131e07bbe9164d99e6371562) — `report/team/bang_loi.md`, `report/team/pilot_plan.yaml`.
- Cách chạy lại: `cd src && python lab13.py`.

## 5. Công cụ AI đã dùng

- **Công cụ:** Claude Code (Claude).
- **Dùng vào việc gì:**
  - Đọc toàn bộ tài liệu của lab và lên kế hoạch theo từng checkpoint.
  - Viết code A1–A4, B1–B4 trong `src/lab13.py` và điền số vào `bang_chi_phi.md`.
  - Rà CP3, CP4 theo checklist; đề xuất bảng khắc phục 5 ca và các chỗ sửa trong `pilot_plan.yaml`, tôi duyệt rồi mới điền.
- **Không dùng AI để:** gắn nhãn 20 ca lỗi (RULES.md cấm; nhãn do Minh và Toản gắn độc lập) và tạo kết quả duyệt chéo.
- **Cách tự kiểm tra:**
  - Chạy `python lab13.py`, xác nhận ba phép thử A1 in ĐẠT.
  - Đối chiếu mọi số A2–B4 với số tham khảo trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (lệch dưới 2%; B4 12.415 so với 12.414 do làm tròn).
  - Kiểm tra B1: mỗi kịch bản "giảm một nửa" bằng nửa mức tăng của "gấp đôi".
  - CP4: `yaml.safe_load` đọc được, không còn dấu `?` ngoài chú thích, lệnh `grep` tìm từ bị cấm theo quy tắc 5 không in gì.

## 6. Tự đánh giá

<!-- Bản nháp, tự viết lại bằng lời của mình trước khi nộp. -->

- Làm tốt: CP1–CP2 chạy đúng và khớp đáp án; hiểu vì sao tử số tính mọi lần chạy còn mẫu số chỉ đếm việc thành công, và vì sao giới hạn chạy lại rẻ nhất cho công ty (2 lần) khác giới hạn cho chi phí mỗi việc thành công thấp nhất (1 lần).
- Cần cải thiện: phụ thuộc nhiều vào AI khi viết code; cần tự tính tay ít nhất một con số (ví dụ 4.373.585 ÷ 978 = 4.472) để chắc chắn tự giải thích được trước hội đồng.
