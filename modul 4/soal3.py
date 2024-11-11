# Inisialisasi variabel
gaji_harian = 100000
maks_lembur_per_hari = 8
batas_lembur_mingguan = 40

total_gaji_reguler = 0
total_gaji_lembur = 0
total_jam_lembur = 0

print("Masukkan jam lembur untuk 7 hari")

# Input jam lembur untuk setiap hari dan perhitungan lembur
for hari in range(1, 8):
    lembur = int(input(f"Jam lembur hari ke-{hari}: "))

    # batas lembur harian
    if lembur > maks_lembur_per_hari:
        print("Lembur melebihi batas, tidak dihitung.")
        lembur = 0

    total_jam_lembur += lembur  # Akumulasi total jam lembur mingguan

    # Cek batas lembur mingguan
    if total_jam_lembur > batas_lembur_mingguan:
        print(f"Lembur hari ke-{hari} dihentikan karena melebihi batas mingguan.")
        total_jam_lembur = batas_lembur_mingguan  
        break  # Keluar dari loop karena lembur dihentikan

    # Hitung bonus lembur harian
    if lembur == 0:
        bonus_lembur = 0
    elif lembur <=3:
        bonus_lembur = lembur * 25000
    elif lembur == 4:
        bonus_lembur = 100000
    elif lembur == 5:
        bonus_lembur = 150000
    elif lembur <= 6:
        bonus_lembur = 200000
    elif lembur == 7:
        bonus_lembur = 250000
    elif lembur <=8:
        bonus_lembur = 300000

    total_gaji_lembur += bonus_lembur
    print(f"Bonus lembur hari ke-{hari}: Rp{bonus_lembur:,}")

# Hitung total gaji mingguan tanpa lembur dan dengan lembur
total_gaji_reguler = gaji_harian * 7
total_gaji_mingguan = total_gaji_reguler + total_gaji_lembur

# Cetak hasil akhir
print("--- Rincian Gaji Mingguan ---")
print(f"Total lembur selama 7 hari {total_jam_lembur} jam")
print(f"Total gaji lembur: Rp{total_gaji_lembur:,}")
print(f"Total gaji mingguan tanpa lembur: Rp{total_gaji_reguler:,}")
print(f"Total gaji mingguan termasuk lembur: Rp{total_gaji_mingguan:,}")