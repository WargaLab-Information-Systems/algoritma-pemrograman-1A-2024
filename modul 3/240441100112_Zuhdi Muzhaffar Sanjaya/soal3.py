while True:
    lama_sewa = int(input("berapa hari lama penyewaan DVD Anda: "))

    if lama_sewa > 5:
        keterlambatan = lama_sewa - 5
        if keterlambatan <= 10:
            # jika keterlambatan <= 10 hari, dendahanya 2500 per hari keterlambatan
            denda = keterlambatan * 2500
        else:
             # jika keterlambatan lebih dari 10 hari
             denda_5_hari_pertama = 10 * 2500 # denda untuk keterlambatan hingga 10 hari
             keterlambatan_selanjutnya = keterlambatan - 10 
             denda_tambahan = (keterlambatan_selanjutnya // 5 + 1) * 5500
             denda = denda_5_hari_pertama + denda_tambahan

        print("total denda keterlambatan: Rp", denda)
    else:
        print("DVD dikembalikan tepat waktu, tidak ada denda.")

    hitung_lagi = input("Apakah Anda ingin menghitung lagi? (iya/tidak): ")
    if hitung_lagi != "iya":
        print("terima kasih telah menyewa DVD di toko kami.")
        break 