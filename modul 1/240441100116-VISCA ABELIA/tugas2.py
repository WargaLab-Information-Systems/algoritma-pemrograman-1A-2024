# u5 = 11
# u8ditambahu12 = 52
u5 = int(input("masukkan u5 :"))
u8ditambahu12 = int(input("masukkan u8+u12 :"))

#menghitung beda
#11 = a+4*b
#52 = a+7*b+a+11*b
#52 = 2a+18*b
#26 = a+9*b - 11 = a+4*b
#15 = 5*b
b = 3
a = u5-4*b

#Sn = n/2*(2*a+(n-1)*b)
Sukuke8 = 8/2*(2*a+(8-1)*b)
print(f"jumlah 8 suku pertama adalah : {Sukuke8}")