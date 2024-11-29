#input siswa
basket = {'ali', 'budi', 'citra', 'dewi', 'vina'}
renang = {'budi', 'citra', 'rina', 'vina', 'rido'}

#mengikuti kedua klub
siswa = (basket & renang)
print("siswa yang mengikuti kedua klub: ", siswa)
print()

#mengikuti satu klub
siswa_basket = basket - renang
siswa_renang = renang - basket
mengikuti_satu = (siswa_basket | siswa_renang)
print("siswa yang hanya mengikuti satu klub: ", mengikuti_satu)
print()

#mengikuti satu dari kedua klub
semua_siswa = (basket | renang)
print("siswa yang mengikuti satu dari dua klub: ", semua_siswa)
print()

#jumlah yang mengikuti satu dari kedua klub
siswa_unik = len(semua_siswa)
print("jumlah siswa unik yang mengikuti satu dari dua klub: ", siswa_unik)
print()