def faktorial(n):
    # Kasus dasar
    if n == 0:
        return 1
    else:
        # Rekursi untuk menghitung faktorial
        return n * faktorial(n - 1)

# Contoh penggunaan
print(f"5! = {faktorial(5)}")  # Output: 120
print(f"3! = {faktorial(3)}")  # Output: 6
print(f"2! = {faktorial(2)}")  # Output: 2
print(f"0! = {faktorial(0)}")  # Output: 1