# NOMER 1
# MENCARI NILAI DARI V0LUME BALOK
print("diketahui")
print("panjang_balok = 20cm")
print("lebar_balok = 13cm")
print("tinggi_balok = 7cm")

# MEMASUKKAN NILAI UNTUK VOLUME BALOK
print("jika anda ingin menghitung volume dari sebuah balok, maka anda harus memasukkan data-data yang telah anda ketahui")
panjang_balok=int(input("masukkan panjang dari balok : "))
lebar_balok=int(input("maaukkan lebar dari balok : "))
tinggi_balok=int(input("masukkan tinggi dari balok : "))

# MENGHITUNG HASIL DARI VOLUME 
hasil=panjang_balok*lebar_balok*tinggi_balok
print('hasil dari volume balok yang telah dihitung adalah',hasil)

# MENCARI NILAI DARI VOLUME TABUNG
print("diketahui")
print("diameter = 14cm")
print("luas selimut = 440cm^2")
print("pi = 22/7")
print("r = ...?")
print("t = ...?") 

# MENGHITUNG NILAI r
print("cara menghitung r adalah diameter/2 ")
r=int(input("masukkan diameternya : "))
hasilr=r/2
print("hasil dari r adalah : ",hasilr)

# MENGHITUNG TINGGI TABUNG
print("cara mencari tinggi = luas selimut / (2.pi.r)")
hasil1=int(2 * 22/7 * hasilr)
luas_selimut=int(input("masukkan luas dari selimut : "))
t= luas_selimut / hasil1
print("hasil dari tingi adalah : ",t)

# MENGHITUNG HASIL DARI VOLUME TABUNG
print("cara menghitung volume dari tabung adalah volume tabung = pi*r^2*t")
volume_tabung = 22/7 *hasilr** 2 *t
print("hasil dari volume adalah : ", volume_tabung )
 


# NOMOR 2
u5 = int(input("masukkan nilai dari u5: "))
u8_plus_u12 = int(input("masukkan nilai dari u8_plus_u12: "))

# menghitung beda
b=(u8_plus_u12-2*u5)/10       

# mencari suku pertama
a=u5-4*b

# menghitung jumlah 8 suku pertama 
i=8
jumlah_8_suku = i*(2*a+(i-1)*b)/2

# menampilkan hasil
print(f"nilai dari suku pertama (a)={a}")
print(f"nilai beda dari (b)= {b}")
print(f"jumlah 8 suku pertama={jumlah_8_suku}")

# NOMOR 3
nilai_tukar=  1510210      #25 september 2024
usd=int(input('masukkan uang usd suraji : '))

rupiah=nilai_tukar*usd
print('nilai uang yang diterima suraji dalam mat  uang rupiah adalah : Rp.',rupiah)



# NOMOR 4
a = int(input("jumlah total dari orang yang ada: "))
b = int(input("jumlah total orang yang dipilih: "))

# menghitung faktorial
faktorialdari7 = 7*6*5*4*3*2*1
faktorialdari4 = 4*3*2*1
faktorialdari3 = 3*2*1

# jumlah dari caranya
jumlahcara = (faktorialdari7)/(faktorialdari4*faktorialdari3)
print(jumlahcara)