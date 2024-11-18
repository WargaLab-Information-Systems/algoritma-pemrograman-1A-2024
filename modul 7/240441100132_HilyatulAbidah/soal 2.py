klub_basket = {"Hilya", "Arinda", "Khofifah", "Gio", "Feby", "Faris"}
klub_renang = {"Arinda", "Khofifah", "Feby", "Nando", "Hendra"}

siswa_kedua_klub = klub_basket.intersection(klub_renang)
print("Siswa yang mengikuti kedua klub:", siswa_kedua_klub)

hanya_basket = klub_basket.difference(klub_renang)
print("Siswa yang hanya mengikuti klub basket:", hanya_basket)
hanya_renang = klub_renang.difference(klub_basket)
print("Siswa yang hanya mengikuti klub renang:", hanya_renang)

# Gabungkan siswa yang hanya mengikuti satu klub
siswa_hanya_satu_klub = hanya_basket.union(hanya_renang)
print("Siswa yang hanya mengikuti satu klub:", siswa_hanya_satu_klub)

#Daftar semua siswa unik yang mengikuti setidaknya satu klub
semua_siswa = klub_basket.union(klub_renang)
print("Semua siswa unik yang mengikuti setidaknya satu klub:", semua_siswa)

#Jumlah siswa unik yang mengikuti setidaknya satu klub
jumlah_siswa_unik = len(semua_siswa)
print("Jumlah siswa unik yang mengikuti setidaknya satu klub:", jumlah_siswa_unik)
