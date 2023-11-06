#CHƯƠNG 6

#bài tập 1.1
print("**    **  ******  **      **      ******")
print("**    **  **      **      **      **  **")
print("********  ******  **      **      **  **")
print("**    **  **      **      **      **  **")
print("**    **  ******  ******  ******  ******")

#bài tập 1.2
X=10
Y=5
C=X+Y
D=X-Y
E=X*Y
F=X/Y
print('Tổng của', X, '+', Y, '=', C)
print('Hiệu của', X, '-', Y, '=', D)
print('Tích của', X, '*', Y, '=', E)
print('Thương của', X, '/', Y, '=', F)

#bài tập 1.3

ten_hang= input("Tên hàng: ")
so_luong= int(input("Số lượng: "))
don_gia= int(input("Đơn giá: "))
tien_phai_tra= so_luong * don_gia
print("\n---")
print("Tên hàng: ",ten_hang)
print("Số lượng: ",so_luong)
print("Đơn giá: ",don_gia)
print("Tiền phải trả: ",tien_phai_tra ,"vnđ")


#1.4
Yêu cầu 1: (5 - 3)/2

Yêu cầu 2: 8 - ((3 * 2) - 1) + 1

#1.5

def tinh_tien_hang(gia, so_luong):
    thanh_tien = gia * so_luong
    return thanh_tien

# Ví dụ sử dụng hàm tinh_tien_hang
gia_san_pham = 10.5  # Giá của sản phẩm
so_luong_san_pham = 3  # Số lượng sản phẩm

tong_tien = tinh_tien_hang(gia_san_pham, so_luong_san_pham)
print("Tổng tiền hàng là:", tong_tien)

#1.6
def chia_deu_so_keo(so_keo, so_nguoi_choi):
    if so_nguoi_choi == 0:
        return "Số người chơi phải lớn hơn 0."
    
    keo_moi_nguoi = so_keo // so_nguoi_choi
    du_thua = so_keo % so_nguoi_choi
    
    ket_qua = f"Mỗi người được {keo_moi_nguoi} viên kẹo."
    
    if du_thua > 0:
        ket_qua += f" Có {du_thua} viên kẹo thừa."
    
    return ket_qua

# Ví dụ sử dụng hàm
so_keo = 10
so_nguoi_choi = 3

ket_qua_chia_deu = chia_deu_so_keo(so_keo, so_nguoi_choi)
print(ket_qua_chia_deu)

#1.7
def nhap_do_c(do_c):
    do_f = (do_c * 9/5) + 32
    return do_f

print(f"{do_c} °C = {do_f} °F")


#1.8
def doi_tien(so_tien):
    menh_gia = [500000, 200000, 100000, 50000]
    so_to = []
    
    for menh_gia_i in menh_gia:
        so_to_i = so_tien // menh_gia_i
        so_to.append(so_to_i)
        so_tien %= menh_gia_i
    
    return so_to, so_tien

so_tien_muon_doi = int(input("Số tiền muốn đổi: "))
so_to, so_tien_con_lai = doi_tien(so_tien_muon_doi)

print("Số tờ 500,000:", so_to[0])
print("Số tờ 200,000:", so_to[1])
print("Số tờ 100,000:", so_to[2])
print("Số tờ 50,000:", so_to[3])
print("Tiền còn lại:", so_tien_con_lai)

#1.9
def tinh_tien_lai(goc, lai_suat, thoi_gian):
    tien_lai = goc * (lai_suat / 100) * thoi_gian
    return tien_lai

goc = float(input("Nhập số tiền gốc: "))
lai_suat = float(input("Nhập tỷ lệ lãi suất hàng năm: "))
thoi_gian = int(input("Nhập số tháng gửi: "))

tien_lai = tinh_tien_lai(goc, lai_suat, thoi_gian)
tong_so_tien = goc + tien_lai

print(f"Số tiền lãi là: {tien_lai}")
print(f"Tổng số tiền sau khi kết thúc kỳ hạn là: {tong_so_tien}")