# SOAL NO 1

nama = input("Masukkan Nama: ")
nim = int(input("Masukkan NIM: "))
nilai_uts = int(input("Masukkan Nilai UTS"))
nilai_uas = int(input("Masukkan Nilai UAS"))

nilai_rata_rata = (nilai_uts+nilai_uas) / 2
print("NAMA Anda :", nama)
print("NIM Anda :", nim)
print("Nilai rata-rata nilai anda", nilai_rata_rata)

if nilai_rata_rata >=81 :
    print ("Anda mendapatkan nilai A")
elif nilai_rata_rata >=71 :
    print ("Anda mendapatkan nilai b")
elif nilai_rata_rata >=61 :
    print ("Anda mendapatkan nilai C")
elif nilai_rata_rata >=41 :
    print ("Anda mendapatkan nilai D")
else:
    print ("Anda mendapatkan nilai E")



