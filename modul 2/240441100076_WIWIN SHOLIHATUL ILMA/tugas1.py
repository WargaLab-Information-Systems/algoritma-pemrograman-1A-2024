Nama = input("Masukkan Nama")
Nim = input("Masukkan Nim")
uts = int(input("Nilai uts yang didapatkan: "))
uas = int(input("Nilai uas yang didapatkan: "))
print("Nama:", Nama)
print("Nim:", Nim)

rata_rata = (uts+uas)/ 2
print("Nilai rata-rata yang anda dapatkan adalah:", rata_rata)

if rata_rata > 81 and rata_rata <= 100:
    print("Anda mendapat nilai A")
elif rata_rata > 71 and rata_rata <= 80:
    print("Anda mendapat nilai B")
elif rata_rata > 61 and rata_rata <= 70:
    print("Anda mendapat nilai C")
elif rata_rata > 41 and rata_rata <= 60:
    print("Anda mendapat nilai D")
else:
    print("Anda mendapat nilai E")