gaji_reguler = 100000 
total_gaji_lembur = 0
total_gaji_mingguan = 0
total_lembur_mingguan = 0

print("---Selamat Datang di Perusahaan ABC---")
n = 7 # 1 minggu (7 hari)
for hari in range(1, n + 1):
    lembur = int(input(f"berapa lama jam lembur anda saat hari ke-{hari} : "))
    
    if lembur > 8:
        print("lembur melebihi batas harian, tidak dihitung")
        lembur = 8  # maksimal lembur/hari hanya 8 jam
    elif 0 <= lembur <= 8:
        # Hitung gaji lembur
        total_lembur_mingguan += lembur

        if 0 < total_lembur_mingguan <= 40:  # Cek total lembur mingguan
            if lembur == 0:
                total_gaji_lembur += 0
            elif 1 <= lembur <= 3:
                total_gaji_lembur += lembur * 25000
            elif lembur == 4:
                total_gaji_lembur += 100000
            elif lembur == 6:
                total_gaji_lembur += 200000
            elif lembur == 8:
                total_gaji_lembur += 300000
        elif total_lembur_mingguan > 40:
            print("maaf lembur melebihi batas mingguan")
            total_lembur_mingguan = 40
            break

        total_gaji_reguler = gaji_reguler * 7
        total_gaji_mingguan = total_gaji_reguler + total_gaji_lembur

if total_lembur_mingguan > 0 or total_gaji_lembur > 0:
    print()
    # Output hasil
    print(f"---Hasil Akhir---")
    print(f"total lembur selama satu minggu     : {total_lembur_mingguan} jam")
    print(f"total gaji lembur                   : Rp {total_gaji_lembur}")
    print(f"total gaji mingguan tanpa lembur    : Rp {total_gaji_reguler}")
    print(f"total gaji mingguan termasuk lembur : Rp {total_gaji_mingguan}") 

elif total_lembur_mingguan == 0 or total_gaji_lembur == 0:
    print(f"---Hasil Akhir---")
    print(f"total lembur selama satu minggu     : {total_lembur_mingguan} jam")
    print(f"total gaji mingguan tanpa lembur    : Rp {total_gaji_reguler}")