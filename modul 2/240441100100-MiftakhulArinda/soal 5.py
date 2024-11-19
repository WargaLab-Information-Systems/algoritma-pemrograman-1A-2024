# input nama dan usia pembeli
nama = str(input("masukkan nama pembeli"))
usia = int(input("masukkan usia pembeli= "))

# penyeleksian kondisi menggunkan if bersarang
if usia < 18:
    print("maaf usia anda belum mencukupi")
else:
    total_belanja = int(input("masukkan total belanja= "))
    memiliki_kartu_member = str(input("memiliki kartu member? (ya/tidak)")) 
    if memiliki_kartu_member == 'ya':
        print(f"mendapatkan diskon 15%")
        diskon_memiliki_kartu_member = 0.15 
        total_harga_setelah_diskon_memiliki_kartu = total_belanja * diskon_memiliki_kartu_member
        print(f"harga yang didapatkan setelah diskon {total_harga_setelah_diskon_memiliki_kartu}")
    elif memiliki_kartu_member == 'tidak': 
        total_belanja > 5000000
        print(f"mendapatkan diskon 10%")
        diskon_total_belanja = 0.1 
        total_harga_setelah_diskon_belanja = total_belanja * diskon_total_belanja
        print(f"harga yang didapatkan setelah diskon {total_harga_setelah_diskon_belanja}")