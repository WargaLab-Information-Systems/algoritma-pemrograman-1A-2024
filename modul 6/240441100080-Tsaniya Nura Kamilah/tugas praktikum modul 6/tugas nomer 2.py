DataPeminjaman = []
def create(ID_peminjaman, NamaPeminjam, JudulBuku, TanggalPinjam):
    Data = (ID_peminjaman, NamaPeminjam, JudulBuku, TanggalPinjam)
    DataPeminjaman.append(Data)
    print('Data berhasil ditambahkan')
    return DataPeminjaman

def read():
    if len(DataPeminjaman) <= 0:
        print('Data kosong')
    else:
        index = 1
        for i in range(len(DataPeminjaman)):
            data = DataPeminjaman[i]
            print(f'{index}. ID peminjam : {data[0]}, Nama Peminjam : {data[1]}, Judul Buku : {data[2]}, Tanggal Pinjam : {data[3]}')
            index += 1

def update():
    if len(DataPeminjaman) > 0:
        nomor = int(input('Data ke berapa yang akan diubah? '))
        if nomor >=1 or nomor <= len(DataPeminjaman):
            Data = DataPeminjaman[nomor - 1]
            print(Data)
            ID_Peminjaman = int(input(f'Masukkan ID peminjaman baru : '))
            NamaPeminjam = input(f'Masukkan nama peminjam baru : ')
            JudulBuku = input(f'Masukkan Judul Buku baru : ')
            TanggalPinjam = input(f'Masukkan Tanggal Peminjaman baru : ')

            DataBaru = (ID_Peminjaman, NamaPeminjam, JudulBuku, TanggalPinjam)
            DataPeminjaman[nomor - 1] = DataBaru
            print('Data berhasil diubah')
        else:
            print('Nomor tidak valid')
    else:
        print('Data kosong')

def delete():
    if len(DataPeminjaman) > 0:
        nomor = int(input('Data ke berapa yang ingin dihapus? '))
        if nomor >= 1 or nomor <= len(DataPeminjaman):
            DataPeminjaman.pop(nomor - 1)
            print('Data berhasil dihapus')
        else:
            print('Nomor tidak valid')
    else:
        print('Data kosong')

while True:
    print('DATA PERPUSTAKAAN')
    print('1. Create Data')
    print('2. Read Data')
    print('3. Update Data')
    print('4. Delete Data')
    print('5. Exit')
    
    menu = int(input('pilih opsi: '))
    
    if menu == 1:
        ID_Peminjaman = int(input('Masukkan ID peminjaman: '))
        NamaPeminjam = input('Masukkan nama peminjam: ')
        JudulBuku = input('Masukkan Judul Buku: ')
        TanggalPinjam = input('Masukkan Tanggal Peminjaman : ')
        create(ID_Peminjaman, NamaPeminjam, JudulBuku, TanggalPinjam)
    
    elif menu == 2:
        read()
    elif menu == 3:
        update()
    elif menu == 4:
        delete()
    elif menu == 5:
        print('Terima kasih! Program selesai.')
        break
    else:
        print("Invalid! Masukkan pilihan yang benar.")