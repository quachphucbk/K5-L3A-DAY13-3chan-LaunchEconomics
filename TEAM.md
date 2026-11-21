# Team

## Thông tin nhóm

- Tên nhóm: 3chan
- Lớp: L3A
- Repo nhóm: `K5-L3A-DAY13-3chan-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo: https://github.com/quachphucbk/K5-L3A-DAY13-3chan-LaunchEconomics
- Nhánh nộp: `main`
- Commit chốt: 0090982

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Quách Ngọc Phúc       | 2A202603665     | quachphucbk@gmail.com      | https://github.com/quachphucbk       | Người viết code (CP1–CP2), Người gắn nhãn 1 (từ CP3)        |
|   2 | Ngô Văn Tuân       | 2A202603630     | 26ai.tuannv3@vinuni.edu.vn      | https://github.com/ngotuna23a       | Người kiểm số        |
|   3 | Nguyễn Đức Minh       | 2A202603633     | Jiji.Minh@gmail.com      | https://github.com/MinhDucDepZaiJ       | Người gắn nhãn 1        |
|   4 | Hồ Quốc Toản          | 2A202603668     | hoquoctoan11122002@gmail.com | https://github.com/hoquoctoan1       | Người gán nhãn 2, kiêm giữ hồ sơ |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## HoVaTen-MSSV

### Phần việc phụ trách

-

### Đóng góp cụ thể

-

### Bằng chứng

-

## Quách Ngọc Phúc — 2A202603665

### Phần việc phụ trách

- Người viết code CP1–CP2: `src/lab13.py` (A1–A4, B1–B4) và `report/team/bang_chi_phi.md`.
- Sau giải lao đổi sang Người gắn nhãn 1: hoàn thiện bảng khắc phục CP3, rà và sửa CP4 theo điều kiện "Xong khi", làm `chi_so.md` và sửa hồ sơ CP5. Không gắn nhãn 20 ca (nhãn do Minh và Toản gắn độc lập).

### Đóng góp cụ thể

- Viết `mo_hinh()` và các bảng A2–A4, B1–B4; ba phép thử A1 ĐẠT, số khớp đáp án (4.472 đ/việc [simulated]).
- Viết lại bảng khắc phục 5 ca có event, ngưỡng, tần suất, vai trò phụ trách.
- Bổ sung D1, D2, đánh đổi, ngưỡng an toàn, vế KHÔNG THÌ và scope trong `pilot_plan.yaml`.
- Thêm code E1 (82,83% · 27,12% · 4,25%), điền `chi_so.md` (11 event có trace_id, 3 dòng rủi ro); sửa người phụ trách, trạng thái và nhãn simulated trong `ho_so_launch_v0.md`; tham gia duyệt chéo.
- Dùng Claude Code hỗ trợ viết code và điền bảng; chi tiết trong báo cáo cá nhân.

### Bằng chứng

- CP1, CP2: commit `d2a520d` (code), `466dc7d` (bảng chi phí).
- CP3, CP4: commit `62480b8` (`bang_loi.md`, `pilot_plan.yaml`).
- CP5: commit `08c428c` (`chi_so.md`, `ho_so_launch_v0.md`, E1 trong `src/lab13.py`).
- Báo cáo cá nhân: `report/team/2A202603665_QuachNgocPhuc.md`.

## Ngô Văn Tuân — 2A202603630

### Phần việc phụ trách

- Người kiểm số: CP1 (A1–A4), CP2 (B1–B4), CP4 (D1–D2), CP5 (kiểm E1–E2 và đối chiếu hồ sơ E3).

### Đóng góp cụ thể

- Đối chiếu các bảng chi phí bằng phép tính độc lập từ CSV với hỗ trợ Codex; bổ sung bằng chứng kiểm số, nhãn simulated và giải thích giả định làm tròn.

### Bằng chứng

- CP1: commit `1e709a7` (`CP1`).
- CP2: bảng B1–B4 trong `report/team/bang_chi_phi.md`; công thức đối chiếu trong `report/team/2A202603630_NgoVanTuan.md`.
- CP4 D1: `src/lab13.py` tính 5 câu cỡ mẫu; kết quả và tỉ lệ mở lại hiện tại nằm trong chú thích `report/team/pilot_plan.yaml`.
- CP4 D2: commit `7b46e87` bổ sung 5 câu kiểm tra tách được tác động.
- CP5: `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`; tính độc lập chỉ số và chi phí pilot tối đa 2 lượt, bổ sung đặc tả event và công thức vào báo cáo cá nhân.
