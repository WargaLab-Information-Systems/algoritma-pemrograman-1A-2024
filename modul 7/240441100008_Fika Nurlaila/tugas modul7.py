
# 1. menetukan sisa alat yang dipinjam heni
alat_pinjaman = {
    'pengukur_tekanan_darah': 2,  # Hari pertama, meminjam 2 alat pengukur tekanan darah
    'termometer': 3,              # Hari pertama, meminjam 3 termometer
    'stetoskop': 4                # Hari kedua, meminjam 4 stetoskop
}
# Setelah seminggu (7 hari), Heni mengembalikan alat dan menukar alat
# Mengembalikan 1 alat pengukur tekanan darah dan 2 termometer
alat_pinjaman['pengukur_tekanan_darah'] -= 1
alat_pinjaman['termometer'] -= 2

# Menukar 3 stetoskop dengan 2 alat inhaler
alat_pinjaman['stetoskop'] -= 3
alat_pinjaman['inhaler'] = 2  # Menambahkan alat inhaler yang baru dipinjam

# Menampilkan hasil akhir alat yang dipinjam
print("Alat kesehatan yang dipinjam Heni saat ini:")
for alat, jumlah in alat_pinjaman.items():
    print(f"{alat}: {jumlah}")



# 2. menentukan siapa saja yang mengikuti club ekstrakurikuler di sekolah
# Dictionary untuk menyimpan klub dan set anggota klub
klub_siswa = {
    "Basket": set(),
    "Renang": set()
}

# Fungsi untuk menambahkan siswa ke klub tertentu
def tambah_siswa_ke_klub(nama_siswa, klub):
    if klub in klub_siswa:
        klub_siswa[klub].add(nama_siswa)
        print(f"Siswa {nama_siswa} berhasil ditambahkan ke klub {klub}.")
    else:
        print(f"Klub {klub} tidak ditemukan!")

# Fungsi untuk menampilkan siswa yang mengikuti kedua klub (irisan)
def siswa_kedua_klub():
    siswa_basket = klub_siswa["Basket"]
    siswa_renang = klub_siswa["Renang"]
    siswa_kedua_klub = siswa_basket.intersection(siswa_renang)
    print("Siswa yang mengikuti kedua klub:", siswa_kedua_klub)

# Fungsi untuk menampilkan siswa yang hanya mengikuti satu klub
def siswa_hanya_satu_klub():
    siswa_basket = klub_siswa["Basket"]
    siswa_renang = klub_siswa["Renang"]
    
    # Siswa yang hanya mengikuti klub Basket
    siswa_hanya_basket = siswa_basket.difference(siswa_renang)
    
    # Siswa yang hanya mengikuti klub Renang
    siswa_hanya_renang = siswa_renang.difference(siswa_basket)
    
    # Gabungkan siswa yang hanya mengikuti satu klub
    siswa_satu_klub = siswa_hanya_basket.union(siswa_hanya_renang)
    print("Siswa yang hanya mengikuti satu klub:", siswa_satu_klub)

# Fungsi untuk menampilkan semua siswa unik yang mengikuti setidaknya satu klub
def siswa_unik():
    siswa_basket = klub_siswa["Basket"]
    siswa_renang = klub_siswa["Renang"]
    siswa_unik = siswa_basket.union(siswa_renang)
    print("Semua siswa unik yang mengikuti setidaknya satu klub:", siswa_unik)

# Fungsi untuk menampilkan jumlah siswa unik yang mengikuti setidaknya satu klub
def jumlah_siswa_unik():
    siswa_basket = klub_siswa["Basket"]
    siswa_renang = klub_siswa["Renang"]
    siswa_unik = siswa_basket.union(siswa_renang)
    print("Jumlah siswa unik yang mengikuti setidaknya satu klub:", len(siswa_unik))

