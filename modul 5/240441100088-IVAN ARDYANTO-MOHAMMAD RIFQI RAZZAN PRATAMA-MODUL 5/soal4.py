def cek_palindrom(kata):
    dibalik = ""

    for i in kata:
        dibalik = i + dibalik
    
    print(f"Kata dibalik: {dibalik}")  
    
    if dibalik == kata:
        return True
    else:
        return False

kata = input("Masukkan kata untuk cek palindrom: ")
print(f"Palindrom: {cek_palindrom(kata)}")