#kbh alat dictionary awal e nilai 0
alat_peminjaman = {
    "alat_tekanandarah": 0,
    "termometer": 0,
    "alat_stetoskop": 0,
    "alat_inhaler": 0
}

#operasi penjumlahan gae nambah alat sg disele
alat_peminjaman["alat_tekanandarah"] += 2  #ditambah dadi 2
alat_peminjaman["termometer"] += 3

alat_peminjaman["alat_stetoskop"] += 4

alat_peminjaman["alat_tekanandarah"] -= 1   #dikurangi dadi 1
alat_peminjaman["termometer"] -= 2

alat_peminjaman["alat_stetoskop"] -= 3
alat_peminjaman["alat_inhaler"] += 2

#cek output e ng alat dictionary, nek jumlah e luwe teko 0 dicetak
print("Alat yang dipinjam Heni saat ini adalah:")
for alat in alat_peminjaman: #gae mengulang key dictionary
    jumlah = alat_peminjaman[alat] #gae njupuk nilai sg sesuai key
    if jumlah > 0: #ngecek 
        print(f"{alat}: {jumlah}")