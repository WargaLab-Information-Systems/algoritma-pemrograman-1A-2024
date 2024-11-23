# #soal no 1
# n =int(input(f"masukkan angka tinggi:"))
# print()

# for i in range (n):
#     for j in range(n,i,-1):
#      print(" ", end = " ")
#     for j in range (2* i + 1):
#       print("o", end = " ")
#     print()
# for i in range(n-2,-1,-1):
#     for j in range(n,i,-1):
#      print(" ", end = " ")
#     for j in range (2* i + 1):
#       print("o", end = " ")
#     print()

#soal no 2
n = int(input("masukkan angka yang ingin kamu masukan angka desimal ke biner:"))
nilai=" "
while n > 0 :
    modulus= n % 2
    n = n//2
    nilai=str(modulus)+nilai
print(int(nilai))
print(f"konverensi bilangan bulatnya adalah{nilai}")
print("untuk bentuk segitiganya")
variabel1 = int(nilai)
variabel2 = len(nilai)

for kolom in range(1, len(nilai)):
    for baris in range(variabel2 - 1):
        print(" " , end = " ")
    for bentuk in range (1 , kolom + 1):
        print(nilai, end = " ")
    print()


#soal no 3






















# def kebiner():
#     biner= " "
#     desimal = int(input("masukkan anka:"))
#     print()
#     while desimal >0:
#         if desimal %2 == 0:
#            biner = " " + biner
#         else:
#             biner ="1" + biner 
#             desimal = desimal / 2
#     print(" angka biner dari " +str(desimal)+ "adalah" + str(biner))
#     print()

        