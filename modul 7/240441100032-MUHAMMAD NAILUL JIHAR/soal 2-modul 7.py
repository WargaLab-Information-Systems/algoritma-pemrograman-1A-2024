klub_basket = {"Andi", "Budi", "Citra", "Deni", "Eva", "Fani"}
klub_renang = {"Budi", "Deni", "Gina", "Hani", "Ira", "Eva"}

print("Daftar Anggota Klub:")
print("--------------------")
print("Klub Basket:", klub_basket)
print("Klub Renang:", klub_renang)
print()

siswa_dua_klub = klub_basket.intersection(klub_renang)
print("Siswa yang mengikuti kedua klub:")
print("--------------------------------")
for siswa in siswa_dua_klub:
    print(siswa)
print()

siswa_basket_saja = klub_basket - klub_renang
siswa_renang_saja = klub_renang - klub_basket

print("Siswa yang hanya mengikuti satu klub:")
print("------------------------------------")
print("Hanya Basket:")
for siswa in siswa_basket_saja:
    print(siswa)
print("\nHanya Renang:")
for siswa in siswa_renang_saja:
    print(siswa)
print()

semua_siswa = klub_basket.union(klub_renang)
print("Daftar semua siswa yang mengikuti minimal satu klub:")
print("--------------------------------------------------")
for siswa in sorted(semua_siswa): 
    print(siswa)
print()

print("Jumlah siswa unik yang mengikuti minimal satu klub:", len(semua_siswa))