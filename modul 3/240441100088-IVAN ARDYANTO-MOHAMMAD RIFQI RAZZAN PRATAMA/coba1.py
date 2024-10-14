size = int(input("Masukkan Size : "))
nim = input("Masukkan NIM : ")

# mendefinisi pola untuk setiap digit menggunakan pattrens dictionary 0 - 9
patterns = {
    '0': ['xxx', 'x x', 'x x', 'x x', 'xxx'],
    '1': ['  x', '  x', '  x', '  x', '  x'],
    '2': ['xxx', '  x', 'xxx', 'x  ', 'xxx'],
    '3': ['xxx', '  x', 'xxx', '  x', 'xxx'],
    '4': ['x x', 'x x', 'xxx', '  x', '  x'],
    '5': ['xxx', 'x  ', 'xxx', '  x', 'xxx'],
    '6': ['xxx', 'x  ', 'xxx', 'x x', 'xxx'],
    '7': ['xxx', '  x', '  x', '  x', '  x'],
    '8': ['xxx', 'x x', 'xxx', 'x x', 'xxx'],
    '9': ['xxx', 'x x', 'xxx', '  x', 'xxx']
}

# Mencetak pola
for row in range(5): #di gunakan untuk pola yang berisi 5 gigit
    for digit in nim: #untuk setiap digit dalam nim yang di inputkan
        pattern = patterns.get(digit, '   ') #untuk digit yang yang sesuai jika tidak akan kembali ke spasi kosong
        if row < len(pattern):#untuk memperbesaer karakter bedarsarkan size
            print(pattern[row].replace('x', 'x' * size).replace(' ', ' ' * size), end='  ')
        else:
            print(' ' * (size * 3), end='  ') #jijka tidak sesuai akan menampilkan spasi kosong
    print()