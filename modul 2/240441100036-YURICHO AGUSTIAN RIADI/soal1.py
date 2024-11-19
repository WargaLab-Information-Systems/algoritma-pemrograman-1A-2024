nama =input("masukkan nama: ")
nim =input("masukkan NIM: ")
nilai_UTS =int(input("masukkan nilai UTS (0-100): "))
nilai_UAS =int(input("masukkan nilai UAS (0-100): "))

#menghitung nilai rata-rata
nilai_rata =(nilai_UTS + nilai_UAS) /2

# Menentukan rata-rata nilai
if nilai_rata >= 81 <100:
    print("nilai: A")
elif nilai_rata >= 71 <80:
    print("nilai: B")
elif nilai_rata >= 61 <70:
    print("nilai: C")
elif nilai_rata >= 41 <60:
    print("nilai: D")
else:
    print("nilai: E")


