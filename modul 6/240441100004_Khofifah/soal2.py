def tambah_peminjaman(data_peminjaman):
    id_peminjaman = input("Masukkan ID Peminjaman: ")
    nama_peminjam = input("Masukkan Nama Peminjam: ")
    judul_buku = input("Masukkan Judul Buku: ")
    tanggal_peminjaman = input("Masukkan Tanggal Peminjaman (dd-mm-yyyy): ")
    
    peminjaman_baru = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
    data_peminjaman.append(peminjaman_baru)
    print("Data peminjaman berhasil ditambahkan!")

def tampilkan_peminjaman(data_peminjaman):
    if data_peminjaman:
        print("Data Peminjaman Buku:")
        for peminjaman in data_peminjaman:
            print(f"ID: {peminjaman[0]}, Nama Peminjam: {peminjaman[1]}, Judul Buku: {peminjaman[2]}, Tanggal Peminjaman: {peminjaman[3]}")
    else:
        print("Tidak ada data peminjaman yang tersedia.")

def perbarui_peminjaman(data_peminjaman):
    id_peminjaman = input("Masukkan ID Peminjaman yang ingin diperbarui: ")
    for i, peminjaman in enumerate(data_peminjaman):
        if peminjaman[0] == id_peminjaman:
            nama_peminjam = input("Masukkan Nama Peminjam Baru: ")
            judul_buku = input("Masukkan Judul Buku Baru: ")
            tanggal_peminjaman = input("Masukkan Tanggal Peminjaman Baru (dd-mm-yyyy): ")

            data_peminjaman[i] = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
            print("Data peminjaman berhasil diperbarui!")
            return
    print("Data peminjaman dengan ID tersebut tidak ditemukan.")

def hapus_peminjaman(data_peminjaman):
    id_peminjaman = input("Masukkan ID Peminjaman yang ingin dihapus: ")
    for i, peminjaman in enumerate(data_peminjaman):
        if peminjaman[0] == id_peminjaman:
            del data_peminjaman[i]
            print("Data peminjaman berhasil dihapus!")
            return
    print("Data peminjaman dengan ID tersebut tidak ditemukan.")

def main():
    data_peminjaman = []  # Daftar peminjaman berada di sini
    while True:
        print("\nSistem Peminjaman Buku Perpustakaan")
        print("1. Tambah Peminjaman")
        print("2. Tampilkan Semua Peminjaman")
        print("3. Perbarui Peminjaman")
        print("4. Hapus Peminjaman")
        print("5. Keluar")
        
        pilihan = input("Pilih opsi (1/2/3/4/5): ")
        
        if pilihan == "1":
            tambah_peminjaman(data_peminjaman)
        elif pilihan == "2":
            tampilkan_peminjaman(data_peminjaman)
        elif pilihan == "3":
            perbarui_peminjaman(data_peminjaman)
        elif pilihan == "4":
            hapus_peminjaman(data_peminjaman)
        elif pilihan == "5":
            print("\nTerima kasih telah menggunakan sistem peminjaman buku.")
            break
        else:
            print("\nPilihan tidak valid. Silakan coba lagi.")

# Menjalankan program utama
if __name__ == "__main__":
    main()
