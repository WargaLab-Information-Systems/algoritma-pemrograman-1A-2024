# #soal 1
# #input
# nama = input("Masukan Nama:")
# nim = input("Masukan NIM:")
# nilai_uts = int(input("Masukan Nilai UTS:"))
# nilai_uas = int(input("Masukan Nilai UAS"))

# #rumus menghitung nilai rata rata
# nilai_rata_rata = (nilai_uas + nilai_uts)/2

# #tentukan nilai
# if nilai_rata_rata >=81:
#     nilai = "A"
# elif nilai_rata_rata >=71:
#     nilai = "B"
# elif nilai_rata_rata >=61:
#     nilai = "C"
# elif nilai_rata_rata >=41:
#     nilai = "D"
# else:
#     nilai = "E"
    
    
# #hasil
# print("Masukan Nama", nama)
# print("NIM Anda", nim)
# print("Nilai rata rata nilai anda",nilai_rata_rata)
# print("Anda Mendapatkan Nilai", nilai)


#soal 2
#Nilai input 
# skor_jaka = 1100
# ipk_jaka = 3.5
# skor_ida = 1000
# ipk_ida = 3.5

#Persyaratan lulus beasiswa
# skor_min = 1100
# ipk_min = 3.5

# #periksa kelayakan jaka
# if skor_jaka > skor_min and ipk_jaka >=ipk_min:
#    print("Jaka memenuhi persyaratan lulus beasiswa:")
# else:
#     print("Jaka tidak memenuhi persyaratan lulus beasiswa:")

# #periksa kelayakan ida
# if skor_ida > skor_min and ipk_ida >=ipk_min:
#     print("Ida memenuhi persyaratan lulus beasiswa:")
# else:
#     print("Ida tidak memenuhi persyaratan lulus beasiswa:")

#soal 3
# Input nilai berat badan dan tinggi badan pasien
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

#soal 4
# tahun = int(input("Masukkan tahun: "))

# if tahun % 4 == 0 and (tahun % 100 != 0 or tahun % 400 == 0):
#     print(tahun, "adalah tahun kabisat")
# else:
#     print(tahun, "bukan tahun kabisat")

#soal 5
# Input data pembeli
# nama_pembeli = input("Masukkan nama pembeli: ")
# usia_pembeli = int(input("Masukkan usia pembeli: "))
# total_belanja = int(input("Masukkan total belanja: "))
# kartu_member = input("Apakah pembeli memiliki kartu member? (ya/tidak): ")

# # Cek usia pembeli
# if usia_pembeli < 18:
#     print("Maaf usia anda belum mencukupi")
# else:
#     # Hitung diskon
#     diskon = 0
#     if kartu_member == "ya":
#         diskon += 15
#     if total_belanja > 500000:
#         diskon += 10

#     # Hitung total harga setelah diskon
#     total_harga_sebelum_diskon = total_belanja
#     total_harga_setelah_diskon = total_belanja - (total_belanja * diskon / 100)

#     # Tampilkan hasil
#     print("Nama Pembeli:", nama_pembeli)
#     print("Diskon yang didapatkan:", diskon, "%")
#     print("Total harga sebelum diskon: Rp", total_harga_sebelum_diskon)
#     print("Total harga setelah diskon: Rp", total_harga_setelah_diskon)
