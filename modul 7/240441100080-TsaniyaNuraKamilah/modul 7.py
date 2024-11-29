#nomer 1
#2 glukometer, 3 termometer, 4 sphygmomanometer,3 sphygmomanometer, 2 inhaler
alat_kesehatan = {}

print('hari pertama')
def peminjaman():
    print('peminjaman')
    alat = int(input('berapa jenis alat yang ingin anda pinjam? '))
    for i in range(alat):
        nama_alat = input('masukkan nama alat: ')
        jumlah = int(input('masukkan jumlah: '))
        alat_kesehatan[nama_alat] = jumlah
    print(f'alat berhasil dipinjam')
peminjaman()
print()

print('hari kedua')
peminjaman()
print()

#pengembalian
def pengembalian():
    print('pengembalian')
    alat = int(input('berapa jenis alat yang ingin anda kembalikan? '))
    for i in range(alat):
        nama_alat = input('masukkan nama alat: ')
        jumlah = int(input('masukkan jumlah: '))
        if nama_alat in alat_kesehatan:
            alat_kesehatan[nama_alat] -= jumlah
            if alat_kesehatan[nama_alat] <=0:
                del alat_kesehatan[nama_alat]
    print(f'alat berhasil dikembalikan')
pengembalian()
print()

def penukaran():
    print('penukaran')
    alat = int(input('berapa jenis alat yang ingin anda tukar? '))
    for i in range(alat):
        nama_alat = input('masukkan nama alat yang akan ditukar: ')
        jumlah = int(input('masukkan jumlah: '))
        alat_kesehatan[nama_alat] -= jumlah
        if nama_alat in alat_kesehatan:
            alat_kesehatan[nama_alat] -= jumlah
            if alat_kesehatan[nama_alat] <=0:
                del alat_kesehatan[nama_alat]
        nama_alat_baru = input('masukkan nama alat baru: ')
        jumlah_baru =  int(input('masukkan jumlah: '))
        alat_kesehatan[nama_alat_baru] = jumlah_baru
    print(f'alat berhasil ditukar')
penukaran()
print()

alat_kesehatan_set = set()
for nama_alat, jumlah in alat_kesehatan.items():
    alat_kesehatan_set.add((nama_alat, jumlah))
    
def read():
    print('alat yang dipinjam setelah proses peminjaman dan penukaran: ')
    no = 1
    for nama_alat, jumlah in alat_kesehatan_set:
        print(f'{no}. {nama_alat} : {jumlah} ')
        no += 1
read()

#nomer 2
#Membuat dua set yang berisi nama siswa yang mengikuti klub Basket dan Renang
klub_basket = {"Alice", "Bob", "Carlie", "Diana", "desi"}
klub_renang = {"Carlie", "Eve", "Frank", "Bob"}

siswa_kedua_klub = (klub_basket & klub_renang)
print("Siswa yang mengikuti kedua klub:")
print(siswa_kedua_klub)

siswa_hanyasatu_klub = (klub_basket - klub_renang|klub_renang - klub_basket)
print("Siswa yang hanya mengikuti satu klub:")
print(siswa_hanyasatu_klub)

siswa_semua_klub =(klub_basket|klub_renang)
print("Daftar semua siswa unik yang mengikuti setidaknya satu dari kedua klub:")
print(siswa_semua_klub)

jumlah_siswa_unik = len(siswa_semua_klub)
print("Jumlah siswa unik yang mengikuti setidaknya satu dari kedua klub:")
print(jumlah_siswa_unik)


# nomer 3
# lembaga bimbingan intensif Gema Ripah

siswa = {}
def pembagian_kelas():
    total_siswa = len(siswa)
    kelas = total_siswa // 3 + 1
    return kelas

def create():
    nama = input('masukkan nama siswa: ')
    kelas = pembagian_kelas()
    asal_sekolah = input('masukkan asal sekolah : ')
    plotting= input('masukkan plotting : ')
    print()
    id_siswa = len(siswa)+1
    siswa[id_siswa] = {
        'nama' : nama,
        'kelas' : kelas,
        'asal sekolah' : asal_sekolah,
        'plotting' : plotting
    }

def read():
    if len(siswa) == 0:
        print('data siswa masih kosong')
    else:
        for id_siswa, data in siswa.items():
            print(f"ID:{id_siswa}\nNama: {data['nama']}\nKelas: {data['kelas']}\nAsal Sekolah: {data['asal sekolah']}\nplotting: {data['plotting']}")
    print()

def update():
    ID = int(input('masukkan ID siswa yang ingin di update: '))
    if ID in siswa:
        print('data siswa yang akan di update')
        print(f"ID:{ID}\nNama: {siswa[ID]['nama']}\nKelas: {siswa[ID]['kelas']}\nAsal Sekolah: {siswa[ID]['asal sekolah']}\nplotting: {siswa[ID]['plotting']}")
        print('masukkan data baru')
        nama = input('masukkan nama siswa: ')
        asal_sekolah = input('masukkan asal sekolah : ')
        plotting= input('masukkan plotting : ')

        siswa[ID]['nama'] = nama
        siswa[ID]['asal sekolah'] = asal_sekolah
        siswa[ID]['plotting'] = plotting
        siswa[ID]['kelas'] = pembagian_kelas()
    else:
        print('ID tidak ditemukan')
    print()

def delete():
    ID = int(input('masukkan id siswa yang ingin dihapus: '))
    if ID in siswa:
        print('Data yang akan dihapus')
        print(f"ID:{ID}\nNama: {siswa[ID]['nama']}\nKelas: {siswa[ID]['kelas']}\nAsal Sekolah: {siswa[ID]['asal sekolah']}\nplotting: {siswa[ID]['plotting']}")
        del siswa[ID]
        print(f'Data berhasil dihapus')
    else:
        print('ID tidak ditemukan')
    print()
while True:
    print('--- DAFTAR SISWA BIMBINGAN INTENSIF GEMA RIPAH ---')
    print('1. Create')
    print('2. Read')
    print('3. Update')
    print('4. Delete')
    print('5. Exit')
    opsi = int(input('pilih opsi? '))

    if opsi == 1:
        create()
    elif opsi == 2:
        read()
    elif opsi == 3:
        update()
    elif opsi == 4:
        delete()
    elif opsi == 5:
        break
    else:
        print('opsi tidak valid')