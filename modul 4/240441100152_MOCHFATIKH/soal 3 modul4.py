gaji_pokok = 100000
total_jam = 0
total_gaji_lembur = 0

for hari in range(7):
    jam_lembur = int(input(f"Masukkan total jam lembur hari ke {hari + 1}: "))

    if jam_lembur > 8:
        print("Lembur melebihi batas, tidak dihitung.")
        jam_lembur = 0
    elif total_jam + jam_lembur > 40:
        print("Total jam dalam seminggu 40 jam, anda melebihi batas, jam lembur dihentikan.")
        jam_lembur = 0
    else:
        total_jam += jam_lembur

    if jam_lembur == 0:
        gaji = 0
    elif jam_lembur <= 3:
        gaji = jam_lembur * 25000
    elif jam_lembur == 4  :
        gaji = 100000
    elif jam_lembur ==6 or jam_lembur ==7:
        gaji = 200000
    elif jam_lembur == 8:
        gaji = 300000    

    total_gaji_lembur += gaji # Menambahkan gaji lembur setiap hari

gaji_per_minggu = gaji_pokok * 7
total_semua_gaji = total_gaji_lembur + gaji_per_minggu

print("Total jam lembur selama 7 hari: ",[total_jam])
print("Total gaji lembur selama 7 hari:", total_gaji_lembur)
print("Gaji pokok per minggu:", gaji_per_minggu)
print("Total seluruh gaji selama 7 hari:", total_semua_gaji)
