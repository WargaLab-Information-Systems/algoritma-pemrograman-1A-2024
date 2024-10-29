size = int(input("masukkan ukuran : "))
bentuk = str(input("masukkan bentuk (X/O) : "))
while bentuk != "X" and bentuk != "O":
    print("bukan opsi bentuk")
    bentuk = str(input("masukkan bentuk (X/O) : "))
for i in range(1, size + 1):
    for j in range (size - i): #memncetak spasi
        print(" ", end="")
    for k in range (1, i + 1):
        print(bentuk + " ", end="") # membuat karakter
    print()
for i in range(1, size + 1): 
    for k in range (1, i + 1): 
        print(" ", end="")
    for j in range (size - i):
        print(bentuk + " ", end="") 
    print()
















#definisikan dimodel integer
#bentuk pake str
#while sama dengan if 
#jika bentuk tidak sama dengan X maka dia bernilai benar,
#Hitunglah 1 sampai dengan ukuran ditambah 1,+1 biar angka 5 keluar  karna tidak dimulai dari 0
# hitunglah j dari ukuran dikurangi i
# hitunglah k dari 1 sampai 1 ditambah 1 
# fungsi end itu untuk kesamping