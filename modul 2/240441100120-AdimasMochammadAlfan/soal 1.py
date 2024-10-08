nama = str(input("masukkan nama = "))
nim = str(input("masukkan nim = "))
nilai_UTS = int(input("masukkan nilai UTS = "))
nilai_UAS = int(input("masukkan nilai UAS = "))
hasil_nilai = (nilai_UTS + nilai_UAS) / 2
print("masukkan nama", nama)
print("masukkan nim", nim)
print("Nilai rata-rata", nama, "adalah", hasil_nilai)
if hasil_nilai <= 100 and hasil_nilai >= 81:
    print("A")
elif hasil_nilai <= 80 and hasil_nilai >= 71:
    print("B")
elif hasil_nilai <= 70 and hasil_nilai >= 61:
    print("C")
elif hasil_nilai <= 60 and hasil_nilai >= 51:
    print("D")
elif hasil_nilai <= 40 and hasil_nilai == 0:
    print("E")
else:
    print("nilai berlebih/nilai tidak sesuai")