# #soal no 1
# nama = input("Nama :")
# nim = input("NIM :")

# # nilaits = int(input("Nilai uts:"))
# # nilaias = int(input("Nilai uas:"))
# total = int(input("total"))
# if 100 >=  total >= 81:
#   nilai = 'A'
# elif 80 >= total >= 71:
#   nilai = 'B'
# elif 70 >= total >= 61:
#    nilai = 'C'
# elif 60 >= total >= 41:
#    nilai = 'D'
# elif 40 >= total >= 0 :
#     nilai = 'E'
# else :
#     nilai = "eror"
# print (f"nilai rata rata nilai anda:", total)
# print (f"anda mendapatkan nilai:", nilai)


# #soal no 2
# # Persyaratan beasiswa
# skor_minimum = 1100
# ipk_minimum = 3.0

# #DATA JAKA
# jaka_nama = "Jaka"
# jaka_skor = 1100
# jaka_ipk = 3.5
# #CEK KELULUSAN JAKA
# if jaka_skor >= skor_minimum and jaka_ipk >= ipk_minimum:
#     print(f"{jaka_nama} Lulus persyaratan beasiswa.")
#     print(f"Selamat untuk anda {jaka_nama}")
# else:
#     print(f"{jaka_nama} Tidak lulus persyaratan beasiswa.")
#     print("Tetap semangat jangan putus asa!! coba lagi tahun depan")

# #DATA IDA
# ida_nama = "Ida"
# ida_skor = 1000
# ida_ipk = 3.5
# #CEK KELULUSAN IDA
# if ida_skor >= skor_minimum and ida_ipk >= ipk_minimum:
#     print(f"{ida_nama} Lulus persyaratan beasiswa.")
#     print(f"Selamat untuk anda {ida_nama}")
# else:
#     print(f"{ida_nama} Tidak lulus persyaratan beasiswa.")
#     print("Tetap semangat jangan putus asa!! coba lagi tahun depan")



# # #soal no 3
# umur = int(input("masukkan umur anda : "))
# if umur >= 18 :
#     bb = int(input("masukkan berat badan anda : "))
#     tb = int(input("masukkan tinggi badan anda : "))
#     tb_meter = tb / 100
#     bmi = bb / (tb_meter * tb_meter)
#     if bmi <= 18.5 :
#         print("anda kurus")
#     elif bmi <= 24.9 :
#         print("anda normal")
#     elif bmi <= 29.9 :
#         print ("anda gemuk")
#     else :
#         print ("anda obesitas")

#     print ("hasil dari bmi", bmi)
# else :
#     print("maaf umur anda tidak mencukupi")


# #soal no 4
# #jika tahun tidak habis dibagi angka 100 atau angka 400,
# #tetapi habis dibagi dengan angka 4 maka tahun tersebut adalah kabisat
# tahun = int(input("Masukkan tahun: "))
# if (tahun % 100 != 0 or tahun % 400 != 0) and tahun % 4 == 0:
#      print(f"Tahun (tahun) adalah tahun kabisat")
# else:
#      print(f"Tahun (tahun) bukanlah tahun kabisat")



# #soal no 5
# # input total belanja
# total_belanja = int (input("masukkan total belanja anda :"))
# nama = input("masukkan nama anda :")
# member = (input("apakah mempunyai member ?, (ya/tidak) : "))
# usia = int(input("masukkan usia anda :"))

# diskon = 0

# if member == "ya" :
#     diskon += 15

# if total_belanja > 500000:
#     diskon += 10
# harga_diskon = total_belanja - (diskon / 100 * total_belanja)

# if (usia < 18) :
#     print ("maaf usia anda kurang")
# else :
#     print ("nama : ", nama)
#     print ("total belanja anda : ", total_belanja)
#     print ("diskon yang anda dapatkan : ", diskon)
#     print ("total harga setelah diskon : ", harga_diskon)


