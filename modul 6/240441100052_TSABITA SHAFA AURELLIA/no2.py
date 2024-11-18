# soal no 2
data = []  # data  list kosong yang akan digunakan untuk menyimpan informasi peminjaman buku
            # Setiap peminjaman akan disimpan sebagai dictionary di dalam list ini.

def daftar_buku():  #  Fungsi ini menampilkan daftar buku yang tersedia untuk dipinjam
    print("===== DAFTAR BUKU =====")
    print("1. BAHASA ARAB")
    print("2. IPS")
    print("3. BUKU NOVEL")
    print("4. SASTRA INDO")

def pilih_buku():  # Fungsi ini meminta pengguna untuk memilih buku, memasukkan nama peminjam, dan tanggal pinjam.
    while True:     # Menggunakan while True untuk terus meminta input hingga pengguna memilih pilihan yang valid.
        pilih = int(input("Silahkan pilih buku : "))
        nama = input("Nama peminjam : ")
        tanggal = input("Tanggal Pinjam (DD/MM/YYYY) : ")
        if pilih == 1:
            judul = "BAHASA ARAB"  # Berdasarkan pilihan pengguna, program menetapkan judul dan id_buku sesuai dengan buku yang dipilih.
            id_buku = 1234
            break
        elif pilih == 2:
            judul = "IPS"
            id_buku = 2345
            break
        elif pilih == 3:
            judul = "BUKU NOVEL"
            id_buku = 3456
            break
        elif pilih == 4:
            judul = "SASTRA INDO"
            id_buku = 4567
            break
        else:
            print("Invalid")
            continue
    
    peminjaman = {"nama": nama, "id_buku": id_buku, "judul": judul, "tanggal": tanggal}
    data.append(peminjaman) # Setelah mendapatkan semua informasi, data peminjaman disimpan dalam dictionary dan ditambahkan ke list data.
    return peminjaman

def edit_buku(): # Fungsi ini memeriksa apakah ada data peminjaman. Jika tidak ada, akan menampilkan pesan.
    if not data:
        print("Tidak ada data yang dapat diubah.....\n")
        return
    
    print("===== DATA PEMINJAMAN =====")
    for i in range(len(data)): # untuk menghitung elemen
        peminjaman = data[i]
        print(f"{i + 1}. Nama: {peminjaman['nama']}, Judul Buku: {peminjaman['judul']}, Tanggal Pinjam: {peminjaman['tanggal']}")
    
    pilihan = input("Pilih nomer yang ingin diubah : ") # Meminta pengguna untuk memilih peminjaman yang ingin diubah
    if not pilihan.isdigit() or int(pilihan) < 1 or int(pilihan) > len(data):
        print("Nomer tidak valid.")
        return
    
    nama_baru = input("Masukkan nama baru : ")  # validasi pilihan
    pilihan = int(pilihan)                      # meminta nama baru dan memilih buku baru

    daftar_buku()
    pilih_baru = int(input("Silahkan pilih buku baru : "))
    if pilih_baru == 1:
        judul_baru = "BAHASA ARAB"
        id_buku_baru = 1234
    elif pilih_baru == 2:
        judul_baru = "IPS"
        id_buku_baru = 2345
    elif pilih_baru == 3:
        judul_baru = "BUKU NOVEL"
        id_buku_baru = 3456
    elif pilih_baru == 4:
        judul_baru = "SASTRA INDO"
        id_buku_baru = 4567
    else:
        print("Invalid")
        return

    data[pilihan - 1]["nama"] = nama_baru
    data[pilihan - 1]["judul"] = judul_baru
    data[pilihan - 1]["id_buku"] = id_buku_baru
    print("\nBerhasil mengubah...\n")

def remove_buku():  # memeriksa data yang dapat di hapus
    if not data:
        print("Tidak ada data yang dapat dihapus.")
        return
    
    print("===== DATA PEMINJAMAN =====") # Menampilkan semua data peminjaman yang ada
    for i in range(len(data)):            # Pengguna dapat memilih nomor peminjaman yang ingin diubah
        peminjaman = data[i]
        print(f"{i + 1}. Nama: {peminjaman['nama']}, Judul Buku: {peminjaman['judul']}, Tanggal Pinjam: {peminjaman['tanggal']}")
    
    pilihan = input("Pilih nomer yang ingin dihapus : ")
    if not pilihan.isdigit() or int(pilihan) < 1 or int(pilihan) > len(data): # digunakan untuk memeriksa apakah semua karakter dalam string tersebut adalah digit (angka)
        print("Nomer tidak valid.")
        return
    pilihan = int(pilihan)  #Meminta pengguna untuk memilih peminjaman yang ingin dihapus melakukan validasi, 
    del data[pilihan - 1]    #dan menghapusnya dari list data.
    print("Berhasil menghapus")

def cek_peminjam():  # memeriksa apakah ada peminjaman yang terdaftar ,jika ada nanti akan ditampilkan
    if not data:
        print("Tidak ada peminjam.")
        return

    print("===== DATA PEMINJAMAN =====")
    for peminjaman in data:
        print(f"Nama: {peminjaman['nama']}, Judul Buku: {peminjaman['judul']}, Tanggal Pinjam: {peminjaman['tanggal']}")

print("=====SELAMAT DATANG DI PERPUSTAKAAN =====")

while True:
    print("\nMenu:")
    print("1. Pilih Buku")
    print("2. Edit Peminjaman")
    print("3. Hapus Peminjaman")
    print("4. Tampilkan Data Peminjaman")
    print("5. Keluar")

    pilih = int(input("Silahkan pilih : "))

    if pilih == 1:     # Mengelola pilihan pengguna. Bergantung pada pilihan, fungsi yang sesuai akan dipanggil 
        daftar_buku()
        peminjaman = pilih_buku()
        print(f"\n Berhasil ID Buku: {peminjaman['id_buku']} \n Judul: {peminjaman['judul']} \n Peminjam: {peminjaman['nama']} \n Tanggal Pinjam: {peminjaman['tanggal']}")
        print()
    elif pilih == 2:
        edit_buku()
    elif pilih == 3:
        remove_buku()
    elif pilih == 4:
        cek_peminjam()
    elif pilih == 5:
        print("Terimakasih sudah berkunjung di perpustakaan! Jangan lupa kembali lagi!")
        break 
    else:
        print("Invalid! Masukkan pilihan di menu..")