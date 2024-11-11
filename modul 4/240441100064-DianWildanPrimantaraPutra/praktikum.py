# soal no 1 ---------------------------------------------------
n = int(input("Masukkan ukuran sisi belah ketupat (n): "))
while True:
    karakter = input("Masukkan karakter (X / O): ")
    
    if karakter == "X" or karakter == "O":
        
        

        # atas belah ketupat
        for i in range(1, n + 1):
            print(' ' * (n - i), end='')
            print(karakter * (2 * i - 1))

        # bawah belah ketupat
        for j in range(n - 1, 0, -1):
            print(' ' * (n - j), end='')  
            print(karakter * (2 * j - 1))  
        break

    else:
        print("Input tidak valid! Silakan masukkan karakter (X / O)")         

# soal no 2 ---------------------------------------------------
n = int(input("Masukkan bilangan desimal: "))
konvers = n
biner = ""

# Mengonversi bilangan desimal ke biner
while n > 0:
    biner = str(n % 2) + biner
    n = n // 2

print("Hasil dari konversi bilangan desimal", konvers, "ke biner adalah", biner)

# pola segitiga
print("\nPola segitiga:")
for i in range(1, len(biner) + 1):
    print(' ' * (len(biner) - i), end='')
    for j in range(i):
        print(biner[j], end=' ')
    print()  



# soal no 3 ---------------------------------------------------
gajiPerHari = 100000
gajiPerMinggu = gajiPerHari * 7
maxLemburMingguan = 40
totalGajiLembur = 0 
totalJamLembur = 0

for hari in range(1, 8):
    jamLembur = int(input(f"Masukkan berapa jam lembur pada hari ke-{hari}: "))

    # Cek jika jam lembur melebihi batas
    if jamLembur > 8:
        print("Lembur melebihi batas, tetapi tetap mendapatkan bonus 300.000.")
        jamLembur = 8  # Hanya hitung 8 jam untuk jam lembur, tetapi tetap berikan bonus

    # Cek jika total jam lembur sudah mencapai batas mingguan
    if totalJamLembur + jamLembur > maxLemburMingguan:
        jamLembur = maxLemburMingguan - totalJamLembur
        if jamLembur < 0:  # Jika sudah mencapai batas, tidak ada lembur yang dihitung
            jamLembur = 0
        print("Sudah mencapai batas lembur, sekarang pulanglah ke rumah.")
        break
    
    totalJamLembur += jamLembur

    # Hitung gaji lembur harian
    gajiLemburHarian = 0

    if jamLembur == 0:
        gajiLemburHarian = 0
    elif jamLembur < 4:
        gajiLemburHarian += 25000 * jamLembur
    elif jamLembur == 4:
        gajiLemburHarian += 100000
    elif jamLembur == 5:
        gajiLemburHarian += 150000
    elif jamLembur == 6:
        gajiLemburHarian += 200000
    elif jamLembur == 7:
        gajiLemburHarian += 200000
    elif jamLembur >= 8: 
        gajiLemburHarian += 300000  # Tetap memberikan bonus 300.000 jika lembur >= 8 jam
    
    totalGajiLembur += gajiLemburHarian
   
    print(f"Hari ke-{hari}: jam lembur {jamLembur}, gaji lembur harian {gajiLemburHarian}")

# Tampilkan total jam lembur
if totalJamLembur < maxLemburMingguan:
    print()
    print("Total jam lembur adalah:", totalJamLembur, "jam")

# Hitung total gaji
totalGajiRegulerLembur = gajiPerMinggu + totalGajiLembur

print()
print("Total gaji hasil lembur: Rp.", totalGajiLembur)
print("Gaji murni tanpa lembur: Rp.", gajiPerMinggu)
print("Total semua gaji       : Rp.", totalGajiRegulerLembur)