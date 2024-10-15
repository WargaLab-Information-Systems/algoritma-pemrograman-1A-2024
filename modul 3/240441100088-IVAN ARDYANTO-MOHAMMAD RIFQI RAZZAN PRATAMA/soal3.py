batas_waktu = 5
denda_per_hari = 2500

#Denda tambahan setelah keterlambatan lebih dari 10 hari
denda_tambahan_per_5_hari = 5500

while True:
    #Meminta input lama penyewaan
    try:
        lama_pinjam = int(input("Masukkan lama penyewaan (dalam hari): "))
        if lama_pinjam < 0:
            print("Lama penyewaan tidak boleh negatif. Coba lagi.")
            continue
    except ValueError:
        print("Input tidak valid! Masukkan angka yang benar.")
        continue

    #Hitung jumlah hari keterlambatan
    keterlambatan = lama_pinjam - batas_waktu

    #Hitung total denda
    if keterlambatan <= 0:
        total_denda = 0  # Tidak ada denda
    else:
        #Denda dasar per hari keterlambatan
        total_denda = keterlambatan * denda_per_hari

        #Jika keterlambatan lebih dari 10 hari
        if keterlambatan > 10:
            denda_tambahan = ((keterlambatan - 10) // 5) * denda_tambahan_per_5_hari
            total_denda += denda_tambahan

    #Tampilkan hasil
    print(f"Total denda keterlambatan: Rp{total_denda}")

    #Tanyakan apakah ingin menghitung kembali
    ulangi = input("Apakah Anda ingin menghitung kembali? (y/n): ").lower()
    if ulangi != 'y':
        print("Terima kasih telah menggunakan program ini!")
        break