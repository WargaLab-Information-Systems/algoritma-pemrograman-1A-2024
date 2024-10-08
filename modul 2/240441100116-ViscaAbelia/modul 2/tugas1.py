#Nilai 100-81 = A
#Nilai 80-71 = B
#Nilai 70-61 = C
#Nilai 60-41 = D
#Nilai 41-0 = E
Nama = str(input("Masukkan Nama "))
NIM = int(input("Masukkan NIM "))
Nilai_UTS = int(input("Masukkan nilai UTS :"))
Nilai_UAS = int(input("Masukkan nilai UAS :"))
Rata_rata = (Nilai_UTS+Nilai_UAS)//2

if (Rata_rata >=81 and Rata_rata <=100):
    print(f"Masukkan Nama {Nama}\nMasukkan NIM {NIM}\nNilai rata-rata nilai anda {Rata_rata}\nAnda mendapatkan Nilai A")
elif (Rata_rata >=71 and Rata_rata <=80):
    print(f"Masukkan Nama {Nama}\nMasukkan NIM {NIM}\nNilai rata-rata nilai anda {Rata_rata}\nAnda mendapatkan Niai B")
elif (Rata_rata >=61 and Rata_rata <=70):
    print(f"Masukkan Nama {Nama}\nMasukkan NIM {NIM}\nNilai rata-rata nilai anda {Rata_rata}\nAnda mendapatkan Niai C")
elif (Rata_rata >=41 and  Rata_rata <=60):
    print(f"Masukkan Nama {Nama}\nMasukkan NIM {NIM}\nNilai rata-rata nilai anda {Rata_rata}\nAnda mendapatkan Niai D")
elif (Rata_rata >=0 and Rata_rata <=40):
    print(f"Masukkan Nama {Nama}\nMasukkan NIM {NIM}\nNilai rata-rata nilai anda {Rata_rata}\nAnda mendapatkan Niai E")
else:
    print("Anda tidak memiliki nilai")