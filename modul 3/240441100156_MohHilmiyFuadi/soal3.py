denda_per_hari = 2500
denda_tambahan = 5500

while True:
    lama_sewa = int(input("Masukkan lama waktu penyewaan (dalam hari): "))
    keterlambatan = lama_sewa - 5
    total_denda = 0

    if keterlambatan > 0:
        total_denda += keterlambatan * denda_per_hari
        if keterlambatan > 10:
            denda_tambahan_hari = (keterlambatan - 10) // 5
            total_denda += denda_tambahan_hari * denda_tambahan

    print("Total denda keterlambatan: Rp.", total_denda)

    ulang = input("Apakah Anda ingin menghitung kembali? (ya/tidak): ").lower()
    if ulang == "ya" or ulang == "y":
        continue
    elif ulang == "tidak" or ulang == "n":
        break
    else:
        print("invalid")