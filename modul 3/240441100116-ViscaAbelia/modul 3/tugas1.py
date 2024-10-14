size = int(input("Masukkan size :"))

#angka 1
for i in range(size):
    if i == 1:
        print('11')
    elif i == size-1:
        print('111')
    else:
        print(' 1 ')
print()

#angka 1
for i in range(size):
    if i == 1:
        print('11')
    elif i == size-1:
        print('111')
    else:
        print(' 1 ')
print()   

#angka 6
for i in range(size):
    if i == size-1 or i == 0 or i == size//2:
        print('666666')
    elif i > size//2:
        print('6    6')
    else:
        print('6')
