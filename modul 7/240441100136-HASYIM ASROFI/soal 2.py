basket = {"Ardi", "Rudi", "Rofi", "Rangga"}
renang = {"Rofi", "Rangga", "Rian", "Dimas"}


kedua_klub = basket & renang 
print("Siswa yang mengikuti kedua klub (Basket dan Renang):")
print(kedua_klub)


satu_klub = (basket ^ renang)
print("Siswa yang hanya mengikuti satu klub:")
print(satu_klub)


semua_siswa = (basket | renang) 
print("Daftar semua siswa unik yang mengikuti setidaknya satu klub:")
print(semua_siswa)


jumlah_siswa_unik = len(semua_siswa)
print("Jumlah siswa unik yang mengikuti setidaknya satu klub:")
print(jumlah_siswa_unik)