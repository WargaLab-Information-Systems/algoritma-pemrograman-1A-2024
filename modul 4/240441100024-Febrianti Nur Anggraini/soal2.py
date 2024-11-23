# Mengambil input dari pengguna
desimal = int(input("Masukkan bilangan desimal: "))

# Konversi desimal ke biner secara manual
biner = ''   # tempat buat menyimpan bilangan biner yang sudah dikonfersi bilangan desimal 
while desimal > 0: #jika kita menginputkan lebih dari 0 maka akan memproses menggunakan rumus tersebut
        biner = str(desimal % 2) + biner #bilangan dasar biner 2
        desimal //= 2

# Menampilkan pola segitigai
print("bilangan biner:",biner)
for i in range(len(biner)):
    print(biner[:i])