# menampilkan menu dan mengelola input dari pengguna
while True:
    print("\nMenu:")
    print("1. Tambah Siswa ke Klub Basket")
    print("2. Tambah Siswa ke Klub Renang")
    print("3. Tampilkan Siswa yang mengikuti kedua klub")
    print("4. Tampilkan Siswa yang hanya mengikuti satu klub")
    print("5. Tampilkan semua siswa unik yang mengikuti setidaknya satu klub")
    print("6. Tampilkan jumlah siswa unik yang mengikuti setidaknya satu klub")
    print("7. Keluar")
        
    pilihan = input("Pilih menu (1-7): ")
        
    if pilihan == '1':
            n = int(input("Berapa siswa yang ingin masuk klub basket (Minimal 3)? "))
            while n < 3:
                n = int(input("Jumlah karyawan minimal 3. Masukkan lagi berapa siswa: "))
            for nama_siswa in range (n):
                nama_siswa = input("Masukkan nama siswa yang akan ditambahkan ke klub Basket: ")
                tambah_siswa_ke_klub(nama_siswa, "Basket")
        
    elif pilihan == '2':
            n = int(input("Berapa siswa yang ingin masuk klub renang (Minimal 3)? "))
            while n < 3:
                n = int(input("Jumlah karyawan minimal 3. Masukkan lagi berapa siswa: "))
            for nama_siswa in range (n):
                nama_siswa = input("Masukkan nama siswa yang akan ditambahkan ke klub Renang: ")
                tambah_siswa_ke_klub(nama_siswa, "Renang")
        
    elif pilihan == '3':
        siswa_kedua_klub()
        
    elif pilihan == '4':
        siswa_hanya_satu_klub()
        
    elif pilihan == '5':
        siswa_unik()
        
    elif pilihan == '6':
        jumlah_siswa_unik()
        
    elif pilihan == '7':
        print("Terima kasih! Program selesai.")
        break
       
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")



# 3. menentukan kelas
# Menyimpan data kelas dan siswa dalam dictionary
kelas = {}

def tambah_siswa(nama, asal_sekolah):
    # Variabel nomor_kelas disimpan di dalam fungsi, tidak global
    nomor_kelas = len(kelas) + 1  # Menentukan nomor kelas berdasarkan jumlah kelas yang ada

    siswa = {
        'nama': nama,
        'asal_sekolah': asal_sekolah
    }
    
    # Cari kelas yang memiliki kurang dari 3 siswa
    for kelas_key, kelas_siswa in kelas.items():
        if len(kelas_siswa) < 3:
            kelas_siswa.append(siswa)
            print(f"Siswa {nama} berhasil ditambahkan ke kelas {kelas_key}.")
            return
    
    # Jika semua kelas sudah penuh (setiap kelas sudah memiliki 3 siswa), buat kelas baru
    kelas[nomor_kelas] = [siswa]
    print(f"Siswa {nama} berhasil ditambahkan ke kelas {nomor_kelas}.")

def tampilkan_siswa():
    # Menampilkan semua siswa di setiap kelas
    if not kelas:
        print("Tidak ada siswa yang terdaftar.")
        return
    
    for kelas_key, kelas_siswa in kelas.items():
        print(f"Kelas {kelas_key}:")
        for siswa in kelas_siswa:
            print(f"  Nama: {siswa['nama']}, Asal Sekolah: {siswa['asal_sekolah']}")

def ubah_data_siswa(nama_lama, nama_baru, asal_sekolah_baru):
    # Mengubah data siswa jika ditemukan
    for kelas_key, kelas_siswa in kelas.items():
        for siswa in kelas_siswa:
            if siswa['nama'] == nama_lama:
                siswa['nama'] = nama_baru
                siswa['asal_sekolah'] = asal_sekolah_baru
                print(f"Data siswa {nama_lama} berhasil diubah.")
                return
    print(f"Siswa dengan nama {nama_lama} tidak ditemukan.")

def hapus_siswa(nama):
    # Menghapus siswa dari daftar
    for kelas_key, kelas_siswa in kelas.items():
        for siswa in kelas_siswa:
            if siswa['nama'] == nama:
                kelas_siswa.remove(siswa)
                print(f"Siswa {nama} berhasil dihapus.")
                return
    print(f"Siswa dengan nama {nama} tidak ditemukan.")

# Fungsi utama untuk interaksi dengan user
while True:
    print("\nMenu:")
    print("1. Tambah Siswa")
    print("2. Tampilkan Data Siswa")
    print("3. Ubah Data Siswa")
    print("4. Hapus Siswa")
    print("5. Keluar")
        
    pilihan = input("Pilih menu (1/2/3/4/5): ")
        
    if pilihan == '1':
        nama = input("Masukkan nama siswa: ")
        asal_sekolah = input("Masukkan asal sekolah: ")
        tambah_siswa(nama, asal_sekolah)
        
    elif pilihan == '2':
        tampilkan_siswa()
        
    elif pilihan == '3':
        nama_lama = input("Masukkan nama siswa yang akan diubah: ")
        nama_baru = input("Masukkan nama baru: ")
        asal_sekolah_baru = input("Masukkan asal sekolah baru: ")
        ubah_data_siswa(nama_lama, nama_baru, asal_sekolah_baru)
        
    elif pilihan == '4':
        nama = input("Masukkan nama siswa yang akan dihapus: ")
        hapus_siswa(nama)
        
    elif pilihan == '5':
        print("Terima kasih! Program selesai.")
        break
        
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
