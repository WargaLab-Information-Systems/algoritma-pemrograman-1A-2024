# for baris in range(1):
#     for baris in range(1):
#         print("x","x","x","x","x")
#     for baris in range(5):
#         print("x"," "," "," ","x")
#     for baris in range(1):
#         print("x","x","x","x","x")
#     print("")

# for baris in range(1):
#     for baris in range(1):
#         print("x","x","x","x","x")
#     for baris in range(2):
#         print(" "," "," "," ","x")
#     for baris in range(1):
#         print("x","x","x","x","x")
#     for baris in range(2):
#         print("x"," "," "," "," ")
#     for baris in range(1):
#         print("x","x","x","x","x")
#     print("")

# for baris in range(1):
#     for baris in range(1):
#         print("x"," "," "," ","x")
#     for kolom in range(2):
#         print("x"," "," "," ","x")
#     for baris in range(1):
#         print("x","x","x","x","x")
#     for baris in range(3):
#         print(" "," "," "," ","x")
#     print("")

#-2 fungsinya untuk spasi agar bentuknya proposional kalau nnga pake itu bentuknya ngga seimbang
size = int(input("Masukkan size : "))

if size < 4:
    print("Size minimal 3 untuk pola yang benar.")
else:
    # Angka 0
    print("x" * size)  
    for i in range(size - 2): 
        print("x" + " " * (size - 2) + "x")
    print("x" * size)  
    print(" ")  
    
    # Angka 2
    print("x" * size)  
    for i in range((size - 2) // 2):  
        print(" " * (size - 1) + "x")
    print("x" * size)  
    for i in range((size - 2) // 2):  
        print("x" + " " * (size - 1))
    print("x" * size)  
    print(" ")  

    # Angka 4
    for i in range((size - 2) // 2):  
        print("x" + " " * (size - 2) + "x")
    print("x" * size)  
    for i in range((size - 2) // 2):  
        print(" " * (size - 1) + "x")
    print(" ")  