# memakai rumus kombinasi yaitu 
# c(n,r) = n! / r! (n-r) !
# Darsono memiliki 7 orang dan ingin memilih 4 orang yang ingin ia masukkan kedalam tim nya
# berarti bisa kita simpulkan bahwa n = 7 dan r = 4 lalu masuukan kedalam rumus kombinasi menjadi 
# c(7,4) = 7! / 4! (7-4) !
    #    = 7! / 4! * 3!

# 7! = 7*6*5*4
# 4! = 4*3*2
# 3! = 3*2 hasil n-r

faktorial_7 = 7*6*5
faktorial_3 = 3*2

hasil_faktorial =int(faktorial_7 / faktorial_3)

print("jadi hasil", hasil_faktorial, "cara untuk memilih 4 orang dari 7 orang")

