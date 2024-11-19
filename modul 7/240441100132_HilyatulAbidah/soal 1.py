peminjaman_alat = {
    "tekanan_darah" : 2,
    "termometer" : 3,
    "Stetoskop" : 4,
    "inhealer" : 0
}
# Melakukan perubahan pada alat
peminjaman_alat["tekanan_darah"] -= 1
peminjaman_alat["termometer"] -= 2
peminjaman_alat["Stetoskop"] -= 3
peminjaman_alat["inhealer"] += 2

alat_yang_dipinjam = set()
for alat, jumlah in peminjaman_alat.items():
    if jumlah > 0: 
        alat_yang_dipinjam.add(alat)

print("Alat kesehatan yang masih dipinjam oleh Heni saat ini adalah:", alat_yang_dipinjam)

for key, value in peminjaman_alat.items():
    if value > 0:  
        print(f"Alat = {key}, Total = {value}")
