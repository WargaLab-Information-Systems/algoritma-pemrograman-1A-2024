peminjaman_buku = []
buku_tersedia = ["Python Programming", "Data Science Fundamentals", "Machine Learning Basics", "Introduction to AI"]

def read_data_peminjaman():
    if not peminjaman_buku:
        print("Tidak ada data peminjaman.")
    else:
        print("\nData Peminjaman Buku:")
        print("ID | Nama Peminjam | Judul Buku | Tanggal Peminjaman")
        print("-" * 40)
        for peminjaman in peminjaman_buku:
            print(f"{peminjaman[0]} | {peminjaman[1]} | {peminjaman[2]} | {peminjaman[3]}")

def read_data_buku():
    if not buku_tersedia:
        print("Tidak ada buku yang tersedia.")
    else:
        print("\nDaftar Buku Tersedia:")
        print("ID Buku | Judul Buku")
        print("-" * 20)
        for i, judul in enumerate(buku_tersedia, start=1):
            print(f"{i} | {judul}")

def add_buku():
    judul_buku = input("Masukkan Judul Buku yang ingin ditambahkan: ")
    buku_tersedia.append(judul_buku)
    print("Buku berhasil ditambahkan ke daftar buku tersedia.")

def create_data_peminjaman():
    id_peminjaman = len(peminjaman_buku) + 1
    nama_peminjam = input("Masukkan Nama Peminjam: ")
    read_data_buku()
    judul_buku = input("Masukkan Judul Buku yang ingin dipinjam: ")
    
    if judul_buku not in buku_tersedia:
        print("Buku tidak tersedia.")
        return

    tanggal_peminjaman = input("Masukkan Tanggal Peminjaman (DD-MM-YYYY): ")
    peminjaman_buku.append((id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman))
    buku_tersedia.remove(judul_buku) 
    print("Peminjaman berhasil ditambahkan.")

def update_data_peminjaman():
    read_data_peminjaman()
    id_peminjaman = int(input("Masukkan ID Peminjaman yang ingin diupdate: "))
    for i, peminjaman in enumerate(peminjaman_buku):
        if peminjaman[0] == id_peminjaman:

            if peminjaman[2] not in buku_tersedia:
                buku_tersedia.append(peminjaman[2])
            
            nama_peminjam = input("Masukkan Nama Peminjam Baru: ")
            read_data_buku()
            judul_buku = input("Masukkan Judul Buku Baru: ")
            
            if judul_buku not in buku_tersedia:
                print("Buku yang dipilih tidak tersedia.")
                return
            
            tanggal_peminjaman = input("Masukkan Tanggal Peminjaman Baru (DD-MM-YYYY): ")
            
            
            buku_tersedia.remove(judul_buku)
            
            
            peminjaman_buku[i] = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
            print("Data peminjaman berhasil diupdate.")
            return
    print("ID tidak ditemukan.")

def delete_data_peminjaman():
    read_data_peminjaman()
    id_peminjaman = int(input("Masukkan ID Peminjaman yang ingin dihapus: "))
    for i, peminjaman in enumerate(peminjaman_buku):
        if peminjaman[0] == id_peminjaman:
            
            if peminjaman[2] not in buku_tersedia:
                buku_tersedia.append(peminjaman[2])
            
            
            peminjaman_buku.pop(i)
            print("Data peminjaman berhasil dihapus.")
            return
    print("ID tidak ditemukan.")

while True:
    print("\nSistem Peminjaman Buku Perpustakaan")
    print("1. Tambah Peminjaman")
    print("2. Lihat Data Peminjaman")
    print("3. Update Data Peminjaman")
    print("4. Hapus Data Peminjaman")
    print("5. Lihat Daftar Buku Tersedia")
    print("6. Tambah Buku Baru")
    print("7. Keluar")

    pilihan = input("Pilih menu (1-7): ")

    if pilihan == "1":
        create_data_peminjaman()
    elif pilihan == "2":
        read_data_peminjaman()
    elif pilihan == "3":
        update_data_peminjaman()
    elif pilihan == "4":
        delete_data_peminjaman()
    elif pilihan == "5":
        read_data_buku()
    elif pilihan == "6":
        add_buku()
    elif pilihan == "7":
        print("Anda keluar dari program. Terima kasih telah mengunjungi perpustakaan kami!")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih lagi.")
