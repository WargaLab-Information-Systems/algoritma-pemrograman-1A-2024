#Volume balok milik andika
#diketahui bahwa andika memiliki celengan berbentuk balok yang memiliki panjang 20cm, lebar 13cm dan tinggi 7cm
tinggi = 7
panjang = 20
lebar = 13
volume_celengan_balok = panjang*lebar*tinggi

print("Volume celengan balok andi adalah :", volume_celengan_balok)
#diketahui bahwa andi memiliki celengan berbentuk tabung yang memiliki diameter 14cm dan luas selimutnya 440cm2
diameter = 14
luas_selimut = 440
radius = diameter/2
tinggi_tabung = luas_selimut/(2*22/7*radius)
volume_tabung = 22/7 * radius ** 2* tinggi_tabung

print("Volume celengan tabung andi adalah :", volume_tabung)

print("")

#suku ke-5 (a+4d)=11 #a untuk nilai pertama dan d merupakan beda deret
#suku ke-8 (a+7d) +suku ke-12 (a+11d)= 52


suku_5 = 11
suku_8_dan_12= 52
#mencari nilai d(beda deret)
'''
1. a+4d = 11 /// a = 11-4d
2. 2a + 18d(7d+11d) = 52 
2(11-4d)+18d = 52
22 - 8d + 18d = 52
10d = 52-22
10 d = 30
d = 30/10
d = 3
'''
n = 8
d = 3
a = 11 - 4 * 3
jumlah_8_suku_pertama = n/2 * (2*a+(n-1)*d)

print("maka suku pertama nya yaitu :", a)
print("beda deret nya adalah :", d)
print("jumlah dari 8 suku pertama yang dicari darmaji adalah :", jumlah_8_suku_pertama)

print("")

#karena suraji ingin menukarkan uang dollar / luar negeri, maka rumus yang digunakan adalah kurs beli
#kurs beli adalah hasil nilai tukar dari pecahan luar negeri ke rupiah atau negara asal.
'''
diketahui, suraji mempunyai uang kertas bernilai US$35.
pada tanggal 25 september 2024, nilai tukar rupiah sebesar RP. 15.102,10
'''

jumlah_dollar = 35
nilai_tukar_rupiah = 15.102

total_rupiah = jumlah_dollar*nilai_tukar_rupiah

print("Jumlah uang rupiah yang diterima suraji adalah sebesar :", total_rupiah)
print("")

#pada soal nomor 4, kita memakai rumus kombinasi(!) yaitu c= n!/r1(n-r)!
#dimana c melambangkan hasil tim, n merupakan jumlah tim dan r merupakan jumlah orang yang akan dipilih
#Diketahui darsono mempunyai 7 orang yang tersedia, namun darsono hanya ingin 4 org yang masuk kedalam tim.
#maka rumusnya adalah c = 7!/4!(7-4)!

n = 7
r = 4
k = 3 #sebagai nilai dari (n-r)

fact_n = 7*6*5*4*3*2*1
fact_r = 4*3*2*1
fact_k = 3*2*1

jumlah_perhitungan_tim = fact_n/(fact_r*fact_k) 
print("Jadi, pak darsono bisa membentuk tim dengan jumlah cara : ", jumlah_perhitungan_tim)