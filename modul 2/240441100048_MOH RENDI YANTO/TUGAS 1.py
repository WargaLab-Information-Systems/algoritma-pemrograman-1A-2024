# input dimanis
nama = str(input("Masukkan nama : "))
NIM = str(input("Masukkan NIM : "))
UTS = int(input("Masukkan Nilai UTS : "))
UAS = int(input("Masukkan Nilai UAS : "))

print(f"Masukkan Nama {nama}")
print(f"NIM anda : {NIM}")

# mencari rata-rata 
Mean = (UTS + UAS) // 2
print(f"Nilai rata-rata anda adalah : {Mean}")

# perintah if elif
if Mean <= 40:
    print("Anda Mendapatkan Nilai E")
elif Mean <= 60:
    print("Anda Mendapatkan Nilai D")
elif Mean <= 70:
    print("Anda Mendapatkan Nilai C")
elif Mean <= 80:
    print("Anda Mendapatkan Nilai B")
elif Mean <= 100:
    print("Anda Mendapatkan Nilai A")
    
    