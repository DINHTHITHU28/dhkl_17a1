#CHƯƠNG 8
#8.1: Tìm số lớn nhất, số nhỏ nhất
n = int(input("Nhập n: "))
x = float(input("Nhập x: "))
A = (x*x + x + 1)**n + (x*x - x + 1)**n
print("A = (x*x + x + 1)^n + (x*x - x + 1)^n","=", A)

a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c: "))
d = float(input("Nhập số d: "))

# Tìm giá trị lớn nhất
max_value = max(a, b, c, d)

# Tìm giá trị nhỏ nhất
min_value = min(a, b, c, d)

print(f"Số lớn nhất là {max_value}")
print(f"Số nhỏ nhất là {min_value}")


#8.2

# Nhập số từ người dùng
number = float(input("Nhập một số: "))

# Tính giá trị tuyệt đối
absolute_value = abs(number)

# In kết quả
print("Giá trị tuyệt đối của", number, "là", absolute_value)



#8.3
def giai_phuong_trinh_bac_nhat(a, b):
    if a == 0:
        if b == 0:
            print("Phương trình vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        x = -b / a
        print(f"Nghiệm của phương trình là: x = {x}")

# Nhập các hệ số từ người dùng
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))

# Gọi hàm để giải phương trình
giai_phuong_trinh_bac_nhat(a, b)


#8.4
a=float(input("Nhập độ dài cạnh a: "))
b=float(input("Nhập độ dài cạnh b: "))
c=float(input("Nhập độ dài cạnh c: "))
p = (a + b + c)
import math
S = math.sqrt(p * (p - a) * (p - b) * (p -c))

print("Diện tích tam giác là: ", S)


#8.5
a=int(input("Nhập năm: "))
if a%4 == 0 and a%100 > 0 or a%400 == 0:
	print(a,"là năm nhuận.")
else:
	print(a,"không phải là năm nhuận.")



#8.6
def tinh_cuoc_taxi(loai_xe, so_km, thoi_gian_cho):
    if loai_xe == 4:
        gia_mo_cua = 11000
        gia_dau_km = 12100
        gia_tiep_theo = 10000
    elif loai_xe == 7:
        gia_mo_cua = 13000
        gia_dau_km = 14100
        gia_tiep_theo = 12000
    else:
        return "Loại xe không hợp lệ. Vui lòng nhập lại."

    cuoc_taxi = gia_mo_cua + (so_km - 0.8) * (gia_dau_km if so_km <= 20 else gia_tiep_theo)
    cuoc_taxi = gia_mo_cua + (so_km - 0.8) * (gia_dau_km if so_km <= 30 else gia_tiep_theo)
    tien_cho = max(0, thoi_gian_cho - 5) * 800

    tong_tien = cuoc_taxi + tien_cho

    return tong_tien

# Test với các giá trị đầu vào khác nhau:
loai_xe1, so_km1, thoi_gian_cho1 = (4, 10, 3)
loai_xe2, so_km2, thoi_gian_cho2 = (7,30 ,10)

tong_tien1= tinh_cuoc_taxi(loai_xe1 ,so_km1 ,thoi_gian_cho1 )
tong_tien2= tinh_cuoc_taxi(loai_xe2 ,so_km2 ,thoi_gian_cho2 )

print("Tổng tiền chuyến đi xe 4 chỗ:", tong_tien1)
print("Tổng tiền chuyến đi xe 7 chỗ:", tong_tien2)


#8.7
def tinh_tien_dien(so_kwh):
    # Giá tiền điện theo bậc thang
    gia_bac_1 = 1678  # Giá bậc 1: từ 0 - 50 kWh
    gia_bac_2 = 1734  # Giá bậc 2: từ 51 -100 kWh
    gia_bac_3 = 2014  # Giá bậc 3: từ101 -200 kWh
    gia_bac_4 = 2536   # Giá bậc >200kWh

    if so_kwh <=50:
        tien_dien = so_kwh * gia_bac_1
    elif so_kwh <=100:
        tien_dien = (50 * gia_bac_1) + ((so_kwh-50) *gia_bac_2)
    elif so_kwh <=200:
        tien_dien =(50*gia_bac_1)+(50*gia_bac_2)+((so_kwh-100)*gia_bac_3)
        
    else:
        tien_dien =(50*gia_bac_1)+(50*gia_bac_2)+(100*gia_bac_b3)+((so_kw_200)*gia_bac_b4)

    return round(tien_dien,2)

# Nhập số lượng kWh sử dụng
so_kwh = float(input("Nhập số lượng kWh sử dụng: "))

# Tính tiền điện
tien_dien = tinh_tien_dien(so_kwh)

# In kết quả
print("Tiền điện cần thanh toán là:", tien_dien, "VNĐ")


