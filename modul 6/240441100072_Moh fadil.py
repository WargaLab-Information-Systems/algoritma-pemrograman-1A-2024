#SOAL NO 1
data_karyawan = []

def tambah_karyawan(nip, nama, alamat, departemen, jabatan):
    karyawan = (nip, nama, alamat, departemen, jabatan)
    data_karyawan.append(karyawan)
    print(f"Data karyawan '{nama}' berhasil ditambahkan.")

def tampilkan_data_karyawan():
    if data_karyawan == False:
        print("Tidak ada data karyawan.")
        return
    print("Data Karyawan:")
    for karyawan in data_karyawan:
        print(f"NIP: {karyawan[0]}, Nama: {karyawan[1]}, Alamat: {karyawan[2]}, Departemen: {karyawan[3]}, Jabatan: {karyawan[4]}")

def cari_karyawan(atribut, nilai):
    hasil_cari = []
    for karyawan in data_karyawan:
        if nilai in [str(item) for item in karyawan]:
            hasil_cari.append(karyawan)
    return hasil_cari

print("=== Sistem Manajemen Data Karyawan ===")
while True:
    print("1. Tambah Karyawan")
    print("2. Tampilkan Data Karyawan")
    print("3. Cari Karyawan")
    print("4. Keluar")
    pilihan = input("Pilih menu (1-4): ")

    if pilihan == '1':
        if len(data_karyawan) >= 5:
            print("Data karyawan sudah mencapai 5, tidak bisa menambah lagi.")
            continue
        nip = input("Masukkan NIP: ")
        nama = input("Masukkan Nama: ")
        alamat = input("Masukkan Alamat: ")
        departemen = input("Masukkan Departemen: ")
        jabatan = input("Masukkan Jabatan: ")
        tambah_karyawan(nip, nama, alamat, departemen, jabatan)
    elif pilihan == '2':
        tampilkan_data_karyawan()
    elif pilihan == '3':
        atribut = input("Cari berdasarkan (NIP, Nama, Alamat, Departemen, Jabatan): ")
        nilai = input("Masukkan nilai yang dicari: ")
        hasil = cari_karyawan(atribut, nilai)
        if hasil:
            print("Hasil Pencarian:")
            for karyawan in hasil:
                print(f"NIP: {karyawan[0]}, Nama: {karyawan[1]}, Alamat: {karyawan[2]}, Departemen: {karyawan[3]}, Jabatan: {karyawan[4]}")
        else:
            print("Tidak ditemukan karyawan dengan atribut tersebut.")
    elif pilihan == '4':
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")




#SOAL NO 2
peminjaman_buku = []

def create_peminjaman(id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman):
    peminjaman = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
    peminjaman_buku.append(peminjaman)
    print(f"Peminjaman buku '{judul_buku}' berhasil ditambahkan.")

def read_peminjaman():
    if not peminjaman_buku:
        print("Tidak ada data peminjaman.")
        return
    print("Data Peminjaman Buku:")
    for peminjaman in peminjaman_buku:
        print(f"ID Peminjaman: {peminjaman[0]}, Nama Peminjam: {peminjaman[1]}, Judul Buku: {peminjaman[2]}, Tanggal Peminjaman: {peminjaman[3]}")

def update_peminjaman(id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman):
    for i in range(len(peminjaman_buku)):
        if peminjaman_buku[i][0] == id_peminjaman:
            peminjaman_buku[i] = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
            print(f"Peminjaman dengan ID {id_peminjaman} berhasil diupdate.")
            return
    print(f"Tidak ditemukan peminjaman dengan ID {id_peminjaman}.")

def delete_peminjaman(id_peminjaman):
    for i in range(len(peminjaman_buku)):
        if peminjaman_buku[i][0] == id_peminjaman:
            del peminjaman_buku[i]
            print(f"Peminjaman dengan ID {id_peminjaman} berhasil dihapus.")
            return
    print(f"Tidak ditemukan peminjaman dengan ID {id_peminjaman}.")

while True:
    print("\n=== Sistem Peminjaman Buku Perpustakaan ===")
    print("1. Tambah Peminjaman")
    print("2. Lihat Peminjaman")
    print("3. Update Peminjaman")
    print("4. Hapus Peminjaman")
    print("5. Keluar")
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == '1':
        id_peminjaman = input("Masukkan ID Peminjaman: ")
        nama_peminjam = input("Masukkan Nama Peminjam: ")
        judul_buku = input("Masukkan Judul Buku: ")
        tanggal_peminjaman = input("Masukkan Tanggal Peminjaman (YYYY-MM-DD): ")
        create_peminjaman(id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
    elif pilihan == '2':
        read_peminjaman()
    elif pilihan == '3':
        id_peminjaman = input("Masukkan ID Peminjaman yang akan diupdate: ")
        nama_peminjam = input("Masukkan Nama Peminjam baru: ")
        judul_buku = input("Masukkan Judul Buku baru: ")
        tanggal_peminjaman = input("Masukkan Tanggal Peminjaman baru (YYYY-MM-DD): ")
        update_peminjaman(id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
    elif pilihan == '4':
        id_peminjaman = input("Masukkan ID Peminjaman yang akan dihapus: ")
        delete_peminjaman(id_peminjaman)
    elif pilihan == '5':
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")



#SOAL NO 3
data_barang = []

def tambah_barang(nama_barang, id_barang, prioritas):
    barang = (nama_barang, id_barang, prioritas)

    if prioritas == "Darurat":
        data_barang.insert(0, barang)  
    elif prioritas == "Biasa":
        for i in range(len(data_barang)):
            if data_barang[i][2] == "Non-Darurat":
                data_barang.append(barang)
                return
        data_barang.append(barang) 
    elif prioritas == "Non-Darurat":

        data_barang.append(barang)

def tampilkan_data_barang():
    if not data_barang:
        print("Tidak ada data barang.")
        return
    print("\nData Barang:")
    for barang in data_barang:
        print(f"Nama Barang: {barang[0]}, ID Barang: {barang[1]}, Prioritas: {barang[2]}")

while True:
    nama_barang = input("Masukkan Nama Barang: ")
    id_barang = input("Masukkan ID Barang: ")
    prioritas = input("Pilih Tingkat Prioritas (Darurat, Biasa, Non-Darurat): ")

    if prioritas not in ["Darurat", "Biasa", "Non-Darurat"]:
        print("Prioritas tidak valid. Silakan pilih antara Darurat, Biasa, atau Non-Darurat.")
        continue

    tambah_barang(nama_barang, id_barang, prioritas)
    tampilkan_data_barang()

    lagi = input("Apakah Anda ingin menambah data barang lagi? (ya/tidak): ")
    if lagi != 'ya':
        print("Terima kasih! Program selesai.")
        break
