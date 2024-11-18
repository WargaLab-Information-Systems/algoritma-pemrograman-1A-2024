tahun = int(input("masukkan tahun :"))

if (tahun % 100 != 0 or tahun % 400 != 0) and tahun % 4 == 0 :
    print (tahun, "adalah tahun kabisat")
else :
    print (tahun, "bukan tahun kabisat")