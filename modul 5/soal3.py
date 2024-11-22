def faktorial(n):
    if n == 0:
        print("0! = 1")
    else:
        hasil = 1
        print(f"{n}! =", end = " ")
        for i in range(n, 0, -1):
            hasil *= i
            print(i, end = "")
            if i > 1:
                print(" x ", end = "")
        print(f" = {hasil}")

# input
n = int(input("masukkan angka non-negatif untuk faktorial: "))

# cek apakah angka negatif
if n < 0:
    print("masukkan angka non-negatif.")
else:
    faktorial(n)