
# membuat belah ketupat
karakter = str (input ("pilih karakter ( O / X ):"))
n = int (input("masukkan size: "))
while karakter !=  "X"  and karakter != "O":
    print("bukan karakter pilihan")
    karakter = str (input ("pilih karakter ( o/x ):"))
for i in range (n):
    for j in range (n -i -1):
        print(" ", end="")
    for j in range (i + 1):
        print (karakter, end=" ")
    print()
for i in range (n-1):
    for j in range (i +1):
        print(" ", end="")
    for j in range (n -i-1):
        print(karakter, end=" ")
    print()


# mengubah desimal ke biner
desimal=int(input("masukkan bilangan desimal:"))
biner=""
while desimal >0 :
    total = desimal % 2
    biner = str (total) + biner
    print(biner)
    desimal = desimal // 2


# menghitung uang lembur
gaji_per_hari = 100000
total_lembur = 0
total_gaji_lembur=0
# Input jam lembur untuk 7 hari
for i in range(1,7+1):
    jam = int(input(f"Masukkan jam lembur hari ke-{i}: "))

    # Batas lembur
    if jam > 8:
        print(f"Hari {i}: Lembur melebihi batas, tidak dihitung.")
        jam = 0  # Lembur akan masuk kedalam 8 jam, dan jika lebih dari 8 jam tidak dihitung
    elif total_lembur + jam > 40:
        print("Total jam lembur dalam seminggu sudah mencapai 40 jam, lembur dihentikan.")
        jam = 0  # Lembur dihentikan setelah 40 jam
        
    if jam == 0:
        gaji_lembur_hari = 0
    elif jam < 4:
        gaji_lembur_hari = jam * 25000
    elif jam == 4:
        gaji_lembur_hari = 100000
    elif jam == 5:
        gaji_lembur_hari = 150000
    elif jam == 6:
        gaji_lembur_hari = 200000
    elif jam == 7:
        gaji_lembur_hari = 250000
    elif jam == 8:
        gaji_lembur_hari = 300000

    # Tampilkan hasil harian
    print(f"Hari {i}: Jam Lembur = {jam}, Gaji Lembur = Rp{gaji_lembur_hari}")

    # Update total lembur dan gaji lembur
    total_lembur += jam
    total_gaji_lembur += gaji_lembur_hari

# Hitung total gaji mingguan
total_gaji_tanpa_lembur = gaji_per_hari * 7
total_gaji_mingguan = total_gaji_tanpa_lembur + total_gaji_lembur

# Tampilkan hasil total
print()
print("TOTAL GAJI MINGGUAN")
print(f"Total Lembur Selama Satu Minggu: {total_lembur} jam")
print(f"Total Gaji Lembur: Rp{total_gaji_lembur}")
print(f"Total Gaji Mingguan Tanpa Lembur: Rp{total_gaji_tanpa_lembur}")
print(f"Total Gaji Mingguan Termasuk Lembur: Rp{total_gaji_mingguan}")
