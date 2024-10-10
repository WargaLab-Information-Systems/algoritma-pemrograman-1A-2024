nama = input("masukan nama:")
nim = int(input("masukkan nim:"))
masukan_nilai_uts = int(input("masukkan nilai uts:"))
masukan_nilai_uas = int(input("masukan nilai uas:"))

# Rumus mencari nilai rata-rata
nilai_rata_rata = (masukan_nilai_uts + masukan_nilai_uas)/2

if nilai_rata_rata >= 81 < 100:
    print("anda mendapatkan nilai A")
elif nilai_rata_rata >= 71 <= 80:
    print("anda mendapatkan nilai B")
elif nilai_rata_rata >= 61 <= 70:
    print("anda mendapat nilai C")
elif nilai_rata_rata >= 41 <= 60:
    print("anda mendapatkan nilai D")
else:
    print("anda mendapatkan nilai E")


print("nama:", nama)
print("nim anda:", nim)
print("nilai rata rata nilai anda:", nilai_rata_rata)