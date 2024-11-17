BUKU = ["SIKANCIL", "PUTRI SALJU", "MATEMATIKA", "KIMIA", "INGGRIS"]
datapeminjaman = []

def data_buku():
    print("Daftar Buku:")
    nomor = 1
    for judul in BUKU:
        print(f"{nomor}. {judul}")
        nomor += 1

def peminjaman():
    data_buku()
    id_peminjam = input("Masukkan ID Anda: ")
    judul_buku = int(input("Masukkan nomor judul buku: "))
    tanggal = input("Masukkan tanggal peminjaman: ")
    if judul_buku > 0:
        datapeminjaman.append((id_peminjam, BUKU[judul_buku - 1], tanggal))
        print("Peminjaman berhasil diinput.")
    else:
        print("Nomor buku yang Anda masukkan salah.")

def tampil():
    if datapeminjaman == []:
        print("Data peminjam kosong.")
    else:
        nomor = 1
        for data in datapeminjaman:
            print(f"{nomor}. ID: {data[0]}, Buku: {data[1]}, Tanggal: {data[2]} ")
            nomor += 1
        print()

def tambah():
    judul_baru = input("Masukkan judul buku baru: ")
    BUKU.append(judul_baru)
    print("Buku telah ditambahkan.")

def edit():
    tampil()
    nomor = int(input("Masukkan nomor data peminjam yang ingin diedit: "))
    if 0 < nomor <= len(datapeminjaman):
        id_peminjam, judul_buku, tanggal = datapeminjaman[nomor - 1]
        print("Pilih data yang ingin diedit:")
        print("1. Judul Buku")
        print("2. Tanggal Peminjaman")
        pilihan = input("Masukkan nomor pilihan: ")
        if pilihan == "1":
            judul_buku = input("Masukkan judul buku baru: ")
        elif pilihan == "2":
            tanggal = input("Masukkan tanggal peminjaman baru: ")
        else:
            print("Pilihan tidak valid.")
            return
        datapeminjaman[nomor - 1] = (id_peminjam, judul_buku, tanggal)
        print("Data berhasil diedit.")
    else:
        print("Nomor data tidak valid.")

def hapus():
    tampil()
    nomor = int(input("Masukkan nomor data peminjam yang ingin dihapus: "))
    if nomor > 0 : 
        noawal = datapeminjaman[nomor-1]
        del datapeminjaman[nomor-1] 
        print(f"data {noawal} telah dihapus.")
    else:
        print("Nomor data tidak valid.")

def menu():
    print("1. input Peminjaman")
    print("2. Tampilkan Data peminjam")
    print("3. Tambah Data buku")
    print("4. Edit Data peminjaman")
    print("5. Hapus Data peminjaman")
    kode  = input("Masukkan nomor: ")
    if kode == "1":
        peminjaman()
    elif kode == "2":
        tampil()
    elif kode == "3":
        tambah()
    elif kode == "4":
        edit()
    elif kode == "5":
        hapus()
    else:
        print("Pilihan yang Anda masukkan salah.")

while True:
    menu()
    jawab = input("apakah ingin melanjutkan program? (ya/tidak): ")
    if jawab != "ya":
        break
