#total orang yang ada
n = 7

#total orang yang di pilih
r = 4

#perehitungan langsung untuk c(7-4)
#c(7,4) = 7! / (4! * (7-4)!)
 #     = (7*6*5*4*3*2*1) / (4*3*2*1) * (3*2*1)

#faktorial dari 7
faktorial_7 = 7*6*5*4*3*2*1

#faktorial dari 4
faktorial_4 = 4*3*2*1

#faktorial dari 3
faktorial_3 = 3*2*1

#perhitungan berapa jumlah caranya 
jumlah_cara = (faktorial_7)/(faktorial_4*faktorial_3)
print(jumlah_cara)