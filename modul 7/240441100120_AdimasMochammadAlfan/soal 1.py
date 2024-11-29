# pertama kita harus mencari tahu apa saja alat yang dipinjam oleh heni dalam semeinggu
# A : hari pertama Hani meminjam 2 alat pengukur tekanan darah dan 3 termometer.
# B : hari kedua Hani meminjam 4 stetoskop
# C : dan setelah seminggu Heni mengembalikan 1 alat pengukur tekanan darah  dan 2 termometer, lalu Heni menukar 3 alat pengukur tekanan darah dengan 2 pengukur tensi.

# Alat yang dipinjam Hani
Alat_kedokteran = {
    'alat pengukur tekanan darah' : 2,
    'termometer' : 3,
    'stetoskop' : 4,
}

# Alat yang dipinjam akan dikembalikan dan ditukar oleh Hani
Alat_kedokteran['alat pengukur tekanan darah'] -= 1 # hani mengembalikan 1 alat ukur tekanan darah
Alat_kedokteran['termometer'] -= 2 # Hani mengembalikan 2 termometer
Alat_kedokteran['stetoskop'] -= 3 # menukar 3 stetoskop
Alat_kedokteran['in healer'] = 2 # menjadi 2 in healer


for alat, jumlah in Alat_kedokteran.items():
    if jumlah < 0:
        print()
    else:
        print(" alat yang di pinjam oleh Heni: ", alat)
        print(" jumlah yang ada pada di Heni: ", jumlah)