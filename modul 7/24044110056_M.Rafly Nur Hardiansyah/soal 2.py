#ng jero himpunan data siswa sg elok club
basket_club = {'Andi', 'Fly', 'Dela', 'Ipan', 'Ica'}
renang_club = {'Fly', 'Dela', 'Eka', 'Bita', 'Rizky'}

siswa_umum = basket_club.intersection(renang_club) #golek siswa sg gabung ng 2club
print(f"Siswa yang mengikuti kedua klub: {', '.join(siswa_umum)}")

#netuno siswa sg gabung 1club tok
only_basket = basket_club - renang_club #selisih -
only_renang = renang_club - basket_club
print(f"Siswa yang hanya mengikuti klub Basket:\n {', '.join(only_basket)}")
print(f"Siswa yang hanya mengikuti klub Renang:\n {', '.join(only_renang)}")

#nentuno kbh siswa
semua_siswa = basket_club.union(renang_club)
print(f"Semua siswa unik yang mengikuti setidaknya satu klub:\n {', '.join(semua_siswa)}")

#ngitung jumlah siswa 
total_siswa = len(semua_siswa) #ngitung jumlah elemen ng himpunan
print(f"Jumlah siswa unik yang mengikuti setidaknya satu klub:\n {total_siswa}")