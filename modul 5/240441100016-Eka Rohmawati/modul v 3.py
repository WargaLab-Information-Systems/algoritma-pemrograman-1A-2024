#input data
n = int(input("masukkan bilangan faktorial: "))

#mengeksekusi data
def bilangan_faktorial(n):
    if n == 0:
        return 1
    elif n < 0:
        print("ini bukan bilangan positif")
    else:
        return n * bilangan_faktorial (n-1)
    
for i in range(1, n + 1):
    print (i)
    
#menampilkan hasil
print("hasil dari faktorial: ", bilangan_faktorial(n))