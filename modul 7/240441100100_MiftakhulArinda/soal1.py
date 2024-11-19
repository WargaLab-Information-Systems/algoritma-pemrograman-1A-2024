alat_kesehatan={
    'Glukometer' : 0,
    'Termometer' : 0,
    'Sphygmomanometer' : 0,
    'Inhaler' : 0
}

def menu():
    while True:
        print("\nSistem pengelolaan alat kesehatan")
        print("1. Pinjam Alat")
        print("2. Kembalikan Alat")
        print("3. Menukar Alat")
        print("4. Alat yang dipinjam saat ini")
        print("5. Keluar")
        sub_menu=input("Pilih menu: ")

        if sub_menu=="1":
            print("1. Pinjam Alat")
            if not alat_kesehatan:
                print(f"{nama_alat} tidak terdaftar.")
            else:
                nama_alat=input("Masukkan alat kesehatan yang ingin dipinjam: ")
                jumlah=int(input(f"Masukkan jumlah {nama_alat} yang ingin dipinjam: "))
                alat_kesehatan[nama_alat]+=jumlah
                print(f"{jumlah} {nama_alat} berhasil dipinjam")
        
        elif sub_menu=="2":
            print("2. Kembalikan Alat")
            if not alat_kesehatan:
                print(f"{nama_alat} gagal kembalikan")
            else:
                nama_alat=input("Masukkan nama alat yang ingin dikembalikan: ")
                jumlah=int(input(f"Masukkan jumlah {nama_alat} yang ingin dikembalikan: "))
                alat_kesehatan[nama_alat]-=jumlah
                print(f"{jumlah} {nama_alat} berhasil dikembalikan")
        
        elif sub_menu=="3":
            print("3. Menukar Alat")
            if not alat_kesehatan:
                print(f"{nama_alat_kembali} gagal ditukar")
            else:
                nama_alat_kembali=input("Masukkan nama alat yang ingin dikembalikan: ")
                jumlah_kembali=int(input(f"Masukkan jumlah {nama_alat_kembali} yang ingin dikembalikan: "))
                nama_alat_pinjam=input("Masukkan nama alat yang ingin dipinjam: ")
                jumlah_pinjam=int(input(f"Masukkan jumlah {nama_alat_pinjam} yang ingin dipinjam: "))
                alat_kesehatan[nama_alat_kembali]-=jumlah_kembali
                alat_kesehatan[nama_alat_pinjam]+=jumlah_pinjam
                print(f"{jumlah_kembali} {nama_alat_kembali} berhasil ditukar dengan {jumlah_pinjam} {nama_alat_pinjam}")

        elif sub_menu=="4":
                print("\nAlat Kesehatan yang dipinjam Heni saat ini:")
                for alat, jumlah in alat_kesehatan.items():
                    print(f"Alat: {alat}, Jumlah: {jumlah}")
            
        elif sub_menu=="5":
            print("Terima kasih")
            
        else:
            print("Program tidak valid")
menu()