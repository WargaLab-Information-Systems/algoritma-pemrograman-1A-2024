import math

# Fungsi untuk menghitung kombinasi
def kombinasi(n, r):
    return math.comb(n, r)

# Input angka 
n = int(input("Masukkan jumlah total orang (n): "))
r = int(input("Masukkan jumlah orang yang ingin dipilih (r): "))

# Menghitung jumlah cara membentuk tim
hasil = kombinasi(n, r)
print(f"Ada {hasil} cara untuk membentuk tim.")
