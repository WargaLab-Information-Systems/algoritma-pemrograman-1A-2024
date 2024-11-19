basket_club = {'Andi', 'Budi', 'Caca', 'Dedi', 'Evi'}
renang_club = {'Budi', 'Caca', 'Eka', 'Fia', 'Gina'}

siswa_umum = basket_club.intersection(renang_club)
print(f"Siswa yang mengikuti kedua klub: {siswa_umum}")

only_basket = basket_club - renang_club  
only_renang = renang_club - basket_club
print(f"Siswa yang hanya mengikuti klub Basket:\n {only_basket}")
print(f"Siswa yang hanya mengikuti klub Renang:\n {only_renang}")

semua_siswa = basket_club.union(renang_club)
print(f"Semua siswa unik yang mengikuti setidaknya satu klub:\n {semua_siswa}")

total_siswa = len(semua_siswa)
print(f"Jumlah siswa unik yang mengikuti setidaknya satu klub:\n {total_siswa}")