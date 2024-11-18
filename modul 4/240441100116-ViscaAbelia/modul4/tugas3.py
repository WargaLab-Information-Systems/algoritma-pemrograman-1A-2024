GajiReguler = 100000
GajiLembur = 0
TotalGajiLembur = 0
TotalLembur = 0

TanyaLembur = input("apakah kamu lembur? (iya/tidak) ")
if TanyaLembur == "tidak":
    print("Kamu tidak lembur, maka tidak mendapatkan gaji tambahan")
else:
    hari = int(input("masukkan jumlah hari :"))
    for i in range(1, hari+1):
        Lembur = int(input(f"hari ke {i} lembur berapa jam? "))
        if Lembur > 8:
            Lembur = 0
            print("lembur melebihi batas, tidak dihitung")
        elif TotalLembur + Lembur > 40:
            print("Total Lembur melebihi 40 jam, program dihentikan")
            break
        elif Lembur <= 3:
            GajiLembur = 25000 * Lembur
            TotalGajiLembur += GajiLembur
            TotalLembur += Lembur
            print(f"[Total lembur hari ke {i} adalah {Lembur} jam]")
        elif Lembur == 4:
            GajiLembur = 100000
            TotalGajiLembur += GajiLembur
            TotalLembur += Lembur
            print(f"[Total lembur hari ke {i} adalah {Lembur} jam]")
        elif Lembur == 6:
            GajiLembur = 200000
            TotalGajiLembur += GajiLembur
            TotalLembur += Lembur
            print(f"[Total lembur hari ke {i} adalah {Lembur} jam]")
        elif Lembur == 8:
            GajiLembur = 300000
            TotalGajiLembur += GajiLembur
            TotalLembur += Lembur
            print(f"[Total lembur hari ke {i} adalah {Lembur} jam]")
        else:
            GajiLembur = 0

    TotalGajiReguler = GajiReguler * hari
    TotalGajiRegulerdanLembur = TotalGajiReguler + TotalGajiLembur
    print()
    print(f"[Total lembur dalam {hari} hari adalah {TotalLembur} jam]")
    print(f"[Total Gaji lembur adalah Rp.{TotalGajiLembur}]")
    print(f"[Total Gaji reguler adalah Rp.{TotalGajiReguler}]")
    print(f"[Total gaji Reguler + gaji lembur adalah Rp.{TotalGajiRegulerdanLembur}]")
