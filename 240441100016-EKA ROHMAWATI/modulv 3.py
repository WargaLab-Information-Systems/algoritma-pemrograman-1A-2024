#input angka
gaji_perhari = 100000
gaji_lembur = 0
total_gaji = 0
total_lembur = 0

# Loop untuk 7 hari
for i in range(1,8):
    lembur = int(input(f"Masukkan jam lembur hari ke-{i}?: "))
    #mengecek dan menghitung lembur
    if total_lembur >= 40:
        print("lembur dalam 1 minggu sudah mencapai atau melebihi 40 jam, lembur dihentikan")
        #mengatur jam lembur
    else:
        if total_lembur + lembur > 40:
            lembur = 40 - total_lembur
            print(f"lembur dibatasi selama {lembur} jam")
        #menghitung gaji lembur
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
            print("lembur melebihi batas,tidak dihitung")
            gaji_lembur = 0
    #total gaji dan lembur
    total_lembur += lembur
    total_gaji += gaji_perhari + gaji_lembur
    print("Total gaji lembur:",gaji_lembur)
    print()

# manampilkan hasil
print("total lembur selama 1 minggu:", total_lembur)
print("total gaji lembur:", total_gaji - (gaji_perhari * 7))
print("Total gaji mingguan tanpa lembur:", gaji_perhari * 7)
print("total gaji mingguan termasuk lembur: ", total_gaji)