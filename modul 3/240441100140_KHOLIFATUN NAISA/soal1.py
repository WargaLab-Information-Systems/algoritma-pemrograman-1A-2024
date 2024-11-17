for i in range (7):
    if (i == 0 or i == 6):
        print ("*" * 7) 
    elif (i > 0 and i < 6):
        print ("*" + " " * 5 + "*")
print()
#menampilkan angka 4
for i in range(7):  
    if (i == 0 or i == 1 or i == 2):
        print("*" + " " * 5 + "*")  
    elif (i == 3):   
        print("*" * 7)                   
    else:
        print(" " * 6 + "*")                         
    print()  
#menampilkan angka 0
for i in range(7):
    if (i == 0 or i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 6  ):
        print(" " * 5 + "a")
print ()