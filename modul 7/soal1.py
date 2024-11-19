alat_kesehatan = {
    "pengukur_tekanan_darah": 0,
    "termometer": 0,
    "stetoskop": 0,
    "inhaler": 0
}

alat_kesehatan["pengukur_tekanan_darah"] += 2
alat_kesehatan["termometer"] += 3

alat_kesehatan["stetoskop"] += 4

alat_kesehatan["pengukur_tekanan_darah"] -= 1
alat_kesehatan["termometer"] -= 2

alat_kesehatan["stetoskop"] -= 3
alat_kesehatan["inhaler"] += 2
alat_dipinjam = {alat for alat, jumlah in alat_kesehatan.items() if jumlah > 0}

print("Jumlah alat kesehatan yang dipinjam Heni:")
for alat, jumlah in alat_kesehatan.items():
    if jumlah > 0:
        print(f"- {alat.replace('_', ' ').capitalize()}: {jumlah}")

print("Alat kesehatan yang masih dipinjam (sebagai set):", alat_dipinjam)