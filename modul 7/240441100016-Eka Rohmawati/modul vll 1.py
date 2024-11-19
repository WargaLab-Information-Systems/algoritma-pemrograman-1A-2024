#input alat
alat = {
    'pengukur_tekanan_darah': 0,
    'termometer': 0,
    'stetoskop': 0,
    'inhaler': 0
}

#hari pertama
alat['pengukur_tekanan_darah'] += 2
alat['termometer'] += 3
print("alat yang dipinjam di hari pertama:")
for nama_alat, jumlah in alat.items():
    print(f"{nama_alat}: {jumlah}")
print()

#hari kedua
alat['stetoskop'] += 4
print("alat yang dipinjam di hari kedua:")
for nama_alat, jumlah in alat.items():
    print(f"{nama_alat}: {jumlah}")
print()

#mengembalikan alat
alat['pengukur_tekanan_darah'] -= 1
alat['termometer'] -= 2
print("alat yang dikembalikan:")
for nama_alat, jumlah in alat.items():
    print(f"{nama_alat}: {jumlah}")
print()

#menukar alat
if alat['stetoskop'] >= 3:
    alat['stetoskop'] -= 3
    alat['inhaler'] += 2
print("alat yang ditukar:")
for nama_alat, jumlah in alat.items():
    print(f"{nama_alat}: {jumlah}")
print()

#menampilkan hasil
print("alat yang dipinjam saat ini:")
for nama_alat, jumlah in alat.items():
    print(f"{nama_alat}: {jumlah}")