data_peminjaman = []

while True:
    print("Sistem Peminjaman Buku Perpustakaan")
    print("1. Tambah peminjaman (Create)")
    print("2. Tampilkan peminjaman (Read)")
    print("3. Update peminjaman")
    print("4. Hapus peminjaman (Delete)")
    print("5. Keluar")
    
    pilihan = input("Pilih menu peminjaman (1-5): ")

    if pilihan == "1":
        print("Tambah peminjaman buku")
        id_peminjaman = input("Masukkan ID peminjaman: ")
        nama_peminjam = input("Masukkan nama peminjam: ")
        judul_buku = input("Masukkan judul buku yang dipinjam: ")
        tanggal_peminjaman = input("Masukkan tanggal peminjaman buku: ")

        peminjaman = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
        data_peminjaman.append(peminjaman)
        print("Peminjaman buku berhasil ditambahkan")
    
    elif pilihan == "2":
        print("Daftar peminjaman buku")
        if not data_peminjaman:
            print("Tidak ada data peminjaman.")
        else:
            for peminjaman in data_peminjaman:
                print(f"ID Peminjaman: {peminjaman[0]}, Nama Peminjam: {peminjaman[1]}, Judul Buku: {peminjaman[2]}, Tanggal Peminjaman: {peminjaman[3]}")
        print()
    
    elif pilihan == "3":
        id_update = input("Masukkan ID yang ingin di update: ")

        for i in range(len(data_peminjaman)):
            if data_peminjaman[i][0] == id_update:
                ketemu = True
                print("Data Peminjaman Ditemukan:")
                print(f"ID Peminjaman: {data_peminjaman[i][0]}, Nama Peminjam: {data_peminjaman[i][1]}, Judul Buku: {data_peminjaman[i][2]}, Tanggal Peminjaman: {data_peminjaman[i][3]}")
                
                nama_peminjam = input("Nama Peminjam baru: ")
                judul_buku = input("Judul Buku baru: ")
                tanggal_peminjaman = input("Tanggal Peminjaman baru (DD-MM-YYYY): ")
                
                data_peminjaman[i] = (id_update, nama_peminjam, judul_buku, tanggal_peminjaman)
                print("Data peminjaman berhasil diupdate")
                break
        
        if not ketemu:
            print("ID Peminjaman tidak ditemukan")
    
    elif pilihan == "4":
        id_hapus = input("Masukkan ID Peminjaman yang ingin dihapus: ")
        ketemu = False
        
        for i in range(len(data_peminjaman)):
            if data_peminjaman[i][0] == id_hapus:
                ketemu = True
                data_peminjaman.pop(i)
                print("Data peminjaman berhasil dihapus")
                break
        
        if not ketemu:
            print("ID peminjaman tidak ditemukan")
    
    elif pilihan == '5':
        print("Terima kasih! Program selesai.")
        break
    
    else:
        print("Pilihan tidak valid. Silakan coba lagi")