#SOAL NO 1
N = int(input("Masukkan ukuran sisi belah ketupat (N): "))
karakter = input("Masukkan karakter untuk pola (contoh: 'X' atau 'O'): ")

# buat pola checkerboard berbentuk belah ketupat
for i in range(N):
    # buat spasi untuk membentuk belah ketupat
    for j in range(N - i - 1):
        print(" ", end="")
    
    # buat pola checkerboard
    for j in range(2 * i + 1):
        if j % 2 == 0:
            print(karakter, end="")
        else:
            print(" ", end="")
    
    print()  

for i in range(N - 2, -1, -1):
    # buat spasi untuk membentuk belah ketupat
    for j in range(N - i - 1):
        print(" ", end="")
    
    # buat pola checkerboard
    for j in range(2 * i + 1):
        if j % 2 == 0:
            print(karakter, end="")
        else:
            print(" ", end="")
    
    print() 



#SOAL NO 2
desimal = int(input("Masukkan bilangan desimal: "))
biner = bin(desimal)[2:]
# hasil
for i in range(1, len(biner) + 1):
    print(biner[:i])


#SOAL NO 3
gaji_harian = 100000
total_gaji_mingguan = 0
total_lembur_mingguan = 0
total_gaji_lembur = 0
total_gaji_tanpa_lembur = 0

for hari in range(1, 8):
    lembur = int(input(f"Masukkan jam lembur hari ke-{hari}: "))
    # gaji tanpa lembur
    total_gaji_mingguan += gaji_harian
    total_gaji_tanpa_lembur += gaji_harian
    if lembur > 8:
        print("Lembur melebihi batas, tidak dihitung.")
        lembur = 0 
    if total_lembur_mingguan + lembur >= 40:
        print("Total jam lembur dalam seminggu sudah mencapai batas 40 jam, lembur dihentikan.")
        lembur = 0 
    # menghitung gaji lembur
    if lembur == 0:
        gaji_lembur = 0
    elif lembur < 4:
        gaji_lembur = lembur * 25000
    elif lembur == 4:
        gaji_lembur = 100000
    elif lembur == 6:
        gaji_lembur = 200000
    elif lembur == 8:
        gaji_lembur = 300000
    # menambahkan gaji lembur ke total
    total_gaji_lembur += gaji_lembur
    total_lembur_mingguan += lembur
    # menampilkan hasil lembur per hari
    print(f"Lembur hari ke-{hari}: {lembur} jam, Gaji lembur: Rp{gaji_lembur}")
#untuk menghitung total gaji mingguan
total_gaji_mingguan = total_gaji_tanpa_lembur + total_gaji_lembur

print(f"\nTotal lembur selama satu minggu: {total_lembur_mingguan} jam")
print(f"Total gaji lembur: Rp{total_gaji_lembur}")
print(f"Total gaji mingguan tanpa lembur: Rp{total_gaji_tanpa_lembur}")
print(f"Total gaji mingguan termasuk lembur: Rp{total_gaji_mingguan}")