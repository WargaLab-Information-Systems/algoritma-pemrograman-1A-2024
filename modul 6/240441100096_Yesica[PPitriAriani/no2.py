data = []

def daftar_buku():
    print("===== DAFTAR BUKU =====")
    print("1. MATEMATIKA")
    print("2. IPA")
    print("3. PPKN")
    print("4. PAI")

def pilih_buku():
    while True:
        pilih = int(input("Silahkan pilih buku : "))
        nama = input("Nama peminjam : ")
        tanggal = input("Tanggal Pinjam (DD/MM/YYYY) : ")
        if pilih == 1:
            judul = "MATEMATIKA"
            id_buku = 1234
            break
        elif pilih == 2:
            judul = "IPA"
            id_buku = 2345
            break
        elif pilih == 3:
            judul = "PPKN"
            id_buku = 3456
            break
        elif pilih == 4:
            judul = "PAI"
            id_buku = 4567
            break
        else:
            print("Invalid")
            continue
    
    peminjaman = {"nama": nama, "id_buku": id_buku, "judul": judul, "tanggal": tanggal}
    data.append(peminjaman)
    return peminjaman

def edit_buku():
    if not data:
        print("Tidak ada data yang dapat diubah.....\n")
        return
    
    print("===== DATA PEMINJAMAN =====")
    for i in range(len(data)):
        peminjaman = data[i]
        print(f"{i + 1}. Nama: {peminjaman['nama']}, Judul Buku: {peminjaman['judul']}, Tanggal Pinjam: {peminjaman['tanggal']}")
    
    pilihan = input("Pilih nomer yang ingin diubah : ")
    if not pilihan.isdigit() or int(pilihan) < 1 or int(pilihan) > len(data):
        print("Nomer tidak valid.")
        return
    
    nama_baru = input("Masukkan nama baru : ")
    pilihan = int(pilihan)

    daftar_buku()
    pilih_baru = int(input("Silahkan pilih buku baru : "))
    if pilih_baru == 1:
        judul_baru = "MATEMATIKA"
        id_buku_baru = 1234
    elif pilih_baru == 2:
        judul_baru = "IPA"
        id_buku_baru = 2345
    elif pilih_baru == 3:
        judul_baru = "PPKN"
        id_buku_baru = 3456
    elif pilih_baru == 4:
        judul_baru = "PAI"
        id_buku_baru = 4567
    else:
        print("Invalid")
        return

    data[pilihan - 1]["nama"] = nama_baru
    data[pilihan - 1]["judul"] = judul_baru
    data[pilihan - 1]["id_buku"] = id_buku_baru
    print("\nBerhasil mengubah...\n")

def remove_buku():
    if not data:
        print("Tidak ada data yang dapat dihapus.")
        return
    
    print("===== DATA PEMINJAMAN =====")
    for i in range(len(data)):
        peminjaman = data[i]
        print(f"{i + 1}. Nama: {peminjaman['nama']}, Judul Buku: {peminjaman['judul']}, Tanggal Pinjam: {peminjaman['tanggal']}")
    
    pilihan = input("Pilih nomer yang ingin dihapus : ")
    if not pilihan.isdigit() or int(pilihan) < 1 or int(pilihan) > len(data):
        print("Nomer tidak valid.")
        return
    pilihan = int(pilihan)
    del data[pilihan - 1]
    print("Berhasil menghapus")

def cek_peminjam():
    if not data:
        print("Tidak ada peminjam.")
        return

    print("===== DATA PEMINJAMAN =====")
    for peminjaman in data:
        print(f"Nama: {peminjaman['nama']}, Judul Buku: {peminjaman['judul']}, Tanggal Pinjam: {peminjaman['tanggal']}")

print("=====SELAMAT DATANG DI PERPUSTAKAAN=====")

while True:
    print("\nMenu:")
    print("1. Pilih Buku")
    print("2. Edit Peminjaman")
    print("3. Hapus Peminjaman")
    print("4. Tampilkan Data Peminjaman")
    print("5. Keluar")

    pilih = int(input("Silahkan pilih : "))

    if pilih == 1:
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