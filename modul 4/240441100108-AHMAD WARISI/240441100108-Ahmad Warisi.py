#Soal no 1
n = int(input("Masukkan angka : "))
bentuk=str(input("masukkan bentuk (x/o) : "))
# Bagian atas ketupat (segitiga)
for i in range(n):
    for j in range(n-i-1):
        print("  ", end="")
    for k in range(2*i+1):
        print(bentuk, end=" ")
    print()

# Bagian bawah ketupat (segitiga terbalik)
for i in range(n-2, -1, -1):
    for j in range(n-i-1):
        print("  ", end="")
    for j in range(2*i+1):
        print(bentuk, end=" ")
    print()

#Soal No 2
# Input bilangan desimal
decimal = float(input("Masukkan Bilangan Decimal: "))

# Mengonversi bilangan desimal ke biner
if decimal == 0:
    binar = "0"
else:
    binar = ""
    n = decimal
    while n > 0:
        sisa = n % 2
        binar = str(sisa) + binar
        n = n // 2

# Menampilkan hasil konversi
print("Angka Decimal: ",decimal)
print("Representasi Biner: ",binar)

print("Pola Segitiga:")
suhu = ""
for angka in binar:
    suhu += angka
    print(suhu)

#Soal no 3
# Inisialisasi konstanta
gaji_harian = 100000
lembur_harian_max = 8
lembur_mingguan_max = 40

total_lembur_mingguan = 0
total_uang_lembur = 0

print("Program Penghitung Gaji Mingguan Mas Ironi")
print("=================================================================")

# Proses input dan perhitungan untuk setiap hari
for hari in range(1, 8):
    print("Masukkan jam lembur untuk hari ke-", hari, ": ", end="")
    jam_lembur = int(input())
    
    if jam_lembur < 0:
        print("Jam lembur tidak boleh negatif!")
        continue
    
    # Cek batas lembur harian
    if jam_lembur > lembur_harian_max:
        print("Lembur melebihi batas, tidak dihitung.")
        continue
        
    # Cek batas lembur mingguan
    if total_lembur_mingguan + jam_lembur > lembur_mingguan_max:
        print("Total lembur mingguan sudah mencapai batas 40 jam!")
        break
        
    # Hitung uang lembur
    uang_lembur = 0
    if jam_lembur == 0:
        uang_lembur = 0
    elif jam_lembur < 4:
        uang_lembur = jam_lembur * 25000
    elif jam_lembur == 4:
        uang_lembur = 100000
    elif jam_lembur == 5:
        uang_lembur = 150000
    elif jam_lembur == 6:
        uang_lembur = 200000
    elif jam_lembur == 7:
        uang_lembur = 250000
    elif jam_lembur == 8:
        uang_lembur = 300000

    
    
    total_lembur_mingguan += jam_lembur
    total_uang_lembur += uang_lembur
    print("Uang lembur hari ke-",hari, ": Rp",uang_lembur)

# Hitung total gaji
total_gaji_tanpa_lembur = gaji_harian * 7
total_gaji_dengan_lembur = total_gaji_tanpa_lembur + total_uang_lembur

# Cetak hasil
print("=================================================================")
print("Total jam lembur selama seminggu: ",total_lembur_mingguan,"jam")
print("Total uang lembur: Rp " ,total_uang_lembur)
print("Total gaji mingguan tanpa lembur: Rp",total_gaji_tanpa_lembur)
print("Total gaji mingguan termasuk lembur: Rp",total_gaji_dengan_lembur)