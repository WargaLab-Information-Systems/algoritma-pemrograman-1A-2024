# #soal no 1
# # Meminta input dari pengguna
# n = int(input("Masukkan ukuran (n) yang anda inginkan: "))
# k = str(input("Masukkan karakter yang anda inginkan (contoh: X atau O): "))

# # Bagian atas belah ketupat
# for i in range(n):
#     for j in range(n - i - 1): 
#         print(" ", end=" ") 
#     for y in range(2 * i + 1):
#         print(k, end=" ")
#     print()  

# # Bagian bawah belah ketupat
# for i in range(n - 2, -1, -1):
#     for j in range(n - i - 1): 
#         print(" ", end=" ")  
#     for y in range(2 * i + 1):
#         print(k, end=" ")
#     print()  

# #soal no 2 

# Input bilangan desimal dari pengguna
# desimal = int(input("Masukkan bilangan desimal: "))

# Mengonversi desimal ke biner 
# biner = ""
# while desimal > 0:
#     biner = str(desimal % 2) + biner
#     desimal //= 2

# # Menampilkan hasil konversi
# print("Hasil konversi ke biner:", biner)
# print("Pola segitiga:")

# # Menampilkan pola segitiga
# for i in range(len(biner)):
#     print(biner[:i + 1])


# #soal no 3
# Inisialisasi variabel
total_gaji = 0
total_lembur = 0
gaji_harian = 100000

for hari in range(1, 8):
    lembur = int(input(f"Anda lembur selama berapa jam di hari ke-{hari}?: "))

    if total_lembur >= 40:
        print("Lembur Anda sudah mencapai batas maksimum 40 jam dalam seminggu, lembur dihentikan.")
        gaji_lembur = 0
    else:
        if total_lembur + lembur > 40:
            lembur = 40 - total_lembur
            print(f"Jam lembur hari ke-{hari} dibatasi hingga {lembur} jam.")
        # Hitung gaji lembur berdasarkan jam lembur
        if lembur == 4:
            gaji_lembur = 100000
        elif lembur == 5:
            gaji_lembur = 150000
        elif lembur == 6:
            gaji_lembur = 200000
        elif lembur == 7:  
            gaji_lembur = 250000
        elif lembur == 8:
            gaji_lembur = 300000
        elif lembur < 4:
            gaji_lembur = 25000 * lembur
        else:
            gaji_lembur = 0
            print("Mohon maaf, lembur Anda melebihi batas, dan tidak akan dihitung.")
    
    total_lembur += lembur
    total_gaji += gaji_harian + gaji_lembur
    print(f"Total gaji lembur yang Anda dapat pada hari ke-{hari} adalah: Rp{gaji_lembur}")
    print()
# Hitung dan tampilkan total gaji mingguan
total_gaji_tanpa_lembur = gaji_harian * 7
total_gaji_lembur = total_gaji - total_gaji_tanpa_lembur
print("Total lembur selama satu minggu adalah:", total_lembur, "jam")
print("Total gaji lembur selama satu minggu adalah: Rp", total_gaji_lembur)
print("Total gaji mingguan tanpa lembur adalah: Rp", total_gaji_tanpa_lembur)
print("Total gaji Anda selama 1 minggu termasuk lembur adalah: Rp", total_gaji)
