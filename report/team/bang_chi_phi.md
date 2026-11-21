# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 · ĐẠT |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 · ĐẠT |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 · ĐẠT (= 1/p, k triệt tiêu) |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` (1.624 lần chạy, kể cả lần lỗi) | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` (5.600 lần gọi × 15 đ) | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` (890 phút × 2.000 đ) | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` (1.132 phút × 2.000 đ) | simulated |
| Tổng chi phí | 4.373.585 | | có phần simulated |
| Số việc thành công | 978 | `ket_qua` == `thanh_cong` | |
| Chi phí mỗi việc thành công | 4.472 | 4.373.585 ÷ 978 | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | (245.585 + 84.000) ÷ 1.200 | đo từ trace |

- Chi phí mỗi việc thành công gấp bao nhiêu lần "hoá đơn chia số yêu cầu"?
  - **Trả lời:** Gấp **16,3 lần** [simulated] (4.472 đ [simulated] ÷ 274,7 đ). Lý do: hoá đơn chỉ có token + tool (329.585 đ, 7,5% tổng chi phí [simulated]) và chia cho cả 1.200 yêu cầu, còn chi phí thật cộng thêm giờ nhân viên xem lại, làm lại và chỉ chia cho 978 việc thành công.
- Khoản nào chiếm tỉ trọng lớn nhất trong tổng chi phí, bao nhiêu phần trăm?
  - **Trả lời:** **Làm lại**, 2.264.000 đ = **51,8%** tổng chi phí [simulated]. Tiếp theo là xem lại 40,7%, token 5,6%, tool 1,9% [simulated]; giờ nhân viên (xem lại + làm lại) chiếm 92,5% [simulated].

Ghi chú khi so với 12.000 đ: 4.472 đ [simulated] chưa tính 222 ca nhân viên phải làm thay; chi phí cả hệ thống = (4.373.585 + 222 × 12.000) ÷ 1.200 = 5.865 đ/yêu cầu = 0,49× [simulated].

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công [simulated] | So với 12.000 đ [simulated] |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ | 0,85× |

Tỉ lệ lần chạy `ok` theo lần thử (đo từ trace):

| Loại | Lần 1 | Lần 2 | Lần 3 |
| --- | ---: | ---: | ---: |
| noi_dia | 91,0% | 75,7% | 38,9% |
| hang_nang | 70,9% | 39,1% | 17,9% |
| quoc_te | 30,0% | 11,4% | 2,2% |
| doi_tac | 51,5% | 18,2% | 14,8% |

- Loại nào không đáng để trợ lý xử lý? Với loại đó, cho chạy lại tới 3 lần có giúp không?
  - **Trả lời (loại nào):** **quoc_te**: chi phí mỗi việc thành công 22.515 đ = **1,88×** của 12.000 đ [simulated], đắt hơn nhân viên tự làm; tỉ lệ thành công chỉ 27,3% dù trung bình 2,32 lần chạy/yêu cầu.
  - **Trả lời (chạy lại có giúp không):** **Không.** Tỉ lệ ok của quoc_te giảm theo lần thử: lần 1 30,0% → lần 2 11,4% → lần 3 2,2%; lỗi lặp lại trên cùng yêu cầu nên chạy lại chỉ tốn thêm token, tool mà không tăng việc thành công.

Ghi chú phạm vi pilot: doi_tac cũng loại vì sát ngưỡng (0,85× [simulated], thành công 54,4%) và có điều khoản riêng; pilot giữ noi_dia (0,22×) + hang_nang (0,69×).

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ [simulated] | 0,38× [simulated] |
| Một nửa khối lượng | 16.875 | 2.370 đ | 5.784 đ [simulated] | 0,48× [simulated] |

Cách tính: phạm vi có 982 yêu cầu, tổng 3.072.513 đ, 900 việc thành công → cps 3.414 đ [simulated]. Việc thành công mỗi tháng = 45.000 × 900 ÷ 1.200; cố định mỗi việc = 40.000.000 ÷ số việc thành công mỗi tháng.

