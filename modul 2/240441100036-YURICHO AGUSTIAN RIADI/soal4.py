tahun =int(input("masukkan  tahun: "))

# memeriksa kondisi tahun kabisat
kabisat = False

# menentukan hasil
if(tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
    print(tahun, "adalah tahun kabisat")
else:
    print(tahun, "bukan tahun kabisat")