basket_club = {"Dian", "Rendy", "yaya", "EKA", "Jefri"}
renang_club = {"Rendy", "yaya", "jihar", "Windy", "Yessica"}

print("a. Himpunan (set) dari setiap Klub")
print("   Siswa yang mengikuti klub Basket:", basket_club)
print("   Siswa yang mengikuti klub Renang:", renang_club)

siswa_kedua_klub = basket_club & renang_club
print("b. Siswa yang mengikuti kedua klub:", siswa_kedua_klub)

siswa_satu_club = basket_club ^ renang_club
print("c. Siswa yang mengikuti satu klub:", siswa_satu_club)

siswa_unik = basket_club | renang_club
print("d. siswa yang mengikuti yang unik cuma mengikuti gapapa satu klub:", siswa_unik )



jumlah_siswa_unik = len(siswa_unik)
print("e. Jumlah siswa unik yang mengikuti setidaknya satu klub:", jumlah_siswa_unik)