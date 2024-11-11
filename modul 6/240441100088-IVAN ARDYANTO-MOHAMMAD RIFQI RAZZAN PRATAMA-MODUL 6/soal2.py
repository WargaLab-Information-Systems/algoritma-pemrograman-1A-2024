# Daftar buku
list_buku = [
    "Eksplorasi Teknologi: Panduan Lengkap bagi Pemula",
    "Jejak Peradaban Islam: Hikmah dan Sejarah",
    "Kode Pemrograman: Panduan Praktis untuk Mahasiswa Teknik Informatika",
    "Lingkungan Hidup dan Teknologi Hijau: Solusi Inovatif untuk Masa Depan",
    "Seni Mengelola Sistem Linux untuk Komunitas Open Source"
]

# Menyimpan peminjaman
# Struktur = [(id peminjam), [nama peminjam, judul buku, tanggal peminjaman]]
list_peminjaman = []

# Tambah peminjaman (Create)
def tambah_peminjaman(nama_peminjam, judul_buku, tanggal_peminjaman):
    judul_buku = list_buku[judul_buku]

    id_peminjaman = f"{str(len(nama_peminjam)) + judul_buku}_{nama_peminjam}_{tanggal_peminjaman}"
    peminjaman_baru = [(id_peminjaman), [nama_peminjam, judul_buku, tanggal_peminjaman]]

    list_peminjaman.append(peminjaman_baru)
    return peminjaman_baru

# Cek peminjaman (Read)
def cek_peminjaman(kata_kunci):
    if not list_peminjaman:
        return False

    for i in range(len(list_peminjaman)):
        if kata_kunci in list_peminjaman[i][1][0]:
            return list_peminjaman[i]

# Edit peminjaman (Update)
def edit_peminjaman(id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman):
    if not list_peminjaman:
        return False

    for i in range(len(list_peminjaman)):
        if id_peminjaman in list_peminjaman[i][0][0]:
            hasil = [(id_peminjaman), [nama_peminjam, judul_buku, tanggal_peminjaman]]
            list_peminjaman[i] = hasil

            return True
    
    return False

# Hapus peminjaman (delete)
def hapus_peminjaman(id_peminjaman):
    if not list_peminjaman:
        False

    for i in range(len(list_peminjaman)):
        if id_peminjaman in list_peminjaman[i][0][0]:
            list_peminjaman.pop(i)
            return True
    
    return False

# Program utama
while True:
    print("Menu:")
    print("1. Tambah peminjaman\n2. Cek peminjaman\n3. Edit peminjaman\n4. Hapus peminjaman\n0. Keluar")
    menu = input("Pilih menu yang anda pilih: ")

    # Tambah peminjaman
    if menu == "1":
        print()
        print("\nMenambah peminjan")
        nama_peminjam = input("Masukkan nama peminjam: ")

        print("Pilih buku yang akan dipinjam:")
        for i in range(len(list_buku)):
            print(f"{i}. {list_buku[i]}")
        
        judul_buku = int(input("Pilih judul buku yang dipinjam: "))
        tanggal_peminjaman = input("Masukkan tanggal peminjaman (DD/MM/YYYY): ")

        hasil = tambah_peminjaman(nama_peminjam, judul_buku, tanggal_peminjaman)

        if not hasil:
            print("Gagal menambahkan buku\n")
            continue
        
        print(f"Berhasil menambahkan buku: {hasil}\n")

    # Cek peminjaman
    elif menu == "2":
        print("\nMengecek peminjaman berdasarkan nama.")
        kata_kunci = input("Masukkan nama peminjam: ")

        hasil = cek_peminjaman(kata_kunci)

        if not hasil:
            print("Data tidak ditemukan!\n")
            continue

        print("Data ditemukan!")
        print(f"id buku: {hasil[0][0]}")
        print(f"Nama Peminjam: {hasil[1][0]}")
        print(f"Judul Buku: {hasil[1][1]}")
        print(f"Tanggal Peminjaman: {hasil[1][2]}")
        print()

    # Edit peminjaman
    elif menu == "3":
        list_opsi = ["Nama peminjam", "Judul buku", "Tanggal peminjaman"]

        print("\nMengedit peminjaman berdasarkan nama.")
        kata_kunci = input("Masukkan nama peminjam: ")

        hasil = cek_peminjaman(kata_kunci)

        if not hasil:
            print("Data tidak ditemukan!\n")
            continue

        print("Opsi pengeditan")
        for i in range(len(list_opsi)):
            print(f"{i}. {list_opsi[i]}")
        
        opsi = int(input("Masukkan opsi anda: "))

        if opsi > len(list_opsi) - 1:
            print("Pilihan anda tidak terdapat dalam menu!")
            continue

        nilai_baru = input("Masukkan nilai baru: ")
        hasil[1][opsi] = nilai_baru

        hasil = edit_peminjaman(
            hasil[0][0],
            hasil[1][0],
            hasil[1][1],
            hasil[1][2]
            )
        
        if not hasil:
            print("Gagal mengedit data!\n")
            continue

        print("Berhasil mengedit data!\n")

    # Menghapus peminjaman
    elif menu == "4":
        print("\nMenghapus peminjaman.")
        kata_kunci = input("Masukkan nama peminjam: ")

        hasil = cek_peminjaman(kata_kunci)

        if not hasil:
            print("Data tidak ditemukan!\n")
            continue

        hasil = hapus_peminjaman(hasil[0][0])
        
        if not hasil:
            print("Gagal menghapus data!\n")
            continue

        print("Berhasil menghapus data!\n")

    elif menu == "0":
        print("\nProgram diakhiri")
        break

    else:
        print("\nMaaf, pilihan yang anda pilih tidak tersedia dalam menu!\n")
        continue