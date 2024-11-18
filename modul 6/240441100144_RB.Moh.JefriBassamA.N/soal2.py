peminjaman_buku = []
id = 101

def create(id, nama, buku, tanggal):

        peminjaman = (id, nama, buku, tanggal)
        peminjaman_buku.append(peminjaman)
        print(f"buku berjudul '{buku}' dipinjam oleh {nama}, berhasil ditambahkan!")

def read():
    print()
    if not peminjaman_buku:
        print("Tidak ada data peminjaman buku.")
    elif peminjaman_buku:
        print("data yang meminjam buku perpustakaan :")
        for peminjaman in peminjaman_buku:
            print(f"ID peminjaman     : {peminjaman[0]}")
            print(f"nama peminjam     : {peminjaman[1]}")
            print(f"judul buku        : {peminjaman[2]}")
            print(f"tanggal peminjaman: {peminjaman[3]}")
            print()

def update(id_pengecekan, nama, buku_baru, tanggal_baru):
    for i in range(len(peminjaman_buku)):
        peminjaman = peminjaman_buku[i]
        if peminjaman[0] == id_pengecekan:
            peminjaman_buku[i] = (id_pengecekan, nama, buku_baru, tanggal_baru)
            print(f"data peminjaman dengan ID {id_pengecekan} berhasil diperbarui!")
        elif peminjaman[0] == id_pengecekan:
            print(f"data peminjaman dengan ID {id_pengecekan} tidak ditemukan!")

def delete(id_pengecekan):
    for i in range(len(peminjaman_buku)):
        peminjaman = peminjaman_buku[i]
        if peminjaman[0] == id_pengecekan:
            del peminjaman_buku[i]
            print(f"data peminjaman dengan ID {id_pengecekan} berhasil dihapus!")
        elif peminjaman[0] == id_pengecekan:    
            print(f"data peminjaman dengan ID {id_pengecekan} tidak ditemukan!")

while True:
    print("---Peminjaman Buku Perpustakaan---")
    print("1. input peminjaman")
    print("2. tampilkan data peminjaman")
    print("3. update peminjaman")
    print("4. hapus peminjaman")
    print("5. keluar")
        
    pilih = int(input("pilih menu yang anda mau : "))
        
    if pilih == 1:
        id += 1
        nama = str(input("masukkan nama peminjam : "))
        buku = str(input("masukkan judul buku : "))
        tanggal = input("masukkan tanggal peminjaman : ")
        create(id, nama, buku, tanggal)
        
    elif pilih == 2:
        read()
        
    elif pilih == 3:
        id_pengecekan = input("masukkan ID yang ingin diupdate : ")
        buku_baru = str(input("masukkan judul buku baru : "))
        tanggal_baru = input("masukkan tanggal peminjaman baru : ")
        update(id, nama, buku_baru, tanggal_baru)
        
    elif pilih == 4:
        id_pengecekan = input("masukkan ID peminjaman yang ingin anda hapus : ")
        delete(id)
        
    elif pilih == 5:
        print("program telah selesai!")
        print("terima kasih! !")
        break
        
    else:
        print("maaf inputan anda salah!")
