nama = "zuhdi"
nim = 240441100124
uts = int(input("masukkan nilai uts: "))
uas = int(input("masukkan nilai uas: "))

rata_rata = (uts + uas) / 2

grade =  ''
if 81 <= rata_rata <= 100:
    grade = 'A'
elif 71 <= rata_rata <= 80:
    grade = 'B'
elif 61 <= rata_rata <= 70:
    grade = 'c'
elif 41 <= rata_rata <= 60:
    grade = 'D' 
elif 0 <= rata_rata <=40:
    grade = 'E'
else:
    grade = "Nilai tidak sesuai limit"

print("\nNama:", nama)
print("Nim:", nim)
print("Nilai rata-rata anda", rata_rata)
print("Anda mendapatkan nilai", grade)

# grade = ''
# if 103 <= "rata_rata" <= 105:
#     grade = "kamu mendapatkan nilai bagus sekali"
# print("nilai rata-rata anda", "rata_rata")
