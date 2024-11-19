a = 10
b = 4
a_b = 3 #a-b
faktorial_a = 10*9*8*7*6*5*4*3*2*1
faktorial_b = 4*3*2*1
faktorial_a_b = 3*2*1 #a_b adalah a-b/selisih
kombinasi = faktorial_a/(faktorial_b*faktorial_a_b)
print(f"banyak cara untuk memilih {a} orang dari {b} orang adalah {int(kombinasi)}")