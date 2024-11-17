ukuran = int (input("masukkan ukuran yang anda inginkan: "))
huruf = str (input("masukkan huruf x/o: "))
for i in range(ukuran):
    for j in range (ukuran-i-1):
        print(" ", end=" ")
    for y in range (2*i+1):
        print (huruf, end= " ")
    print()

for i in range (ukuran-2,-1,-1):
    for j in range (ukuran-i-1):
        print(" ", end= " ")
    for y in range (2*i+1):
        print (huruf, end= " ")
    print()
