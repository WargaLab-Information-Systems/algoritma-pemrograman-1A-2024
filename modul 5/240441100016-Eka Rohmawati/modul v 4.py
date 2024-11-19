#input data
kata = input("masukkan kata: ")

#mengeksekusi
def cek_palindrom(kata):
    if kata == kata [:: -1]:
        dibalik = kata[:: -1]
        print("kebalikan dari kata:", dibalik)
        print(f"kata {kata} adalah palindrom berarti true")
        return dibalik
    else :
        dibalik = kata[:: -1]
        print("kebalikan dari kata:",dibalik)
        print(f"kata {kata} adalah bukan palindrom berarti false")
        return dibalik
        
cek_palindrom(kata)