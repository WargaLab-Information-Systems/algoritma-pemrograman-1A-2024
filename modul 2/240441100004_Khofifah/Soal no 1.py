nama = str(input("Masukkan Nama anda:"))
NIM = str(input("Masukkan NIM anda:"))
# nilai_UTS = int(input("Masukkan nilai UTS anda:"))
# nilai_UAS = int(input("Masukkan nilai UAS anda:"))
rata_rata =float(input("Masukkan rata_rata anda:"))
print("Nama anda", nama)
print("NIM adna", NIM)
print(f"Rata-Rata nilai anda adalah = {rata_rata}" )
if rata_rata <= 100 and rata_rata >=80:
    print("Anda mendapatkan nilai A")
elif rata_rata <= 80 and rata_rata >= 71:
    print("Anda mendapatkan nilai B")
elif rata_rata <= 70 and rata_rata >= 61:
    print("Anda mendapatkan nilai C")
elif rata_rata <= 60 and rata_rata >= 41:
    print("Anda mendapatkan nilai D")
elif rata_rata <= 40 and rata_rata >= 0:
    print("Anda mendapatkan nilai E")
else:
    print("Nilai yang anda masukkan salah")
