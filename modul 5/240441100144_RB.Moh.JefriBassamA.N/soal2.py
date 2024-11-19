print("---Fibonacci---")
# n = int(input("masukkan bil bulat non-negatif yang anda mau : "))
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     elif n > 1:
#         return fibonacci(n - 2) + fibonacci(n - 1)

# for i in range(1):
#     for j in range(1, n + 1):
#         print(fibonacci(j), end=" ")



n = int(input("masukkan bil bulat non-negatif yang anda mau : "))
def fibonacci(n):
    a, b = 0, 1

    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        for i in range(2, n + 1):
            c =  a + b
            a, b = b, c
        return b

for i in range(1):
    for j in range(n + 1):
        print(fibonacci(j), end=" ")












 