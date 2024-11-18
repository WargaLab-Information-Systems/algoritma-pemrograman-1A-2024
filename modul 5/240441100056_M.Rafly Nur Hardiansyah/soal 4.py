def cek_palindrom(kata):
    dibalik = ""
    for i in kata:
        dibalik = i + dibalik
        print(i)
    if dibalik == kata:
        return True
    else:
        return False
kata = input("Masukkan kata untuk cek palindrom: ")
print(cek_palindrom(kata))
