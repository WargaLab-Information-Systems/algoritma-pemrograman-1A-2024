#membuat belah ketupat
n = int (input("masukkan ukuran pola: "))
karakter = (input("masukkan karakter pola: "))

#bagian atas
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end= " ")
    for j in range (2 * i + 1):
        print(karakter, end=" ")
    print()

#bagian bawah
for i in range (n-2, -1, -1):
    for j in range(n-i-1):
        print(" ", end= " ")
    for j in range(2 * i + 1):
        print(karakter, end=" ")
    print()