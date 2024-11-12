# # soal 1
angka = int(input("masukkan ukuran : "))
bentuk = input("masukkan bentuk (X/O) : ") 

if bentuk.lower() == "x" : # percabangan
    for atas in range(1, angka +1): # perulangan
      for j in range (angka - atas):
        print('  ', end='')
      for k in range (1, atas+1):
        print(bentuk, end='   ')
      print()
    for bawah in range(1, angka +1):
      for k in range (1, bawah+1):
        print('  ',end='')
      for J in range (angka - bawah):
        print(bentuk, end='   ')
      print()
elif bentuk.lower() == "o" :
    for atas in range(1, angka +1):
      for j in range (angka - atas):
        print('  ', end='')
      for k in range (1, atas+1):
        print(bentuk, end='   ')
      print()
    for bawah in range(1, angka +1):
      for k in range (1, bawah+1):
        print('  ',end='')
      for J in range (angka - bawah):
        print(bentuk, end='   ')
      print()
else:
  print("maaf huruf harus (x dan o) selain itu tidak bisa")

 # #saol 2
desimal = float(input("masukkan bilangan desimal : "))

biner =""
n = desimal
panjang_biner = 0

while n > 0:
    panjang_biner += 1
    n //= 2
    biner = str(n % 2) + biner

print("hasil bilangan ke biner : ", biner)

print("pola segitiga :")
for atas in range (1, panjang_biner +1):
  for j in range (panjang_biner - atas):
    print('  ', end='')
  for k in range (1, atas+1):
    print(biner[k-1],end='   ')
  print()
    
# #soal 3
gaji_harian = 100000
total_gajimingguan = 0
total_gajilembur = 0
total_lemburmingguan = 0

for hari in range(7):
    lembur_hari = int(input(f"Masukkan jam lembur untuk hari ke-{hari + 1}: "))
    gaji_hari = gaji_harian
    
    if lembur_hari > 8:
        print("Lembur melebihi batas, tidak akan dihitung.")
        lembur_hari = 0
    elif total_lemburmingguan + lembur_hari >= 40:
        print("Total jam lembur dalam seminggu sudah mencapai batas, lembur dihentikan.")
        lembur_hari = 0
    else:
        if lembur_hari == 0:
            tambahan_lembur = 0
        elif 1 <= lembur_hari <= 3:
            tambahan_lembur = lembur_hari * 25000
        elif lembur_hari == 4:
            tambahan_lembur = 100000
        elif lembur_hari == 6:
            tambahan_lembur = 200000
        elif lembur_hari == 8:
            tambahan_lembur = 300000
        
        total_lemburmingguan += lembur_hari
        total_gajilembur += tambahan_lembur
        gaji_hari += tambahan_lembur

    total_gajimingguan += gaji_hari
    
    print(f"Lembur hari ke-{hari + 1}: {lembur_hari} jam, Gaji hari ke-{hari + 1}: Rp{gaji_hari}")


print("\nTotal lembur selama satu minggu:", total_lemburmingguan, "jam")
print("Total gaji lembur: Rp", total_gajilembur)
print("Total gaji mingguan tanpa lembur: Rp", gaji_harian * 7)
print("Total gaji mingguan termasuk lembur: Rp", total_gajimingguan + (gaji_harian * 7))
