nama = input("Masukkan Nama Anda : ")
nim = input("Masukkan NIM Anda : ")

nilai_uts = int(input ("Masukkan nilai UTS Anda : "))
nilai_uas = int(input ("Masukkan nilai UAS Anda : "))

total_Nilai = nilai_uts + nilai_uas
jumlah_nilai = 2
nilai_rata_Rata = total_Nilai / jumlah_nilai

if nilai_rata_Rata >= 81 and nilai_rata_Rata <= 100:
    print(f"Nilai rata - rata anda adalah {nilai_rata_Rata:.0f}")
    print("nilai kamu A")
elif nilai_rata_Rata >= 71 and nilai_rata_Rata <= 80:
    print(f"Nilai rata - rata anda adalah {nilai_rata_Rata:.0f}")
    print("nilai kamu B")
elif nilai_rata_Rata >= 61 and nilai_rata_Rata <= 70:
    print(f"Nilai rata - rata anda adalah {nilai_rata_Rata:.0f}")
    print("Nilai kamu C")
elif nilai_rata_Rata >= 41 and nilai_rata_Rata <= 60:
    print(f"Nilai rata - rata anda adalah {nilai_rata_Rata:.0f}")
    print("Nilai kamu D")
else: 
    print(f"Nilai rata - rata anda adalah {nilai_rata_Rata:.0f}")
    print("Nilai kamu E")