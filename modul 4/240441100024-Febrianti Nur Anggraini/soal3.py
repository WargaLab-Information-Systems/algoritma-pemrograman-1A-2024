total_gaji_reguler = 100000 * 7  
total_jam_lembur_mingguan = 0
total_gaji_lembur = 0

for hari in range(1,8):
    jam_lembur = int(input(f"Masukkan jam lembur hari ke-{hari}: "))

    if jam_lembur > 8:
        print("Lembur melebihi batas, tidak dihitung.")
        jam_lembur = 0
    elif total_jam_lembur_mingguan + jam_lembur >= 40:
        print("Total lembur mencapai batas mingguan, lembur dihentikan.")
        jam_lembur = 0

    # Hitung gaji lembur
    if jam_lembur == 0:
        gaji_lembur_harian = 0
    elif jam_lembur < 4:
        gaji_lembur_harian = jam_lembur * 25000
    elif jam_lembur == 4:
        gaji_lembur_harian = 100000
    elif jam_lembur == 6:
        gaji_lembur_harian = 200000
    elif jam_lembur == 8:
        gaji_lembur_harian = 300000

    # Tambahkan jam lembur dan gaji lembur harian ke total
    total_jam_lembur_mingguan += jam_lembur
    total_gaji_lembur += gaji_lembur_harian

    print(f"Lembur hari ke-{hari}: {jam_lembur} jam, Gaji lembur: Rp{gaji_lembur_harian}")

# Total gaji mingguan termasuk lembur
total_gaji_mingguan = total_gaji_reguler + total_gaji_lembur

print("\n Total lembur selama satu minggu:", total_jam_lembur_mingguan, "jam")
print("Total gaji lembur selama satu minggu: Rp", total_gaji_lembur)
print("Total gaji mingguan tanpa lembur: Rp", total_gaji_reguler)
print("Total gaji mingguan termasuk lembur: Rp", total_gaji_mingguan)