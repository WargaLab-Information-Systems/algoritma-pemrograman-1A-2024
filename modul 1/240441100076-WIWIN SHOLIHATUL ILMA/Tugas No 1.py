panjang = 20 
lebar = 13
tinggi = 7
diameter = 14
selimut = 440
phi = 22/7

# volume balok
VB=panjang*lebar*tinggi

# Volume Tabung
r = diameter/2
tt = selimut/(2*phi*r)
VT = phi*2*r*tt

print("hasil dari volume balok adalah:", VB)
print("hasil dari volume tabung adalah:", VT)