klub_basket = {"Andi", "Budi", "Citra", "Dina", "Eka"}
klub_renang = {"Citra", "Dina", "Fajar", "Gita", "Hana"}

print("Anggota klub Basket:", klub_basket)
print("Anggota klub Renang:", klub_renang)

# b. Siswa yang mengikuti kedua klub (irisan)
kedua_klub = klub_basket & klub_renang
print("Siswa yang mengikuti kedua klub:", kedua_klub)

satu_klub_saja = klub_basket ^ klub_renang  # Simetri difference
print("Siswa yang hanya mengikuti satu klub:", satu_klub_saja)

semua_siswa = klub_basket | klub_renang  # Union
print("Semua siswa yang mengikuti setidaknya satu klub:", semua_siswa)

jumlah_siswa_unik = len(semua_siswa)
print("Jumlah siswa unik yang mengikuti setidaknya satu klub:", jumlah_siswa_unik)

