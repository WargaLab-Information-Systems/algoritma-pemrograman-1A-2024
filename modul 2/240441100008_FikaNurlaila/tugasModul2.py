
# script penyeleksian kondisi secara dinamis (di isi oleh pengguna)
# ketentuan:
# 100 – 81 = A
# 80 – 71 = B
# 70 – 61 = C
# 60 – 41 = D
# 40 – 0 = E
# print("1. Penyeleksian kondisi secara dinamis")
# nama=str(input("masukkan nama anda: "))
# nim=int(input("masukkan NIM anda: "))
# nilai_uts=int(input("masukkan nilai UTS anda:"))
# nilai_uas=int(input("masukkan nilai UAS anda:"))
rata_rata=int(input("masukkan nilai rata-rata:"))   #rumus rata-rata 
print()
# print("NAMA :",nama)
# print("NIM :",nim)
# proses penentuan nilai 
if rata_rata >=81  <= 100:
    print("nilai rata rata anda adalah :",rata_rata)
    print("selamat!! anda mendapatkan nilai A ")
elif rata_rata >=71 <= 80:
    print("nilai rata rata anda adalah :",rata_rata)
    print("selamat! anda mendapatkan nilai B")
elif rata_rata >=61 <= 70:
    print("nilai rata rata anda adalah :",rata_rata)
    print("anda mendapatkan nilai C")
elif rata_rata >=41 <= 60:
    print("nilai rata rata anda adalah :",rata_rata)
    print("anda mendapatkan nilai D")
elif rata_rata >=0 <= 40:
    print("nilai rata rata anda adalah :",rata_rata)
    print("anda mendapatkan nilai E")
else:
    print("nilai rata rata anda adalah :",rata_rata)
    print("nilai anda tidak valid")
print()


print("2. menentukan siapa yang bisa lolos beasiswa")
# Diketahui:
# syarat lulus skor > 1100 dan ipk min 3.0
nama_jaka = "Jaka"
skor_jaka = 1100
ipk_jaka = 3.5
nama_ida = "Ida"
skor_ida = 1000
ipk_ida = 3.5
# proses cek lulus persyaratan beasiswa
if skor_jaka > 1100 and ipk_jaka >= 3.0:
    print(nama_jaka, "lulus persyaratan beasiswa.")
elif skor_ida > 1100 and ipk_ida >= 3.0:
    print(nama_ida, "lulus persyaratan beasiswa.")
else:
    print("Tidak ada yang lulus persyaratan beasiswa.")
print()


# (Kurus <18.5)
# (Normal <=24.9)
# (Gemuk <=29.9)
# (Obesitas >=30)
print("3. Menghitung BMI (Body Mass Index) diatas umur 18 tahun")
nama=str(input("masukkan nama anda: "))
usia=int(input("masukkan usia anda: "))
# proses penentuan nilai 
if usia <= 18:
    print(" maaf !!!! program ini hanya berlaku pada umur 18 keatas ")
else: 
    bb=float(input("masukkan berat badan anda (kg): "))
    tb=float(input("masukkan tinggi badan anda (m2):"))
    bmi=bb/(tb**2)
    print()
    print("NAMA :",nama)
    print("Berat Badan (kg):",bb)
    print("Tinggi Badan (m2):",tb)
    if bmi <18.5:
        print("BMI anda adalah :",bmi)
        print("anda kurus")
    elif bmi >=18.5 <=24.9:
        print("BMI anda adalah :",bmi)
        print("anda normal")
    elif bmi >24.9 <=29.9 :
        print("BMI anda adalah :",bmi)
        print("anda gemuk")
    else :
        print("BMI anda adalah :",bmi)
        print("anda obesitas")
print()


print("4. menentukan tahun kabisat dari pengguna")
tahun = int(input("Masukkan tahun: "))
# proses Mengecek tahun kabisat
if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
    print(tahun, "adalah tahun kabisat.")
else:
    print(tahun, "bukan tahun kabisat.")
print()


print("5. membuat kasir sederhana di bar")
nama_pembeli = input("Masukkan nama pembeli: ")
usia_pembeli = int(input("Masukkan usia pembeli: "))
# Mengecek apakah usia di bawah 18 tahun
if usia_pembeli < 18:
    print("Maaf, usia anda belum mencukupi.")
else:
    diskon = 0
    total_belanja = int(input("Masukkan total belanja : "))
    if total_belanja < 500000:
        print("Minimal pembelanjaan rp.400.000")
    else:
        diskon = diskon + 10  # Diskon belanja lebih dari Rp500.000
        kartu_member = input("Apakah anda memiliki kartu member? (ya/tidak): ")
        if kartu_member == "ya":
            diskon = diskon + 15

            # diskon member

            total_harga_sebelum_diskon = total_belanja
            total_harga_setelah_diskon = total_harga_sebelum_diskon * (1 - (diskon / 100))
            print()
            # Menampilkan hasil
            print("RINCIAN PEMBELI")
            print("Nama Pembeli:", nama_pembeli)
            print("Diskon yang didapatkan:", diskon, "%")
            print("Total harga sebelum diskon: Rp", total_harga_sebelum_diskon)
            print("Total harga setelah diskon: Rp", total_harga_setelah_diskon)
