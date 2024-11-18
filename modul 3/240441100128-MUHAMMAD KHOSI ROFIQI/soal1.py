
size = int(input("masukan size:"))
rumus=int(size/2)

# 1
for i in range (size):
    print(" " * (size - 3) + "xx")
print() 

#angka 2
print("x" * size)
for i in range(1,rumus):
    print(" " * (size - 1) + "x")
print("x" * size)
for i in range(1,rumus):
    print("x"+" " * (size - 2))
print("x" * size)
print ()

#angka 8
print("x" * size)
for i in range(1,rumus):
    print("x"+" " * (size - 2) + "x")
print("x" * size)
for i in range(1,rumus):
    print("x"+" " * (size - 2) + "x")
print("x" * size)