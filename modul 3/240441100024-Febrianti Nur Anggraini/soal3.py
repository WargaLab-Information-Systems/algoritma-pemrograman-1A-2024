# meminta input lama waktu pinjam 
ulang_ya = 'ya' #variabel ulang
 
#menggunakan perintah while
while True :
    lama_pinjam = int(input("masukkan lama peminjaman:"))

    if lama_pinjam <= 5:
        print("tidak di denda karena masih batas waktu")
    else:
        if lama_pinjam >= 5:
            hari_terlambat = lama_pinjam
            denda_per_hari = 2500
            total_denda = hari_terlambat * denda_per_hari

            if hari_terlambat > 10:
                sisa_hari_terlambat = hari_terlambat 
                total_denda += (sisa_hari_terlambat) * 5500

            print(f"total denda leterlambatan : {total_denda}")

    #menanyakan apakah user ingin menghitung kembali
    ulang_ya = input ("apakah anda ingin menghitung lagi? (ya/tidak)")
    break