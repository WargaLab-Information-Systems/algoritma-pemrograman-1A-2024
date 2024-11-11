gaji_harian = 100000
gajimingguan = 0
total_gaji_mingguan = 0
total_gaji_lembur = 0
total_lembur_1minggu = 0

#masukan jam lembur per hari selama 7 hari
for hari in range(7):
    lembur = int(input(f"Masukkan jam lembur mas Ironi pada hari ke-{hari + 1}: "))
    
    if lembur > 8:
        print("Lembur melebihi batas, tidak dihitung tetapi tetap mendapatkan bonus 300.000")
        
    #total lembur selama seminggu
    if total_lembur_1minggu + lembur > 40:
        print("total lembur sudah mencapai batas! selamat beristirahat ")
        break

    #menghitung gaji lembur per jam
    if lembur == 0:
        gaji_lembur_hari = 0
    if lembur < 4:
        gaji_lembur_hari = lembur * 25000
    if lembur == 4:
        gaji_lembur_hari = 100000 
    if lembur == 5:
        gaji_lembur_hari = 150000
    if lembur == 6:
        gaji_lembur_hari = 200000
    if lembur == 7:
        gaji_lembur_hari = 250000
    if lembur >= 8:
        gaji_lembur_hari = 300000
    print("lembur hari ke-",hari+1, " mendapat gaji lembur sebanyak Rp.", gaji_lembur_hari)

    
    total_lembur_1minggu += lembur
    total_gaji_lembur += gaji_lembur_hari
    total_gaji_mingguan += gaji_harian + gaji_lembur_hari
    total_gaji_mingguan_tanpa_lembur = gaji_harian * 7
    
#output gaji mas ironi
print()
print("Berikut perincian gaji Mas ironi")
print("Total lembur selama satu minggu:", total_lembur_1minggu, "jam")
print("Total gaji lembur Rp.", total_gaji_lembur)
print("Total gaji mingguan tanpa lembur Rp.", total_gaji_mingguan_tanpa_lembur)
print("Total gaji mingguan termasuk lembur Rp.", total_gaji_mingguan)