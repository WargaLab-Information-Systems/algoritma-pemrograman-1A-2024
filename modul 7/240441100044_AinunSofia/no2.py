#membuat 2 set berisi data siswa klub basket dan renang
basket = {'Ainun','Windi','Yeyen','Yesica','Rendi','Hilmy','Jefri'}
renang = {'Yeyen','Dian','Hilmy','Naisa','Eka','Bita','Rendi'}

#daftar siswa yang mengikuti kedua klub
print('sisiwa yang mengikuti klub basket dan renang adalah:\n',basket.intersection(renang))

#daftar siswa yang mengikuti hanya satu klub saja
a = basket.difference(renang)
b = renang.difference(basket)
gabung = a.union(b)
print('\nSiswa yang mengikuti satu klub saja:\n',gabung)

#daftar semua siswa unik yang mengikuti setidaknya satu dari kedua klub tersebut
print('\ndaftar semua siswa unik yang mengikuti setidaknya satu klub:\n',basket.union(renang))

#jumlah siswa unik yang mengikuti setidaknya satu dari kedua klub tersebut
print("\nJumlah siswa unik yang mengikuti setidaknya satu klub:",len(basket.union(renang)))
