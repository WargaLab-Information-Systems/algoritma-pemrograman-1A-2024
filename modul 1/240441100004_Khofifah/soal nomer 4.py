n = 7
r = 4
q = n-r
print("diketahui n,k (n,k) adalah", n,r,n-r)
#menghitung faktorial secara manual
faktorial_n= 7*6*5*4*3*2*1
faktorial_r= 4*3*2*1
faktorial_q= 3*2*1
print("faktorial_n=",n,"adalah",faktorial_n)
print("faktorial_r=",r,"adalah",faktorial_r)
print("faktorial_(n-r)= ","adalah", faktorial_q)
#Kombinasi
kombinasi=faktorial_n/(faktorial_r*(faktorial_q))

#Hasilnya
print("Banyaknya cara yang bisa digunakan pak Darsono adalah:", kombinasi)