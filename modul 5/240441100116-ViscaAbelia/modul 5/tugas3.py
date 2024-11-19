#fungsi faktorial
def factorial(n):
    if n < 0:
        print('faktorial tidak bisa untuk bilangan negatif')
    elif n == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, n+1):
            factorial *= i 
        return factorial
        
n = int(input('masukkan bilangan : '))
print(f'{n}! =', end = ' ')
for i in range(n,0,-1):
    if i > 1:
        print(i, end = ' x ')
    else:
        print(i, '=', end = ' ')
print(factorial(n))
