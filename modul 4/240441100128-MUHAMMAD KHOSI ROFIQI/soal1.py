ukuran = int(input("masukkan ukuran: "))
ukuran_bagi = ukuran // 2
for i in range (ukuran_bagi) :
    for b in range (ukuran_bagi - (i+1)):
        print (" ", end = "")
    for k in range (i + 1) :
        print ("o",end= " ")
    print()
    
for i in range (ukuran_bagi-1) :
    for b in range (i+1):
        print (" ", end = "")
    for k in range (ukuran_bagi - (i + 1)) :
        print ("o",end= " ")
    print()