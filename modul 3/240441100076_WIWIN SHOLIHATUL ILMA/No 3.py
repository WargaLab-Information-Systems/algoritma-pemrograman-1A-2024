while True:
    lama_sewa = int(input("Masukkan lama sewa: "))

    if lama_sewa <= 5:
        print("DVD dikembalikan tepat waktu, maka tidak ada denda")
    else:
        hari_telat = lama_sewa - 5
        denda_hari = 2500
        denda_tambahan = 5500

        total_denda = hari_telat * denda_hari

        if hari_telat > 10:
            keterlambatan_tambahan = hari_telat - 10
            total_denda += (keterlambatan_tambahan // 5) * denda_tambahan

        print(f"Total denda keterlambatan anda: Rp {total_denda}")

    ulang = input("Apakah anda ingin menghitung kembali? (ya/tidak): ")
    if ulang.lower() != 'ya':
        print("Terima kasih!")
        break
