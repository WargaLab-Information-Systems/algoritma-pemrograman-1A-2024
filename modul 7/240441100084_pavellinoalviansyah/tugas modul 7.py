
# 1
def peminjaman_alat():
    alat_kesehatan = {}

    print("=== Program Peminjaman Alat Kesehatan ===")

    while True:
        print("Pilih menu:")
        print("1. Tambah alat yang dipinjam")
        print("2. Kembalikan alat")
        print("3. Tukar alat")
        print("4. Lihat alat yang sedang dipinjam")
        print("5. Keluar")

        pilihan = input("Masukkan pilihan Anda (1-5): ")
        if pilihan == "1":  # Tambah alat yang dipinjam
            alat = input("Masukkan nama alat yang ingin dipinjam: ").strip().lower()
            jumlah = input(f"Masukkan jumlah {alat} yang ingin dipinjam: ").strip()

            if not jumlah.isdigit() or int(jumlah) <= 0:
                print("Jumlah harus berupa angka lebih dari 0.")
                continue

            jumlah = int(jumlah)
            if alat in alat_kesehatan:
                alat_kesehatan[alat] += jumlah
            else:
                alat_kesehatan[alat] = jumlah

            print(f"{jumlah} {alat} berhasil ditambahkan.")

        elif pilihan == "2":  # Kembalikan alat
            alat = input("Masukkan nama alat yang ingin dikembalikan: ").strip().lower()
            if alat in alat_kesehatan:
                jumlah = input(f"Masukkan jumlah {alat} yang ingin dikembalikan: ").strip()

                if not jumlah.isdigit() or int(jumlah) <= 0:
                    print("Jumlah harus berupa angka lebih dari 0.")
                    continue

                jumlah = int(jumlah)
                if jumlah >= alat_kesehatan[alat]:
                    del alat_kesehatan[alat]
                    print(f"Semua {alat} telah dikembalikan.")
                else:
                    alat_kesehatan[alat] -= jumlah
                    print(f"{jumlah} {alat} berhasil dikembalikan.")
            else:
                print(f"{alat} tidak ditemukan dalam daftar alat yang dipinjam.")

        elif pilihan == "3":
            alat_tukar = input("Masukkan nama alat yang ditukar: ").strip().lower()
            if alat_tukar in alat_kesehatan:
                jumlah_tukar = int(input(f"Masukkan jumlah {alat_tukar} yang ditukar: "))
                alat_kesehatan[alat_tukar] -= jumlah_tukar

                if alat_kesehatan[alat_tukar] <= 0:
                    del alat_kesehatan[alat_tukar]

                alat_baru = input("Masukkan nama alat pengganti: ").strip().lower()
                jumlah_baru = int(input(f"Masukkan jumlah {alat_baru} yang dipinjam: "))

                if alat_baru in alat_kesehatan:
                    alat_kesehatan[alat_baru] += jumlah_baru
                else:
                    alat_kesehatan[alat_baru] = jumlah_baru

                print(f"{jumlah_tukar} {alat_tukar} berhasil ditukar dengan {jumlah_baru} {alat_baru}.")
            else:
                print(f"{alat_tukar} tidak ditemukan dalam daftar alat yang dipinjam.")

        elif pilihan == "4":
            if alat_kesehatan:
                print("=== Alat yang Sedang Dipinjam ===")
                for alat, jumlah in alat_kesehatan.items():
                    print(f"- {alat}: {jumlah} buah")
            else:
                print("Tidak ada alat yang sedang dipinjam.")

        elif pilihan == "5":
            print("Terima kasih telah menggunakan program ini!")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


peminjaman_alat()

# 2
def main():
    klub_basket = {"Ali", "Budi", "Citra", "Dina", "Eka"}
    klub_renang = {"Budi", "Fahri", "Dina", "Gita", "Hana"}

    print("=== Informasi Klub Ekstrakurikuler ===\n")

    print("a. Daftar siswa:")
    print(f"Klub Basket: {klub_basket}")
    print(f"Klub Renang: {klub_renang}\n")


    siswa_kedua_klub = klub_basket & klub_renang
    print(f"b. Siswa yang mengikuti kedua klub: {siswa_kedua_klub}\n")


    siswa_satu_klub = (klub_basket ^ klub_renang)
    print(f"c. Siswa yang hanya mengikuti satu klub: {siswa_satu_klub}\n")


    semua_siswa = klub_basket | klub_renang
    print(f"d. Semua siswa unik yang mengikuti setidaknya satu klub: {semua_siswa}\n")


    jumlah_siswa_unik = len(semua_siswa)
    print(f"e. Jumlah siswa unik: {jumlah_siswa_unik}")


