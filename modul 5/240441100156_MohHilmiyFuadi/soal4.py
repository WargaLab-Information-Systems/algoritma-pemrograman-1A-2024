def cek_palindrom(kata):
    
    kata = kata.lower()
    
    # Membandingkan kata dengan kebalikannya
    return kata == kata[::-1]

kata_input = input("Masukkan kata atau frasa untuk dicek: ")

if cek_palindrom(kata_input):
    print(f'"{kata_input}" True')
else:
    print(f'"{kata_input}" False')