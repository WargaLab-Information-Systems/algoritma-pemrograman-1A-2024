
print ("1. menampilkan nim terakhir : 008")
# angka 0
n=int(input("masukkan size:"))
for baris in range(n):
    for colom in range (n):
        if baris==0 or colom==0 or baris==n-1 or colom==n-1:
            print("X", 
                  end="")
        else:
            print(end=" ")
    print()
print()
for baris in range(n):
    for colom in range (n):
        if baris==0 or colom==0 or baris==n-1 or colom==n-1:
            print("X", end="")
        else:
            print(end=" ")
    print()
print()
# angka 8
for baris in range(n):
    for colom in range (n):
        if baris==0 or colom==0 or baris==n-1 or colom==n-1 or baris==n//2:
            print("X", end="")
        else:
            print(end=" ")
    print()
print()


print("2. Membalikkan angka bulat")
# memebalikkan angka
angka = int (input("masukkan angka bulat:"))
angka_int=str(angka)
angka_dibalik = ""

while angka_int:
    angka_dibalik += angka_int[-1]
    angka_int = angka_int[:-1]
angka_dibalik = int (angka_dibalik)
angka=print("membalikkan angka bulat dari:", angka_dibalik)
print()


print("3. Total benda berdasarkan waktu")
denda_per_hari=2500
denda_tambahan=5500     # 5 hari dari 10 hari
while True:
    hari_keterlambatan=int(input("berapa hari anda telat mengembalikan DVD?:"))
    if hari_keterlambatan <= 10 :
        total_denda=hari_keterlambatan * denda_per_hari
        print("anda mendapatkan denda rp",total_denda)
    else :
        total_denda=hari_keterlambatan* denda_per_hari
        sisa_keterlambatan = hari_keterlambatan-10
        total_denda +=(sisa_keterlambatan//5)*denda_tambahan     
        print("anda mendapatkan total denda rp",total_denda)

    ulang=input ("apakah anda ingin menghitung kembali? (ya/tidak) :")
    if ulang == "tidak":
        print ("terim kasih")
        break 


