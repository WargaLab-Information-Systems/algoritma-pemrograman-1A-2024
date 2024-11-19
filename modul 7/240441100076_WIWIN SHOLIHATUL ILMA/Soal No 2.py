klub_basket = {"Ali", "Budi", "Cindy", "Diana", "Eko"}
for klub in klub_basket:
    print(klub)
klub_renang = {"Budi", "Cindy", "Fajar", "Gina"}
for klub in klub_renang:
    print(klub)

siswa_kedua_klub = klub_basket.intersection(klub_renang)
print("Siswa yang mengikuti kedua klub:")
print(siswa_kedua_klub)

siswa_hanya_basket = klub_basket - klub_renang
siswa_hanya_renang = klub_renang - klub_basket
siswa_hanya_satu_klub = siswa_hanya_basket.union(siswa_hanya_renang)

print("Siswa yang hanya mengikuti satu klub:")
print(siswa_hanya_satu_klub)

semua_siswa_unik = klub_basket.union(klub_renang)
print("Semua siswa unik yang mengikuti setidaknya satu klub:")
print(semua_siswa_unik)

jumlah_siswa_unik = len(semua_siswa_unik)
print("Jumlah siswa unik yang mengikuti setidaknya satu klub:", jumlah_siswa_unik)