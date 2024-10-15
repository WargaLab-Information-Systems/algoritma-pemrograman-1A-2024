
while True:
    hari_terlambat = int(input("masukkan hari keterlambatan : "))
    denda = 0

    if hari_terlambat > 5 :
            # denda lebih 5 hari kurang dari 10 hari
        if hari_terlambat <= 10 :
            denda = (hari_terlambat - 5) * 2500
        else :
                # denda normal 5 hari pertama (2500)
                denda = (10 - 5 ) * 2500
 
                # hitung denda tambahan untuk lebih 10 hari
                hari_tambahan = hari_terlambat - 10
                denda += hari_tambahan * 2500

                # denda tambahan setiap 5 hari lebih 10 hari
                denda += (hari_tambahan // 5 ) * 5500 
        print ("total denda keterlambatan : ", denda)
    ulang = input("Ingin menghitung kembali? (ya/tidak): ").strip().lower()
    if ulang != "ya" :
        break
