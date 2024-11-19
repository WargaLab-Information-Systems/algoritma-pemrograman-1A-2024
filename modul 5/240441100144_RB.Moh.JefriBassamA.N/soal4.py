print("---Selamat Datang di Pengecekan kata Palindrom---")
while True:
    kata = str(input("masukkan kata yang ingin ada cek : "))
    def cek_palindrom(kata):
        return kata == kata[::-1]
    
    if cek_palindrom(kata) == True :
        print(f"{kata} adalah kata Palindrom")
    elif cek_palindrom(kata) == False:
        print(f"{kata} adalah bukan kata Palindrom")

    ulang = str(input("ingin mengecek kembali? [y/n]"))
    if ulang == "y":
        continue
    elif ulang == "n":
        break


