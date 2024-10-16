# tugas no 1
# celengan balok diketahui
# panjang = 20
# lebar = 13
# tinggi = 7
panjang = int(input("masukkak panjang celengan balok:"))
lebar = int(input("masukkak lebar celengan balok:"))
tinggi = int(input("masukkak tinggi celengan balok:"))

# volume celengan balok
volume_balok = panjang * lebar * tinggi
print(f"volume celengan balok adalah:{volume_balok} cm")

# celengan tabung diketahui 
# diameter = 14
# radius = 7
# luas_selimut = 440

diameter = int(input("masukkan diameter:"))
radius = int(input("masukkan radius:"))
luas_selimut = int(input("masukkan luas selimut:"))
# menghitung tinggi tabung dari luas selimut
tinggi_tabung = luas_selimut / (2 *3.14 * radius) 

# volume celengan tabung
volume_tabung = 3.14 * radius**2 * tinggi_tabung
print(f"volume celengan tabung adalah:{volume_tabung} cm")

# tugas no 2
# u5 = 11
# u8 ditambah u12 = 52
u5 = int(input("masukkan nilai u5:"))
u8_ditambah_u12 = int(input("masukkan nilai u8 + u12:"))

# menghitung beda
# 11 = a + 4 * b
# 52 = a + 7 * b + a + 11 * b
# 52 = 2a + 18 * b
# 26 = a + 9 * b - 11 = a+4*b
# 15 = 5 * b
b = 3
a = u5 - 4 * b
 
suku_8 = 8*(2*a+(8-1)*b)/2
print(f"jumlah 8 suku pertama: {suku_8}")

#tugas no 3
# diketahui 
# usd = 35
# kurs = 15.102,10
usd = int(input("masukkan usd :"))
kurs = float(input("masukkan kurs :"))

hasil = usd * kurs
print(f"hasil nominal uang dalam rupiah adalah : Rp.{hasil}")

# tugas no 4
# diketahui
# n = 7
# r = 4
n = int(input("masukkan jumlah orang:"))
r = int(input("masukkan yang di pilih:"))

faktorial7 =7*6*5*4*3*2*1
faktorial4 =4*3*2*1
faktorial3 =3*2*1
# menghitung kombinasi
kombinasi =  faktorial7//(faktorial4*faktorial3)

print(f"banyaknya cara untuk membentuk tim:{kombinasi}")
