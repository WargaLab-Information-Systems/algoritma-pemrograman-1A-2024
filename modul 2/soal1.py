nama = input("masukkan nama :")
nim = input("masukkan nim :")
nilai_uts = int(input("masukkan nilai uts :"))
nilai_uas = int(input("masukkan nilai uas :"))

total_nilai = (nilai_uts + nilai_uas ) / 2

if 100 >= total_nilai >= 81:
    nilai = 'A'
elif 80 >= total_nilai >= 71:
    nilai = 'B'
elif 70 >= total_nilai >= 61:
    nilai = 'C'
elif 60 >= total_nilai >= 41:
    nilai = 'D'
elif 40 >= total_nilai >= 0:
    nilai = 'E'
else:
    nilai = "masukkan ulang nilai"

print ("nilai rata rata : ",total_nilai)
print ("nilai anda : ",nilai)