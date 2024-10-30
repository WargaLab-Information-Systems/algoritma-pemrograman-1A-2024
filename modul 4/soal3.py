# # Input jam lembur per hari dari pengguna untuk 7 hari
# jam_lembur = []
# for i in range(7):
#     lembur_hari = int(input(f"Masukkan jam lembur untuk hari ke-{i+1}: "))
#     if lembur_hari > 8:
#         print("Lembur melebihi batas, tidak dihitung.")
#         lembur_hari = 8  # Batasi maksimal lembur 8 jam per hari
#     jam_lembur.append(lembur_hari)

# # Inisialisasi variabel
# gaji_reguler_per_hari = 100000
# gaji_reguler_mingguan = 7 * gaji_reguler_per_hari
# total_jam_lembur = 0
# total_gaji_lembur = 0

# # Hitung gaji lembur harian dan total gaji lembur
# for i, lembur_hari in enumerate(jam_lembur):
#     if total_jam_lembur >= 40:
#         print("Total lembur minggu ini sudah mencapai batas 40 jam, lembur dihentikan.")
#         lembur_hari = 0  # Hentikan lembur jika sudah mencapai 40 jam
#         lembur_mingguan_dibatasi = True
#     total_jam_lembur = total_jam_lembur + lembur_hari

#     # Hitung gaji lembur harian berdasarkan aturan yang diberikan
#     if lembur_hari >= 8:
#         gaji_lembur_harian = 300000
#     elif lembur_hari >= 6:
#         gaji_lembur_harian = 200000
#     elif lembur_hari >= 4:
#         gaji_lembur_harian = 100000
#     elif lembur_hari > 0:
#         gaji_lembur_harian = lembur_hari * 25000
#     else:
#         gaji_lembur_harian = 0

#     total_gaji_lembur = total_gaji_lembur + gaji_lembur_harian
#     print(f"Lembur hari ke-{i+1}: {lembur_hari} jam, Gaji lembur: Rp{gaji_lembur_harian:,}")

# # Total gaji mingguan termasuk lembur
# gaji_mingguan_total = gaji_reguler_mingguan + total_gaji_lembur

# # Cetak hasil
# print("\n--- Rincian Gaji Mingguan Mas Ironi ---")
# print(f"Total jam lembur selama seminggu: {total_jam_lembur} jam")
# print(f"Total gaji lembur: Rp{total_gaji_lembur:,}")
# print(f"Total gaji mingguan tanpa lembur: Rp{gaji_reguler_mingguan:,}")
# print(f"Total gaji mingguan termasuk lembur: Rp{gaji_mingguan_total:,}")

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