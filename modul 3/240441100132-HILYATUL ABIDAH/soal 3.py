while True:
    hari_penyewaan = int(input("Masukkan hari keberapa anda mengembalikan DVD: "))
    denda = 0
    keterlambatan = hari_penyewaan - 5

    if hari_penyewaan > 5:
        denda += (hari_penyewaan - 5) * 2500  
    if hari_penyewaan > 15:
        denda += ((hari_penyewaan - 15) // 5) * 5500  
    
    if denda > 0:
        print(f"Denda keterlambatan total adalah: Rp.{denda:,}")
    else:
        print("Tidak ada denda keterlambatan.")
    
    respons = input("Apakah Anda ingin menghitung lagi? (ya/tidak): ")
    if respons == "ya" or respons == "y": 
        print("Silahkan masukkan ulang!")
        continue
    elif respons == "tidak" or respons == "n":
        print("Program selesai")
        break
    else:
        print("output invalid")
        break