# Fungsi untuk memeriksa apakah sebuah kata adalah palindrom
def cek_palindrom(kata):
    # Mengubah kata menjadi huruf kecil agar tidak peka terhadap huruf besar/kecil
    kata = kata.lower()
    
    # Memeriksa apakah kata sama dengan kata yang dibalik
    if kata == kata[::-1]:  # [::-1] digunakan untuk membalik urutan karakter
        return True
    else:
        return False

# Input dari pengguna
kata = input("Masukkan sebuah kata: ")

# Memeriksa apakah kata adalah palindrom dan menampilkan hasil
if cek_palindrom(kata):
    print(f"{kata} adalah palindrom.")
else:
    print(f"{kata} bukan palindrom.")