gaji_harian = 100000

total_lembur = 0
total_gaji_lembur = 0

for i in range(1, 8): #karena 1 minggu ada 7 hari dan index dimulai darin 0, maka dalam range dimulai dari 1 sampai ke 8.
    lembur = float(input(f"Masukkan jam lembur hari ke-{i}: ")) #operator yang digunakan agar kita tidak menginputkan manual dari hari 1 ke 7
    
    if lembur > 8: 
        print("Lembur melebihi batas, tidak dihitung.")
    elif lembur >= 4:
        total_lembur += lembur
        if lembur == 4:
            total_gaji_lembur += 100000
        elif lembur == 6:
            total_gaji_lembur += 200000
        elif lembur == 8:
            total_gaji_lembur += 300000
    elif lembur >= 1:
        total_lembur += lembur
        total_gaji_lembur += lembur * 25000 #jika kurang dari 4, per jam akan ditambahkan 25 ribu
    else:
        print("Tidak ada lembur, tidak ada tambahan.")

if total_lembur > 40:
    print("Total lembur lebih dari 40 jam, lembur dihentikan pada batas 40 jam.")
    total_lembur = 40

total_gaji_reguler = gaji_harian * 7
total_gaji_mingguan = total_gaji_reguler + total_gaji_lembur

print("\n--- Hasil Gaji Mingguan Mas Ironi ---") #\n digunakan untuk menambahkan spasi garis atau mengosongkan 1 line agar terdapat jarak
print(f"Total lembur selama satu minggu: {total_lembur} jam")
print(f"Total gaji lembur: Rp. {total_gaji_lembur}")
print(f"Total gaji mingguan tanpa lembur: Rp. {total_gaji_reguler}")
print(f"Total gaji mingguan termasuk lembur: Rp. {total_gaji_mingguan}")