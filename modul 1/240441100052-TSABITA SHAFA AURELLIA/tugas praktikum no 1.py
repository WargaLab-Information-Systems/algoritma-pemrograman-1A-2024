# input dimensi balok
panjang = 20  # cm
lebar = 13    # cm
tinggi = 7    # cm
jari_jari = 14 / 2  # cm
luas_selimut = 440  # cm2

# konstanta pi (π)
pi = 3.14159

# menghitung volume balok
volume_balok = panjang * lebar * tinggi

# menghitung tinggi tabung dari luas selimut
tinggi_tabung = luas_selimut / (2 * pi * jari_jari)

# menghitung volume tabung
volume_tabung = pi * (jari_jari ** 2) * tinggi_tabung

# tampilkan hasil
print("Volume Balok:", volume_balok, "cm3")
print("Volume Tabung:", volume_tabung, "cm3")
