n=int(input("Nhập số phương trình cần giải n="))
i=1
tong=0
for i in range(n):
    a=float(input("Nhập a="))
    b=float(input("Nhập b="))
    c=float(input("Nhập c="))
    delta=b**2-4*a*c
    if a==0 and b!=0 :
        tong+=(-c/b)
    elif delta==0:
        tong+=(-b/(2*a))
print("Tổng nghiệm của phương trình 1 nghiệm là:", tong)
