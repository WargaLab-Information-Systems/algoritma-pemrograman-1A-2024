tahun_kabisat = int(input("masukkan tahun: "))
if (tahun_kabisat % 4 == 0 and tahun_kabisat % 100 != 0) or (tahun_kabisat % 400 == 0):
    print(f"{tahun_kabisat} Adalah Tahun kabisat") 
else :
    print(f"{tahun_kabisat} Bukan Tahun kabisat") 