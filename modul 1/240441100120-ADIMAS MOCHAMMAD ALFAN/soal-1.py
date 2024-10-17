# andi mempunyai tabung yang berbentuk balok dan tabung

# BALOK
panjang = 20
lebar = 13
tinggi = 7

# rumus mencari volume balok adalah p X l X t, hitung volume balok.
volume_balok = panjang * lebar * tinggi

# TABUNG
diameter = 14  
luas_selimut = 440

# mencari jari-jari dengan membagi 2 diameter karena diameter adalah jari jari yang dikalikan 2
jari_jari = diameter / 2

# mencari tinggi tabung dengan menggunakan rumus luas_selimut
tinggi_tabung =(luas_selimut / (2 * 3.14 * jari_jari))

# menghitung volume tabung
volume_tabung = int(3.14 * jari_jari**2 * tinggi_tabung)

# hasil dari volume tabung dan volume balok
print(f"tinggi dari tabung tersebut ialah : ", tinggi_tabung)
print(f"volume celengan balok andi adalah : ", volume_balok)
print(f"volume celengan tabung andi adalah : ", volume_tabung)