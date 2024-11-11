# pola awal
n=int(input("masukkan ukuran sisi n: "))

# cetak bagian atas menggunakan nested loops
for i in range(n):
    print(" " * (n-i-1), end= "")
    for j in range(1*i+1):
        print("", "x", end= "")
    print()

# cetak bagian bawah menggunakan nested loops
for i in range(n):
    print(" " * i, end=" ")
    for j in range(n-i-1):
        print("", "x", end= "")
    print()