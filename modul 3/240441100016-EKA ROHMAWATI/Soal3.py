 #input jumlah hari keterlambatan 
def hitung_denda():
    while True:
        #input jumlah hari
        hari_terlambat = int(input("masukkan jumlah hari keterlambatan: "))

        #hitung denda
        denda = 0
        if hari_terlambat <= 10:
            denda = 2500 * hari_terlambat
        else:
            denda = 2500 * 10
            keterlambatan_sisa = hari_terlambat - 10
 
            if keterlambatan_sisa > 10:
                denda += (2500 * 10) + 2500 * (5500 * ((keterlambatan_sisa - 10) // 5))
            else:
                denda += 2500 * keterlambatan_sisa

        #menampilkan hasil
        print(f"total denda: Rp.{denda:,}")

        #input jika ingin mengulang
        ulang = input("apakah ingin menghitung ulangkembali?(ya,no): ")
        if ulang != 'ya':(lower)
            print("terimakasi")
            break

hitung_denda()