# nomor  1
angka = int(input("masukkan ukuran"))
bentuk = input("masukkan bentuk yang di inginkan: ")

for i in range(1, angka +1): 
  for j in range (angka - i):
    print(" ", end=" ")
  for k in range (1, i+1):
    print(bentuk, end="   ")
  print()

for i in range(1, angka +1):
  for j in range (1, i+1):  
    print(" ",end=" ")
  for k in range (angka - i):
    print(bentuk, end="   ")

  print()


# nomor 2
desimal = float(input("Masukkan bilangan desimal: "))

biner = ''
while desimal > 0:
    desimal //= 2
    biner = str(desimal % 2) + biner
  
for i in range(len(biner)):
    for j in range(i + 1):
         print(biner[j], end= " ")
    print()



# nomor 3
gaji_pokok = 100000
total_jam = 0 
total_gaji_lembur = 0 
for hari in range(1, 7+1):
    jam_lembur = int(input(f"Masukkan total jam lembur hari ke {hari}: ")) 

    if jam_lembur > 8:  
        print("Lembur melebihi batas, tidak dihitung.")
        jam_lembur = 0
    elif total_jam + jam_lembur > 40:
        print("Total jam dalam seminggu 40 jam, anda melebihi batas, jam lembur dihentikan.")
        jam_lembur = 0
    else:
        total_jam += jam_lembur

    if jam_lembur == 0:
        gaji = 0
    elif jam_lembur <= 3:
        gaji = jam_lembur * 25000
    elif jam_lembur == 4 or jam_lembur ==5:
        gaji = 100000
    elif jam_lembur ==6 or jam_lembur ==7:
        gaji = 200000
    elif jam_lembur == 8:
        gaji = 300000    

    total_gaji_lembur += gaji 


gaji_per_minggu = gaji_pokok * 7
total_semua_gaji = total_gaji_lembur + gaji_per_minggu

print("Total jam lembur selama 7 hari: ",[total_jam])
print("Total gaji lembur selama 7 hari:", total_gaji_lembur)
print("Gaji pokok selama 1 minggu:", gaji_per_minggu)
print("Total seluruh gaji selama 7 hari:", total_semua_gaji)












