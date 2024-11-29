# 2. struktur peminjaman buku di perpustakaan
# List untuk menyimpan data dari sebuah tuple yang nantinya tuple tersebut berisi 4 elemen
peminjaman_buku = []

# Fungsi untuk menambah peminjaman buku (Create)
def tambah_peminjaman():
    id = input("Masukkan ID Peminjaman: ")
    nama = input("Masukkan Nama Peminjam: ")
    judul = input("Masukkan Judul Buku: ")
    tanggal = input("Masukkan Tanggal Peminjaman (hh-bb-tttt): ")
    # Menyimpan data ke dalam list sebagai tuple
    peminjaman_buku.append((id, nama, judul, tanggal))
    print("Peminjaman berhasil ditambahkan.")

# Fungsi untuk menampilkan peminjaman buku
def tampilkan_peminjaman():
    if len(peminjaman_buku) == 0:
        print("Daftar kosong.")
    else:
        print("\nDAFTAR PEMINJAMAN BUKU:")
        for peminjaman in peminjaman_buku:
            print(f"ID Peminjaman: {peminjaman[0]}   Nama: {peminjaman[1]}     Judul Buku: {peminjaman[2]}     Tanggal: {peminjaman[3]}")

# Fungsi untuk menghapus peminjaman berdasarkan ID
def hapus_peminjaman(id_peminjam):
    # Mencari peminjaman berdasarkan ID dan menghapus langsung jika ditemukan
    for peminjaman in peminjaman_buku:
        if peminjaman[0] == id_peminjam:  # Peminjaman[0] adalah ID
            peminjaman_buku.remove(peminjaman)
            print(f"Peminjaman dengan ID {id_peminjam} berhasil dihapus.")
            return
    print(f"Peminjaman dengan ID {id_peminjam} tidak ditemukan.")

# Fungsi untuk memperbarui data peminjaman
def perbarui_data(id_peminjam):
    # Mencari peminjaman berdasarkan ID dan langsung memperbarui data jika ditemukan
    for i in range(len(peminjaman_buku)):
        if peminjaman_buku[i][0] == id_peminjam:  # Peminjaman[0] adalah ID
            print(f"\nData yang ingin diperbarui:")
            print(f"ID: {peminjaman_buku[i][0]}   Nama: {peminjaman_buku[i][1]}   Judul Buku: {peminjaman_buku[i][2]}   Tanggal: {peminjaman_buku[i][3]}")
            
            print("\nPilih data yang ingin diperbarui")
            print("a. ID Peminjaman")
            print("b. Nama Peminjam")
            print("c. Judul Buku")
            print("d. Tanggal Peminjaman")
            print("e. Semua Data")
            
            pilihan = input("Pilih (a/b/c/d/e): ")
            
            if pilihan == "a":
                id_baru = input("Masukkan ID Peminjaman baru: ")
                peminjaman_buku[i] = (id_baru, peminjaman_buku[i][1], peminjaman_buku[i][2], peminjaman_buku[i][3])
            elif pilihan == "b":
                nama_baru = input("Masukkan Nama Peminjam baru: ")
                peminjaman_buku[i] = (peminjaman_buku[i][0], nama_baru, peminjaman_buku[i][2], peminjaman_buku[i][3])
            elif pilihan == "c":
                judul_baru = input("Masukkan Judul Buku baru: ")
                peminjaman_buku[i] = (peminjaman_buku[i][0], peminjaman_buku[i][1], judul_baru, peminjaman_buku[i][3])
            elif pilihan == "d":
                tanggal_baru = input("Masukkan Tanggal Peminjaman baru: ")
                peminjaman_buku[i] = (peminjaman_buku[i][0], peminjaman_buku[i][1], peminjaman_buku[i][2], tanggal_baru)
            elif pilihan == "e":
                id_baru = input("Masukkan ID Peminjaman baru: ")
                nama_baru = input("Masukkan Nama Peminjam baru: ")
                judul_baru = input("Masukkan Judul Buku baru: ")
                tanggal_baru = input("Masukkan Tanggal Peminjaman baru: ")
                peminjaman_buku[i] = (id_baru, nama_baru, judul_baru, tanggal_baru)
            else:
                print("Pilihan tidak valid.")
            
            print("Data peminjaman berhasil diperbarui.")
            return
    print(f"ID Peminjaman {id_peminjam} tidak ditemukan.")

# Menu untuk memilih operasi CRUD
while True:
    print("\nSISTEM PEMINJAMAN BUKU PERPUSTAKAAN")
    print("1. Tambah Peminjaman Buku")
    print("2. Perbarui Data Peminjaman")
    print("3. Hapus Peminjaman")
    print("4. Tampilkan Semua Peminjaman")
    print("5. Keluar")
    pilih = input("Pilih menu (1-5): ")
    
    if pilih == "1":
        tambah_peminjaman()
    elif pilih == "2":
        f = input("Masukkan ID Peminjaman yang ingin diperbarui: ")
        perbarui_data(f)
    elif pilih == "3":
        f = input("Masukkan ID Peminjaman yang ingin dihapus: ")
        hapus_peminjaman(f)
    elif pilih == "4":
        tampilkan_peminjaman()
    elif pilih == "5":
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih lagi.")