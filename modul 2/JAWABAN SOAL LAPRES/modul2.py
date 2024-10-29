# # # # Tugas 1
# nama = input("Masukkan Nama: ")
# nim = int(input("Masukkan NIM: "))
# nilai_uts = int(input("Masukkan Nilai UTS"))
# nilai_uas = int(input("Masukkan Nilai UAS"))

# nilai_rata_rata = (nilai_uts+nilai_uas) / 2
# print("NAMA Anda :", nama)
# print("NIM Anda :", nim)
# print("Nilai rata-rata nilai anda", nilai_rata_rata)

# if nilai_rata_rata <=81 and nilai_rata_rata >=100  :
#     print ("Anda mendapatkan nilai A")
# elif nilai_rata_rata >=80 <= 71:
#     print ("Anda mendapatkan nilai b")
# elif nilai_rata_rata >=70 <= 61:
#     print ("Anda mendapatkan nilai C")
# elif nilai_rata_rata >=60 <= 41:
#     print ("Anda mendapatkan nilai D")
# else:
#     print ("Anda mendapatkan nilai E")


# # # # # Tugas 2
# skor_jaka = int(input("silahkan masukkan nilai jaka : "))
# ipk_jaka = float(input("masukkan nilai ipk jaka : "))
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



# tugas nomer 3 
# # BMI (Body Massa Index) 
# umur_pasien = 18 
# kurus = 18.5 
# normal = 24.9 
# gemuk = 29.9 
# obesitas = 30 
# umur = int(input("masukkan umur Anda: ")) 
# if umur <= 18 : 
#     print("Pak sumanto hanya memeriksa pasien dewasa") 
# else : 
#     berat = float(input("Masukkan berat badan : ")) 
#     tinggi = float(input("Masukkan tinggi badan : ")) 
#     bmi = berat//(tinggi*tinggi) 
#     if bmi < 18.5: 
#         print(f"bmi (body massa index) {bmi} Anda Kurus") 
#     elif bmi <= 24.9: 
#         print(f"bmi (body massa index) {bmi} Anda Normal") 
#     elif bmi <= 29.9: 
#         print(f"bmi (body massa index) {bmi} Anda Gemuk") 
#     else: 
#         print(f"bmi (body massa index) {bmi} Anda Obesitas")



# # # # Tugas 4
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

# kartu member diskon 15%
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
#     hasil_diskon = total_belanja * (1 - diskon / 100)
#     print(f"Nama pembeli: {nama}")
#     print(f"Total belanja sebelum diskon: {total_belanja:}Rp")
#     print(f"Diskon yang didapatkan: {diskon}%")
#     print(f"Total harga setelah diskon: {hasil_diskon:}Rp")
# else:
#     print("mohon maaf anda belum memenuhi kriteria")
