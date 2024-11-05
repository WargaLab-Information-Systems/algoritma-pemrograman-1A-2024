def cek_palindrom(kata):
    # Mengubah semua huruf menjadi kecil
    kata = kata.lower()
    # Menggunakan slicing untuk membandingkan
    return kata == kata[::-1]
    #mengambil elemen dari urutan dalam arah terbalik

# Input dari pengguna
kata_input = input("Masukkan kata: ")
if cek_palindrom(kata_input):
    print(f"'{kata_input}' adalah palindrom.")
else:
    print(f"'{kata_input}' bukan palindrom.")