kata = input("Masukkan sebuah kata: ")
def cek_palindrom(kata):
    kata_dibalik = ""
    kata_dibalik += kata [-1]
    kata = kata [:1]
    return kata == kata_dibalik
    
if cek_palindrom(kata):
    print(f"kata {kata}, adalah palindrom")
else:
    print(f"kata {kata}, bukan palindrom")