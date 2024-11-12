# Input tahun dari pengguna
tahun = int(input("Masukkan tahun: "))

# Cek apakah tahun kabisat
if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
    print(tahun, "adalah tahun kabisat")
else:
    print(tahun, "bukan tahun kabisat")