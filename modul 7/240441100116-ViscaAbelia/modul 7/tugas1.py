#alat kesehatan
#2 glukometer, 3 termometer, 4 sphygmomanometer,3 sphygmomanometer, 2 inhaler
alat_kesehatan = {}

print('hari pertama')
def peminjaman():
    print('---peminjaman---')
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
    print('---pengembalian---')
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
    print('---penukaran---')
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