total_gaji = 0
total_lembur = 0
gaji_harian = 100000
for hari in range(1, 8):
    lembur = int(input(f"Anda lembur selama berapa jam di hari ke-{hari}?: "))
    if total_lembur >= 40:
        print("Lembur Anda sudah mencapai batas maksimum 40 jam dalam seminggu, lembur dihentikan.")
        gaji_lembur = 0
    else:
        if total_lembur + lembur > 40:
            lembur = 40 - total_lembur
            print(f"Jam lembur hari ke-{hari} dibatasi hingga {lembur} jam.")
        if lembur == 4:
            gaji_lembur = 100000
        elif lembur == 5:
            gaji_lembur = 150000
        elif lembur == 6:
            gaji_lembur = 200000
        elif lembur == 7:
            gaji_lembur = 250000
        elif lembur == 8:
            gaji_lembur = 300000
        elif lembur < 4:
            gaji_lembur = 25000 * lembur
        else:
            gaji_lembur = 300000
            print("Mohon maaf, lembur Anda melebihi batas, dan tidak akan dihitung.")
        total_lembur += lembur
    total_gaji += gaji_harian + gaji_lembur
    print(f"Total gaji lembur yang Anda dapat pada hari ke-{hari} adalah: {gaji_lembur}")
print()
print("Total lembur selama satu minggu adalah:", total_lembur)
print("Total gaji lembur selama satu minggu adalah:", total_gaji - (gaji_harian * 7))
print("Total gaji mingguan tanpa lembur adalah:", gaji_harian * 7)
print(f"Total gaji Anda selama 1 minggu termasuk lembur adalah: {total_gaji}")
