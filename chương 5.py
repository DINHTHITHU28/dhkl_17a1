#CHƯƠNG 5


#bài tập 1
print("**    **  ******  **      **      ******")
print("**    **  **      **      **      **  **")
print("********  ******  **      **      **  **")
print("**    **  **      **      **      **  **")
print("**    **  ******  ******  ******  ******")

#bài tập 2
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

#bài tập 3

ten_hang= input("Tên hàng: ")
so_luong= int(input("Số lượng: "))
don_gia= int(input("Đơn giá: "))
tien_phai_tra= so_luong * don_gia
print("\n---")
print("Tên hàng: ",ten_hang)
print("Số lượng: ",so_luong)
print("Đơn giá: ",don_gia)
print("Tiền phải trả: ",tien_phai_tra ,"vnđ")

#bài tập 4
a = int(input("Nhập độ dài cạnh a: "))
b = int(input("Nhập độ dài cạnh b: "))
c = int(input("Nhập độ dài cạnh c: "))
p = (a + b + c)
import math
s = math.sqrt(p * (p - a) * (p - b) * (p -c))
print("Diện tích tam giác là:", s)

