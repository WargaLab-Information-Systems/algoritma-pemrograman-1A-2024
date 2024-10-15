tahun = int(input("masukkan tahun : "))
if tahun % 4 == 0:
    print("tahun kabisat")
elif tahun % 100 == 0:
    print("bukan tahun kabisat")
elif tahun % 400 == 0:
    print("tahun kabisat")
else:
    print("bukan tahun kabisat")