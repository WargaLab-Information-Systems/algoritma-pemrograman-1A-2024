def calculate_discount():
    while True:
        nama=str(input("masukan nama: "))
        total_belanja=int(input("masukan total belanja: "))
        keanggotaan=str(input("apakah memiliki keanggotaan? (ya/tidak) "))
        if keanggotaan=='tidak':
            print("pelanggan tidak mendapat diskon")
            break
        if keanggotaan=='ya':
            jenis_keanggotaan=str(input("jenis keanggotaan? "))
            diskon=0
            if jenis_keanggotaan=='gold':
                diskon=0.15
            elif jenis_keanggotaan=='silver':
                diskon=0.1
            elif jenis_keanggotaan=='bronze':
                diskon=0.05
        if total_belanja>1000000:
            diskon_lebih_1_jt=0.05
            print(f"totalnya beserta diskon adalah: {total_belanja*(diskon+diskon_lebih_1_jt)}")
            break
        kalkulasi_diskon=(total_belanja*diskon)/100
        print(f"diskon yang didapat adalah {kalkulasi_diskon}")
calculate_discount()