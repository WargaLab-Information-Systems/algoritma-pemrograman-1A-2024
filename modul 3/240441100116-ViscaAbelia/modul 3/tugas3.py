while True:
    #jumlah hari pinjam
    HariPinjam = int(input("Masukkan jumlah hari peminjaman :"))
    HariTerlambat = HariPinjam-5

    #variabel denda
    DendaPerhari = 2500
    DendaPer5hari = 5500

    if HariPinjam <=5: #menghitung hari pinjam <=5
        print("Anda tidak perlu membayar denda")
    elif HariTerlambat <=10:    #menghitung terlambat <=10 hari
        TotalDenda = HariTerlambat*DendaPerhari
        print(f"Anda terlambat {HariTerlambat} hari")
        print(f"Anda harus membayar denda Rp.{TotalDenda}")
    else:   #menghitung terlambat >10 hari
        DendaAwal = 10*DendaPerhari #variabel denda awal sebelum lebih dari 10 hari
        Terlambat_LebihDari10 = HariTerlambat - 10 #variabel terlambat >10
        DendaSetiapHari = Terlambat_LebihDari10*DendaPerhari #menghitung DendaSetiapHari setelah lebih dari 10
        #menghitung denda tambahan setiap 5 hari
        if Terlambat_LebihDari10 >=5:
            DendaTambahan = (Terlambat_LebihDari10//5) *DendaPer5hari
        else:
            DendaTambahan = 0


        #menghitung total denda
        TotalDenda = DendaAwal + DendaTambahan + DendaSetiapHari
        print(f"Anda terlambat {HariTerlambat} hari dan lebih dari 10 hari")
        print(f"Anda harus membayar denda Rp.{TotalDenda}")

    #menanyakan hitung ulang atau tidak
    Ulang = input("Apakah anda ingin menghitung ulang total denda? (iya/tidak)")
    if Ulang != "iya":
        break

