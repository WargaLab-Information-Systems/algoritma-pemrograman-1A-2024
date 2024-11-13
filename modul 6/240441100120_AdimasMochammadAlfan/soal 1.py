 = []

def inputan_karyawan():
    for menambahkan in range(5):
        print("masukkan data karyawan dalam perusahaan", menambahkan + 1)
        Nip = input("masukkan Nip: ")
        Nama = input("masukkan Nama: ")
        Alamat = input("masukkan Alamat: ")
        Departemen = input("masukkan Departemen: ")
        Jabatan = input("masukkan jabatan: ")

        karyawan_dalam = {
            'Nip' : Nip,
            'Nama' : Nama,
            'Alamat' : Alamat,
            'Departemen' : Departemen,
            'Jabatan' : Jabatan

        } 
        karyawan.append(karyawan_dalam)
    
    return karyawan

def mencari_karyawan(karyawan,Atribut,Nilai):
    hasil = []
    for karyawan_dalam in karyawan:
        if karyawan.get(Atribut, "").lower() == Nilai.lower():
            hasil.append(karyawan_dalam)
    return hasil

karyawan = inputan_karyawan()

while True:
    print("mencari data karyawan")
    print("pilihlah atribut untuk mencari (Nip, Nama, Alamat, Departemen, Jabatan) atau ketik '0' untuk berhenti")
    Atribut = input("Atribut: ").strip().lower()
    if Atribut == '0':
        break
    elif Atribut in ["Nip", "Nama", "Alamat", "Departemen", "Jabatan"]:
        nilai = input("msukkan nilai untuk ", Atribut(),": ").strip()
        hasil_pencarian = mencari_karyawan(karyawan,Atribut,nilai)
        if hasil_pencarian:
            print("hasil pencarian: ")
            for karyawan in hasil_pencarian:
                print("NIP: ",karyawan['nip'],"Nama: ", karyawan['nama'], "Alamat: ", karyawan['alamat'], "Departemen: ", karyawan['departemen'], "Jabatan: ", karyawan['jabatan'])
        else:
            print("Tidak ada karyawan yang ditemukan dengan kriteria tersebut")
    else:
        print("Atribut tidak valid, silakan coba lagi.")