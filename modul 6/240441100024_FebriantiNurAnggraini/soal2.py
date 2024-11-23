data_peminjaman = []

# Fungsi untuk menambah peminjaman buku
def tambah_peminjaman(id_peminjaman, nama_peminjam, judul_buku, tgl_peminjaman):
    data_peminjaman.append((id_peminjaman, nama_peminjam, judul_buku, tgl_peminjaman))
    print(f"Peminjaman dengan ID {id_peminjaman} berhasil ditambahkan.")

# Fungsi untuk menampilkan seluruh data peminjaman
def tampilkan_peminjaman():
    if data_peminjaman:
        for peminjaman in data_peminjaman:
            print(f"ID: {peminjaman[0]}, Nama: {peminjaman[1]}, Buku: {peminjaman[2]}, Tanggal: {peminjaman[3]}")
    else:
        print("Tidak ada data peminjaman.")

# Fungsi untuk memperbarui data peminjaman
def perbarui_peminjaman(id_peminjaman, nama, buku, tanggal):
    for i, peminjaman in enumerate(data_peminjaman):
        if peminjaman[0] == id_peminjaman:
            data_peminjaman[i] = (peminjaman[0],
                                  nama if nama else peminjaman[1],
                                  buku if buku else peminjaman[2],
                                  tanggal if tanggal else peminjaman[3])
            print(f"Peminjaman dengan ID {id_peminjaman} berhasil diperbarui.")
            return
    print(f"Peminjaman dengan ID {id_peminjaman} tidak ditemukan.")

# Fungsi untuk menghapus peminjaman buku
def hapus_peminjaman(id_peminjaman):
    global data_peminjaman
    data_peminjaman = [peminjaman for peminjaman in data_peminjaman if peminjaman[0] != id_peminjaman]
    print(f"Peminjaman dengan ID {id_peminjaman} berhasil dihapus.")

# Menu utama
def menu():
    while True:
        print("\nMenu:")
        print("1. Tambah Peminjaman Buku")
        print("2. Lihat Data Peminjaman Buku")
        print("3. Update Data Peminjaman Buku")
        print("4. Hapus Peminjaman Buku")
        print("5. Keluar")
        pilihan = input("Pilih menu (1/2/3/4/5): ")

        if pilihan == "1":
            id_peminjaman = input("ID Peminjaman: ")
            nama_peminjam = input("Nama Peminjam: ")
            judul_buku = input("Judul Buku: ")
            tgl_peminjaman = input("Tanggal Peminjaman: ")
            tambah_peminjaman(id_peminjaman, nama_peminjam, judul_buku, tgl_peminjaman)

        elif pilihan == "2":
            tampilkan_peminjaman()

        elif pilihan == "3":
            id_peminjaman = input("ID Peminjaman yang akan diperbarui: ")
            nama_peminjam = input("Nama Peminjam baru (kosongkan jika tidak ada perubahan): ")
            judul_buku = input("Judul Buku baru (kosongkan jika tidak ada perubahan): ")
            tgl_peminjaman = input("Tanggal Peminjaman baru (kosongkan jika tidak ada perubahan): ")
            perbarui_peminjaman(id_peminjaman, nama_peminjam, judul_buku, tgl_peminjaman)

        elif pilihan == "4":
            id_peminjaman = input("ID Peminjaman yang akan dihapus: ")
            hapus_peminjaman(id_peminjaman)

        elif pilihan == "5":
            print("Terima kasih! Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
menu()