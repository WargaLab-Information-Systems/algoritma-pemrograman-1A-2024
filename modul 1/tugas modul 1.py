
# SOAL NO1
# VOLUME BALOK
p = 20 #cm
l = 13 #cm
t = 7 #cm
print("menghitung volume balok dengan rumus V=pxlxt")
volumeBalok = p * l * t
print(f'volume celengan balok milik Andi adalah {volumeBalok}cm^3')

# VOLUME TABUNG
diameter = 14 #cm
luasSelimut = 440 #cm^2

print("mencari jari-jari dengan rumus diameter/2")
jariJari = diameter / 2
print(f"diperoleh jari-jari={jariJari}cm")
print("mencari tinggi tabung dengan rumus tinggi=luas selimut / (2*22/7*jari-jari)") 
tinggi = luasSelimut / (2 * 22/7 * jariJari)
print(f"diperoleh tinggi tabung={tinggi}cm")
print("menghitung volume tabung dengan rumus V= 22/7 * (jari-jari**2) * tinggi")
volumeTabung = 22/7 * (jariJari ** 2) * tinggi
print(f'volume celengan tabung milik Andi adalah {volumeTabung}cm^3')

#SOAL NO2 
u5 = 11
u8_u12 = 52  
print("diketahui U5=11, maka a+4b=11....(pers1)")
print("diketahui U8+U12, maka 2a+18b=52....(pers2)")
print("dari kedua persamaan diatas, maka diperoleh nilai a=-1,b=3")
a=-1
b=3
sn=8
print("menghitung S8 dengan rumus S8=s8/2*(2a+(n-1)*b)")
s8=sn/2 * ((2*a)+((sn-1)*b))
print(f'jumlah nilai dari 8 suku pertama adalah {s8}')

#SOAL NO3
#MENGHITUNG NOMINAL UANG 
dolar = 35
kurs = 15104
uangsuraji = dolar * kurs
print(f'setelah Suraji menukarkan uangnya, ia akan mendapatkan uang sebanyak Rp.{uangsuraji}')

#S0AL N04
print("mencari banyak cara untuk membentuk tim menggunakan rumus kombinasi")
print("rumus C=n!/(r!*(n-r)!)")
n=7
r=4
q=n-r 
print("diketahui n,r,(n-r) adalah",n,r,n-r)
#faktorial
faktorial_n= 7*6*5*4*3*2*1
faktorial_r= 4*3*2*1
faktorial_q= 3*2*1
print("faktorial dari n=",n,"adalah",faktorial_n)
print("faktorial dari r=",r,"adalah",faktorial_r)
print("faktorial dari (n-r)=",n-r,"adalah",faktorial_q)
#menghitung kombinasi
kombinasi = faktorial_n / (faktorial_r * faktorial_q)
print(f'terdapat {kombinasi} cara Darsono membentuk tim')
