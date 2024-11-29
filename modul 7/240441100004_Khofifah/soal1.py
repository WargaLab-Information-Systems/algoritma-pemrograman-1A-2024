# Membuat dictionary untuk menyimpan jumlah alat yang dipinjam
alat_pinjaman = {
    'Alat Pengukur Tekanan Darah': 0,
    'Termometer': 0,
    'Stetoskop': 0,
    'Alat Inhaler': 0
}

# Hari pertama
alat_pinjaman['Alat Pengukur Tekanan Darah'] += 2
alat_pinjaman['Termometer'] += 3

# Hari kedua
alat_pinjaman['Stetoskop'] += 4

# Setelah seminggu (pengembalian dan penukaran)
alat_pinjaman['Alat Pengukur Tekanan Darah'] -= 1
alat_pinjaman['Termometer'] -= 2
alat_pinjaman['Stetoskop'] -= 3
alat_pinjaman['Alat Inhaler'] += 2

# Menampilkan hasil alat yang dipinjam saat ini
print("Alat Kesehatan yang Dipinjam Heni Saat Ini:")
for alat, jumlah in alat_pinjaman.items():
    print(f"{alat}: {jumlah}")