#dalam soal kali ini, diminta untuk membalikkan urutan dari angka angka yang sudah dimasukkan.
bilangan_asli = int(input("Masukkan bilangan bulat: "))
bilangan_terbalik = ""

while bilangan_asli > 0:
    digit_terakhir = bilangan_asli % 10
    bilangan_terbalik += str(digit_terakhir)
    bilangan_asli //= 10

print("Bilangan yang dibalik:", bilangan_terbalik)