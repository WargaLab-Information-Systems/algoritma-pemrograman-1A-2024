# Set siswa yang mengikuti klub Basket
basket_club = {"Salsa", "Nino", "Cinta", "Dina", "Eka"}

# Set siswa yang mengikuti klub Renang
renang_club = {"Budi", "Dina", "Eka", "Gina", "Hana"}

# b. Menampilkan daftar siswa yang mengikuti kedua klub
siswa_kedua_klub = basket_club.intersection(renang_club)
print("Siswa yang mengikuti kedua klub:", siswa_kedua_klub)

# c. Menampilkan daftar siswa yang hanya mengikuti satu klub saja
siswa_hanya_basket = basket_club.difference(renang_club)
siswa_hanya_renang = renang_club.difference(basket_club)
siswa_hanya_satu_klub = siswa_hanya_basket.symmetric_difference(siswa_hanya_renang)
print("Siswa yang hanya mengikuti satu klub:", siswa_hanya_satu_klub)

# d. Menampilkan daftar semua siswa unik yang mengikuti setidaknya satu dari kedua klub
siswa_ikuti_satu_atau_kedua_klub = basket_club.union(renang_club)
print("Siswa yang mengikuti setidaknya satu klub:", siswa_ikuti_satu_atau_kedua_klub)

# e. Menampilkan jumlah siswa unik yang mengikuti setidaknya satu dari kedua klub
jumlah_siswa_unik = len(siswa_ikuti_satu_atau_kedua_klub)
print("Jumlah siswa unik yang mengikuti setidaknya satu klub:", jumlah_siswa_unik)