print("A. Membuat dua set yang berisi nama siswa yang mengikuti klub Basket dan Renang.")
Basket={'Arinda','Aidzin','Shintia','Axel','Dila','Dewa','Dipat','Nabila','Zaid'}
Renang={'Rohmah','Firman','Amanda','Sobari','Shofi','Dewa','Nabila','Dipat','Dila'}
print("Basket:", end=" ")
for Nama in Basket:
    print(Nama, end=", ")
print("\nRenang:", end=" ")
for Nama in Renang:
    print(Nama, end=", ")

print("\n\nB. Menampilkan daftar siswa yang mengikuti kedua klub.")
print("Kedua klub:", end=" ")
for Nama in Basket&Renang:
    print(Nama, end=", ")

print("\n\nC. Menampilkan daftar siswa yang hanya mengikuti satu klub saja.")
satu_klub=Basket^Renang
print("Satu klub:", end=" ")
for Nama in satu_klub:
    print(Nama, end=", ")

print("\n\nD. Menampilkan daftar semua siswa unik yang mengikuti setidaknya satu dari kedua klub tersebut.")
siswa_unik=Basket|Renang
print("Siswa unik:", end=" ")
for Nama in siswa_unik:
    print(Nama, end=", ")

print("\n\nE. Menampilkan jumlah siswa unik yang mengikuti setidaknya satu dari kedua klub tersebut.")
print("Jumlah siswa unik:", len(siswa_unik))