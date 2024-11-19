alat_kesehatan = {}

def tambah_alat(nama_alat, jumlah):
    if nama_alat in alat_kesehatan:
        alat_kesehatan[nama_alat] += jumlah
    else:
        alat_kesehatan[nama_alat] = jumlah

def kurangi_alat(nama_alat, jumlah):
    if nama_alat in alat_kesehatan:
        alat_kesehatan[nama_alat] -= jumlah
        if alat_kesehatan[nama_alat] <= 0:
            del alat_kesehatan[nama_alat]

# H1
tambah_alat("Alat Pengukur Tekanan Darah", 2)
tambah_alat("Termometer", 3)

# H2
tambah_alat("Stetoskop", 4)

# H3
kurangi_alat("Alat Pengukur Tekanan Darah", 1)
kurangi_alat("Termometer", 2)
kurangi_alat("Stetoskop", 3)
tambah_alat("Alat Inhaler", 2)

# Mengkonversi dictionary ke set untuk mendapatkan daftar unik alat
daftar_alat = set(alat_kesehatan.keys())

print("\nDaftar alat yang dipinjam Heni saat ini:")
print("----------------------------------------")
for alat in daftar_alat:
    print(f"{alat}: {alat_kesehatan[alat]} buah")