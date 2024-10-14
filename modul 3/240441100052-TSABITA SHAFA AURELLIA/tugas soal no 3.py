# soal 3
while True:
    hari_penyewaan = int(input(" Masukkan lama penyewaan DVD (dalam hari):"))
    denda = 0 

    if hari_penyewaan >= 5:
        denda += (hari_penyewaan - 5) * 2500
    if hari_penyewaan > 10:
        denda += ((hari_penyewaan - 5)//5)* 5500
    
    if denda > 0:
        print(f"denda keterlambatan total adalah: rp.{denda:,}")
    else:
        print("tidak ada denda keterlambatan.")
    respons = input("Apakah anda ingin menghitung lagi? (ya/tidak):")
    if respons.lower()!= "ya":
        print("terima kasih! program selesai")
        break
        

