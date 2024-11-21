#peminjaman hari pertama
brgpinjaman = {'alat pengukur tekanan darah': 2,'termometer': 3}

#peminjaman hari kedua
brgpinjaman ['stetoskop'] = 4

#peminjaman setelah seminggu
brgpinjaman.update({'alat pengukur tekanan darah' : 1, 'stetoskop':1, 'termometer':1})
brgpinjaman ['inhaler'] = 2

#apa saja yang dipinjam hani?
print('barang yg dipinjam Hani adalah')
for key,value in brgpinjaman.items():
    print(f'{key} : {value}')
