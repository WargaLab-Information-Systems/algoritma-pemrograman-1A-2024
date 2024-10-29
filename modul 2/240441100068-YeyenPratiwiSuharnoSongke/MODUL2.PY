# # # Tugas 1
# nama = input("Masukkan Nama: ")
# nim = int(input("Masukkan NIM: "))
# nilai_uts = int(input("Masukkan Nilai UTS :"))
# nilai_uas = int(input("Masukkan Nilai UAS :"))

# nilai_rata_rata = (nilai_uts+nilai_uas) / 2
# print("NAMA Anda :", nama)
# print("NIM Anda :", nim)
# print("Nilai rata-rata nilai anda", nilai_rata_rata)

# if nilai_rata_rata >=81 :
#     print ("Anda mendapatkan nilai A")
# elif nilai_rata_rata >=71 :
#     print ("Anda mendapatkan nilai b")
# elif nilai_rata_rata >=61 :
#     print ("Anda mendapatkan nilai C")
# elif nilai_rata_rata >=41 :
#     print ("Anda mendapatkan nilai D")
# else:
#     print ("Anda mendapatkan nilai E")


# # Tugas 2
# skor_jaka = 1100
# ipk_jaka = 3.5
# skor_ida = 1000
# ipk_ida = 3.5

# if skor_jaka >1100 and ipk_jaka >= 3.0:
#     print("Jaka lulus persyaratan beasiswa.")
# else:
#     print("Jaka tidak lulus persyaratan beasiswa.")

# if skor_ida >1100 and ipk_ida >= 3.0:
#     print("Ida lulus persyaratan beasiswa.")
# else:
#     print("Ida tidak lulus persyaratan beasiswa.")

# #Tugas 3
# #BMI (Body Massa Index)
# berat_badan = float(input("Masukkan berat badan pasien (kg): "))
# tinggi_badan = float(input("Masukkan tinggi badan pasien (m): "))

# # Hitung BMI
# bmi = berat_badan / (tinggi_badan ** 2)
    
# # Cetak hasil BMI
# print("BMI pasien:", bmi)

# # Periksa kategori BMI
# if bmi < 18.5:
#     print("Kategori BMI: Kurus")
# elif bmi <= 24.9:
#     print("Kategori BMI: Normal")
# elif bmi <= 29.9:
#     print("Kategori BMI: Gemuk")
# else:
#     print("Kategori BMI: Obesitas")

# # Tugas 4
# tahun = int(input("Masukkan Tahun: "))

# if tahun % 4 != 0:
#     print(f" {tahun}  Bukan Tahun kabisat") 
# elif tahun % 100 != 0:
#     print(f" {tahun} Adalah Tahun kabisat") 
# elif tahun % 400 != 0 :
#     print(f" {tahun}  Bukan Tahun kabisat") 
# else:
#     print(f" {tahun} Adalah Tahun kabisat")


# #Tugas 5
# # kartu member diskon 15%
# # total belanja > 500000 diskon 10%

# nama = (input("masukkan nama anda: "))
# usia = int(input("masukkan usia anda: "))

# if usia > 18:
#     total_belanja = int(input("masukkan total belanja: "))
#     member = input("apakah anda memiliki kartu member? (iya/tidak:) )")
#     diskon = 0
    
#     if member == "iya":
#         diskon +=15
#     if total_belanja > 500000:
#         diskon += 10
#     total_harga_setelah_diskon = total_belanja * (1 - (diskon / 100))
#     print(f"Nama pembeli: {nama}")
#     print(f"Total belanja sebelum diskon: {total_belanja:}Rp")
#     print(f"Diskon yang didapatkan: {diskon}%")
#     print(f"Total harga setelah diskon: {total_harga_setelah_diskon:}Rp")
# else:
#     print("mohon maaf anda belum memenuhi kriteria")