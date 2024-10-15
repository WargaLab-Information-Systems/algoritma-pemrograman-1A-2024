#input angka nim
t = int(input("masukkan angka : "))
#input membentuk nim
#angka 0
for i in range(t):
    for j in range(t):
        if (i == 0 or i == t-1) and (0 < j < t-1) or (j == 0 or j == t-1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print()

#angka 1
for i in range (t):
    print(" "*(t-1)+"*")

print()
 
#angka 6
for i in range(t):
    for j in range(t):
        if i == 0 or i == t//2 or i == t-1 or (j == 0 and i < t-1) or (j == t-1 and i > t//2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()