main()

# 3
kelas = {}

kapasitas_kelas = 3


def tambah_siswa():
    global kelas, kapasitas_kelas

    nama = input("Masukkan nama siswa: ").strip()
    asal_sekolah = input("Masukkan asal sekolah: ").strip()
    plotting = input("Masukkan plotting bimbingan: ").strip()

    kelas_ditemukan = None
    for nama_kelas, daftar_siswa in kelas.items():
        if len(daftar_siswa) < kapasitas_kelas:
            kelas_ditemukan = nama_kelas
            break

    if not kelas_ditemukan:
        kelas_ditemukan = f"Kelas-{len(kelas) + 1}"
        kelas[kelas_ditemukan] = []

    kelas[kelas_ditemukan].append({
        "nama": nama,
        "asal_sekolah": asal_sekolah,
        "plotting": plotting
    })

    print(f"Siswa {nama} berhasil ditambahkan ke {kelas_ditemukan}.")


def lihat_data():
    global kelas

    print("\n=== Data Kelas ===")
    if not kelas:
        print("Belum ada data kelas.")
        return

    for nama_kelas, daftar_siswa in kelas.items():
        print(f"\n{nama_kelas} (Total: {len(daftar_siswa)} siswa):")
        for idx, data in enumerate(daftar_siswa, start=1):
            print(f"  {idx}. Nama: {data['nama']}, Asal Sekolah: {data['asal_sekolah']}, Plotting: {data['plotting']}")


def edit_siswa():
    global kelas

    lihat_data()
    if not kelas:
        return

    nama_kelas = input("Masukkan nama kelas yang ingin diubah: ").strip()
    if nama_kelas not in kelas:
        print("Kelas tidak ditemukan.")
        return
    
    try:
        idx = int(input(f"Masukkan nomor siswa di {nama_kelas} yang ingin diubah: ")) - 1
        if 0 <= idx < len(kelas[nama_kelas]):
            nama = input("Masukkan nama baru (kosongkan jika tidak ingin diubah): ").strip()
            asal_sekolah = input("Masukkan asal sekolah baru (kosongkan jika tidak ingin diubah): ").strip()
            plotting = input("Masukkan plotting bimbingan baru (kosongkan jika tidak ingin diubah): ").strip()

            if nama:
                kelas[nama_kelas][idx]["nama"] = nama
            if asal_sekolah:
                kelas[nama_kelas][idx]["asal_sekolah"] = asal_sekolah
            if plotting:
                kelas[nama_kelas][idx]["plotting"] = plotting

            print("Data siswa berhasil diubah.")
        else:
            print("Nomor siswa tidak valid.")
    except ValueError:
        print("Input tidak valid.")


def hapus_siswa():
    global kelas

    lihat_data()
    if not kelas:
        return

    nama_kelas = input("Masukkan nama kelas yang ingin dihapus siswa: ").strip()
    if nama_kelas not in kelas:
        print("Kelas tidak ditemukan.")
        return

    try:
        idx = int(input(f"Masukkan nomor siswa di {nama_kelas} yang ingin dihapus: ")) - 1
        if 0 <= idx < len(kelas[nama_kelas]):
            siswa_dihapus = kelas[nama_kelas].pop(idx)
            print(f"Siswa {siswa_dihapus['nama']} berhasil dihapus dari {nama_kelas}.")

            if not kelas[nama_kelas]:
                del kelas[nama_kelas]
                print(f"{nama_kelas} dihapus karena sudah tidak ada siswa.")
        else:
            print("Nomor siswa tidak valid.")
    except ValueError:
        print("Input tidak valid.")


def menu():
    while True:
        print("\n=== Menu Gema Ripah ===")
        print("1. Tambah Siswa")
        print("2. Lihat Data")
        print("3. Edit Siswa")
        print("4. Hapus Siswa")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ").strip()
        if pilihan == "1":
            tambah_siswa()
        elif pilihan == "2":
            lihat_data()
        elif pilihan == "3":
            edit_siswa()
        elif pilihan == "4":
            hapus_siswa()
        elif pilihan == "5":
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")



menu()
