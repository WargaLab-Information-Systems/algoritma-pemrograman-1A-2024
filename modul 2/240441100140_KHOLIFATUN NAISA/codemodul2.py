#soal no 1
# predikatA = 100-81 
# predikatB = 80-71
# predikatC = 70-61
# predikatD = 60-41
# predikatE = 40-0
nama = input("masukkan nama anda: ")
nim = int(input("masukkan nim anda: "))
uts = int(input("masukkan nilai UTS anda: "))
uas = int(input("masukkan nilai UAS anda: "))
rata_rata = (uts+uas)/2
print (f"nilai rata-rata anda adalah: {rata_rata}")
if  81 >= rata_rata >=100 :
    print("ANDA MENDAPATKAN NILAI: A")
elif  80 >= rata_rata  >=71 :
    print("ANDA MENDAPATKAN NILAI: B")
elif  70 >= rata_rata  >=61 :
    print("ANDA MENDAPATKAN NILAI: C")
elif  60 >= rata_rata  >=41 :
    print("ANDA MENDAPATKAN NILAI: D")
elif 40 >= rata_rata  >=0 :
    print("ANDA MENDAPATKAN NILAI: E")
else :
    print("silahkan masukkan data dengan benar")


#soal no 2
#skor jaka 1100 dan ipk 3.5
#skor ida 1000 dan ipk 3.5
#note skor lebih besar dari 1100 dan ipk minimal 3.0
nama = (input("masukkan nama anda: "))
skor = int (input("masukkan skor anda: "))
ipk = float (input("masukkan ipk anda: "))

if (skor > 1100 and ipk >= 3.0):
    print (f"selamat {nama} anda terpilih sebagai penerima beasiswa")
else:
    print(f"mohon maaf {nama} belum bisa mendapatkan beasiswa")


#soal no 3
#Sumanto adalah seorang perawat dan ia hanya memeriksa 
#pasien dewasa diatas umur 18 tahun, namun ia perlu mengukur 
# BMI (Body Mass Index) dari pasien-pasiennya sebelum masuk klinik. 
# bantulah Sumanto untuk menghitung BMI pasiennya,  berikut index BMI nya =
#(Kurus <18.5)
#(Normal <=24.9)
#(Gemuk <=29.9)
#(Obesitas >=30)
#Berikut soal pengganti no. 3 yang ada pada modul dan cara menghitung 
# BMI silahkan dicari pada search engine yang disukai

usia = int(input("masukkan usia anda: "))
if usia < 18 :
    print("pak sumanto hanya memeriksa usia 18 tahun keatas")
else:
    tb = float(input ("silahkan masukkan tinggi badan anda: "))
    bb = float(input ("silahkan masukkan berat badan anda: "))
    bmi = bb//(tb*tb)
if  18.5 >= bmi >= 0 :
    print ("anda kurus")
elif 24.9 >= bmi >=17:
    print ("anda normal")
elif 29.9 >= bmi >=23.9:
    print ("anda gemuk")
elif 100 >= bmi >= 30:
    print("anda obesitas")
else:
    print("tidak terdaftar di bmi")
print (f"hasil bmi anda adalah {bmi}")


# soal no 4
tahun_kabisat = int(input("masukkan tahun: "))
if (tahun_kabisat % 4 == 0 and tahun_kabisat % 100 != 0) or (tahun_kabisat % 400 == 0):
    print(f"{tahun_kabisat} Adalah Tahun kabisat") 
else :
    print(f"{tahun_kabisat} Bukan Tahun kabisat") 


#soal no 5
#kartu member diskon 15%
#total belanja > 500000 diskon 10%

nama = (input("masukkan nama anda: "))
usia = int(input("masukkan usia anda: "))
if usia > 18:
    total_belanja = int(input("masukkan total belanja: "))
    member = input("apakah anda memiliki kartu member? (iya/tidak:) )")
    diskon = 0
    if member == "iya":
        diskon += 15
    if total_belanja > 500000:
        diskon += 10
    hasil_diskon = total_belanja * (1 - diskon / 100) #1 adalah 100/100 rumus dari diskon 
    print(f"Nama pembeli: {nama}")
    print(f"Total belanja sebelum diskon: {total_belanja:}Rp")
    print(f"Diskon yang didapatkan: {diskon}%")
    print(f"Total harga setelah diskon: {hasil_diskon:}Rp")
else:
    print("mohon maaf anda belum legal")








    
    