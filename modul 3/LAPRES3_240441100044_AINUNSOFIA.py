#NO1
print("membuat program dengan bentuk angka NIM terakhir ")
print ("NIM terakhir saya adalah 044")
print()
#membuat angka 0
for i in range(6):
    for j in range(5):
        if ( i == 0) or (j == 0) or (i == 5) or (j == 4 ):
            print("x",end = " ")
        else:
            print(" ",end = " ")
    print()
print()

#membuat angka 4 yg ke1
for i in range (6):
    for j in range (5):
        if (i<3 and j == 0) or (j == 4) or ( i ==2 ):
            print("x",end = " ")
        else:
            print(" ",end = " ")
    print()
print()

#membuat angka 4 yg ke2
for i in range (6):
    for j in range (5):
        if (i<3 and j == 0) or (j == 4) or ( i ==2 ):
            print("x",end = " ")
        else:
            print(" ",end = " ")
    print()
print()


#NO2
#membantu Sudarso untuk membalikkan urutan dari sebuah angka
angka=int(input("masukkan angka yang ingin diulang: "))
for i in reversed(range(angka + 1)):
    print(i)

#NO3
while True:
    lamasewa = int(input("berapa lama kamu menyewa DVD ini?: "))
    denda = 0
    if lamasewa >= 5:
        denda += (lamasewa - 5) * 2500  
    if lamasewa > 10:
        denda += ((lamasewa - 5) // 5) * 5500
    if denda > 0:
        print(f"kamu dikenai denda Rp.{denda:,}")
    else:
        print("terimakasih telah mengembalikan DVD kami tepat waktu ")
    ulangi = input("Apakah Anda ingin menghitung lagi? (ya/tidak): ")
    if ulangi == "tidak":
        print("Terima kasih!")
        break