# soal 1 
size = int(input("Masukkan size: "))
for i in range(7):
    if (i == 0 or i == 6):
        print("0000000")
    elif (i == 1 or i == 2 or i == 3 or i == 4 or i == 5):
        print("0     0")
print()
for i in range(size):
    if i == 0 or i == 1 or i == 2:   
        print("4     4")
    elif i == 3:
        print("4444444")
    elif i == 4 or i == 5 or i == 6:
        print("      4")
print()
for i in range(size):
    if i == 0 or i == 3 or i == 6:
        print("8888888")
    elif i == 1 or i == 2 or i == 4 or i == 5:
        print("8     8")
