 #nomor 1
Nama = input("Masukkan nama anda:")
NIM = input("Masukkan NIM anda :")
nilai_uts = float(input("Masukkan nilai UTS anda:"))
nilai_uas = float(input("Masukkan nilai UAS anda :"))

rata_rata = (nilai_uts+nilai_uas)/2

if 100 >= rata_rata >= 81 :
    grade = "A"
elif 80 >= rata_rata >= 71:
    grade = "B"
elif 70 >= rata_rata >= 61:
    grade = "C"
elif 60 >= rata_rata >= 41:
    grade = "D"
elif 40 >= rata_rata >= 0:
    grade = "E"
else:
    grade = "Nilai tidak valid"

print (f"Nama: {Nama}")
print(f"NIM: {NIM}")
print(f"Nilai UTS: {nilai_uts:.2f}")
print(f"Nilai UAS: {nilai_uas:.2f}")
print(f"Nilai rata rata anda: {rata_rata}")
print(f"Grade: {grade}")
print("")

# #nomor 2
nama_mahasiswa_1 = "jaka"
total_skor_1 = 1100
Ipk_1 = 3.5

nama_mahasiswa_2 = "ida"
total_skor_2 = 1000
ipk_2 = 3.5

persyaratan_skor = 1100
persyaratan_ipk = 3.0

if total_skor_1 > persyaratan_skor and Ipk_1 >= persyaratan_ipk :
    hasil_jaka = f"{nama_mahasiswa_1} lulus persyaratan untuk mendapatkan beasiswa"
else:
    hasil_jaka = f"{nama_mahasiswa_1} tidak lulus persyaratan untuk mendapatkan beasiswa"

if total_skor_2 > persyaratan_skor and ipk_2 >= persyaratan_ipk:
    hasil_ida = f"{nama_mahasiswa_2} lulus persyaratan untuk mendapatkan beasiswa"
else:
    hasil_ida = f"{nama_mahasiswa_2} tidak lulus persyaratan untuk mendapatkan beasiswa"

print(hasil_jaka)
print(hasil_ida)
print("")

# #soal nomor 3
umur = int(input("Masukkan umur pasien : "))

if umur < 18 :
    print("Maaf, Pasien belum mencukupi umur dan harus berusia diatas 18 tahun.")
else:
    berat = float(input("Masukkan berat badan pasien (Dengan format kg): "))
    tinggi = float(input("Masukkan tinggi badan pasien (format meter): "))

bmi = berat/(tinggi ** 2)

if bmi <0 :
    kategori = "maaf tidaak terdeksi"
elif bmi <=18.50:
    kategori = "Kurus"
elif bmi <= 24.9:
    kategori = "Normal"
elif bmi <= 29.9 :
    kategori = "Gemuk"
else:
    kategori = "Obesitas"

print(f"Nilai body mass index pasien adalah : {bmi: .2f}") #.2f menunjukkan format float dan akan ditampilkan 2 digit setelah koma
print(f"Kategori BMI nya adalah : {kategori}")
print("")

# #nomor 4
tahun = int(input("Masukkan tahun :"))
if(tahun % 4== 0 and tahun % 100 != 0 ) or (tahun % 400 == 0): #menggunakan 400 karena thn kabisat bisa didhitung dengan cara dibagi 400. dan thn kabisat terjadi 4 th sekali
    print(f"{tahun} merupakan tahun kabisat")
else:
    print(f"{tahun} bukan merupakan tahun kabisat")
print("")

# #nomor 5
nama_pembeli = input("Masukkan nama pembeli :")
usia = int(input("Masukkan usia pembeli :"))
if usia <18 :
    print("Maaf usia anda belum mencukupi")
else:
    total_belanja = float(input("Total belanja anda adalah :"))
    kartu_membership = input("Apakah anda memiliki kartu membership bar kami? (ya/tidak): ")

diskon = 0
if kartu_membership == "ya":
    diskon += 15
if total_belanja > 500000:
    diskon += 10 

total_harga_sebelum_diskon = total_belanja
total_harga_saat_mendapat_diskon = total_belanja - (total_belanja * diskon/100)

print("Rincian pembelian")
print("")
print(f"Nama pembeli : {nama_pembeli}")
print(f"diskon yang didapat : {diskon}%")
print(f"Total harga sebelum diskon : Rp {total_harga_sebelum_diskon:.2f}")
print(f"Total harga saat mendapatkan diskon : Rp{total_harga_saat_mendapat_diskon:.2f}")