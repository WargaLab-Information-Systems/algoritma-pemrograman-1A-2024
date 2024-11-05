gaji_harian = 100000
total_lembur = 0
total_gaji_mingguan = gaji_harian * 7
total_gaji_lembur = 0
batas_jam_lembur_per_hari = 8
batas_jam_lembur_mingguan = 40

for i in range(7):
    jam_lembur = int(input(f"Masukkan jam lembur hari ke - {i+1}: "))
    
    if jam_lembur > batas_jam_lembur_per_hari:
        print("Anda lembur melebihi batas, lembur anda tidak dihitung.")
        jam_lembur = 0
    elif total_lembur + jam_lembur > batas_jam_lembur_mingguan:
        print("Total jam lembur anda melebihi batas, lembur akan dihentikan.")
        jam_lembur = 0
    else:
        if jam_lembur < 4:
            gaji_lembur = jam_lembur * 25000
        elif jam_lembur == 4:
            gaji_lembur = 100000
        elif jam_lembur == 6:
            gaji_lembur = 200000
        elif jam_lembur == 8:
            gaji_lembur = 300000
        else:
            gaji_lembur = 0  

    total_lembur += jam_lembur
    total_gaji_lembur += gaji_lembur
    total_gaji_harian = gaji_harian + gaji_lembur
    total_gaji_mingguan += total_gaji_harian
    total_gaji_reguler = gaji_harian * 7

    print(f"Total lembur hari ke-{i+1}: {jam_lembur} jam, gaji lembur Anda hari ini Rp {gaji_lembur}, total gaji hari ini Rp {total_gaji_harian}")
    print("---------------------------------------------")

print("                                ")
print("Total lembur anda selama seminggu: Jam", total_lembur)
print("Total gaji lembur anda: Rp", total_gaji_lembur)
print("Total gaji reguler anda: Rp", total_gaji_reguler)
print("Total gaji mingguan dan lembur anda: Rp", total_gaji_mingguan)
print("                                ")