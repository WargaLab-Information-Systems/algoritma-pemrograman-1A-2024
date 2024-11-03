n = int(input("Masukkan bilangan : "))
simbol = input("Masukkan simbol (x/o) : ")

for i in range(1, n+1):
    
    for j in range(n-i):
        print(" ", end=" ")
    
    for k in range(1, i+1):
        print(" ", simbol, end=" ")
    print()

for i in range(1, n+1):
    
    for k in range(1, i+1):
        print(" " , end=" ")
    
    for j in range(n-i):
        print(" ", simbol, end=" ")
    print()
