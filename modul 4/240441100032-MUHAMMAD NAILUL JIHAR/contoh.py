# Contoh 1
# # Loop luar (outer loop)
# for i in range(1, 4): # Loop ini akan berjalan 3 kali (i = 1, 2, 3)
#     print(f"Loop luar i = {i}")

# # Loop dalam (inner loop)
# for j in range(1, 4): # Loop ini akan berjalan 3 kali untuk setiap iterasi dari loop luar
#     print(f"Loop dalam j = {j}")

# Contoh 2
# a = 24
# b = 36

# while b != 0:
#     a, b = b, a % b
# print(f"FPB-nya adalah : {a}")

# Contoh 3
# n = 100 # batas angka
# a, b = 0, 1

# print("Bilangan fibonacci hingga", n)
# while a <= n:
#     print(a, end=" ")
#     a, b = b, a + b

# Contoh 4
n = 5
for i in range(1, n+1):

    for j in range(n-1):
        print(" ", end=" ")
        
    for k in range(1, i+1):
        print(k, end=" ")
    print()