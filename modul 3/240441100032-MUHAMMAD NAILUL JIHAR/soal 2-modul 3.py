print("Selamat datang di program pembalik urutan angka")
angka = int(input("Masukkan bilangannya : "))
angka_terbalik = ""

while angka > 0:
    angka_terakhir = angka % 10
    angka_terbalik += str(angka_terakhir)
    angka //= 10

print (f"Berikut hasil yang anda inginkan : {angka_terbalik}")