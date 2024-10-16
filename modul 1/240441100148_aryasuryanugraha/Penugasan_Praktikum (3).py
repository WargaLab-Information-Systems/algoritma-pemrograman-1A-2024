# soal 1
print("jawaban no 1")
print("memcari volume")
# Celengan berbentuk balok mempunyai panjang 20 cm, lebar 13 cm dan tinggi 7 cm
# rumusnya adalah panjang*lebar*tinggi

p = 20 #panjang
l = 13 #lebar
t = 7  #tinggi

v_b  = p*l*t
print("Volume dari balok adalah ", v_b, "cm3")

# celengan berbentuk tabung memiliki diameter 14 cm dan luas selimut 440 Cm2
# rumusnya adalah phi*jari jari*jari jari*tinggi
# jari jari adalah diameter di bagi 2
# karena tinggi belum di ketahui, kita cari dulu, rumusnya adalah luas/2*22/7*jari jari

d = 14 #diameter tabung
l = 440 #luas selimut tabung

r = d/2 #jari
t = (l/2)/(22/7*r) #tinggi

v_t = 22/7*r*r*r #volume

print("volumenya dari tabung adalah ", v_t, "Cm3")

# Soal 2
print("soal no 2")
print("mencari suku ke 8")
# di ketahui suku ke 5 adalah 11
# di ketahui suku ke 8 dan suku ke 12 adalah 52
# berapakah suku ke 8

# U5 = a + (5-1) * b hasilnya a = 11-4b

# U8 + U12 = (a+(8-1)b) + (a+(12-1)b)
#          = (a+7b) + (a+11b)
#          = 2a + 18b
# dan hasil dari a = 26-9b

# bila seudah diketahui sepeti ini kita bisa mengitung a dan b
# b

rumusb = (26-11)/(9-4) #5b = 15 b=15/5 3
b     = rumusb 
print("nilai b adalah ", b)

# untuk nilai b sudah di ketahui, sekarang mencari nilai a
rumusa = 11-4*(3) # 11-12 = -1
# 3 adalah hasil dari b yang sebelumnya udah kita hitung
a     = rumusa
print("nilai a adalah ", a)
    
# sekarang kita aplikasikan nilai a dan nilai b untuk mencari suku ke 8
n   = 8
rumusn  = (n/2)*(2*a+(n-1)*b)
print("jadi suku ke 8 adalah", rumusn)

# soal
print("soal no 3")
print("nilai tukar uang amerika dan indonesia")
# ketika ingin menukar uang dolar merika ke indonesia harus menggunakan kurs beli
# kurs beli dolar amerika pada tanggal 25september adalah 15.110,07 di ambil dari https://datacenter.ortax.org/ortax/kursbi/show/USD

usd= 35 #1 USD= 15.110.07 Rp
kurs_beli= 15110

tukar   = usd * kurs_beli
print("hasil uang yang di miliki oleh darmaji adalah ", tukar, "Rp")

# soal
print("soal no 4")
print("berapa cara yang dapat digunakan untuk memilih tim")
# 7 orang dan hanya 4 yang dipilih, berapa metode yang dapat digunakan

orang = 7
n     = 5040 # n adalah faktorial dari nilai orang
pilih = 4
r     = 24 # r adalah faktorial dari orang yang bisa di pilih
nCr   = 6 # nCr adalah hasil dari (n-r)! 7 - 4 = 3 kemudian di faktorisasikan hasil nya 6.

rumusP  = (n)//(r*nCr) #5040/(144) = 35
print("jadi cara yang bisa di gunakan oleh darsono ada ", rumusP, "cara")

