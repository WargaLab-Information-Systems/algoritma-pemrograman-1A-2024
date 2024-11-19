def cek_palindrom(kata):
    if kata == kata[::-1]:
        print(kata[::-1])
        return 'true,merupakan palindrom'
    else:
        print(kata[::-1])
        return 'false,bukan palindrom'
while True:    
    kata = str(input("masukkan sebuah kata: "))
    if kata.isalpha():
        print(cek_palindrom(kata))
        break
    else:
        print('masukan huruf')