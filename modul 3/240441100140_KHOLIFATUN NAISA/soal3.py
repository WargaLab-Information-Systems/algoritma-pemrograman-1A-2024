while True:
    lama_sewa = int(input("Masukkan lama waktu penyewaan: "))
    if lama_sewa <= 0:
        print("Maaf, anda salah penginputan.")
        break

    keterlambatan = lama_sewa - 5
    harga_sewa = 5000

    if keterlambatan < 0:
        print("Tidak ada denda keterlambatan.")
        print(f"Total yang harus anda bayar adalah: {harga_sewa}")
    else:
        denda_per_hari = 2500
        denda_tambahan = 0
        if keterlambatan > 10:
            denda_tambahan = (keterlambatan - 10) // 5 * 5500
        total_denda = keterlambatan * denda_per_hari + denda_tambahan
        print(f"Total harga sebelum denda: {harga_sewa}")
        print(f"Total denda keterlambatan: {total_denda}")
    
    jawab = input("Apakah ingin menghitung kembali? (ya/y atau tidak/n): ")
    if jawab == "y" or jawab == "ya":
        continue
    elif jawab == "t" or jawab == "tidak" :
        print("terimakasih")
        break
    else:
        print("invalid")   
        break