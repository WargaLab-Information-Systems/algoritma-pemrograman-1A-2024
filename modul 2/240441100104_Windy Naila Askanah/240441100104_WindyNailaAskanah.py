# nomor 1

# nama = (input("masukkan nama : "))
# nim = int(input("masukkn nim : "))
# nilaiuts= int(input("masukkan nilai uts : "))
# nilaiuas = int(input("masukkan nilai uas : "))
# ratarata = (nilaiuts+nilaiuas)/2

# print("nama anda : " , nama)
# print("nim anda : " , nim)
# print("nilai rata rata anda : " , ratarata)

# if ratarata  >=81 and ratarata <= 100  :
#     print("predikat anda adalah A")
# elif ratarata >=71 and ratarata <= 80:
#     print("predikat anda adalah B")
# elif ratarata >=61 and ratarata <= 70:
#     print("predikat anda adalah C")
# elif ratarata >=41 and ratarata <= 60:
#     print("predikat anda adalah D")
# elif ratarata >=0 and ratarata <= 40:
#     print("predikat anda adalah E")
# else:
#     print("nilai anda melebihi limit")


# #  nomor 2

# skorjaka=1100
# ipkjaka=3.5
# skorida=1000
# ipkida=3.5

# skorjaka = int(input("masukkan skor yang dimiliki jaka : "))
# ipkjaka = float(input("masukkan ipk yang berhasil didapat jaka : "))
# skorida = int(input("masukkan skor yang dimiliki ida : "))
# ipkida = float(input("masukkan ipk yang berhasil didapat ida : "))

# skorlulus=1100
# ipklulus=3.0

# if (skorjaka > skorlulus) and (ipkjaka > ipklulus):
#     print('jaka lulus persyaratan beasiswa')
# else:
#     print('jaka tidak lulus persyaratan beasiswa')

# if (skorida > skorlulus) and (ipkida > ipklulus):
#     print('ida lulus persyaratan beasiswa')
# else:
#     print('ida tidak lulus persyaratan beasiswa')


# # nomor 3

# beratbadan = int(input("Masukkan berat badan pasien (kg): ")) 
# tinggibadan = float(input("Masukkan tinggi badan pasien (m): ")) 
# umur = int(input("masukkan umur pasien: "))
 
# # Hitung BMI 
# bmi = (beratbadan / tinggibadan**2)
 
# # Cetak hasil BMI 
# print("BMI pasien:", bmi) 
 
# # Periksa kategori BMI 
# if bmi <= 18.5: 
#    print("Kategori BMI: Kurus") 
# elif bmi <= 24.9: 
#     print("Kategori BMI: Normal") 
# elif bmi <= 29.9: 
#     print("Kategori BMI: Gemuk") 
# else: 
#     print("Kategori BMI: Obesitas")


# # nomor 4


# tahun = int(input("Masukkan Tahun: "))

# if tahun % 4 != 0:
#     print(f" {tahun}  Bukan Tahun kabisat") 
# elif tahun % 100 != 0:
#     print(f" {tahun} Adalah Tahun kabisat") 
# elif tahun % 400 != 0 :
#     print(f" {tahun}  Bukan Tahun kabisat") 
# else:
#     print(f" {tahun} Adalah Tahun kabisat")

# nomor 5


# print("***selamat datang di naila shop***")
# nama = input("Masukkan nama pembeli: ")
# usia = int(input("Masukkan usia pembeli: "))
# total_harga = int(input("Masukkan total harga: "))
# kartu_member = input("Apakah anda memiliki kartu member? (ya/tidak): ")

# if usia < 18:
#     print("Maaf, usia anda belum mencukupi.")
# else:
#     diskon = 0
    
 
#     if kartu_member == 'ya' or kartu_member == 'Ya':
#         diskon = total_harga * 0.15
#     elif total_harga > 500000:
#         diskon = total_harga * 0.10
    
#     total_setelah_diskon = total_harga - diskon           
    
#     print("Nama Pembeli:", nama)
#     print("Diskon yang didapatkan: Rp", diskon)
#     print("Total harga sebelum diskon: Rp", total_harga)
#     print("Total harga setelah diskon: Rp", total_setelah_diskon)         



