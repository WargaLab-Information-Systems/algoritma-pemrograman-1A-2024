#lembaga bimbingan intensif Gema Ripah

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