klub_basket = {"Ali", "Budi", "Cindy", "Dina", "Eko"}
klub_renang = {"Budi", "Dina", "Fani", "Gina"}

siswa_kedua_klub = (klub_basket&klub_renang)
print("Siswa yang mengikuti kedua klub:")
print(siswa_kedua_klub)

siswa_hanya_satu_klub = (klub_basket - klub_renang|klub_renang - klub_basket)
print("\nSiswa yang hanya mengikuti satu klub:")
print(siswa_hanya_satu_klub)

siswa_unik = (klub_basket|klub_renang)
print("\nSemua siswa unik yang mengikuti setidaknya satu dari kedua klub:")
print(siswa_unik)

jumlah_siswa_unik = len(siswa_unik)
print("\nJumlah siswa unik yang mengikuti setidaknya satu dari kedua klub:", jumlah_siswa_unik)