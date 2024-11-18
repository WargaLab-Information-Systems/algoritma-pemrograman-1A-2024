#soal 1
Nama = input("Masukkan nama:")
Nim = int(input("Masukkan nim kamu:"))
Nilai_UTS = int(input("Masukkan Nilai UTS"))
Nilai_UAS = int(input("Masukkan Nilai UAS"))

# Mencari rumus
Nilai_rata_rata = (Nilai_UTS + Nilai_UAS)/2
if Nilai_rata_rata >= 81 <= 100:
    print("Anda mendapatkan nilai A")
elif Nilai_rata_rata >= 71 <= 80:
    print("Anda mendapatkan nilai B")
elif Nilai_rata_rata >= 61 <= 70:
    print("Anda mendapatkan nilai C")
elif Nilai_rata_rata >= 41 <= 60:
    print("Anda mendapatkan nilai D")
else:
    print("Anda mendapatkan nilai E")

# Menampilkan hasil
print("Masukkan nama", Nama)
print("Nim anda :", Nim)
print("Nilai rata rata anda", Nilai_rata_rata)

#soal 2
#skor dan ipk jaka
nama_jaka = "jaka"
score_jaka = 1100
ipk_jaka = 3.5

#skor dan ipk ida
nama_ida = "ida"
score_ida = 1000
ipk_ida = 3.5

#Persyaratan beasiswa
skor_minimal = 1100
ipk_minimal = 3.0

#Memeriksa kelayakan Jaka
if score_jaka > skor_minimal and ipk_jaka >= ipk_minimal:
    print(f"{nama_jaka} memenuhi persyaratan beasiswa.")
else:
    print(f"{nama_jaka} tidak memenuhi persyaratan beasiswa.")
    
if score_ida > skor_minimal and ipk_ida >= ipk_minimal:
    print(f"(nama_ida) memenuhi persyaratan beasiswa.")
else:
    print(f"{nama_ida} tidak memenuhi persyaratan beasiswa.")
    
#soal 3
umur = int(input("Masukkan umur: "))

if umur >= 18:
    bb = int(input("Masukkan berat badan (kg): "))
    tb = int(input("Masukkan tinggi badan (cm): "))
    
# Rumus Konversi tinggi dari cm kem yg ada di google
    tb_mtb = tb / 100

# Rumus Hitung BMI yang ada di google
    bmi = bb / (tb_mtb * tb_mtb)

    if bmi < 18.5:
        kategori = "Kurus"
    elif bmi <= 24.9:
        kategori = "Normal"
    elif bmi <= 29.9:
        kategori = "Gemuk"
    else:
        kategori = "Obesitas"
    print("BMI = {bmi:.2f}")
    print(f"Kategori: {kategori}")
else:
    print("Maaf, dokter Sumanto hanya memeriksa pasien berusia 18 tahun ke atas")
    
#soal 4
tahun = int(input("Masukkan tahun: "))

# Rumus tahun kabisat:
# Jika "tahun" tidak habis dibagi angka 100 atau angka 400,
# tetapi habis dibagi dengan angka 4 maka tahun tersebut adalah
# tahun kabisat.

#jika tahun ini di bagi 100 tidak hbs atau tahun dibagi 400 tdk ada sisa dan
#tahun dibagi 4 ada sisa maka hasilnya kabisat

if (tahun % 100 != 0 or tahun % 400 != 0) and tahun % 4 == 0:
    print(f"Tahun (tahun) adalah tahun kabisat")
else:
    print(f"Tahun (tahun) bukanlah tahun kabisat")

#soal 5
# Dapatkan input pengguna
nama_pembeli = input("Masukan nama pembeli: ")
usia_pembeli = int(input("Masukan usia pembeli: "))
member = input("Apakah pembeli memiliki kartu member? (y/tidak): ")
total_belanja = int(input("Masukan total belanja anda:"))

# Inisialisasi total diskon
total_diskon = 0
if member == "y":
    total_diskon += 15
if total_belanja > 500000:
    total_diskon += 10

diskon = total_belanja * total_diskon / 100 
total_harga_diskon = total_belanja - diskon

# Jika usia pembeli dibawah 18 tahun , maka tidak akan menjalankan proses transaksi
if usia_pembeli < 18:
    print("Maaf usia anda belum mencukupi")
else:
    print(f"nama pembeli:{nama_pembeli}")
    print(f"diskon yang anda dapatkan:{total_diskon}%")
    print(f"total harga sebelum diskon:{total_belanja}")
    print(f"total harga setelah diskon:{total_harga_diskon}")