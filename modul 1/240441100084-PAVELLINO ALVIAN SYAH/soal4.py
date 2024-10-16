# # soal nomer 4
import math
def calculate_combinations(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n-k))
n = 7
k = 4

number_of_combinations = calculate_combinations(n, k)
print("Jumlah cara membentuk tim adalah:", number_of_combinations)