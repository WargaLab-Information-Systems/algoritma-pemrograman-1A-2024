# Tugas No.1
N = int(input("masukkan ukuran:"))
karakter = input("masukkan karakter:")
for i in range(N-1):
    for j in range(i,N):
        print(' ', end=' ')
    for j in range(i):
        print(karakter, end=' ')
    for j in range(i+1):
        print(karakter, end=' ')
    print()
for i in range(N):
    for j in range(i+1):
        print(' ', end=' ')
    for j in range(i, N-1):
        print(karakter, end=' ')
    for j in range(i,N):
        print(karakter, end=' ')
    print()

# Tugas No.2
# Memasukan input
desimal = float(input("Masukkan bilangan desimal: "))
biner = ""
while desimal > 0:
    desimal //= 2
    biner = str(desimal % 2) + biner
# membuat segitiga
for i in range(1, len(biner) + 1):
    print(biner[:i])


# Tugas No.3

pertanyaan = input("apa kamu lembur?(iya/tidak):")
if pertanyaan == "tidak":
    print("kamu tidak lembur jadi tidak dapat gaji tambahan")
else:
    gaji_lembur = 0
    total_gajilembur = 0
    total_lembur = 0
    hari = int(input("masukkan berapa hari:"))
    for i in range(1,hari+1):
        lembur = int(input(f"hari ke {i} lembur berapa jam?:"))
        if lembur > 8:
            print("lembur melebihi batas, jadi tidak dihitung")
        elif total_lembur+lembur >40:
            print("total lembur lebih 40 jam, program akan berhenti")
            break
        elif lembur <= 3:
             gaji_lembur = 25000*lembur
             total_lembur += lembur
             total_gajilembur += gaji_lembur
             print(f"total lembur hari ke {i},adalah {lembur} jam")
        elif lembur == 4:
             gaji_lembur = 100000
             total_lembur += lembur
             total_gajilembur += gaji_lembur
             print(f"total lembur hari ke {i},adalah {lembur} jam")
        elif lembur == 6:
             gaji_lembur = 200000
             total_lembur += lembur
             total_gajilembur += gaji_lembur
             print(f"total lembur hari ke {i},adalah {lembur} jam")
        elif lembur == 8:
             gaji_lembur = 300000
             total_lembur += lembur
             total_gajilembur += gaji_lembur
             print(f"total lembur hari ke {i},adalah {lembur} jam")
        else:
            gaji_lembur = 0
gaji_reguler = 100000
total_reguler = gaji_reguler*hari
total_reguler_dan_lembur = total_reguler + total_gajilembur
print()
print(f"total lembur dalam {hari}hari adalah {total_lembur}jam")
print(f"total gaji lembur adalah Rp.{total_gajilembur}")
print(f"total gaji reguler adalah Rp.{total_reguler}")
print(f"total gaji reguler ditambah gaji lembur adalah Rp.{total_reguler_dan_lembur}")
     