- Chi phí cố định có đổi kết luận không? Ở khối lượng nào?
  - **Trả lời (có đổi kết luận không):** **Không đổi kết luận** trong phạm vi noi_dia + hang_nang: sau khi cộng cố định vẫn rẻ hơn nhân viên tự làm, 0,38× ở quy mô đầy đủ và 0,48× khi khối lượng còn một nửa [simulated].
  - **Trả lời (ở khối lượng nào):** Ở **45.000 yêu cầu/tháng** cố định chỉ thêm 1.185 đ/việc (3.414 → 4.599 đ) [simulated]; khối lượng càng nhỏ thì cố định càng nặng: còn một nửa (giai đoạn pilot) là 2.370 đ/việc (5.784 đ). Hồ sơ phải ghi rõ số đã cộng cố định chưa và ở khối lượng nào.

## B1 · Đổi từng yếu tố

Gốc (A2): 4.472 đ [simulated]. Mỗi kịch bản là một lần gọi `mo_hinh(runs, reqs, ...)` với một tham số đã đổi.

| Kịch bản | Cách tính | Chi phí mỗi việc thành công [simulated] | Thay đổi (%) [simulated] |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 đ | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ | −8,1% |

Tự kiểm tra: mỗi kịch bản "giảm một nửa" giảm đúng bằng nửa mức tăng của kịch bản "gấp đôi" (5,6 → 2,8 · 40,7 → 20,3 · 51,8 → 25,9).

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi:
  - **Trả lời:** **6.543 đ, +46,3%** [simulated], đúng bằng tổng hai tác động riêng (+5,6% + 40,7%) vì mô hình cộng tuyến tính các khoản chi phí.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất:
  - **Trả lời:** 1. **Số ca làm lại** (±51,8% / −25,9%) · 2. **Tỉ lệ xem lại** (+40,7% / −20,3%) · 3. **Lương nhân viên** (+23,1% khi tăng 25%) [simulated]. Giá token chỉ +5,6% khi gấp đôi, nên pilot phải theo dõi tỉ lệ làm lại và xem lại chứ không phải giá token.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

Chi phí cả hệ thống = tổng chi phí trợ lý + 12.000 đ × số yêu cầu không thành công (nhân viên phải làm thay).

| Giới hạn | Tổng chi phí trợ lý [simulated] | Số yêu cầu không thành công | Chi phí cả hệ thống [simulated] | Chi phí mỗi việc thành công [simulated] |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | 4.111 đ (thấp nhất) |
| 2 lần | 4.093.220 đ | 234 | **6.901.220 đ (rẻ nhất)** | 4.237 đ |
| 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |

- Giới hạn nào rẻ nhất cho công ty? Có trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất không?
  - **Trả lời (rẻ nhất cho công ty):** **Tối đa 2 lần chạy**, chi phí cả hệ thống 6.901.220 đ [simulated], rẻ hơn 3 lần 136.365 đ và rẻ hơn 1 lần 548.561 đ.
  - **Trả lời (có trùng không):** **Không trùng.** Chi phí mỗi việc thành công thấp nhất là giới hạn 1 lần (4.111 đ [simulated]), nhưng giới hạn này đẩy thêm 85 yêu cầu sang nhân viên (319 so với 234), nên cả hệ thống đắt hơn.

## B4 · Nếu phải xem lại tất cả

Cách tính (982 yêu cầu noi_dia + hang_nang): 948 yêu cầu có ≥ 1 lần chạy ok × 5 phút × 2.000 đ = 9.480.000 đ; 48 ca lam_lai × 9 phút × 2.000 đ = 864.000 đ; token + tool 224.513 đ; tổng 10.568.513 đ ÷ 900 việc thành công.

- Chi phí mỗi việc thành công khi xem lại 100% (`noi_dia` + `hang_nang`), so với 12.000 đ:
  - **Trả lời:** **11.743 đ = 0,98×** của 12.000 đ [simulated] với 9 phút làm lại như đề cho. Nếu dùng 15,3 phút làm lại trung bình trong dữ liệu (trung vị 14,5) thì lên **12.415 đ = 1,03×** [simulated], tức đắt hơn nhân viên tự làm.
- Kết quả này nói gì về thứ pilot cần học được?
  - **Trả lời:** Xem lại 100% thì gần như không tiết kiệm, vì tiền xem lại chiếm 90% chi phí (9.480.000 / 10.568.513 đ) [simulated]. Pilot phải đo được tỉ lệ xem lại có thể giảm an toàn xuống mức nào, và mỗi lần xem lại có ngắn hơn mức hoà vốn **5,1 phút** (làm lại 9 phút) hoặc **4,8 phút** (làm lại 15,3 phút) không [simulated].
