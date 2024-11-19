klub_basket = {"yesica", "windy", "eka", "dian", "ikbal"}
for klub in (klub_basket):
    print(klub)
klub_renang = {"windy", "dian", "yeyen", "ainun", "alip"}
for klub in (klub_renang):
    print(klub_renang)

siswa_kedua_klub = klub_basket.intersection(klub_renang)
print("Siswa yang mengikuti kedua klub:")
print(siswa_kedua_klub)

siswa_hanya_basket = klub_basket.difference(klub_renang)
siswa_hanya_renang = klub_renang.difference(klub_basket)
siswa_hanya_satu_klub = siswa_hanya_basket.union(siswa_hanya_renang)
print("Siswa yang hanya mengikuti satu klub:")
print(siswa_hanya_satu_klub)

siswa_unik = klub_basket.union(klub_renang)
print("Semua siswa unik yang mengikuti setidaknya satu dari kedua klub:")
print(siswa_unik)

jumlah_siswa_unik = len(siswa_unik)
print("Jumlah siswa unik yang mengikuti setidaknya satu dari kedua klub:")
print(jumlah_siswa_unik)





