# input sesuai contoh
nama = str(input("Masukkan Nama"))
NIM = str(input("Masukkan NIM"))
Nilai_UTS = int(input("Masukkan Nilai UTS:"))
Nilai_UAS = int(input("Masukkan Nilai UAS:"))

# menghitung nilai rata-rata
Rata_rata = (Nilai_UTS + Nilai_UAS) / 2
print(f"Rata rata nilai anda = {Rata_rata} ")

# penyeleksian kondisi menggunakan if-elif
if Rata_rata <= 100 and Rata_rata >= 81:
    print("Anda mendapatkan nilai A")
elif Rata_rata <= 80 and Rata_rata >= 71:
    print("Anda mendapatkan nilai B")
elif Rata_rata <= 70 and Rata_rata >= 61:
    print("Anda mendapatkan nilai C")
elif Rata_rata <= 60 and Rata_rata >= 41:
    print("Anda mendapatkan nilai D")
elif Rata_rata <= 40 and Rata_rata >= 0:
    print("Anda mendapatkan nilai E")
else:
    print("nilai anda melebihi limit")