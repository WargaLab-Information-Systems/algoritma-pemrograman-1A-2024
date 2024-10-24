# nomor 1
# NIM : 096
# mencetak angka 0
print()
for i in range(7):
    if (i == 0 or i == 6):
        print("*" * 7)
    elif (i > 0 and i < 6):
        print("*" + " " * 5 + "*")

# mencetak angka 9
print()
for i in range(7):
    if (i == 0 or i == 3 or i == 6):
        print("*" * 7)
    elif (i == 1 or i == 2):
        print("*" + " " * 5 + "*")
    elif (i == 3 ):
        print("*" * 7)
    elif (i < 6 ):
         print(" " * 6 + "*")
    else:
       print("*" * 7)

# mencetak angka 6
print()
for i in range(7):
    if (i == 0 or i == 3 or i == 6):
        print("*" * 7)
    elif (i < 3 ):
        print("*" * 1 )
    else:
        print("*" + " " * 5 + "*")




# nomor 2

# soal no 2
bilangan_asli = int(input("Masukkan bilangan bulat: "))
bilangan_terbalik = " "

while bilangan_asli > 0:
    angka_terakhir = bilangan_asli % 10
    bilangan_terbalik += str(angka_terakhir)
    bilangan_asli //= 10

print("Bilangan yang dibalik:", bilangan_terbalik)



# soal no 3
# denda penyewaan DVD
while True:
    hari_penyewaan = int(input("Masukkan hari keberapa anda mengembalikan DVD: "))
    denda = 0
    
    if hari_penyewaan > 5:
        denda += (hari_penyewaan - 5) * 2500  
    if hari_penyewaan > 10:
        denda += ((hari_penyewaan - 10) // 5) * 5500  
    
    if denda > 0:
        print(f"Denda keterlambatan total adalah: Rp.{denda:,}")
    else:
        print("Tidak ada denda keterlambatan.")
    
    respons = input("Apakah Anda ingin menghitung lagi? (ya/tidak): ")
    if respons != "ya":
        print("Terima kasih!")
        break