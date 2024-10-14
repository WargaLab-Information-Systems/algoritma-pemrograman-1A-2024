def hitung_denda(lama_pinjam):
    batas_waktu = 5
    denda_per_hari = 2500
    denda_tambahan_per_5_hari = 5500

    keterlambatan = lama_pinjam - batas_waktu

    if keterlambatan <= 0:
        return 0  # Tidak ada denda

    total_denda = keterlambatan * denda_per_hari

    if keterlambatan > 10:
        denda_tambahan = ((keterlambatan - 10) // 5) * denda_tambahan_per_5_hari
        total_denda += denda_tambahan

    return total_denda

def main():
    while True:
        try:
            lama_pinjam = int(input("Masukkan lama penyewaan (dalam hari): "))
            if lama_pinjam < 0:
                print("Lama penyewaan tidak boleh negatif. Coba lagi.")
                continue
        except ValueError:
            print("Input tidak valid! Masukkan angka yang benar.")
            continue

        total_denda = hitung_denda(lama_pinjam)
        
        print(f"Total denda keterlambatan: Rp{total_denda}")

        ulangi = input("Apakah Anda ingin menghitung kembali? (y/n): ").lower()
        if ulangi != 'y':
            print("Terima kasih telah menggunakan program ini!")
            break

main()