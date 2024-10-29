# Konstanta
gaji_harian = 100000
jam_lembur_maksimal = 8
jam_lembur_mingguan_maksimal = 40
bonus_lembur = {4: 100000, 6: 200000, 8: 300000}
bonus_per_jam = 25000

# Variabel untuk menyimpan total
total_gaji = 0
total_lembur = 0
total_gaji_lembur = 0
total_gaji_mingguan = 0

# Input jam lembur per hari
jam_lembur_per_hari = []

for i in range(7):
    jam_lembur = int(input(f"Masukkan jam lembur untuk hari ke-{i + 1}: "))
    
    # Memeriksa batas lembur
    if jam_lembur > jam_lembur_maksimal:
        print("Lembur melebihi batas, tidak dihitung.")
        jam_lembur = 0  # Tidak dihitung
    elif total_lembur + jam_lembur >= jam_lembur_mingguan_maksimal:
        print("Total jam lembur mingguan sudah mencapai batas, lembur dihentikan.")
        jam_lembur = 0  # Tidak dihitung
    
    # Menyimpan jam lembur
    jam_lembur_per_hari.append(jam_lembur)
    total_lembur += jam_lembur
    
    # Menghitung gaji lembur
    if jam_lembur == 0:
        tambahan_lembur = 0
    elif 1 <= jam_lembur < 4:
        tambahan_lembur = jam_lembur * bonus_per_jam
    elif jam_lembur in bonus_lembur:
        tambahan_lembur = bonus_lembur[jam_lembur]
    else:
        tambahan_lembur = 0
    
    total_gaji_lembur += tambahan_lembur

# Menghitung total gaji mingguan
total_gaji = gaji_harian * 7
total_gaji_mingguan = total_gaji + total_gaji_lembur

# Menampilkan hasil
print("\nRincian Gaji Mas Ironi:")
for i in range(7):
    print(f"Hari ke-{i + 1}: Jam lembur = {jam_lembur_per_hari[i]}, Tambahan lembur = Rp{bonus_lembur.get(jam_lembur_per_hari[i], jam_lembur_per_hari[i] * bonus_per_jam)}")

print(f"\nTotal jam lembur selama satu minggu: {total_lembur} jam")
print(f"Total gaji lembur: Rp{total_gaji_lembur}")
print(f"Total gaji mingguan tanpa lembur: Rp{total_gaji}")
print(f"Total gaji mingguan termasuk lembur: Rp{total_gaji_mingguan}")