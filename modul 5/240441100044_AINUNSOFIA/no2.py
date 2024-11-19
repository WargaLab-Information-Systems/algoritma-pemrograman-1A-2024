def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fn = fibonacci(n-1) + fibonacci(n-2)
        return fn

n = int(input('masukkan angka ke-n yang ingin dihitung menggunakan deret fibonacci: '))
print(fibonacci(n)) 

a,b = 0,1
for i in range (n):
    a,b = b, a+b
    print(a, end=" ")
