# kombinasi 
# rumus: C(a, b) = a! / b!(a-b)!
import math

a = 7 # total semua
b = 4 # total orang yg dipilih

# kombinasi dengan menggunakan fungsi
def kombinasi(a, b):
    # menggunakan rumus math.comb 
    comb = math.comb(a, b)
    return comb

# memanggil fungsi untuk mencari hasil
hasil = kombinasi(a, b)

# output
print(f"banyak cara untuk memilih tim adalah {hasil} ")