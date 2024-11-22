# List untuk menyimpan data peminjaman buku
peminjaman_buku = []

def tambah_peminjaman(id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman):
    """Menambah data peminjaman buku baru."""
    peminjaman = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
    peminjaman_buku.append(peminjaman)
    print("Peminjaman buku berhasil ditambahkan!")

def tampilkan_peminjaman():
    """Menampilkan seluruh data peminjaman buku."""
    if peminjaman_buku:
        print("Daftar Peminjaman Buku:")
        for peminjaman in peminjaman_buku:
            print(f"ID Peminjaman: {peminjaman[0]}")
            print(f"Nama Peminjam: {peminjaman[1]}")
            print(f"Judul Buku: {peminjaman[2]}")
            print(f"Tanggal Peminjaman: {peminjaman[3]}")
            print("="*30)
    else:
        print("Belum ada data peminjaman buku.")

def cari_peminjaman(id_peminjaman):
    """Mencari data peminjaman berdasarkan ID."""
    for peminjaman in peminjaman_buku:
        if peminjaman[0] == id_peminjaman:
            return peminjaman
    return None

def update_peminjaman(id_peminjaman, nama_peminjam="", judul_buku="", tanggal_peminjaman=""):
    """Memperbarui data peminjaman berdasarkan ID."""
    peminjaman = cari_peminjaman(id_peminjaman)
    if peminjaman:
        index = peminjaman_buku.index(peminjaman)
        
        # Jika nama_peminjam, judul_buku, atau tanggal_peminjaman kosong, tetap menggunakan nilai lama
        new_peminjaman = (
            peminjaman[0],  # ID tetap sama
            nama_peminjam if nama_peminjam else peminjaman[1],  # Jika kosong, pakai yang lama
            judul_buku if judul_buku else peminjaman[2],  # Jika kosong, pakai yang lama
            tanggal_peminjaman if tanggal_peminjaman else peminjaman[3]  # Jika kosong, pakai yang lama
        )
        
        peminjaman_buku[index] = new_peminjaman
        print("Data peminjaman berhasil diperbarui!")
    else:
        print("ID peminjaman tidak ditemukan.")

def hapus_peminjaman(id_peminjaman):
    """Menghapus data peminjaman berdasarkan ID."""
    peminjaman = cari_peminjaman(id_peminjaman)
    if peminjaman:
        peminjaman_buku.remove(peminjaman)
        print("Peminjaman buku berhasil dihapus!")
    else:
        print("ID peminjaman tidak ditemukan.")

def menu():
    print("===== Menu Perpustakaan =====")
    print("1. Tambah Peminjaman Buku")
    print("2. Tampilkan Semua Peminjaman Buku")
    print("3. Cari Peminjaman Buku")
    print("4. Update Peminjaman Buku")
    print("5. Hapus Peminjaman Buku")
    print("6. Keluar")

def input_data_peminjaman():
    id_peminjaman = input("Masukkan ID Peminjaman: ")
    nama_peminjam = input("Masukkan Nama Peminjam: ")
    judul_buku = input("Masukkan Judul Buku: ")
    tanggal_peminjaman = input("Masukkan Tanggal Peminjaman (DD/MM/YYYY): ")
    return id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman

def Peminjaman():
    while True:
        menu()
        pilihan = input("Pilih menu (1/2/3/4/5/6): ")

        if pilihan == '1':
            print("\n=== Tambah Peminjaman Buku ===")
            id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman = input_data_peminjaman()
            tambah_peminjaman(id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)

        elif pilihan == '2':
            print("\n=== Tampilkan Semua Peminjaman Buku ===")
            tampilkan_peminjaman()

        elif pilihan == '3':
            print("\n=== Cari Peminjaman Buku ===")
            id_peminjaman = input("Masukkan ID Peminjaman yang ingin dicari: ")
            peminjaman = cari_peminjaman(id_peminjaman)
            if peminjaman:
                print(f"ID Peminjaman: {peminjaman[0]}")
                print(f"Nama Peminjam: {peminjaman[1]}")
                print(f"Judul Buku: {peminjaman[2]}")
                print(f"Tanggal Peminjaman: {peminjaman[3]}")
                print("="*30)
            else:
                print("ID peminjaman tidak ditemukan.")

        elif pilihan == '4':
            print("\n=== Update Peminjaman Buku ===")
            id_peminjaman = input("Masukkan ID Peminjaman yang ingin diupdate: ")
            print("Masukkan data yang ingin diperbarui (Kosongkan untuk tidak mengubah):")
            nama_peminjam = input("Nama Peminjam: ")
            judul_buku = input("Judul Buku: ")
            tanggal_peminjaman = input("Tanggal Peminjaman: ")
            update_peminjaman(id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)

        elif pilihan == '5':
            print("\n=== Hapus Peminjaman Buku ===")
            id_peminjaman = input("Masukkan ID Peminjaman yang ingin dihapus: ")
            hapus_peminjaman(id_peminjaman)

        elif pilihan == '6':
            print("Terima kasih! Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

Peminjaman()
