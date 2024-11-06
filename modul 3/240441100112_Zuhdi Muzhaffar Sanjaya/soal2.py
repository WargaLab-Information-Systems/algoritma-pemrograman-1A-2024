while True :
    angka = input("masukkan angka bilangan bulat: ")
    angka_terbalik = angka[-1]
    print("angka setelah di balik: ",angka_terbalik)

    hitung_lagi = input("apakah anda ingin menghitung lagi? (iya/tidak): ")
    if hitung_lagi != "iya":
        print("terimakasih telah mencoba programku")
        break