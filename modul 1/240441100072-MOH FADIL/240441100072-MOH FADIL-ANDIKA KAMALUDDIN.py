#soal no.1
#input
P = 20
L = 13
T = 7
D = 14
LS = 440

#Hitung volume celengan balok
Vb = P * L * T

#Hitung radiuscelengan tabung
r = D / 2

#Hitung tinggi celengan tabung 
t = LS / (2 * 3.14 * r)

#Hitung volume celengan tabung
Vt = 3.14 * r**2 * t

#output
print("Volume celengan balok:", Vb)
print("volume celengan tabung:", Vt)


#soal no.2
def calculate_sum():
    suku_ke_5 = 11
    jumlah_suku_8_12 = 52

    # Find the common difference (d)
    d = (jumlah_suku_8_12 - 2 * suku_ke_5) / 6

    # Find the first term (a1)
    a1 = suku_ke_5 - 4 * d

    # Calculate the sum of the first 8 terms
    sum = 8/2 * (2*a1 + (8 - 1) * d)

    return sum

print("Jumlah 8 suku pertama adalah :",calculate_sum())


#soal no.3
#bantu suraji menukar uang USD ke IDR pada tanggal 25 September 2024
usd = 35
idr = 15102.10
hasil = usd * idr
print ("hasil dari idr adalah",hasil)


#soal no.4
#input
total_orang=7
jumlah_orang_yang_ingin_dipilih=4

#hitung kombinasi
kombinasi=1
for i in range(1,jumlah_orang_yang_ingin_dipilih + 1):
    kombinasi=kombinasi*(total_orang-i+1)/i

#output
print("jumlah cara untuk membentuk tim adalah",int(kombinasi))