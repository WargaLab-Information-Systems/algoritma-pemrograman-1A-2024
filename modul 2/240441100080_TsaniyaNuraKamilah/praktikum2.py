# # tugas no.1
# # Diketahui
# # Nilai 100-81 = A
# # Nilai 80-71 = B
# # Nilai 70-61 = C
# # Nilai 60-41 = D
# # Nilai 40-0  = E

# Nama = str(input("masukkan nama:"))
# NIM = int(input("masukkan NIM:"))
# UTS = float(input("masukkan nilai uts:"))
# UAS = float(input("masukkan nilai uas:"))
# # rumus menghitung rata - rata 
# rata_rata = (UTS + UAS)/2
# # menentukan grade menggunakan if-else
# if (rata_rata >=81 and rata_rata <= 100):
#     print(f"masukan {Nama}\nmasukan {NIM}\n nilai rata-rata {rata_rata}\nanda mendapat nilai adalah A")
# elif 71<= rata_rata <= 80:
#     print(f"masukan {Nama}\nmasukan {NIM}\nnilai rata-rata {rata_rata}\nanda mendapat nilai adalah B")
# elif 61 <= rata_rata <= 70:
#     print(f"masukan {Nama}\nmasukan {NIM}\nnilai rata-rata {rata_rata}\nanda mendapat nilai adalah C")
# elif 41 <= rata_rata <= 60:
#     print(f"masukan {Nama}\nmasukan {NIM}\nnilai rata-rata {rata_rata}\nanda mendapat nilai adalah D")
# elif 0 <= rata_rata <= 40:
#     print(f"masukan {Nama}\nmasukan {NIM}\nnilai rata-rata {rata_rata}\nanda mendapat nilai adalah E")
# else:
#     print(f"nilai melebihi limit ")

# # tugas no.2
# # data yang diketahui
# # sekor jaka = 1100
# # ipk jaka = 3.5
# # sekor ida = 1000
# # ipk ida = 3.5
# sekor_jaka = int(input("masukkan sekor jaka:"))
# ipk_jaka = float(input("masukkan ipk jaka:"))
# sekor_ida = int(input("masukkan sekor ida:"))
# ipk_ida = float(input("masukkan ipk ida:"))
# # syarat 
# sekor_minimum = 1100
# ipk_minimum = 3.0

# if sekor_jaka > 1100 and ipk_jaka >= 3.0:
#     print("jaka dinyatakan mendapat beasiswa")
# elif sekor_ida > 1100 and ipk_ida >= 3.5:
#     print("ida dinyatakan mendapat beasiswa")
# else:
#     print("tidak ada yang mendapat beasiswa")

#tugas no.3
# umur = int(input("masukkan umur:"))
# bb = int(input("masukkan berat badan:"))
# tb = float(input("masukan tinggi badan:"))
# #rumus 
# BMI = bb/(tb*tb)
# if umur < 18:
#     print("maaf anda belum cukup umur")
# elif BMI < 18.5:
#     print("badan kurus")
# elif BMI <= 24.9:
#     print("badan normal")
# elif BMI <= 29.9:
#     print("badan gemuk")
# elif BMI >= 30:
#     print("badan obesitas")
# else:
#     print()


# # tugas no.4
# #rumus tahun kabisat = angka tahun habis yang dibagi 400 adalah tahun kabisat 
# tahun = int(input("masukkan tahun:"))
# # menentukan apakah tahun tersebut adalah tahun kabisat atau bukan
# if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
#     print(f"{tahun} adalah tahun kabisat")
# else:
#     print(f"{tahun} bukan termasuk tahun kabisat ")


# tugas no.5
nama_pembeli = str(input("masukkan nama anda:"))
umur = int(input("masukkan umur anda:"))
# seleksi umur
if umur < 18:
    print(f"maaf {nama_pembeli},anda belum cukup umur")
else: 
    print("untuk melakukan pembayaran isi data dibawah ini")
    kartu_member = str(input("apa anda memiliki kartu member?(iya/tidak) :"))
    total_belanja = float(input("masukkan total belanjaan anda:"))
    # seleksi diskon
    diskon10 = total_belanja * (10/100)
    diskon15 = total_belanja * (15/100)
    diskon25 = total_belanja * (25/100)
    # menghitung harga setelah diskon
    hargasetelah_diskon10 = total_belanja - diskon10
    hargasetelah_diskon15 = total_belanja - diskon15
    hargasetelah_diskon25 = total_belanja - diskon25
    if kartu_member == "ya" and total_belanja >= 500000:
        print("halo", nama_pembeli )
        print("anda mendapatkan diskon 25%")
        print("total belanjaan sebesar Rp.", total_belanja)
        print("anda mendapatkan potongan harga Rp.", diskon25)
        print("total akhir harga yg harus dibayar Rp.",hargasetelah_diskon25)
    elif kartu_member =="tidak" and total_belanja >= 500000:
        print("halo", nama_pembeli )
        print("anda mendapatkan diskon 10%")
        print("total belanjaan sebesar Rp.", total_belanja)
        print("anda mendapatkan potongan harga Rp.", diskon10)
        print("total akhir harga yg harus dibayar Rp.",hargasetelah_diskon10)
    elif kartu_member == "iya" and total_belanja <= 500000:
        print("halo", nama_pembeli )
        print("anda mendapatkan diskon 15%")
        print("total belanjaan sebesar Rp.", total_belanja)
        print("anda mendapatkan potongan harga Rp.", diskon15)
        print("total akhir harga yg harus dibayar Rp.",hargasetelah_diskon15)
    else:
        print("halo", nama_pembeli)
        print("anda tidak mendapatkan diskon belanja")
        print("total harga yang harus di bayar adalah Rp.", total_belanja)
