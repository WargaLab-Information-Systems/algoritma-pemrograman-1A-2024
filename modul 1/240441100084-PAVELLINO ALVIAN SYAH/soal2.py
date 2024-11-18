# Pernyataan Masalah:
# Kita memiliki deret aritmatika dengan ketentuan berikut:
# Suku ke-5 dari deret tersebut adalah 11.
# Jumlah suku ke-8 dan ke-12 adalah 52.
# Kita perlu mencari jumlah 8 suku pertama dari deret tersebut.
# Langkah 1: Mari kita nyatakan suku pertama dari deret tersebut sebagai a dan bedanya sebagai d.
# Kita dapat menuliskan deret tersebut sebagai: a, a + d, a + 2d, ..., a + (n-1)d
# Langkah 2: Karena suku ke-5 adalah 11, kita dapat membuat persamaan:
# a + 4d = 11
# Langkah 3: Diketahui jumlah suku ke-8 dan ke-12 adalah 52.
# Mari kita tulis suku ke-8 dan ke-12 dalam suku a dan d:
# a + 7d (suku ke-8) a + 11d (suku ke-12)
# Jumlah kedua suku ini adalah 52, jadi kita dapat membuat persamaan lain:
# a + 7d + a + 11d = 52
# Gabungkan suku-suku yang sejenis:
# 2a + 18d = 52
# Langkah 4: Sekarang kita memiliki sistem dua persamaan dengan dua variabel:
# a + 4d = 11 2a + 18d = 52
# Kita dapat menyelesaikan sistem ini menggunakan substitusi atau eliminasi. Mari kita gunakan substitusi.
# Susun ulang persamaan pertama untuk mengisolasi a:
# a = 11 - 4d


def calculate_sum(a, d, n):
    return (n/2) * (2*a + (n-1)*d)

a = -1
d = 3
n = 8 

sum_of_first_8_terms = calculate_sum(a, d, n)
print("The sum of the first 8 terms is:", sum_of_first_8_terms)