nama = "Hasyim Asrofi"
nim = 240441100136
uts = int(input("Masukkan nilai UTS:"))
uas = int(input("masukkan nilai UAS:"))

rata_rata = (uts + uas) / 2

grade = ''
if 81 <= rata_rata <= 100:
    grade = 'A'
elif 71 <= rata_rata <= 80:
    grade = 'B'
elif 61 <= rata_rata <= 70:
    grade = 'C'
elif 41 <= rata_rata <= 60:
    grade = 'D'
elif 0 <= rata_rata <= 40:
    grade = 'E'
else:
    print("maaf inputan anda salah")

print("Nama:", nama)
print("Nim:", nim)
print("Nilai rata-rata  anda", rata_rata)
print("Anda mendapatkan nilai", grade)