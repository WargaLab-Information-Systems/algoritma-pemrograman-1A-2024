gaji_harian = 100000
total_lembur = 0
total_gaji_lembur = 0

for i in range(1, 8):
    lembur = float(input(f"Masukkan jam lembur hari ke-{i}: "))
    
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
        total_gaji_lembur += lembur * 25000 
    else:
        print("Tidak ada lembur, tidak ada tambahan.")

if total_lembur > 40:
    print("Total lembur lebih dari 40 jam, lembur dihentikan pada batas 40 jam.")
    total_lembur = 40

total_gaji_reguler = gaji_harian * 7
total_gaji_mingguan = total_gaji_reguler + total_gaji_lembur

print("\n--- Hasil Gaji Mingguan Mas Ironi ---") 
print(f"Total lembur selama satu minggu: {total_lembur} jam")
print(f"Total gaji lembur: Rp. {total_gaji_lembur}")
print(f"Total gaji mingguan tanpa lembur: Rp. {total_gaji_reguler}")
print(f"Total gaji mingguan termasuk lembur: Rp. {total_gaji_mingguan}")