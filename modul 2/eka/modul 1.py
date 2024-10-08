#input biodata
nama = input("Masukkan NAMA: ")
nim = input("Masukkan NIM: ")
nilai_rata2 = int(input("masukkan nilai rata-rata: "))

#menghitung nilai rata-rata
if nilai_rata2 >= 81:
    nilai_huruf = "A"
elif nilai_rata2 >= 71:
    nilai_huruf = "B"
elif nilai_rata2 >= 61:
    nilai_huruf = "C"
elif nilai_rata2 >= 41:
    nilai_huruf = "D"
else :
    nilai_huruf = "E"

#menampilkan hasil
print("nama", nama)
print("nim",nim)
print("nilai rata-rata:", nilai_rata2)
print("anda mendapat nilai: ",nilai_huruf)

    