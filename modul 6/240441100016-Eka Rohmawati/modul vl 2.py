# Daftar untuk menyimpan data peminjaman buku
peminjaman_list = []

def peminjaman():
    id_peminjaman = input("masukkan ID peminjaman buku: ")
    nama_peminjam = input("masukkan nama peminjam: ")
    judul_buku = input("masukkan judul buku: ")
    tanggal_peminjaman = input("masukkan tanggal peminjaman buku: ")

    peminjaman_data = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
    peminjaman_list.append(peminjaman_data)
    print("peminjaman berhasil diinput")

def read():
    if not peminjaman_list:
        print("tidak ada data peminjaman")
    else:
        for i in range(len(peminjaman_list)):
            peminjaman = peminjaman_list[i]
            print(f"Nomor: {i + 1}")
            print(f"ID Peminjaman: {peminjaman[0]}")
            print(f"Nama Peminjam: {peminjaman[1]}")
            print(f"Judul Buku: {peminjaman[2]}")
            print(f"Tanggal Peminjaman: {peminjaman[3]}")

def update():
    nomor = int(input("masukkan nomor data peminjam yang ingin diedit: "))
    if 0 < nomor <= len(peminjaman_list):
        id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman = peminjaman_list[nomor - 1]
        print("pilih data yang ingin diedit:")
        print("1. judul buku")
        print("2. tanggal peminjaman")
        pilihan = input("masukkan nomor pilihan: ")
        if pilihan == "1":
            judul_buku = input("masukkan judul buku baru: ")
        elif pilihan == "2":
            tanggal_peminjaman = input("masukkan tanggal peminjaman baru: ")
        else:
            print("kode tidak valid")
            return

        peminjaman_list[nomor - 1] = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
        print("data berhasil diperbarui.")
    else:
        print("nomor data tidak valid.")

def delete():
    nomor = int(input("masukkan nomor data peminjam yang ingin dihapus: "))
    if 0 < nomor <= len(peminjaman_list):
        noawal = peminjaman_list[nomor - 1]
        del peminjaman_list[nomor - 1]
        print(f"data {noawal} telah dihapus.")
    else:
        print("nomor data tidak valid.")

while True:
    print("1. tambah peminjaman")
    print("2. tampilkan peminjaman")
    print("3. update peminjaman")
    print("4. hapus peminjaman")
    kode = input("masukkan nomor: ")
    
    if kode == "1":
        peminjaman()
    elif kode == "2":
        read()
    elif kode == "3":
        update()
    elif kode == "4":
        delete()
    else:
        print("kode tidak ada")

    ulang = input("apakah ingin menghitung ulang kembali? (ya/no): ")
    if ulang != 'ya':
        print("terimakasi")
        break