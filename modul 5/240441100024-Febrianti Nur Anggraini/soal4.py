def cek_palindrom(kata):
    return kata == kata[::-1]# untuk melangkah mundur satu karakter pada satu waktu,jika tidak pakai - urutanya tidak terbal

kata_input = input("Masukkan kata: ")
if cek_palindrom(kata_input):
    print(f"'{kata_input}' adalah palindrom.")
else:
    print(f"'{kata_input}' bukan palindrom.")