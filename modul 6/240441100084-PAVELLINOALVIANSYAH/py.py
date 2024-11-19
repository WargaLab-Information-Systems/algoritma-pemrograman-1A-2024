# 1
data_karyawan = []

def tambah_karyawan(nip, nama, alamat, departemen, jabatan):
    karyawan = (nip, nama, alamat, departemen, jabatan)
    data_karyawan.append(karyawan)
    print("Data karyawan berhasil ditambahkan.")

def tambah_banyak_karyawan():
    for i in range(5):
        print(f"Menambah Karyawan ke-{i+1}:")
        nip = input("NIP: ")
        nama = input("Nama: ")
        alamat = input("Alamat: ")
        departemen = input("Departemen: ")
        jabatan = input("Jabatan: ")
        tambah_karyawan(nip, nama, alamat, departemen, jabatan)

def tampilkan_karyawan():
    if not data_karyawan:
        print("Belum ada data karyawan.")
    else:
        print("Daftar Karyawan:")
        for karyawan in data_karyawan:
            print(f"NIP: {karyawan[0]}, Nama: {karyawan[1]}, Alamat: {karyawan[2]}, Departemen: {karyawan[3]}, Jabatan: {karyawan[4]}")

def cari_karyawan(key, value):
    hasil_cari = []
    for karyawan in data_karyawan:
        if (key == "nip" and karyawan[0] == value) or \
           (key == "nama" and karyawan[1].lower() == value.lower()) or \
           (key == "alamat" and karyawan[2].lower() == value.lower()) or \
           (key == "departemen" and karyawan[3].lower() == value.lower()) or \
           (key == "jabatan" and karyawan[4].lower() == value.lower()):
            hasil_cari.append(karyawan)
    return hasil_cari

def main():
    while True:
        print("=== Menu Utama ===")
        print("1. --Tambah Data Karyawan--")
        print("2. --Tambah 5 Karyawan Sekaligus--")
        print("3. --Tampilkan Semua Karyawan--")
        print("4. --Cari Karyawan Berdasarkan Atribut--")
        print("5. --Keluar--")
        
        pilihan = input("Pilih menu (1/2/3/4/5): ")
        
        if pilihan == "1":
            nip = input("NIP: ")
            nama = input("Nama: ")
            alamat = input("Alamat: ")
            departemen = input("Departemen: ")
            jabatan = input("Jabatan: ")
            tambah_karyawan(nip, nama, alamat, departemen, jabatan)
        
        elif pilihan == "2":
            tambah_banyak_karyawan()
        
        elif pilihan == "3":
            tampilkan_karyawan()
        
        elif pilihan == "4":
            print("Pencarian Data Karyawan")
            print("Atribut pencarian: nip, nama, alamat, departemen, jabatan")
            key = input("Masukkan atribut yang dicari: ").lower()
            value = input("Masukkan nilai untuk pencarian: ")
            
            hasil = cari_karyawan(key, value)
            if hasil:
                print("Hasil Pencarian:")
                for karyawan in hasil:
                    print(f"NIP: {karyawan[0]}, Nama: {karyawan[1]}, Alamat: {karyawan[2]}, Departemen: {karyawan[3]}, Jabatan: {karyawan[4]}")
            else:
                print("Data karyawan tidak ditemukan dengan kriteria tersebut.")
        
        elif pilihan == "5":
            print("Anda keluar dari program.")
            break
        
        else:
            print("Pilihan tidak valid, silakan pilih menu yang tersedia.")

main()

# 2
data_peminjaman = []

def tambah_peminjaman():
    id_peminjaman = input("ID Peminjaman: ")
    for peminjaman in data_peminjaman:
        if peminjaman['id_peminjaman'] == id_peminjaman:
            print("ID peminjaman sudah ada. Gunakan ID lain.")
            return
    
    nama_peminjam = input("Nama Peminjam: ")
    judul_buku = input("inti Judul Buku: ")
    tanggal_peminjaman = input("Tanggal Peminjaman (DD-MM-YYYY): ")
    
    peminjaman = {
        'id_peminjaman': id_peminjaman,
        'nama_peminjam': nama_peminjam,
        'judul_buku': judul_buku,
        'tanggal_peminjaman': tanggal_peminjaman
    }
    
    data_peminjaman.append(peminjaman)
    print("Data peminjaman berhasil ditambahkan.")

