data = []

def daftar_buku():
    print("\nTOP 4 BUKU PALING LARIS")
    print("1. AMBALAN 1969")
    print("2. AMBARAWA SOSOK PENJAGA RAWA HYTAM MISTERIYUS")
    print("3. AMBABELLE BONEKA YANG TERKUTUK")
    print("4. LEOAMBA DA VINCI")

def pilih_buku():
    while True:
        pilih = int(input("Silahkan pilih buku : "))
        nama = input("Nama peminjam : ")
        tanggal = input("Tanggal Pinjam (DD/MM/YYYY) : ")
        if pilih in [1, 2, 3, 4]:
            judul = ["AMBALAN 1969", "AMBARAWA SOSOK PENJAGA RAWA HYTAM MISTERIYUS", "AMBABELLE BONEKA YANG TERKUTUK", "LEOAMBA DA VINCI"][pilih - 1]
            id_buku = 1234 + (pilih - 1) * 1111  
            break
        else:
            print("Invalid, silahkan pilih buku yang tersedia.")

    peminjaman = [nama, id_buku, judul, tanggal]
    data.append(peminjaman)
    return peminjaman

def tampilkan_data():
    if not data:
        print("Tidak ada data peminjaman.")
    else:
        print("\nDATA PEMINJAMAN")
        for i in range(len(data)):
            peminjaman = data[i]
            print(f"{i + 1}. Nama: {peminjaman[0]}, Judul Buku: {peminjaman[2]}, Tanggal Pinjam: {peminjaman[3]}")

def edit_peminjaman():
    tampilkan_data()
    if not data:
        return
    
    pilihan = input("Pilih nomor peminjaman yang ingin diubah : ")
    if not pilihan.isdigit() or int(pilihan) < 1 or int(pilihan) > len(data):
        print("Nomor tidak valid.")
        return
    
    pilihan = int(pilihan) - 1
    peminjaman = data[pilihan]
    
    print(f"Data saat ini: Nama: {peminjaman[0]}, Judul Buku: {peminjaman[2]}, Tanggal Pinjam: {peminjaman[3]}")
    
    nama_baru = input("Masukkan nama peminjam baru (tekan enter untuk tidak mengubah): ")
    if nama_baru:
        peminjaman[0] = nama_baru  
    
    tanggal_baru = input("Masukkan tanggal pinjam baru (DD/MM/YYYY, tekan enter untuk tidak mengubah): ")
    if tanggal_baru:
        peminjaman[3] = tanggal_baru  

    print("\nPilih buku baru jika ingin mengubah buku yang dipinjam:")
    daftar_buku()
    buku_baru = input("Silahkan pilih buku baru (tekan enter untuk tidak mengubah): ")
    if buku_baru.isdigit() and int(buku_baru) in [1, 2, 3, 4]:
        judul_baru = ["AMBALAN 1969", "AMBARAWA SOSOK PENJAGA RAWA HYTAM MISTERIYUS", "AMBABELLE BONEKA YANG TERKUTUK", "LEOAMBA DA VINCI"][int(buku_baru) - 1]
        id_buku_baru = 1234 + (int(buku_baru) - 1) * 1111  
        peminjaman[2] = judul_baru
        peminjaman[1] = id_buku_baru
    
    print("\nBerhasil mengubah data peminjaman.")

def remove_buku():
    tampilkan_data()
    if not data:
        return
    
    pilihan = input("Pilih nomor yang ingin dihapus : ")
    if not pilihan.isdigit() or int(pilihan) < 1 or int(pilihan) > len(data):
        print("Nomor tidak valid.")
        return
    
    pilihan = int(pilihan) - 1
    del data[pilihan]
    print("Berhasil menghapus peminjaman.")

while True: 
    print("\nWELCOME TO LIBRARY OF NGAWI CITY")
    print("1. Pilih Buku")
    print("2. Edit Peminjaman")
    print("3. Hapus Peminjaman")
    print("4. Tampilkan Data Peminjaman")
    print("5. Keluar")

    pilih = int(input("Silahkan pilih : "))

    if pilih == 1:
        daftar_buku()
        peminjaman = pilih_buku()
        print(f"\nBerhasil meminjam... \nID Buku: {peminjaman[1]} \nJudul: {peminjaman[2]} \nPeminjam: {peminjaman[0]} \nTanggal Pinjam: {peminjaman[3]}")
    elif pilih == 2:
        edit_peminjaman()
    elif pilih == 3:
        remove_buku()
    elif pilih == 4:
        tampilkan_data()
    elif pilih == 5:
        print("Terima kasih sudah berkunjung di perpustakaan! Jangan lupa kembali lagi!")
        break
    else:
        print("Invalid! Masukkan pilihan yang benar.")