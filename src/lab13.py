"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
from statistics import NormalDist
import pandas as pd
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# CP1: ba hàm dưới đây được kiểm tra bằng kiem_tra_dap_an_biet_truoc().
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    # Lần chạy thứ i xảy ra khi i-1 lần trước đều sai: tổng (1-p)^(i-1), i = 1..k
    if k is None:
        return 1 / p
    return (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if k is None:
        return 1.0
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    # Tử số: số lần chạy trung bình (mọi lần, kể cả lần sai); mẫu số: xác suất thành công
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# CP1: mô hình chi phí; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    # Chỉ giữ các lần chạy thuộc tập yêu cầu đang xét (để A3 chỉ cần lọc reqs)
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        # Bỏ các lần chạy vượt giới hạn; yêu cầu cần nhiều lần hơn coi như chuyển nhân viên
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    # Tử số: MỌI lần chạy, kể cả lần lỗi (chia 1.000 trước khi nhân giá token)
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    # Giờ nhân viên — số GIẢ LẬP (simulated)
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    # Mẫu số: chỉ yêu cầu thành công
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    return dict(
        token=tien_token.sum(),
        tool=tien_tool.sum(),
        chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        thanh_cong=thanh_cong,
        cps=tong / thanh_cong,
        hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs),
    )


