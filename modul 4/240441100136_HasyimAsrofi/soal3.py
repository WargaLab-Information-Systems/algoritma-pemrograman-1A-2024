# Konstanta
Gaji_Harian = 100000
Maks_Lembur = 8
Bonus_Lembur = {4: 100000, 6: 200000, 8: 300000}
Tarif_Lembur_Rendah = 25000
Maks_Lembur_Minggu = 40

# variabel
total_gaji_mingguan = 0
total_gaji_lembur = 0
total_lembur_minggu = 0

# Menghitung gaji selama 7 hari
for hari in range(1, 8):
    lembur = int(input(f"Masukkan jam lembur untuk hari ke-{hari}: "))
    
    # Memastikan lembur tidak melebihi batas
    if lembur > Maks_Lembur:
        print("Lembur melebihi batas, tidak dihitung.")
        lembur = 0  # Lembur tidak dihitung jika melebihi batas
    total_lembur_minggu += lembur

    # Menghentikan lembur jika total lembur minggu mencapai atau melebihi 40 jam
    if total_lembur_minggu >= Maks_Lembur_Minggu:
        print("Total jam lembur dalam seminggu telah mencapai batas maksimum. Lembur dihentikan.")
        break

    # Menghitung gaji lembur
    if lembur == 0:
        gaji_lembur = 0
    elif lembur < 4:
        gaji_lembur = lembur * Tarif_Lembur_Rendah
    else:
        gaji_lembur = Bonus_Lembur.get(lembur, 0)

    # Update total gaji
    total_gaji_mingguan += Gaji_Harian + gaji_lembur
    total_gaji_lembur += gaji_lembur

# Menampilkan hasil
print(f"\nTotal lembur selama satu minggu: {total_lembur_minggu} jam")
print(f"Total gaji lembur: Rp{total_gaji_lembur}")
print(f"Total gaji mingguan tanpa lembur: Rp{Gaji_Harian * 7}")
print(f"Total gaji mingguan termasuk lembur: Rp{total_gaji_mingguan}")