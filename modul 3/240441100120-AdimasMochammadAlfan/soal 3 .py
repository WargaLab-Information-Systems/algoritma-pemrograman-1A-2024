ulang = "ya"
while ulang.lower() == "ya":
    # Meminta input lama waktu penyewaan
    lama_pinjam = input("Masukkan lama waktu penyewaan (dalam hari): ")

    # Penyeleksian kondisi untuk mengecek apakah input terdiri dari angka saja
    hanya_angka = True  # Asumsikan input valid
    for angka in lama_pinjam:
        if angka < '0' or angka > '9':  # Memeriksa apakah setiap karakter adalah digit
            hanya_angka = False  # Jika ada karakter yang bukan digit, input tidak valid
            break

    if hanya_angka and lama_pinjam != "":  # Memastikan input tidak kosong dan hanya terdiri dari angka
        lama_pinjam = int(lama_pinjam)  # Mengonversi input menjadi integer
        batas_pinjam = 5
        denda_per_hari = 2500
        denda_tambahan = 5500
        total_denda = 0

        # Menghitung keterlambatan
        keterlambatan = lama_pinjam - batas_pinjam

        if keterlambatan > 0:
            # Denda Rp.2500/hari untuk keterlambatan sampai 10 hari
            if keterlambatan <= 10:
                total_denda = keterlambatan * denda_per_hari
            else:
                # Denda Rp.2500/hari untuk 10 hari pertama
                total_denda = 10 * denda_per_hari
                # Denda tambahan Rp.5500 untuk setiap 5 hari tambahan setelah 10 hari
                sisa_hari = keterlambatan - 10
                total_denda += (sisa_hari // 5) * denda_tambahan
                # Jika ada sisa hari yang kurang dari 5 hari, dihitung dengan denda Rp.2500/hari
                total_denda += (sisa_hari % 5) * denda_per_hari

        print(f"Total denda keterlambatan adalah: Rp {total_denda}")
    else:
        print("Masukkan angka yang valid.")

    ulang = input("Apakah Anda ingin menghitung denda lagi? (ya/tidak): ").lower()

print("Program selesai.")
