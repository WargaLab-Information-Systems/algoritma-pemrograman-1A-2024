ukuran = int(input("Masukkan ukuran :"))

for i in range(ukuran):
    if i == 0 or i == ukuran - 1:
        print('x' * ukuran)
    else:
        print('x' + ' ' * (ukuran - 2) + 'x')

print()

for i in range(ukuran):
    if i == 0 or i == ukuran // 2 or i == ukuran - 1:
        print('x' * ukuran)
    elif i < ukuran // 2:
        print(' ' * (ukuran - 1) + 'x')
    else:
        print('x')
print()

for i in range(ukuran):
    if i == 0 or i == ukuran - 1:
        print('x' * ukuran)  
    else:
        print('x' + ' ' * (ukuran - 2) + 'x') 

print()