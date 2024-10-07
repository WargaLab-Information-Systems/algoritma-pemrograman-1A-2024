# # SOAL NOMOR 1

# print("=== Mengecek Nilai Rata-Rata ===")

# # menginput value
# nama = input("Masukkan Nama : ")
# nim = int(input("Masukkan NIM : "))
# nilai_uts = int(input("Masukkan Nilai UTS : "))
# nilai_uas = int(input("Masukkan Nilai UAS : "))

# # menghitung rata-rata
# nilai_rata_rata = (nilai_uts + nilai_uas) / 2

# print(f"Nama Anda                 : {nama}")
# print(f"NIM Anda                  : {nim}")
# print(f"Nilai rata-rata nilai anda: {nilai_rata_rata}")

# # penyeleksian kondisi
# if 100 >= nilai_rata_rata >=81 :
#     print ("Selamat anda mendapatkan nilai A")
# elif 80 >= nilai_rata_rata >=71 :
#     print ("Selamat anda mendapatkan nilai B")
# elif 70 >= nilai_rata_rata >=61 :
#     print ("Selamat anda mendapatkan nilai C")
# elif 60>= nilai_rata_rata >=41 :
#     print ("Selamat anda mendapatkan nilai D")
# elif 40 >= nilai_rata_rata >=0 :
#     print ("Selamat anda mendapatkan nilai E")
# else:
#     print("maaf inputan anda salah")



# # SOAL NOMOR 2

# # diketahui
# nama1 = "Jaka"
# nama2  = "ida"
# skor1 = 1100
# ipk1 = 3.5
# skor2 = 1000
# ipk2 = 3.5

# # syarat lulus beasiswa
# skor = 1100
# ipk = 3.0

# print("=== Syarat Kelulusan Beasiswa ===")

# # penyeleksian kondisi
# if skor1 > skor and ipk1 >= ipk:
#     print(f"Selamat kepada Saudara {nama1} Anda Lulus Persyaratan Beasiswa, Karena Skor Anda {skor1} dengan IPK {ipk1}")
# else:
#     print(f"Maaf kepada Saudara {nama1} Anda Tidak Lulus Persyaratan Beasiswa, Karena Skor Anda {skor1} dengan IPK {ipk1}")

# if skor2 > skor and ipk2 >= ipk:
#     print(f"Selamat kepada Saudari {nama2} Anda Lulus Persyaratan Beasiswa, Karena Skor Anda {skor2} dengan IPK {ipk2}")
# else:
#     print(f"Maaf kepada Saudari {nama2} Anda Tidak Lulus Persyaratan Beasiswa, Karena Skor Anda {skor2} dengan IPK {ipk2}")



# SOAL NOMOR 3

print("=== Cek Body Mass Index Anda ===")
print("BMI (Body Mass Index)") 
print("kurus    <  18.5")
print("normal   <= 24.9")
print("gemuk    <= 29.9")
print("obesitas >= 30")

# penentuan umur karena pak Sumanto hanya ingin pasien diatas umur 18 tahun
umur = int(input("Masukkan umur Anda : "))

# penyeleksian kondisi
if umur <= 18 :
    print("Pak sumanto hanya memeriksa pasien dewasa diatas umur 18 tahun")
else :
    bb = int(input("Masukkan berat badan Anda : "))
    tb = float(input("Masukkan tinggi badan Anda : "))

# rumus untuk mengecek BMI
    bmi = bb // (tb * tb)

    if 0 <= bmi < 18.5:
        print(f"Dengan BMI (body massa index) {bmi} Anda termasuk kategori Kurus")
    elif 18.5 <= bmi <= 24.9:
        print(f"Dengan BMI (body massa index) {bmi} Anda termasuk kategori Normal")
    elif 25 <= bmi <= 29.9:
        print(f"Dengan BMI (body massa index) {bmi} Anda termasuk kategori Gemuk")
    elif 30 <= bmi <= 100:
        print(f"Dengan BMI (body massa index) {bmi} Anda termasuk kategori Obesitas")
    else:
        print("maaf inputan anda salah")



# # SOAL NOMOR 4

# print("=== Pengecekan Tahun Kabisat ===")

# # menginput value (tahun)
# tahun = int(input("Masukkan Tahun Yang Anda Mau : "))

# # penyeleksian kondisi
# if tahun % 4 != 0:
#     print(f" {tahun} Bukan Tahun kabisat") 
# elif tahun % 100 != 0:
#     print(f" {tahun} Adalah Tahun kabisat") 
# elif tahun % 400 != 0 :
#     print(f" {tahun}  Bukan Tahun kabisat") 
# else:
#     print(f" {tahun} Adalah Tahun kabisat")



# # SOAL NOMOR 5

# print("=== Selamat Datang di Bar Jefri ===")

# # menginput value
# nama_pembeli = (input("masukkan nama anda : "))
# usia_pembeli = int(input("masukkan usia anda : "))

# # penyeleksian kondisi
# if usia_pembeli >= 18:
#     total_belanja = int(input("masukkan total belanja : "))
#     member = input("apakah anda memiliki kartu member? (iya/tidak:)")
    
#     diskon = 0
#     if member == "iya":
#         diskon += 15
#     if member == "tidak":
#         diskon += 0
#     if total_belanja > 500000:
#         diskon += 10
    
#     # rumus diskon (harga setelah diskon)
#     harga_after_diskon = total_belanja * (100/100 - diskon / 100)
        
#     print(f"Nama pembeli                 : {nama_pembeli}")
#     print(f"Total belanja sebelum diskon : Rp.{total_belanja}")
#     print(f"Diskon yang didapatkan       : {diskon}%")
#     print(f"Total harga setelah diskon   : Rp.{harga_after_diskon}")
# else:
#     print("mohon maaf usia anda belum mencukupi kriteria")