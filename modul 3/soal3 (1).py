while True:
    lama_sewa = int(input("masukkan lama sewa DVD (dalam hari): "))
    keterlambatan = max(0 , lama_sewa - 5) #hitung keterlambatan
    total_denda = 0

    # Hitung denda harian satu persatu
    for hari in range(1, keterlambatan + 1):
        total_denda += 2500 #denda Rp.2500 perhari

        # Tambah denda Rp.5500 setiap kelipatan 5 hari setelah 10 hari
        if hari > 10 and hari % 5 == 0:
            total_denda += 5500

    if keterlambatan > 0:
        print(f"total denda keterlambatan: Rp.{total_denda}")
    else:
        print("DVD dikembalikkan tepat waktu. tidak ada denda.")

    if input("hitung lagi? (ya/tidak): ").strip().lower() != 'ya':
        print("terimakasih telah menggunakan program ini.")
        break 