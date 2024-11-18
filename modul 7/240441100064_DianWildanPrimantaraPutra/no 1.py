alat_pinjaman = {
    "alat_pengukur_tekanan_darah": 0,
    "termometer": 0,
    "stetoskop": 0,
    "alat_inhaler": 0
}

# Hari pertama: meminjam 2 alat pengukur tekanan darah dan 3 termometer
alat_pinjaman["alat_pengukur_tekanan_darah"] += 2
alat_pinjaman["termometer"] += 3

# Hari kedua: meminjam 4 stetoskop
alat_pinjaman["stetoskop"] += 4

# Setelah seminggu: mengembalikan 1 alat pengukur tekanan darah dan 2 termometer
alat_pinjaman["alat_pengukur_tekanan_darah"] -= 1
alat_pinjaman["termometer"] -= 2

# Menukar 3 stetoskop dengan 2 alat inhaler
alat_pinjaman["stetoskop"] -= 3
alat_pinjaman["alat_inhaler"] += 2

# Menampilkan alat kesehatan yang dipinjam saat ini
print("Alat kesehatan yang dipinjam Heni saat ini:")
for alat, jumlah in alat_pinjaman.items():
    if jumlah > 0:  
        print(f"{alat}: {jumlah}")