alat_kesehatan = {
    'glukometer': 2,  
    'termometer': 3,                   
    'sphygmomanometer': 4,
    'alat_inhaler': 2
}

while True:
    nama_alat = input("Masukkan nama alat kesehatan yang ingin dipinjam: ")
    
    if nama_alat in alat_kesehatan:
        jumlah_pinjam = int(input(f"Masukkan jumlah {nama_alat} yang ingin dipinjam: "))
        
        if jumlah_pinjam <= alat_kesehatan[nama_alat]:
            alat_kesehatan[nama_alat] -= jumlah_pinjam
        else:
            print(f"Jumlah {nama_alat} yang tersedia hanya {alat_kesehatan[nama_alat]}")

    else:
        print(f"{nama_alat} tidak tersedia dalam daftar alat kesehatan")
        break

    print("Alat kesehatan yang dipinjam Heni saat ini: " )

    for alat, jumlah in alat_kesehatan.items():
        if jumlah < 2:  
            print(f"{alat}: {2 - jumlah}")