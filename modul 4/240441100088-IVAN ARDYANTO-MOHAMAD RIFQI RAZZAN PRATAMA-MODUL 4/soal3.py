GAJI_HARIAN = 100000
GAJI_LEMBUR_4_JAM = 100000
GAJI_LEMBUR_6_JAM = 200000
GAJI_LEMBUR_8_JAM = 300000
GAJI_LEMBUR_PER_JAM = 25000  #untuk 1-3 jam

total_jam_lembur = 0
total_gaji_lembur = 0

print("PROGRAM HITUNG GAJI MINGGUAN")
print("-" * 30)

#input dan hitung 7 hari
for hari in range(1, 8):
    print(f"Hari ke-{hari}")
    jam_lembur = int(input("Jam lembur: "))
    
    #untuk mengecek batas lembur harian dan mingguan
    if jam_lembur > 8:
        print("Lembur melebihi batas!")
        gaji_hari_ini = 0
    elif total_jam_lembur + jam_lembur > 40:
        print("Sudah mencapai batas mingguan!")
        gaji_hari_ini = 0
    else:
         
        if jam_lembur == 0:
            gaji_hari_ini = 0
        elif jam_lembur == 4:
            gaji_hari_ini = GAJI_LEMBUR_4_JAM
        elif jam_lembur == 6:
            gaji_hari_ini = GAJI_LEMBUR_6_JAM
        elif jam_lembur == 8:
            gaji_hari_ini = GAJI_LEMBUR_8_JAM
        else:
            gaji_hari_ini = jam_lembur * GAJI_LEMBUR_PER_JAM
        
        total_jam_lembur += jam_lembur
        total_gaji_lembur += gaji_hari_ini
        
        print(f"Lembur: {jam_lembur} jam")
        print(f"Gaji lembur: Rp{gaji_hari_ini:,}")

#menghitung total gaji
gaji_reguler = GAJI_HARIAN * 7
total_gaji = gaji_reguler + total_gaji_lembur


print("RINGKASAN MINGGUAN")
print("-" * 30)
print(f"Total jam lembur: {total_jam_lembur} jam")
print(f"Gaji reguler: Rp{gaji_reguler:,}")
print(f"Gaji lembur: Rp{total_gaji_lembur:,}")
print(f"Total gaji: Rp{total_gaji:,}")