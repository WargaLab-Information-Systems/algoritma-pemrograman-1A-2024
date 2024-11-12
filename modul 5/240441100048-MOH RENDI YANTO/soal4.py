def cek_palindrom(kata):
    kata = kata.lower()
    return kata == kata[::-1]

kata = input("masukkan kata yang ingin cek : ")
print(f"Apakah '{kata}' adalah palindrom? {cek_palindrom(kata)}")