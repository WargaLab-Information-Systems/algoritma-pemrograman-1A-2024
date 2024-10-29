n = int(input("masukkan n (kecuali 1) : "))
karakter = input("masukkan karakter : ")

for i in range(n-1):
    for j in range(i, n):
        print(" ", end = " ")
    for j in range(i):
        print(karakter, end = " ")
    for j in range(i+1):
        print(karakter, end = " ")
    print()
for i in range(n):
    for j in range(i+1):
        print(" ", end = " ")
    for j in range(i, n-1):
        print(karakter, end = " ")
    for j in range(i, n):
        print(karakter, end = " ")
    print()
