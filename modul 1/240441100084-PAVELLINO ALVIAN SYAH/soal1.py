# # soal ke satu

# tentukan dimensi celengan yang berbentuk balok
panjang = 20
lebar = 13
tinggi = 7
# volume celengan yang berbentuk balok
volume_balok = panjang * lebar * tinggi
print(f"Celengan berbentuk balok volumetrik: {volume_balok} cubic cm")
# tentukan dimensi celengan berbentuk tabung
diameter = 14
luas_selimut = 440 
# jari jari silnder tersebut
radius = diameter / 2
#tinggi tabung dengan menggunakan rumus luas permukaan
height = luas_selimut / (2 * 3.14 * radius)
print(f"Tinggi celengan berbentuk tabung: {height} cubic cm")
# volume celengan berbentuk tabung
volume_tabung = 3.14 * radius ** 2 * height
print(f"celengan berbentuk tabung bervolume: {volume_tabung} cubic cm")