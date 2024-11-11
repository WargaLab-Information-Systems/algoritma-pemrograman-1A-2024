kata=input("masukan kata: ")
def cek_palindrom(kata):
    return kata==str(kata)[::-1]
if cek_palindrom(kata):
    print("kata tersebut merupakan palindrom")
else:
    print("kata tersebut bukan merupakan palindrom")