nama = input("masukkan nama anda: ")
nim = int(input("masukkan nim anda: "))
uts = int(input("masukkan nilai UTS anda: "))
uas = int(input("masukkan nilai UAS anda: "))
rata_rata = (uts+uas)/2
print (f"nilai rata-rata anda adalah: {rata_rata}")
if  81 >= rata_rata >=100 :
    print("ANDA MENDAPATKAN NILAI: A")
elif  80 >= rata_rata  >=71 :
    print("ANDA MENDAPATKAN NILAI: B")
elif  70 >= rata_rata  >=61 :
    print("ANDA MENDAPATKAN NILAI: C")
elif  60 >= rata_rata  >=41 :
    print("ANDA MENDAPATKAN NILAI: D")
elif 40 >= rata_rata  >=0 :
    print("ANDA MENDAPATKAN NILAI: E")
else :
    print("silahkan masukkan data dengan benar")