def co_mau_hai_ty_le(p1, p2, alpha, power):
    """Tính cỡ mẫu mỗi nhánh với phân bổ 1:1 và kiểm định hai phía."""
    normal = NormalDist()
    z_alpha = normal.inv_cdf(1 - alpha / 2)
    z_power = normal.inv_cdf(power)
    p_tb = (p1 + p2) / 2
    do_lech_goc = math.sqrt(2 * p_tb * (1 - p_tb))
    do_lech_thay_the = math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))
    return math.ceil(((z_alpha * do_lech_goc + z_power * do_lech_thay_the) / (p2 - p1)) ** 2)


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()

    # ----- A2 -----
    SIM = '[simulated]'
    ket_qua = mo_hinh(runs, reqs)
    nhan = dict(token='đo từ trace', tool='đo từ trace', chay_lai='đo từ trace (attempt > 1)',
                xem_lai=SIM, lam_lai=SIM, tong='có phần simulated', thanh_cong='',
                cps=SIM, hoa_don_moi_yc='đo từ trace')
    print('\n== A2 · Mô hình chi phí từ trace ==')
    for ten, gia_tri in ket_qua.items():
        dinh_dang = f'{gia_tri:>14,.0f}' if ten == 'thanh_cong' else f'{gia_tri:>14,.2f}'
        print(f'{ten:15s} {dinh_dang}  {nhan[ten]}')
    print(f"Số phút xem lại {reqs['phut_xem_lai_simulated'].sum():,} · làm lại "
          f"{reqs['phut_lam_lai_simulated'].sum():,} {SIM}; số lần gọi tool {runs['tool_calls'].sum():,}")
    print(f"cps gấp {ket_qua['cps'] / ket_qua['hoa_don_moi_yc']:.1f} lần hoá đơn token+tool chia số yêu cầu")
    for khoan in ['token', 'tool', 'xem_lai', 'lam_lai']:
        print(f"  tỉ trọng {khoan:8s} {ket_qua[khoan] / ket_qua['tong'] * 100:5.1f}%")
    gio_nv = (ket_qua['xem_lai'] + ket_qua['lam_lai']) / ket_qua['tong']
    print(f'  giờ nhân viên chiếm {gio_nv * 100:.1f}% tổng chi phí {SIM}')
    khong_tc = len(reqs) - ket_qua['thanh_cong']
    he_thong = (ket_qua['tong'] + khong_tc * BASELINE) / len(reqs)
    print(f'Cả hệ thống / yêu cầu (cộng {khong_tc} ca nhân viên làm thay × 12.000 đ): '
          f'{he_thong:,.0f} đ = {he_thong / BASELINE:.2f}× {SIM}')

    # ----- A3 -----
    print('\n== A3 · Tách theo loại yêu cầu ==')
    print(f"{'loai':10s} {'so_yc':>6s} {'ti_le_tc':>9s} {'lan/yc':>7s} {'cps [sim]':>10s} {'so 12k':>7s}")
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        r = reqs[reqs['loai'] == loai]
        kq = mo_hinh(runs, r)
        so_lan = runs['request_id'].isin(r['request_id']).sum() / len(r)
        print(f"{loai:10s} {len(r):6d} {kq['thanh_cong'] / len(r) * 100:8.1f}% {so_lan:7.2f} "
              f"{kq['cps']:10,.0f} {kq['cps'] / BASELINE:6.2f}×")
    # Chạy lại có giúp không: tỉ lệ ok theo từng lần thử
    ok_theo_lan = (runs.merge(reqs[['request_id', 'loai']], on='request_id', validate='many_to_one')
                   .assign(ok=lambda d: (d['status'] == 'ok').astype(float))
                   .pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean'))
    print('Tỉ lệ ok theo lần thử (đo từ trace):')
    print((ok_theo_lan * 100).round(1).to_string())

    # ----- A4 -----
    print('\n== A4 · Chi phí cố định, phạm vi noi_dia + hang_nang ==')
    CO_DINH = 40_000_000   # đ / tháng
    YC_THANG = 45_000      # yêu cầu / tháng ở quy mô đầy đủ
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kq_pv = mo_hinh(runs, pham_vi)
    print(f"Phạm vi: {len(pham_vi)} yêu cầu, tổng {kq_pv['tong']:,.0f} đ, "
          f"{kq_pv['thanh_cong']} việc thành công, cps {kq_pv['cps']:,.0f} đ {SIM}")
    for ten_kl, he_so_kl in [('45.000 yêu cầu/tháng', 1.0), ('Một nửa khối lượng', 0.5)]:
        tc_thang = YC_THANG * he_so_kl * kq_pv['thanh_cong'] / len(reqs)
        co_dinh_viec = CO_DINH / tc_thang
        tong_viec = kq_pv['cps'] + co_dinh_viec
        print(f'{ten_kl:22s} {tc_thang:9,.0f} việc/tháng · cố định {co_dinh_viec:9,.2f} đ/việc · '
              f'cps + cố định {tong_viec:9,.2f} đ = {tong_viec / BASELINE:.2f}× {SIM}')
    # ----- B1 · Đổi từng yếu tố -----
    print('\n== B1 · Đổi từng yếu tố (cps [simulated]) ==')
    goc = ket_qua['cps']
    kich_ban = {
        'Giá token gấp đôi':          dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa':     dict(gia_vao=13, gia_ra=65),
        'Tỉ lệ xem lại gấp đôi':      dict(he_so_xem_lai=2),
        'Tỉ lệ xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Số ca làm lại gấp đôi':      dict(he_so_lam_lai=2),
        'Số ca làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương nhân viên tăng 25%':   dict(luong_phut=2500),
        'Chỉ cho chạy tối đa 2 lần':  dict(max_lan_chay=2),
        'Chỉ cho chạy 1 lần':         dict(max_lan_chay=1),
    }
    print(f"{'Gốc (A2)':28s} {goc:8,.0f}")
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        print(f'{ten:28s} {cps:10,.2f} {(cps / goc - 1) * 100:+7.2f}%')

    # ----- B2 · Đổi một cặp -----
    cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    print(f'\n== B2 · Token gấp đôi + xem lại gấp đôi: {cap:,.2f} đ ({(cap / goc - 1) * 100:+.2f}%) [simulated]')

    # ----- B3 · Giới hạn chạy lại và chi phí cả hệ thống -----
    print('\n== B3 · Giới hạn số lần chạy (chi phí cả hệ thống = trợ lý + 12.000 đ × ca không thành công) [simulated] ==')
    print(f"{'gioi_han':9s} {'tong_tro_ly':>12s} {'khong_tc':>9s} {'ca_he_thong':>12s} {'cps':>7s}")
    for gioi_han in [1, 2, 3]:
        kq = mo_hinh(runs, reqs, max_lan_chay=gioi_han)
        khong_tc = len(reqs) - kq['thanh_cong']
        print(f"{gioi_han:<9d} {kq['tong']:12,.2f} {khong_tc:9d} "
              f"{kq['tong'] + khong_tc * BASELINE:12,.2f} {kq['cps']:9,.2f}")

    # ----- B4 · Nếu phải xem lại 100% (noi_dia + hang_nang) -----
    print('\n== B4 · Xem lại 100%, phạm vi noi_dia + hang_nang [simulated] ==')
    PHUT_XEM, PHUT_LAM_DE = 5, 9
    runs_pv = runs[runs['request_id'].isin(pham_vi['request_id'])]
    co_ok = runs_pv.loc[runs_pv['status'] == 'ok', 'request_id'].nunique()
    so_lam_lai = int((pham_vi['ket_qua'] == 'lam_lai').sum())
    token_tool = (runs_pv['tokens_in'] / 1000 * GIA_VAO + runs_pv['tokens_out'] / 1000 * GIA_RA
                  + runs_pv['tool_calls'] * GIA_TOOL).sum()
    tc_pv = kq_pv['thanh_cong']
    phut_lam_tb = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated']
    print(f'{co_ok} yêu cầu có ≥ 1 lần ok × {PHUT_XEM} phút; {so_lam_lai} ca lam_lai; '
          f'token + tool {token_tool:,.0f} đ; {tc_pv} việc thành công')
    print(f'Phút làm lại trong dữ liệu: trung bình {phut_lam_tb.mean():.4f}, trung vị {phut_lam_tb.median():.1f} {SIM}')
    for nhan_lam, phut_lam in [('đề cho 9 phút', PHUT_LAM_DE), ('dữ liệu, làm tròn 1 chữ số', round(phut_lam_tb.mean(), 1))]:
        tien_xem = co_ok * PHUT_XEM * LUONG_PHUT
        tien_lam = so_lam_lai * phut_lam * LUONG_PHUT
        tong_b4 = tien_xem + tien_lam + token_tool
        hoa_von = (BASELINE * tc_pv - tien_lam - token_tool) / (co_ok * LUONG_PHUT)
        print(f'Làm lại {phut_lam} phút ({nhan_lam}): xem lại {tien_xem:,.2f} + làm lại {tien_lam:,.2f} '
              f'→ tổng {tong_b4:,.2f} đ → {tong_b4 / tc_pv:,.2f} đ/việc = {tong_b4 / tc_pv / BASELINE:.2f}× · '
              f'hoà vốn khi xem lại ≤ {hoa_von:.2f} phút {SIM}')
    # CP4 · D1: cỡ mẫu theo công thức hai tỷ lệ trong đề.
    p_goc, p_muc_tieu = 0.70, 0.75
    alpha, power, icc = 0.05, 0.80, 0.02
    n_5 = co_mau_hai_ty_le(p_goc, p_muc_tieu, alpha, power)
    n_6 = co_mau_hai_ty_le(p_goc, 0.76, alpha, power)
    m = 75
    de = 1 + (m - 1) * icc
    n_theo_nhan_vien = math.ceil(n_5 * de)
    nhan_vien_moi_nhanh = 20
    depot_moi_nhanh = 6
    m_6 = math.ceil(n_6 * (1 - icc) / (nhan_vien_moi_nhanh - n_6 * icc))
    de_6 = 1 + (m_6 - 1) * icc
    n_thuc_6 = nhan_vien_moi_nhanh * m_6
    power_5 = NormalIndPower().power(
        proportion_effectsize(p_goc, p_muc_tieu),
        nobs1=n_thuc_6 / de_6,
        alpha=alpha,
    )

    print('\n== D1 · Cỡ mẫu pilot ==')
    print(f'a) Chia theo yêu cầu: {n_5:,} mỗi nhánh.')
    print(f'b) {m} yêu cầu/nhân viên: DE = {de:.2f}, {n_theo_nhan_vien:,} yêu cầu '
          f'và {math.ceil(n_theo_nhan_vien / m)} nhân viên mỗi nhánh.')
    print(f'c) {nhan_vien_moi_nhanh} nhân viên/nhánh: giới hạn hiệu dụng '
          f'{nhan_vien_moi_nhanh / icc:,.0f}.')
    print(f'd) {depot_moi_nhanh} depot/nhánh: giới hạn hiệu dụng {depot_moi_nhanh / icc:,.0f}.')
    print(f'e) MDE 6 điểm phần trăm: {n_6:,} yêu cầu hiệu dụng/nhánh, '
          f'{m_6} yêu cầu/nhân viên, DE = {de_6:.2f}, {n_thuc_6:,} yêu cầu thực/nhánh.')
    print(f'Với mức tăng thật 5 điểm phần trăm, power của phương án e: {power_5:.2%}.')

    for ten, nhom in [('Toàn mẫu', reqs),
                      ('Nội địa + hàng nặng', reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])])]:
        mo_lai = nhom['mo_lai_trong_7_ngay'].eq(1).sum()
        print(f'{ten} · mở lại trong 7 ngày: {mo_lai}/{len(nhom):,} = {mo_lai / len(nhom):.2%}.')

    # ----- CP5 · E1 · Tính thử ba chỉ số trên 1.200 yêu cầu (đợt chạy thử, chưa có đối chứng) -----
    print('\n== E1 · Ba chỉ số trong đợt chạy thử ==')
    chinh = (reqs['dong_trong_24h'] == 1) & (reqs['mo_lai_trong_7_ngay'] == 0)
    duoc_xem = reqs[reqs['duoc_xem_lai'] == 1]
    bo_qua = duoc_xem['quyet_dinh_xem_lai'].isin(['sua', 'bo'])
    an_toan = reqs['mo_lai_trong_7_ngay'] == 1
    print(f'Chính · đóng trong 24h, không mở lại 7 ngày: {chinh.sum()}/{len(reqs):,} = {chinh.mean():.2%}')
    print(f'Dùng  · bỏ qua gợi ý (sua + bo) / được xem lại: {bo_qua.sum()}/{len(duoc_xem)} = {bo_qua.mean():.2%}')
    print(f'An toàn · mở lại trong 7 ngày: {an_toan.sum()}/{len(reqs):,} = {an_toan.mean():.2%}')
    pv_e = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    print(f"Trong phạm vi noi_dia + hang_nang: tỉ lệ lam_lai {(pv_e['ket_qua'] == 'lam_lai').mean():.1%}, "
          f"tỉ lệ được xem lại {pv_e['duoc_xem_lai'].mean():.1%}")
