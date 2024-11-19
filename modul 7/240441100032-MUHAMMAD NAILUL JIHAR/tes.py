klub_basket = {"kaka", "ronaldo", "nazario", "messi", "james"}
klub_renang = {"messi", "kaka", "dybala", "halaand", "james"}

print("Siswa yang mengikuti kedua klub ekstrakulikuler")
print(klub_basket.intersection(klub_renang))
print()

print("Siswa yang hanya mengikuti satu klub")
print(klub_basket.difference(klub_renang))
print()

semua_siswa = klub_basket.union(klub_renang)

print("----Data semua siswa unik yang mengikuti setidaknya satu klub----")
print(semua_siswa)
print()

print("Jumlah siswa unik yang setidaknya mengikuti satu dari kedua klub : ", len(semua_siswa))