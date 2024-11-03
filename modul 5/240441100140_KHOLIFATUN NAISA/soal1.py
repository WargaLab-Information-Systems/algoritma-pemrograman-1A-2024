def calculate_diskon():
    # total_belanja = 0
    belanja = int (input("masukkan total belanja anda: "))
    anggota = input("apakah anda mempunyai ke anggotaan? bronze/silver/gold/tidak: ")
    potongan = 0
    # bronze = 5
    # silver = 10
    # gold = 15   
    if belanja >= 1000000:
        if anggota == "bronze":
            print("selamat anda mendapatkan potongan sebesar 5% juga mendapat potongan 5%")
            potongan += 10
            print(f"total belanja anda sebelum diskon adalah: {belanja}")
            print(f"total belanja anda setelah diskon adalah: {belanja * (1-potongan/100)}")
        elif anggota == "silver":
            print("selamat anda mendapatkan potongan sebesar 10% juga mendapat potongan 5%")
            potongan += 15
            print(f"total belanja anda sebelum diskon adalah: {belanja}")
            print(f"total belanja anda setelah diskon adalah: {belanja * (1-potongan/100)}")
        elif anggota == "gold":
            print("selamat anda mendapatkan potongan sebesar 15% juga mendapat potongan 5%")
            potongan += 20
            print(f"total belanja anda sebelum diskon adalah: {belanja}")
            print(f"total belanja anda setelah diskon adalah: {belanja * (1-potongan/100)}") 
        else:
            print("selamat anda mendapatkan potongan sebesar 5%")
            print(f"total belanja anda sebelum diskon adalah: {belanja}")
            print(f"total belanja anda adalah: {belanja * (1- 5/100)}")
    else:
        if anggota == "bronze":
            print("selamat anda mendapatkan potongan sebesar 5%")
            print(f"total belanja anda sebelum diskon adalah: {belanja}")
            print(f"total belanja anda adalah: {belanja * (1- 5/100)}") 
        elif anggota == "silver":
            print("selamat anda mendapatkan potongan sebesar 10%")
            print(f"total belanja anda sebelum diskon adalah: {belanja}")
            print(f"total belanja anda adalah: {belanja * (1- 10/100)}") 
        elif anggota == "gold":
            print("selamat anda mendapatkan potongan sebesar 15%")
            print(f"total belanja anda sebelum diskon adalah: {belanja}")
            print(f"total belanja anda adalah: {belanja * (1- 15/100)}") 
        else:
            print("mohon maaf anda tidak mendapat potongan")
            print(f"total belanja anda adalah: {belanja}") 
calculate_diskon()
