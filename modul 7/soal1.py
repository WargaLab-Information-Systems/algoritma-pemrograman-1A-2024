alat_dipinjam = {
    'pengukur_tekanan_darah': 0,
    'termometer': 0,
    'stetoskop': 0,
    'inhaler': 0
}

# Hari pertama 
alat_dipinjam['pengukur_tekanan_darah'] += 2
alat_dipinjam['termometer'] += 3

#  Hari kedua
alat_dipinjam['stetoskop'] += 4

# 1 minggu
alat_dipinjam['pengukur_tekanan_darah'] -= 1
alat_dipinjam['termometer'] -= 2
alat_dipinjam['stetoskop'] -= 3
alat_dipinjam['inhaler'] += 2

# Menggunakan set untuk menyimpan alat yang masih dipinjam
jenis_alat_dipinjam = set([alat for alat, jumlah in alat_dipinjam.items() if jumlah > 0])

print("Alat kesehatan yang dipinjam Heni saat ini:")
for alat, jumlah in alat_dipinjam.items():
    if jumlah > 0:
        print(f"{alat}: {jumlah} buah")