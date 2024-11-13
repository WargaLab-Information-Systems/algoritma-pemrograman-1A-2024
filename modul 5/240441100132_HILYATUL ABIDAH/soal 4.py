kata = str(input("Masukkan contoh kata palindrom: "))
def palindrom(kata):  
    if kata == kata [::-1] : # titik dua seperti pada perulangan for (start,stop,step)
        print(f"'{kata}' adalah palindrom.") 
    else: 
        print(f"'{kata}' bukan palindrom.")
    return kata
print(palindrom(kata))

#palindrom adalah kata kata yang dapat dibaca sama dari depan dan belakang