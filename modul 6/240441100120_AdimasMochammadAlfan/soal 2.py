pinjaman = []

def menambah_peminjaman_buku():
    id_peminjam = input("Masukkan ID peminjam: ")
    nama_peminjam = input("Masukkan nama peminjam: ")
    judul_buku = input("Masukkan judul buku yang dipinjam: ")
    tanggal_peminjaman = input("Masukkan tanggal peminjaman: ")

    meminjam = (id_peminjam, nama_peminjam, judul_buku, tanggal_peminjaman)
    pinjaman.append(meminjam)
    print("Penambahan data berhasil dilakukan.\n")


def layarawal_peminjaman():
    if not pinjaman:
        print("Tidak ada data buku yang dipinjam.\n")
    else:
        print("=== Data Peminjaman ===\n")
        for meminjam in pinjaman:
            print("ID Peminjaman: ", meminjam[0])
            print("Nama Peminjam: ", meminjam[1])
            print("Judul Buku: ", meminjam[2]) 
            print("Tanggal Peminjaman: ", meminjam[3])
            print()
        print()


def pembaruan_peminjaman():
    id_peminjam = input("Masukkan ID peminjam yang ingin diperbarui: ")
    for i in range(len(pinjaman)):
        if pinjaman[i][0] == id_peminjam:
            id_pembaruan = input("Masukkan ID yang ingin diperbarui: ")
            pembaruan_nama = input("Masukkan nama peminjam yang diperbarui: ")
            judul_buku = input("Masukkan judul buku yang diperbarui: ")
            tanggal_peminjaman = input("Masukkan tanggal yang diperbarui: ")

            pinjaman[i] = (id_pembaruan, pembaruan_nama, judul_buku, tanggal_peminjaman)
            print("Data berhasil diperbarui.\n")
            return
    print("ID peminjam tidak ditemukan.\n")


def menghapus_peminjaman():
    id_peminjam = input("Masukkan ID peminjam yang ingin dihapus: ")
    for i in range(len(pinjaman)):
        if pinjaman[i][0] == id_peminjam:
            del pinjaman[i]
            print("Data peminjam berhasil dihapus.\n")
            return
    print("ID peminjam tidak ditemukan.\n")


while True:
    print("Menu Sistem Peminjaman Buku Perpustakaan:")
    print("1. Penambahan Data Peminjaman")
    print("2. Layar Awal Data Peminjaman")
    print("3. Pembaruan Data Peminjaman")
    print("4. Hapus Data Peminjaman")
    print("5. Keluar")
    pilihan = input("Pilih opsi (1/2/3/4/5): ")

    if pilihan == '1':
        menambah_peminjaman_buku()
    elif pilihan == '2':
        layarawal_peminjaman()
    elif pilihan == '3':
        pembaruan_peminjaman()
    elif pilihan == '4':
        menghapus_peminjaman()
    elif pilihan == '5':
        print("Terima kasih telah memilih program ini.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.\n")
