def cek_palindrom(kata):
    # Mengubah kata menjadi huruf kecil untuk perbandingan yang konsisten
    kata = kata.lower()
    
    # Memeriksa apakah kata sama jika dibaca dari depan dan belakang
    return kata == kata[::-1]

# Contoh penggunaan
print(cek_palindrom("katak")) # Output: True
print(cek_palindrom("madam")) # Output: True
print(cek_palindrom("hello")) # Output: False
print(cek_palindrom("Radar")) # Output: True