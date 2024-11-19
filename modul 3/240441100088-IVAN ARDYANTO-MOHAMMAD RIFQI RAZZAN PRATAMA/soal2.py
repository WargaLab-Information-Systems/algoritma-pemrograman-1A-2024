angka = int(input("Masukkan sebuah angka bulat: "))

angka_terbalik = 0

# Proses membalikkan angka menggunakan loop
while angka > 0:
    digit = angka % 10
    angka_terbalik = (angka_terbalik * 10) + digit
    angka = angka // 10

# Menampilkan hasil
print("Angka yang sudah dibalik:", angka_terbalik)