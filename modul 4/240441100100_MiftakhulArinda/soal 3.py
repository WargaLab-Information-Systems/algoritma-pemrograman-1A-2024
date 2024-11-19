# input variabel yang diketahui
gaji_harian=100000
total_lembur_seminggu=0
total_gaji_lembur=0

# input berapa jam lemburnya 
for i in range(7):
    jam_lembur=int(input(f"jam lembur hari ke {i+1}: "))
    if jam_lembur>8:
        print("lembur melebihi batas, tidak dihitung")
        break
    elif jam_lembur>=40:
        print("lembur melebihi batas, tidak dihitung")
        break
    # input bonus lembur yang diperoleh
    else:
        bonus_lembur=0
        if jam_lembur<4:
            bonus_lembur=jam_lembur*25000
        elif jam_lembur==4:
            bonus_lembur=100000
        elif jam_lembur==6:
            bonus_lembur=200000
        elif jam_lembur==8:
            bonus_lembur=300000
        else:
            bonus_lembur=0

    # total menggunakan operasi aritmatika
    total_gaji_lembur += bonus_lembur
    total_lembur_seminggu += jam_lembur
    total_gaji_mingguan_tanpa_lembur=gaji_harian*7
    total_gaji_mingguan_termasuk_lembur=total_gaji_mingguan_tanpa_lembur+total_gaji_lembur

    # beri output sesuai yang diinginkan
print(f"total lembur selama satu minggu: {total_lembur_seminggu}")
print(f"total gaji lembur: {total_gaji_lembur}")
print(f"total gaji mingguan tanpa lembur: {total_gaji_mingguan_tanpa_lembur}")
print(f"total gaji mingguan termasuk lembur: {total_gaji_mingguan_termasuk_lembur}")