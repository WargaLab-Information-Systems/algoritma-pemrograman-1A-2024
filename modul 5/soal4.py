def cek_palindrom(kata):
    # membandingkan kata dengan versi terbaliknya 
    return kata == kata[::-1]

# masukkan kata
kata_input = input("masukkan kata: ")

# memeriksa dan mencetak hasil
if cek_palindrom(kata_input):
    print(f"kata adalah palindrom")
else:
    print(f"kata tersebut bukan palindrom")