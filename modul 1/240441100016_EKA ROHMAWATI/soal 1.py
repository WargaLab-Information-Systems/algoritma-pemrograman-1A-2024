#mencari volume celengan balok
panjang =20
lebar =13
tinggi =7
v = panjang*lebar*tinggi
print("volume celengan balok: ",v)
 
#mencari volume celengan tabung
diameter=14
luas_selimut=440
jari_jari = diameter/2
pi= 22/7
tinggi = luas_selimut/(2*pi*jari_jari)
print("mencari tinggi: ", tinggi)
v =pi*jari_jari**2*tinggi
print("volume celengan tabung:", v)

a = float(input("masukan nilai a: "))
b = int(input("masukan nilai b: "))
keliling =2*(a+b)
print("keliling jajar genjang:", keliling)