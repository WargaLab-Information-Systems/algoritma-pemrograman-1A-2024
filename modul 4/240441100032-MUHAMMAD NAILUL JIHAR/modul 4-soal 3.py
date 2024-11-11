print("Selamat datang di program penghitungan gaji Lembur")
jk = 12
gaji = 100000
tambahan = 0
hari = 0
total = 0

while True:
    waktu = input("Apakah anda sekarang lembur atau tidak (ya/tidak) : ")
    
    if waktu == "ya":
        lembur = int(input("Anda lembur berapa jam? : "))
        total += lembur
        if lembur < 4:
            tambahan += 25000
            hari += 1
        if lembur == 4:
            tambahan += 100000
            hari += 1
        if lembur == 5:
            tambahan += 150000
            hari += 1
        if lembur == 6:
            tambahan += 200000
            hari += 1
        if lembur == 7:
            tambahan += 250000
            hari += 1
        if lembur == 8:
            tambahan += 300000
            hari += 1
        if total >= 40:
            break
        if hari == 7:
            break

    if waktu == "tidak":
        gaji + gaji
        hari += 1
        lembur = 0
        tambahan += tambahan
        if hari == 7:
            break

total_gaji_tl = gaji * 7
hari_lembur = lembur + lembur / 7
total_gaji = total_gaji_tl + tambahan
print("\n Rincian gaji dan jam kerja karyawan")
print(f"Karyawan lembur per harinya sebanyak : {hari_lembur:.0f} jam")
print(f"Total karyawan lembur selama satu minggu adalah : {hari}")
print(f"Total gaji lembur karyawan sebanyak : Rp {tambahan}")
print(f"Total gaji karyawan tanpa lembur adalah : Rp {total_gaji_tl:.0f}")
print(f"Total gaji karyawan termasuk lembur adalah : Rp {total_gaji:.0f}")
print(f"Total jam lembur karyawan adalah : {total} jam")