def tampilkan_peminjaman():
    if not data_peminjaman:
        print("Belum ada data peminjaman.")
    else:
        print("Daftar Peminjaman Buku:")
        for peminjaman in data_peminjaman:
            print(f"ID: {peminjaman['id_peminjaman']}, Nama Peminjam: {peminjaman['nama_peminjam']}, "
                  f"Judul Buku: {peminjaman['judul_buku']}, Tanggal: {peminjaman['tanggal_peminjaman']}")

def update_peminjaman():
    id_peminjaman = input("Masukkan ID peminjaman yang akan diupdate: ")
    for peminjaman in data_peminjaman:
        if peminjaman['id_peminjaman'] == id_peminjaman:
            print("Masukkan data baru:")
            nama_peminjam = input("Nama Peminjam: ")
            judul_buku = input("Judul Buku: ")
            tanggal_peminjaman = input("Tanggal Peminjaman (DD-MM-YYYY): ")

            peminjaman['nama_peminjam'] = nama_peminjam
            peminjaman['judul_buku'] = judul_buku
            peminjaman['tanggal_peminjaman'] = tanggal_peminjaman
            print("Data peminjaman berhasil diperbarui.")
            return
    print("ID peminjaman tidak ditemukan.")

def hapus_peminjaman():
    id_peminjaman = input("Masukkan ID peminjaman yang akan dihapus: ")
    for peminjaman in data_peminjaman:
        if peminjaman['id_peminjaman'] == id_peminjaman:
            data_peminjaman.remove(peminjaman)
            print("Data peminjaman berhasil dihapus.")
            return
    print("ID peminjaman tidak ditemukan.")

def main():
    while True:
        print("=== Menu Sistem Peminjaman Buku ===")
        print("1. Tambah Peminjaman")
        print("2. Tampilkan Semua Peminjaman")
        print("3. Update Peminjaman")
        print("4. Hapus Peminjaman")
        print("5. Keluar")

        pilihan = input("Pilih menu (1/2/3/4/5): ")

        if pilihan == "1":
            tambah_peminjaman()

        elif pilihan == "2":
            tampilkan_peminjaman()

        elif pilihan == "3":
            update_peminjaman()

        elif pilihan == "4":
            hapus_peminjaman()

        elif pilihan == "5":
            print(" anda Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

main()


# 3
barang_list = {
    'darurat': [],
    'biasa': [],
    'non-darurat': []
}

def tambah_barang():
    nama_barang = input("Nama Barang: ")
    id_barang = input("ID Barang: ")
    prioritas = input("Tingkat Prioritas (Darurat/Biasa/Non-Darurat): ").lower()

    while prioritas not in ['darurat', 'biasa', 'non-darurat']:
        print("Prioritas tidak valid. Harap pilih Darurat, Biasa, atau Non-Darurat.")
        prioritas = input("Tingkat Prioritas (Darurat/Biasa/Non-Darurat): ").lower()

    barang = (id_barang, nama_barang)
    barang_list[prioritas].append(barang)

    print("Barang berhasil ditambahkan!")#

def tampilkan_barang():
    if not any(barang_list.values()):
        print("Belum ada barang yang ditambahkan.")
    else:
        print("Daftar Barang yang Dikirim:")
        for prioritas, barang_list_prio in barang_list.items():
            if barang_list_prio:
                print(f"{prioritas.capitalize()}:")
                for barang in barang_list_prio:
                    print(f"ID Barang: {barang[0]}, Nama Barang: {barang[1]}")

def main():
    while True:
        tambah_barang()

        tampilkan_barang()

        lagi = input("Apakah Anda ingin menambahkan barang lain? (ya/tidak): ").lower()
        if lagi != "ya":
            print("Terima kasih!!!!!!!")
            break

main()
