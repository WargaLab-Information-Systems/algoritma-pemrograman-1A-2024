#DATA PERUSAHAAN
DataPerusahaan = []
def TambahData():
    tambahdata= int(input('berapa banyak data yang ingin anda inputkan (minimal 5): '))
    for i in range(1, tambahdata +1):
        NIP = input('NIP : ')
        Nama = input('Nama : ')
        Alamat = input('Alamat : ')
        Departemen = input('Departemen : ')
        Jabatan = input('Jabatan : ')

        Data = (NIP, Nama, Alamat, Departemen, Jabatan)
        DataPerusahaan.append(Data)
        print('Data berhasil ditambahkan')

def CariData(DataPerusahaan):
    print('cari berdasarkan: ')
    print('1. NIP ')
    print('2. Nama ')
    print('3. Alamat ')
    print('4. Departemen ')
    print('5. Jabatan ')

    opsi = int(input('pilih opsi :'))

    index = 0
    KataKunci = ''
    if opsi == 1:
        index = 0
        KataKunci = input('masukkan nip yang dicari : ')
    elif opsi == 2:
        index = 1
        KataKunci = input('masukkan nama yang dicari : ')
    elif opsi == 3:
        index = 2
        KataKunci = input('masukkan alamat yang dicari : ')
    elif opsi == 4:
        index = 3
        KataKunci = input('masukkan departemen yang dicari : ')
    elif opsi == 5:
        index = 4
        KataKunci = input('masukkan jabatan yang dicari : ')
    else:
        print('opsi tidak valid')

    ditemukan = False
    for data in DataPerusahaan:
        if KataKunci in data[index]:
            print(f'ID barang : {data[0]}, Nama Barang : {data[1]}, Tingkat Prioritas : {data[2]}')
            ditemukan = True
    
    if not ditemukan:
        print('Data Tidak ditemukan')

TambahData()
while True:
    CariData(DataPerusahaan)

    carilagi = input('cari lagi? ')
    if carilagi == 'tidak':
        break