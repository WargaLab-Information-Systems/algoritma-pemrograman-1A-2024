# #nomor 1

# angka = int(input("masukkan angka yang anda inginkan : "))
# bentuk = input("masukkan bentuk yang diinginkan : ")

# for i in range(1, angka +1):
#   for j in range (angka - i):
#     print(' ', end=" " )
#   for k in range (1, i+1):
#     print(bentuk, end="   ")
#   print()

# for i in range(1, angka +1):
#   for j in range (1, i+1):
#     print(' ',end=" ")
#   for k in range (angka - i):
#     print(bentuk, end="   ")
#   print()


# #nomor 2


desimal = float(input("Masukkan bilangan desimal: "))

biner = ''
while desimal > 0:
    desimal //= 2
    biner = str(desimal % 2) + biner
  
for i in range(len(biner)):
    for j in range(i + 1):
          print(biner[j], end= " ")
    print()

#nomor 3


waktu = 0
lembur = 0
totallembur= 0
totaljam = 0
gajiharian = 100000
for i in range(1, 8):
    if totaljam >= 40:
        lembur+=0
    print(f"apakah anda lembur dihari ke-{i}? (ya/tidak)")
    kerjalembur = str(input("Jawaban anda: "))
    if kerjalembur == "ya":
        waktu = int(input(f"Berapa lama anda kerja lembur hari ke-{i}: "))
        if waktu < 4:
            lembur = (25000 * waktu)
        elif waktu == 4 or waktu == 5:
            lembur = 100000
        elif waktu == 6 or waktu == 7:
            lembur = 200000
        elif waktu == 8:
            lembur = 300000
        else:
            lembur = 0
            print("waktu lembur melebihi batas, tidak di hitung")
        print(f"total waktu {waktu} dan gaji {lembur}")
        totallembur += lembur
        totaljam += waktu
        print()
    if kerjalembur == "tidak":
        print(f"anda tidak lembur pada hari ke-{i}")
        print()
print()
total_gajiharian= gajiharian*7
total_gajiharian_serta_lembur = total_gajiharian + totallembur

print(f"anda lembur selama {totaljam} jam dalam 1 minggu.")
print(f"total gaji lembur anda adalah Rp. {totallembur} ")
print(f"total gaji tanpa lembur adalah Rp. {total_gajiharian}")
print(f"total gaji harian dan lembur adalah Rp. {total_gajiharian_serta_lembur}")