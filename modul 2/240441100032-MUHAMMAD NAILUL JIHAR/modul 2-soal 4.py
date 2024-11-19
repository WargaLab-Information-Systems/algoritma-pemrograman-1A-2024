tahun_Kabisat = int(input("Masukkan Tahun yang Anda Inginkan : "))

if (tahun_Kabisat % 4 ==0 and tahun_Kabisat % 100 != 0) or (tahun_Kabisat % 400 ==0):
    print(f"{tahun_Kabisat} Adalah Tahun Kabisat")
else:
    print(f"{tahun_Kabisat} Adalah bukan Tahun Kabisat")