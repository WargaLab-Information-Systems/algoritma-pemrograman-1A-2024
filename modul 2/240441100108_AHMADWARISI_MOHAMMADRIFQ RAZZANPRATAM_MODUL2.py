#Soal No 1
print ("Scrip penyeleksian kondisi")
nama = input("Masukkan Nama Anda : ")
nim = int(input("Masukkan NIM anda : "))
nilai_uts = float(input("Masukkan nilai UTS anda : "))
nilai_uas = float(input("Masukkan nilai UAS anda : "))

nilai = (nilai_uts + nilai_uas) / 2
if nilai > 81 and nilai < 100:
    keterangan = "A"
elif nilai > 71 and nilai < 80:
    keterangan = "B"
elif nilai >61 and nilai < 70 :
    keterangan = "C"
elif nilai > 41 and nilai < 60 :
    keterangan = "D"
elif nilai > 0 and nilai < 40:
    keterangan = "E"
else :
    keterangan = "anda tidak mendapatkan nilai"

print ("Nama anda : ",nama)
print ("NIM anda adalah : ",nim)
print ("Nilai rata rata anda adalah : ",nilai)
print ("Anda Mendapatkan Nilai : ",keterangan)

#Soal No 2
print ("menghitung siapa yang lulus persyaratan beasiswa dengan skor dan ipk yang sudah di tentukan")
print ("diketahui : lulus dengan skor lebih dari 1100 dan IPK 3.0")
print ("Jaka memiliki skor 1100 dan IPK 3.5 ")
print ("Ida memiliki skor 1000 dan IPK 3.5 ")

nama1 = input ("Masukkan nama anda (jaka) : ")
skor1 = int(input ("Masukkan skor jaka : "))
ipk1 = float(input("Masukkan IPK jaka : "))

nama2 = input ("Masukkan nama anda (ida) : ")
skor2 = int(input ("Masukkan skor ida : "))
ipk2 = float(input("Masukkan IPK ida : "))

skor = 1100
ipk = 3.0

if skor1 > skor and ipk1 > ipk :
    print (nama1," lulus persyaratan beasiswa.")
else :
    print (nama1, " tidak lulus persyaratan beasiswa.")

if skor2 > skor and ipk2 > ipk :
    print (nama2," lulus persyaratan beasiswa.")
else :
     print (nama2," tidak lulus persyaratan beasiswa.")

# #Soal No 3
print ("===Membantu sumanto untuk memilih pasien dewasa dan menghitung BMI pasiennya===")
umur = int(input("Masukkan umur anda : "))
if umur <18 :
    print ("umur anda tidak cukup")
else :
    bb = int(input("Masukkan Berat Badan anda : "))
    tb = int(input("Masukkan Tinngi Badan anda  : "))

    tinggi_badan = tb/100
    bmi = (bb / (tinggi_badan**2))

    if bmi <18.5 :
        print("anda kurus")
    elif bmi <=24.9 :
        print ("anda normal")
    elif bmi <= 29.9 :
        print ("anda gemuk")
    else :
        print ("anda obesitas")

    bmi=round(bmi,1)
   
    print ("BMI anda : ",bmi)

#Soal No 4
print ("===Menentuka tahun kabisat===")
tahun = int(input("Masukkan tahun : "))

if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
    print(tahun, "adalah tahun kabisat.")
else:
    print(tahun, "bukan tahun kabisat.")

# #Soal No 5
print ("Program diskon di sebuah bar")
nama = input("Masukkan Nama Anda : ")
umur = int(input("Masukkan Umur Anda : "))

if umur <18 :
    print ("Umur anda tidak cukup")
else :
    total = float(input("Masukkan total Belanjaan Anda : "))
    kartu = input("Apakah anda mempunyai karu member ? (iya/tidak) : ")
    if kartu == "iya" :
        diskon = 15
    elif total > 500000 :
        diskon = 10
    else :
        diskon = 0

    jumlah = total * (diskon/100)
    semua = total - jumlah

    print ("Nama Anda Adalah : ",nama)
    print ("Diskon yang di Dapat : ",diskon,"%")
    print ("harga sebelum diskon : ",total)
    print ("harga setelah diskon : ",semua)


# # a = 10
# # b= 3

# # c = float(a/b)

# # c=round(c,2)
# # print(c)
