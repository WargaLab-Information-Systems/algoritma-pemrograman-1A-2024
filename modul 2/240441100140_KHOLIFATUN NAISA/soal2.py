nama = (input("masukkan nama anda: "))
skor = int (input("masukkan skor anda: "))
ipk = float (input("masukkan ipk anda: "))

if (skor > 1100 and ipk >= 3.0):
    print (f"selamat {nama} anda terpilih sebagai penerima beasiswa")
else:
    print(f"mohon maaf {nama} belum bisa mendapatkan beasiswa")