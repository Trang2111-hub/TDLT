n=int(input("Nhập số phương trình : "))
s=0
for i in range (1,n,1):
    a=float(input("Nhập a="))
    b=float(input("Nhập b="))
    c=float(input("Nhập c="))
    a1= float(input("Nhập a1="))
    b1 = float(input("Nhập b1="))
    c1 = float(input("Nhập c1="))
    delta=b**2 - 4*a*c
    delta1=b1**2 - 4*a1*c1
if (delta>0):
    x1 = float((-b + delta) / (2 * a))
    x2 = float((-b - delta) / (2 * a))
if (delta1>0):
    x3 = float((-b1 + delta) / (2 * a1))
    x4 = float((-b1 - delta) / (2 * a1))
s=x1+x2+x3+x4
print (s)
