# SOAL PERTAMA MENGHITUNG VOLUME CELENGAN BERBENTUK BALOK DAN TABUNG
# VOLUME TABUNG
# DIKETAHUI:

panjang = 20
lebar = 13
tinggi = 7

volume_balok = panjang*lebar*tinggi
print("Jadi nilai dari volume balok adalah: ",volume_balok ,"cm")

# VOLUME TABUNG
# DIKETAHUI:

diameter = 14
luas_selimut = 440
phi = 22/7
a = 2
hasil_jari_jari = diameter/2
print("hasil dari jari jari tabung adalah: ",hasil_jari_jari)

tinggi_tabung = luas_selimut / (a*phi*hasil_jari_jari)
print("Hasil nilai dari tinggi tabung adalah: ",tinggi_tabung)
# VOLUME TABUNG

volume_tabung = phi* hasil_jari_jari**a *tinggi_tabung
print("Jadi hasil dari volume tabung ",volume_tabung ,"cm")