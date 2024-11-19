#soal1
nama=(input("masukkan nama:"))
nim=(input("masukkan NIM:"))
print("Untuk mengetahui nilai anda silahkan lakukan perintah dibawah ini")
uts=int(input("1. Masukkan nilai UTS Anda:"))
uas=int(input("2. Masukkan nilai UAS Anda:"))
#menghitug rata-rata
ratarata=(uts+uas)/2
print(f"halo {nama}")
print(f"NIM anda: {nim} ")
print(f"Nilai rata-rata Anda {ratarata}")
#menentukan nilai
if ratarata <=40:
    print("Anda memperoleh nilai E") 
elif ratarata <=60:
    print("Anda memperoleh nilai D")
elif ratarata <=70:
    print("Anda memperoleh nilai C")
elif ratarata <=80:
    print("Anda memperoleh nilai B")
else:
    print("Anda memperoleh nilai A")

