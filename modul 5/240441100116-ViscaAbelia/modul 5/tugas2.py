#fungsi fibonacci
def fibonacci(n):
    if n < 0:
        print('fibonacci tidak bisa untuk bilangan negatif')
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n = int(input('masukkan bilangan : '))
print(f'deret fibonacci ke {n} adalah', fibonacci(n))