# BENAR SOAL 3
gaji_reguler = 100000
total_gaji = 0
hari_lembur = 0
total_gaji_lembur = 0

apakah = input("apakah kamu ingin lembur? (ya/tidak)")
if apakah == "tidak" :
    print ("tanpa lembur", gaji_reguler*7)
    print ("total semua gaji :", total_gaji_lembur + gaji_reguler*7)
elif apakah == "ya" :
    for hari in range (1, 8) :
        dino = int(input(f"jam hari {hari} :"))
        if dino > 8 :
            print ("lembur melebihi batas, tidak dihitung")
        elif hari_lembur + dino > 40 :
            print ("program tidak bisa melanjutkan")
        else :
            if dino == 0 :
                total_gaji =+ 0
            elif dino == 1 :
                total_gaji += (25000 + 25000)
            elif dino == 2 :
                total_gaji += (50000 + 25000)
            elif dino == 3 :
                total_gaji += (75000 + 25000)
            elif dino == 4 :
                total_gaji += 100000
            elif dino == 5 :
                total_gaji += 150000
            elif dino == 6 :
                total_gaji += 200000
            elif dino == 7 :
                total_gaji += 250000
            elif dino == 8 :
                total_gaji += 300000
        
            hari_lembur += dino
    total_gaji_lembur += total_gaji
    print ("total gaji lembur :",total_gaji_lembur )
    print ("total semua gaji :", total_gaji_lembur + gaji_reguler*7)
    print ("hari lembur", hari_lembur)
    print ("tanpa lembur", gaji_reguler*7)