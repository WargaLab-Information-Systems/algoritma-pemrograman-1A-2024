#cek palindrom
def cek_palindrom(kata):
    Kata = kata[::-1]
    if kata == Kata:
        return True
    else:
        return False
    
kata = input('masukkan kata yang akan di cek :')
print(cek_palindrom(kata))