# konversi bilangan desimal ke biner
a=float(input("masukkan bilangan desimal: "))
b=''
while a>0:
    a//=2
    b=str(a%2)+b

# membentuk pola segitiga
for i in range(1, len(b)+1):
    print(b[:i])