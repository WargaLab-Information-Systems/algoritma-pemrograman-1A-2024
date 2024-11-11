def print_number_0(size):
    for row in range(size):
        if row == 0 or row == size - 1:
            print("x" * size)
        else:
            print("x" + " " * (size - 2) + "x")
    print()

def print_number_5(size):
    print("x" * size)
    for row in range(size // 2 - 1):
        print("x")  
    print("x" * size)
    for row in range(size // 2 - 1):
        print(" " * (size - 1) + "x")
    print("x" * size)
    print()


def print_number_6(size):
    for row in range(size):
        if row == 0 or row == size // 2 or row == size - 1:
            print("x" * size)
        elif row < size // 2:
            print("x")
        else:
            print("x" + " " * (size - 2) + "x")
    print()

def print_nim_numbers(size):
    print_number_0(size)
    print_number_5(size)
    print_number_6(size)

# Input NIM size
size = int(input("Masukan Size : "))
print_nim_numbers(size)