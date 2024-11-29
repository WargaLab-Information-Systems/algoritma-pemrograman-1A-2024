# menampilkan 2 set yang berisi nama dari siswa yang mengikuti klub basket dan renang
klub_basket ={"adimas", "jefri", "naisa", "hilmy", "rifky", "hilya", "wibi"}
klub_renang ={"jefri", "wibi", "fatikh", "rofi", "arya", "adimas", "rifky"}

# daftar yang mengikuti kedua klub
mengikuti_kedua_klub = klub_basket.intersection(klub_renang)
print("siswa/siswi yang mengikuti kedua klub ialah: ",mengikuti_kedua_klub)
print()

# daftar siswa yang hanya satu klub
hanya_siswa_basket = klub_basket.difference(klub_renang)
print("hanya siswa/siswi basket: ", hanya_siswa_basket)
print()

hanya_siswa_renang = klub_renang.difference(klub_basket)
print("hanya siswa/siswi renang: ",hanya_siswa_renang)
print()

siswa_satu_klub = hanya_siswa_basket.union(hanya_siswa_renang)
print("siswa/siswi yang mengikuti hanya satu klub: ",siswa_satu_klub)
print()

# daftar siswa unik yang mengikuti setidaknya satu klub dari kedua klub tersebut
siswa_unik =klub_basket.union(klub_renang)
print("siswa/siswi yang mengikuti setidaknya satu klub dari kedua klub: ", siswa_unik)
print()

# jumlah dari siswa unik yang mengikuti setidaknya satu dari kedua klub tersebut.
jumlah_siswa_unik =len(siswa_unik)
print("jumlah siswa/siswi unik yang setidaknya mengikuti satu dari dua klub tersebut ialah: ",jumlah_siswa_unik)