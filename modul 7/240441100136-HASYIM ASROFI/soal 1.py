alat_kesehatan = {
    "pengukur tekanan darah": 0,
    "termometer": 0,
    "stetoskop": 0,
    "inhaler": 0  
 }

# Hari pertama meminjam alat
alat_kesehatan["pengukur tekanan darah"] += 2
alat_kesehatan["termometer"] += 3

 # Hari kedua meminjam alat
alat_kesehatan["stetoskop"] += 4
print(alat_kesehatan)

# # Setelah seminggu mengembalikan alat
# alat_kesehatan["pengukur tekanan darah"] -= 1
# alat_kesehatan["termometer"] -= 2

# # Menukar 3 alat stetoskop dengan 2 inhaler
# alat_kesehatan["stetoskop"] -= 3
# alat_kesehatan["inhaler"] += 2

# alat_terakhir = {alat: jumlah for alat, jumlah in alat_kesehatan.items()}

# #hasil akhir
# print("Alat kesehatan yang dipinjam Heni saat ini:")
# for alat, jumlah in alat_terakhir.items():
#     print(f"{alat}: {jumlah}")
