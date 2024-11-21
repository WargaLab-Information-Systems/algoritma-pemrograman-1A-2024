kelas = []  #dictioary 
max_siswa = 3 

def tambah_siswa(nama, asal_sekolah): #nambah siswa ng kls sg kosong
    for k in kelas:
        if len(k) < max_siswa: #cek jumlah siswa -dari
            k.append({'nama': nama, 'asal_sekolah': asal_sekolah})
            print(f"Siswa {nama} berhasil ditambahkan ke kelas.")
            return #berhenti nek mari nmbh
    kelas.append([{'nama': nama, 'asal_sekolah': asal_sekolah}]) #nambah data siswa
    print(f"Kelas baru dibuat. Siswa {nama} berhasil ditambahkan ke kelas.")

def tampilkan_semua_kelas(): #nampilno mbe nyetak nama
    if len(kelas) == 0: #nek gk ono siswa +
        print("Belum ada siswa yang terdaftar.")
    else:
        # Menggunakan perulangan biasa dan penghitungan manual
        for i in range(len(kelas)): #nampilno data kbh  kls
            print(f"Kelas {i+1}:") 
            for siswa in kelas[i]: #setiap siswa ng kls nampilno nm + as
                print(f"{siswa['nama']} ({siswa['asal_sekolah']})")

#memperbarui data siswa
def update_siswa(nama_lama, nama_baru, asal_sekolah_baru):
    for k in kelas:
        for siswa in k:
            if siswa['nama'] == nama_lama:
                siswa['nama'] = nama_baru
                siswa['asal_sekolah'] = asal_sekolah_baru
                print(f"Siswa {nama_lama} berhasil diupdate.")
                return #nek nama tdk ditemukan progam ctk
    print(f"Siswa dengan nama {nama_lama} tidak ditemukan.")

def hapus_siswa(nama):
    for k in kelas:
        for siswa in k: #golek siswa berdasarkan nama
            if siswa['nama'] == nama:
                k.remove(siswa) #hps data siswa teko kls
                print(f"Siswa {nama} telah dihapus.")
                return #nek nama g ditemuno  program ctk
    print(f"Siswa dengan nama {nama} tidak ditemukan.")

#nampilno menu ge pengguna
def menu():
    while True:
        print("== Menu Bimbingan ==")
        print("1. Tambah Siswa")
        print("2. Tampilkan Semua Kelas")
        print("3. Update Data Siswa")
        print("4. Hapus Siswa")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1/2/3/4/5): ")

        if pilihan == '1': #nambah siswa dan as
            nama = input("Masukkan nama siswa: ")
            asal_sekolah = input("Masukkan asal sekolah siswa: ")
            tambah_siswa(nama, asal_sekolah)
            print(f"Siswa {nama} berhasil ditambahkan.")
        
        elif pilihan == '2': #nampilno kbh kls sg mari ditambahno
            tampilkan_semua_kelas()

        elif pilihan == '3': #memperbarui nama dn as
            nama_lama = input("Masukkan nama siswa yang ingin diupdate: ")
            nama_baru = input("Masukkan nama baru: ")
            asal_sekolah_baru = input("Masukkan asal sekolah baru: ")
            update_siswa(nama_lama, nama_baru, asal_sekolah_baru)
        
        elif pilihan == '4': #ngehps nama siswa dgn nulis jeneng
            nama = input("Masukkan nama siswa yang ingin dihapus: ")
            hapus_siswa(nama)
        
        elif pilihan == '5':
            print("Terima kasih! Program selesai.")
            break
        
        else: 
            print("Pilihan tidak valid. Silakan pilih lagi.")

menu()