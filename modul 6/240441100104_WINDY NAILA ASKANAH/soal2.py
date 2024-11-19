peminjaman_buku = []

def create_peminjaman():
    peminjaman = (
        input("Masukkan ID Peminjaman: "),
        input("Masukkan Nama Peminjam: "),
        input("Masukkan Judul Buku: "),
        input("Masukkan Tanggal Peminjaman (YYYY/MM/DD): ")
    )
    peminjaman_buku.append(peminjaman)
    print("Peminjaman buku berhasil ditambahkan.")

def read_peminjaman():
    if not peminjaman_buku:
        print("Tidak ada data peminjaman.")
    else:
        for i in peminjaman_buku:
            print(f"ID: {i[0]}, Nama: {i[1]}, Judul: {i[2]}, Tanggal: {i[3]}")

def update_peminjaman():
    id_peminjaman = input("Masukkan ID Peminjaman yang ingin diupdate: ")
    for i, p in enumerate(peminjaman_buku):
        if p[0] == id_peminjaman:
            peminjaman_buku[i] = (
                id_peminjaman,
                input("Masukkan Nama Peminjam baru: "),
                input("Masukkan Judul Buku baru: "),
                input("Masukkan Tanggal Peminjaman baru (YYYY/MM/DD): ")
            )
            print("Data peminjaman berhasil diperbarui.")
            return
    print("ID peminjaman tidak ditemukan.")

def delete_peminjaman():
    id_peminjaman = input("Masukkan ID Peminjaman yang ingin dihapus: ")
    for i, p in enumerate(peminjaman_buku):
        if p[0] == id_peminjaman:
            del peminjaman_buku[i]
            print("Data peminjaman berhasil dihapus.")
            return
    print("ID peminjaman tidak ditemukan.")

def main():
    functions = [
        create_peminjaman, 
        read_peminjaman,    
        update_peminjaman,  
        delete_peminjaman,  
    ]
    
    while True:
        print("\n**** Sistem Peminjaman Buku ****")
        print("1. Tambah Peminjaman\n2. Tampilkan Peminjaman\n3. Update Peminjaman\n4. Hapus Peminjaman\n5. Keluar")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan in {'1', '2', '3', '4'}:
            functions[int(pilihan) - 1]()  
        elif pilihan == '5':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()