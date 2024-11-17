bilangan_bulat = int (input("masukkan bilangan bulat: "))
if bilangan_bulat < 0:
    print ("silahkan masukkan angka dengan benar")
else:
    bilangan_terbalik = " "
    while bilangan_bulat > 0:
        digit_terakhir = bilangan_bulat % 10
        bilangan_terbalik += str(digit_terakhir)
        bilangan_bulat //= 10
    print ("berikut hasil dari bilangan yang dibalik:", (bilangan_terbalik))