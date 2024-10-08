# Data celengan balok
panjang = 20  # dalam cm
lebar = 13    # dalam cm
tinggi_balok = 7  # dalam cm

# Menghitung volume balok
volume_balok = panjang * lebar * tinggi_balok

# Data celengan tabung
diameter = 14  # dalam cm
r = diameter / 2  # radius dalam cm
luas_selimut = 440  # dalam cm²

# Menghitung tinggi tabung
tinggi_tabung = luas_selimut / (2 * 3.14 * r)

# Menghitung volume tabung
volume_tabung = 3.14 * r**2 * tinggi_tabung

# Menampilkan hasil
print(f"Volume celengan berbentuk balok adalah {volume_balok} cm³")
print(f"Volume celengan berbentuk tabung adalah {volume_tabung} cm³")