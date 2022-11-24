n= int(input('Nhập n: '))
f1= 0
f2= 1
fn= 0
for i in range(3, n+1):
    fn = f1 + f2
    f1 = f2
    f2 = fn
print("số hạng thứ", n, "của dãy fibonaci là:", fn)
 
