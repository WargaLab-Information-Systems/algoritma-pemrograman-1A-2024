buku=[]

def menu():
    while True:
        print("\nMenu")
        print("1. Create")
        print("2. Read")
        print("3. Update")
        print("4. Delete")
        print("5. Exit")
        sub_menu=input("pilih menu (1-5): ")

        if sub_menu=="1":
            print("1. Create")
            id=input("Masukkan ID: ")
            nama=input("Masukkan nama peminjam: ")
            judul=input("Masukkan judul buku: ")
            tanggal=input("Masukkan tanggal peminjaman: ")

            create=(id,nama,judul,tanggal)
            buku.append(create)
            print("Buku berhasil ditambahkan")
            
        elif sub_menu=="2":
            print("2. Read")
            if buku:
                print("\nDaftar peminjaman Buku")
                for create in buku:
                    print(f"ID: {create[0]}, nama: {create[1]}, judul: {create[2]}, tanggal: {create[3]}")
            else:
                print("Tidak ada buku yg ditemukan")

        elif sub_menu=="3":
            print("3. Update")
            id_update=input("Masukkan ID buku yang ingin di update: ")
            buku[create]=(id_update,nama,judul,tanggal)

            for create in buku:
                if buku[create][0]==id_update:
                    print(f"ID: {buku[create][0]}, nama: {buku[create][1]}, judul buku: {buku[create][2]}, tanggal: {buku[create][3]}")

                    nama=input("Nama peminjam baru: ")
                    judul=input("Judul buku baru: ")
                    tanggal=input("Tanggal peminjaman baru: ")

                    print("Buku peminjaman berhasil diupdate")
                    return
            print("Buku tidak ditemukan")

        elif sub_menu=="4":
            print("4. Delete")
            id_delete=input("Masukan ID buku yang ingin dihapus: ")
            
            for create in buku:
                if buku[create][0]==id_delete:
                    buku.remove(create)
                    print("Buku peminjaman berhasil dihapus")
                    return

            print("ID tidak ditemukan")

        elif sub_menu=="5":
            print("Terima kasih.")
            break

        else:
            print("Pilihan tidak valid")
menu()