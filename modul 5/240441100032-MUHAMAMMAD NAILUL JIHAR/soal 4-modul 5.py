def cek_palindrom(kata):
    kata = kata.lower()
    return kata == kata[::-1]

print(F"Kata KATAK bernilai = {cek_palindrom("katak")}")
print(F"Kata KAKAK bernilai = {cek_palindrom("kakak")}")
print(F"Kata KAPAK bernilai = {cek_palindrom("kapak")}")
print(F"Kata KAMUS bernilai = {cek_palindrom("kamus")}")