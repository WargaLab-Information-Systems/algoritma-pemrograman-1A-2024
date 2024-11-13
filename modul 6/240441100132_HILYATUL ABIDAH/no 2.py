def tambah_peminjaman(peminjaman_list):
    print("Masukkan Data Peminjaman Buku:")
    id_peminjaman = input("Tambahkan ID Peminjaman: ")
    nama_peminjam = input("Nama kamu sebagai peminjam: ")
    judul_buku = input("Judul Buku yang dipinjam: ")
    tanggal_peminjaman = input("Tanggal Peminjaman buku (dd/mm/yyyy): ")

    peminjaman = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
    peminjaman_list.append(peminjaman)
    print("Data peminjaman berhasil ditambahkan!")

def tampilkan_peminjaman(peminjaman_list):
    if len(peminjaman_list) == 0:
        print("Tidak ada data peminjaman.")
    else:
        print("Daftar Peminjaman Buku:")
        for peminjaman in peminjaman_list:
            print(f"ID Peminjaman: {peminjaman[0]}, Nama Peminjam: {peminjaman[1]}, Judul Buku yang dipinjam: {peminjaman[2]}, Tanggal Peminjaman buku: {peminjaman[3]}")

def cari_peminjaman(peminjaman_list, id_peminjaman, nama_peminjam=None):
    for peminjaman in peminjaman_list:
        if peminjaman[0] == id_peminjaman and peminjaman[1] == nama_peminjam:
            print(f"Data Peminjaman ditemukan: ID Peminjaman: {peminjaman[0]}, Nama Peminjam: {peminjaman[1]}, Judul Buku: {peminjaman[2]}, Tanggal Peminjaman: {peminjaman[3]}")
            return
    
    print("Data Peminjaman tidak ditemukan.")

def update_peminjaman(peminjaman_list, id_peminjaman, nama_peminjam):
    for i in range(len(peminjaman_list)):
        peminjaman = peminjaman_list[i]
        if peminjaman[0] == id_peminjaman and peminjaman[1] == nama_peminjam:
            print(f"Data Peminjaman yang akan diperbarui: ID Peminjaman: {peminjaman[0]}, Nama Peminjam: {peminjaman[1]}, Judul Buku: {peminjaman[2]}, Tanggal Peminjaman: {peminjaman[3]}")
            
            nama_peminjam_baru = input("Nama Peminjam (baru): ")
            judul_buku_baru = input("Judul Buku (baru): ")
            tanggal_peminjaman_baru = input("Tanggal Peminjaman (baru) (dd/mm/yyyy): ")
            
            peminjaman_list[i] = (id_peminjaman, nama_peminjam_baru, judul_buku_baru, tanggal_peminjaman_baru)
            print("Data peminjaman berhasil diperbarui!")
            return
    print("Data Peminjaman tidak ditemukan.")

def delete_peminjaman(peminjaman_list, id_peminjaman, nama_peminjam):
    for i in range(len(peminjaman_list)):
        peminjaman = peminjaman_list[i]
        if peminjaman[0] == id_peminjaman and peminjaman[1] == nama_peminjam:
            peminjaman_list.pop(i)
            print("Data peminjaman berhasil dihapus!")
            return
    print("Data Peminjaman tidak ditemukan.")

def menu():
    peminjaman_list = []  
    while True:
        print("===== Sistem Peminjaman Buku Perpustakaan =====")
        print("1. Tambah Peminjaman Buku")
        print("2. Tampilkan Semua Peminjaman")
        print("3. Cari Peminjaman Berdasarkan ID dan Nama")
        print("4. Update Peminjaman Buku Berdasarkan ID dan Nama")
        print("5. Hapus Peminjaman Buku Berdasarkan ID dan Nama")
        print("6. Keluar")
        
        pilihan = input("Pilih menu (1-6): ")
        
        if pilihan == '1':
            tambah_peminjaman(peminjaman_list)
        elif pilihan == '2':
            tampilkan_peminjaman(peminjaman_list)
        elif pilihan == '3':
            id_peminjaman = input("Masukkan ID Peminjaman yang dicari: ")
            nama_peminjam = input("Masukkan Nama Peminjam: ")
            cari_peminjaman(peminjaman_list, id_peminjaman, nama_peminjam)
        elif pilihan == '4':
            id_peminjaman = input("Masukkan ID Peminjaman yang akan diperbarui: ")
            nama_peminjam = input("Masukkan Nama Peminjam: ")
            update_peminjaman(peminjaman_list, id_peminjaman, nama_peminjam)
        elif pilihan == '5':
            id_peminjaman = input("Masukkan ID Peminjaman yang akan dihapus: ")
            nama_peminjam = input("Masukkan Nama Peminjam: ")
            delete_peminjaman(peminjaman_list, id_peminjaman, nama_peminjam)
        elif pilihan == '6':
            print("Terima kasih telah menggunakan sistem peminjaman buku.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1-6.")

menu()

#agar penghapusan dan pencarian menggunakan nama dan id, apabilamenggunakan id yg sama maka semua data akan tetap dikeluarkan