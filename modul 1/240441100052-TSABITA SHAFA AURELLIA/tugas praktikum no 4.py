# Inisialisasi nilai n dan k
n = 5
r= 3
q = n- r 
print ("diketahui n,k (n-k) adalah",n,r,n-r )
# Menghitung faktorial secara langsung
faktorial_n = 7*6*5*4*3*2*1
faktorial_r = 4*3*2*1
faktorial_q = 3*2*1
print ("faktorial_n = ", n,"adalah",faktorial_n)
print ("faktorial_r = ", r,"adalah",faktorial_r)
print ("faktorial_(n-r) = ", n-r,"adalah",faktorial_q)
# Menghitung kombinasi 
kombinasi = faktorial_n / (faktorial_r * faktorial_q)

# Menampilkan hasil
print("Banyaknya cara untuk memilih", r, "orang dari", n, "orang adalah:",kombinasi)

