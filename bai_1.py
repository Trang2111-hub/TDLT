a=int(input(" Nhập a : "))
b=int(input(" Nhập b : "))
ucln = 1
if (a<b):
 min=a
else:
  min=b
for i in range (1,min+1):
  if (a%i == 0):
    if (b%i == 0):
     ucln=i
print('Ước chung lớn nhất là: ', ucln)
