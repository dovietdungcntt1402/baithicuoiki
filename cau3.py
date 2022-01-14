name = input("Nhập tên đầy đủ của bạn:")
print(name)
#câu b
def ThuanNghich(n):
    str1 = str(n)
    str2 = str1[::-1]
    if (str1 == str2):
        return True
    else:
        return False
x=len(input("Nhập họ của bạn:"))
y=len(input("Nhập tên đệm của bạn:"))
z=len(input("Nhập tên của bạn:"))
n = str(x)+str(y)+str(z)
print("n=",n)
print("Số", n , "là" ,ThuanNghich(n))
