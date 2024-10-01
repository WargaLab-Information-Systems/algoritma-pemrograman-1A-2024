panjang_balok = 20
lebar_balok = 13
tinggi_balok = 7
diameter_tabung = 14
luas_selimut_tabung = 440
jari_jari_tabung = 7

volume_balok = panjang_balok*lebar_balok*tinggi_balok
tinggi_tabung = luas_selimut_tabung / (2 * 22/7*(diameter_tabung/2))
volume_tabung = 22/7 * (diameter_tabung / 2)**2 *tinggi_tabung

print("volume balok:", volume_balok, "cm3")
print("volume tabung:", volume_tabung, "cm3")
