
while True:
    hari_penyewaan = int(input("Masukkan hari keberapa anda mengembalikan DVD: "))
    denda = 0
    
    if hari_penyewaan >= 5:
        denda += (hari_penyewaan - 5) * 2500  
    if hari_penyewaan > 10:
        denda += ((hari_penyewaan - 5) // 5) * 5500
    
    if denda > 0:
        print(f"Denda keterlambatan total adalah: Rp.{denda:,}")
    else:
        print("Tidak ada denda keterlambatan.")
    
    respons = input("Apakah Anda ingin menghitung lagi? (ya/tidak): ")
    if respons.lower() != "ya":
        print("Terima kasih!")
        break