n = int(input ("masukan ukuran (n): "))
karakter = input ("masukan karakter input(contoh: '*'): ")
for i in range (n):
    for j in range (n - i - 1):
        print (" ", end="")