while True:
    terlambat = int(input("Anda telat mengembalikan DVD berapa hari : "))
    denda = 0

    if terlambat >= 5:
        denda += (terlambat - 5) * 2500
    if terlambat > 10:
        denda += ((terlambat - 5) // 5) * 5500

    if denda > 0:
        print(f"Total denda anda adalah : Rp {denda:,}")
    else:
        print("Anda tidak perlu membayar denda")
        
    print("Terima Kasih sudah mengembalikan DVD!")
    break