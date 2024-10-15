size = int(input("masukkan size yang anda mau : "))

# Menampilkan angka 1
for i in range(size):
    if i < 7:  
        print("   1   ")

print()   

# Menampilkan angka 4
for i in range(size):
    if i == 0 or i == 1 or i == 2:   
        print("4     4")
    elif i == 3:
        print("4444444")
    elif i == 4 or i == 5 or i == 6:
        print("      4")

print()

for i in range(size):
    if i == 0 or i == 1 or i == 2:   
        print("4     4")
    elif i == 3:
        print("4444444")
    elif i == 4 or i == 5 or i == 6:
        print("      4")


# # CARA KEDUA
# size = int(input("masukkan size yang anda mau:"))
# rumus = int(size/2)

# # menampilkan angka 1
# for i in range (size):
#     print(" " * (size - 3) + "1")
# print() 

# # menampilkan angka 4
# for i in range(rumus):
#     print("4" + (size - 2) * " " + "4")
# print("4" * size)
# for i in range(rumus): 
#     print(" " * (size-1) + "4")

# print()

# for i in range(rumus):
#     print("4" + (size - 2) * " " + "4")
# print("4" * size)
# for i in range(rumus): 
#     print(" " * (size-1) + "4")