#8.8

def tinh_tien_thue_phong(loai_phong, so_dem):
    gia_phong = {
        1: 1260000,   # Standard
        2: 1550000,   # Superior Garden View
        3: 1830000,   # Superior Ocean View
        4: 1830000,   # Garden View Bungalow
        5: 2120000,   # Pool View Bungalow
        6: 2120000,   # Family Room
        7: 2540000,   # Beach Front Bungalow
        8: 4800000    # VIP Sea View
    }

    if so_dem >= 4:
        ti_le_giam = 0.3
    else:
        ti_le_giam = 0.25

    gia_phong_giam = gia_phong[loai_phong] - gia_phong[loai_phong] * ti_le_giam
    thanh_tien = gia_phong_giam * so_dem

    return thanh_tien

# Nhập loại phòng và số đêm từ người dùng
loai_phong = int(input("Nhập loại phòng (từ 1-8): "))
so_dem = int(input("Nhập số đêm: "))

# Tính tổng số tiền thuê phòng
thanh_tien = tinh_tien_thue_phong(loai_phong, so_dem)

# Xuất kết quả
print("Thành tiền =", thanh_tien, "VNĐ")




#8.9
n=int(input("Nhập n: "))
for i in range(0,n):
	print(n-i)


#8.10
n = int(input("Nhập n: "))
x = float(input("Nhập x: "))
S = (x*x + 1)^n 
print("S = (x*x + 1)^n =", S)


#8.11
n = int(input("Nhập n: "))
x = float(input("Nhập x: "))
A = (x*x + x + 1)^n + (x*x - x + 1)^n
print("A = (x*x + x + 1)^n + (x*x - x + 1)^n","=", A)


#8.12
a = int(input("Nhập số: "))
if a/1 == a and a%a == 0 and a > 1: 
	print(a,"là số nguyên tố")
else:
	print(a,"không phải là số nguyên tố")


#8.13
def is_prime(x):
    if x <= 1:
        return False
    if x <= 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    i = 5
    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        i += 6
    return True
x = int(input("Nhập số x: "))

if is_prime(x):
    print(x, "là số nguyên tố")
else:
    print(x, "không là số nguyên tố")



#8.14
def tinh_tong(n):
    tong = 0
    for i in range(n):
        so_nguyen = int(input("Nhập số nguyên thứ {}: ".format(i+1)))
        tong += so_nguyen
    return tong

n = int(input("Nhập số lượng số nguyên: "))
ket_qua = tinh_tong(n)
print("Tổng của các số nguyên là:", ket_qua)



#8.15
total = 0

while True:
    num = int(input("Nhập một số nguyên (nhập 0 để kết thúc): "))
    
    if num == 0:
        break
    
    total += num

print("Tổng các số đã nhập là:", total)



#8.16
def UCLN(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Nhập hai số nguyên từ bàn phím
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

# Tìm UCLN của a và b
ucln = UCLN(a, b)

# In kết quả
print("UCLN của", a, "và", b, "là:", ucln)


#8.17
def gcd(a, b):
    while(b):
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

# Nhập từ bàn phím hai số nguyên a và b
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
# Tìm bcLN của a và b
bcln = BCLN(a, b)

# In kết quả
print("BCLN của", a, "và", b, "là:", bcln)


#8.18
def is_perfect_number(num):
    # Kiểm tra xem num có phải là số nguyên dương không
    if num <= 0:
        return False

    # Tính tổng các ước của num (không tính chính nó)
    total = 0
    for i in range(1, num):
        if num % i == 0:
            total += i

    # Kiểm tra xem tổng các ước có bằng num hay không
    if total == num:
        return True
    else:
        return False

# Nhập số từ bàn phím và kiểm tra xem nó có phải là số hoàn hảo hay không
num = int(input("Nhập một số nguyên dương: "))
if is_perfect_number(num):
    print(num, "là một số hoàn hảo.")
else:
    print(num, "không phải là một số hoàn hảo.")



#8.19

n = int(input("Nhập số lượng số lẻ : "))

# Tạo một danh sách số ban đầu bắt đầu từ 1
sequence = [i for i in range(1, 2 * n, 2)]

# Đảo ngược danh sách
reversed_sequence = list(reversed(sequence))

# In ra dãy số lẻ sau khi đảo ngược
print("Dãy số lẻ sau khi đảo ngược:", reversed_sequence)


#8.20
import math

def approximate_exp(x):
    n = 1
    approximation = 1 + x**2 / n
    
    while abs(math.exp(x) - approximation) > 1e-4:
        n += 1
        approximation = 1 + x**2 / n
    
    return approximation

x = 1
approximation = approximate_exp(x)
print(f"e ≈ {approximation:.5f}")

















