# #Soal Nomor 1
    # Menghitung celengan balok
print ("membantu andi menghitung celengan berbentuk balok dengan ukuran sebagai berikut")
print ("panjang : 20")
print ("lebar : 13")
print ("tinggi : 7")

print ("Untuk menghitung volume panjang, lebar, dan tinngi silahkan masukkan di bawah ini")
panjang = int(input("masukkan Panjang : "))
lebar = int(input("Masukkan Lebar : "))
tinggi = int(input("Masukkan Tinngi : "))

hasil = (panjang*lebar*tinggi)

# menghitung celengan berbentuk tabung
print ("membantu andi menghitung celengan berbentuk tabung dengan diameter sebagai berikut:")
print("diameter : 14 cm")
print("luas selimut : 440cm2")
print ("silahkan input diameter dan luas selimut untuk menghitung ")

diameter = int(input("masukkan diameter : "))
luas_selimut = int(input("masukkan luas selimut : "))
# jari jari silnder tersebut
radius = diameter / 2
#tinggi tabung dengan menggunakan rumus luas permukaan
besar= int(luas_selimut /( 2 * 3.14 * radius))
# volume celengan berbentuk tabung
volume_tabung = int(3.14 * radius ** 2 * besar)
# Hasilnya adalah
print ("=== Hasil perhitungan di atas adalah ===")
print("hasil celengan berbentuk balok adalah : ",hasil, "cm")
print("tinggi celengan berbentuk tabung :",besar, "cm")
print("celengan berbentuk tabung bervolume : ",volume_tabung, "cm³")


# #soal nomor 2
print ("nilai suku k-5 : 11")
print ("jumlah suku ke-8 dan 12 : 52")
print ("untuk mengetahui nilai suku ke-8 silahkan input nilai sudah di ketahui")

u5 = int(input("Masukkan nilai suku ke-5: "))
u8_plus_u12 = int(input("Masukkan jumlah nilai suku ke-8 dan suku ke-12: "))

# Menghitung beda (b) menggunakan u8 dan u12
b = (u8_plus_u12 - 2 * u5) / 6

# Menghitung suku pertama (a) menggunakan u5
a = u5 - 4 * b

# Menghitung jumlah 8 suku pertama
n = 8
S8 = (n / 2) * (2 * a + (n - 1) * b)

# Menampilkan hasil
print("Hasil perhitungan:")
print("Suku pertama (a): ",a)
print("Beda (b): ",b)
print("Jumlah 8 suku pertama (S8): ",S8)


# #Soal Nomor 3
print ("membantu suraji menukar uang USD ke IDR pada tanggal 25 September 2024")
print ("jumlah USD yang dimiliki : 35")
print ("nilai tukar IDR : 15102.10")

print ("untuk membantu menghitung silahkan input di bawah")

usd = float(input("masukkan USD : "))
idr = float(input("masukkan IDR : "))

hasil = usd * idr
print ("hasilnya adalah : ",float(hasil))

# #soal nomor 4
print("jumlah orang yang ada : 7")
print("jumlah yang akan dipiplih : 4")
print ("Silahkan input jumlah orang yang ada dan yang akan dipilih")
n = int(input("Masukkan total jumlah orang: "))
r = int(input("Masukkan jumlah orang yang akan dipilih: "))

# Memastikan r tidak lebih besar dari n
if r > n:
    print("Error: Jumlah orang yang dipilih tidak boleh lebih besar dari total orang.")
else:
    # Menghitung kombinasi
    pembilang = 1
    penyebut = 1
    
    # Menggunakan min(r, n-r) untuk mengurangi jumlah iterasi
    for i in range(min(r, n-r)):
        pembilang *= (n - i)
        penyebut *= (i + 1)
    
    kombinasi = pembilang // penyebut



    # Menampilkan hasil
    print ("Dari ",n, "orang, ada",kombinasi, "cara berbeda untuk memilih ",r, "orang.")
