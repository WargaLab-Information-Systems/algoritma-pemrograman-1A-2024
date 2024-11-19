#membuat list untuk menyimpan data
datapeminjaman = []

#membuat fungsi untuk create
def create():
    id = input('masukkan ID buku : ')
    nama = input('masukkan nama peminjam : ')
    Judul = input('masukkan Judul buku : ')
    tgl =  input('masukkan Tanggal peminjaman : ')
    peminjaman = (id,nama,Judul,tgl)
    datapeminjaman.append(peminjaman)
    print('data peminjaman berhasil dibuat')

#membuat fungsi untuk read
def read():
    if not datapeminjaman:
        print('Tidak ada data peminjaman buku di YUTIEM LIBRARY ')
    else:
        print('\nberikut data peminjaman buku di YUTIEM LIBRARY ')
        for peminjaman in datapeminjaman:
            print('ID buku:',peminjaman[0],'\nNama peminjam:',peminjaman[1],'\nJudul Buku:',peminjaman[2],'\nTanggal peminjaman:',peminjaman[3])


#membuat fungsi untuk update
def update():
    perbarui = input('\nuntuk memperbarui data, silahkan masukkan ID buku: ')
    for i, peminjaman in enumerate(datapeminjaman):
        if peminjaman[0] == perbarui:
            print('data dengan ID buku', perbarui,' ditemukan')
            for peminjaman in datapeminjaman:
                print('ID buku:',peminjaman[0],'\nNama peminjam:',peminjaman[1],'\nJudul Buku:',peminjaman[2],'\nTanggal peminjaman:',peminjaman[3])
                id = perbarui
                namabaru = input('masukkan nama peminjam: ')
                judulbaru = input('masukkan judul buku: ')
                tglbaru = input('masukkan Tanggal: ')
                datapeminjaman[i] = (id,namabaru,judulbaru,tglbaru)
                print('data berhasil diperbarui')
                return 
    print('ID buku tidak ditemukan')

#membuat fungsi untuk delete
def delete():
    hapus = input('untuk melakukan penghapusan data, silahkan masukkan ID buku: ')
    for i, peminjaman in enumerate(datapeminjaman):
        if peminjaman[0] == hapus:
            print('data dengan ID buku',hapus,'ditemukan')
            for peminjaman in datapeminjaman:
                print('ID buku:',peminjaman[0],'\nNama peminjam:',peminjaman[1],'\nJudul Buku:',peminjaman[2],'\nTanggal peminjaman:',peminjaman[3])
                tanya = input(str('serius mau hapus data ini?(y/n):'))
                if tanya == 'y':
                    del datapeminjaman[i]
                    print('data berhasil dihapus')
                else:
                    print('okey, kembali ke program')
        else:
            print('data tidak ditemukan')
            return


while True:
    print('\nSelamat datang di YUTIEM LIBRARY')
    print('Berikut perincian menu di YUTIEM LIBRARY')
    print('1.Meminjam Buku')
    print('2.Tampilkan Data Peminjaman Buku')
    print('3.Memperbarui Data Peminjaman Buku')
    print('4.Menghapus Data Peminjaman Buku')
    print('5.Exit')

    menu = int(input('\nmasukkan menu yang kamu inginkan: '))
    if menu == 1:
        create()
    elif menu == 2:
        read()
    elif menu == 3:
        update()
    elif menu == 4:
        delete()
    elif menu == 5:
        print('okeyy, terimakasih atas kunjungannya')
        break
    else:
        print('masukkan menu yang sesuai :)')