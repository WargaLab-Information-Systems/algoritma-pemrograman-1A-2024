# Menggunakan dictionary untuk menyimpan jumlah alat kesehatan yang dipinjam Heni
alat_pinjaman = {
    "pengukur_tek_darah": 2,  
    "termometer": 3,         
    "stetoskop": 4,           
    "inhaler": 0              
}

# Mengembalikan alat
alat_pinjaman["pengukur_tek_darah"] -= 1  # Heni mengembalikan 1 pengukur tekanan darah
alat_pinjaman["termometer"] -= 2          # Heni mengembalikan 2 termometer

# Menukar stetoskop dengan inhaler
alat_pinjaman["stetoskop"] -= 3           # Heni menukar 3 stetoskop
alat_pinjaman["inhaler"] += 2             # Heni mendapatkan 2 inhaler sebagai pengganti stetoskop

# Menampilkan hasil alat yang dipinjam saat ini
print("Alat kesehatan yang dipinjam Heni saat ini:")
for alat, jumlah in alat_pinjaman.items():
    print(f"{alat}:{jumlah}")