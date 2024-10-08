# Buatlah program untuk menentukan tahun kabisat

# input tahun
tahun = int(input("masukkan tahun: "))

# penyeleksian kondisi menggunakan if bersarang
if tahun % 4 == 0:
    if tahun % 100 == 0:
        if tahun % 400 == 0:
            print("tahun kabisat")
        else:
            print("bukan tahun kabisat")
    else:
        print("tahun kabisat")
else:
    print("bukan tahun kabisat")

#arinda