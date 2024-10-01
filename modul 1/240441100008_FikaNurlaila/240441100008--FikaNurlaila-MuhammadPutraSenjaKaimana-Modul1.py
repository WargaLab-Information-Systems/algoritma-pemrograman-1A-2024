
print("1. mencari volume dari tabungan andi yang berbentuk balok dan tabung")
print("- menghitung volume Balok")
# rumus volume balok (v = pxlxt)
#diket:
p=20
l=13
t=7
print("celengan andi yang berbentuk balok memiliki volume =", p*l*t)


print("- menghitung volume tabung") 
# diket:
L = 440 #Luas selimut
r = 7 #diameter = 2 kali nya jari jari (14/2)
n= 22/7
# mencari tinggi (rumusnnya  " t=L/2*22/7*r ")
t = (L/(2*n*r))
# rumus volume tabung"v = 22/7(r)t"  # r=pangkat 2
print("celengan andi yang berbentuk tabung memiliki volume =",n*(r*r)*t)
print()

# print("2. Deret aritmatika")
# Mencari jumlah nilai dari 8 suku pertama
# Diket :
# U5 = 11
# U8&U12 = 52
# U8 = .......?
# Un = a + (n-1)b
# U5 = a + (5-1)b     = a + 4b
# U8 = a + (8-1)b     = a + 7b
# U12 = a + (12-1)b   = a + 11b
# a + 7b + a + 11b =54
# 2a + 18b = 52
# a + 9b = 26
# a + 4b = 11
#      a = 11 - 4b
# substitusi a pada U8 dan U12
# a + 9b = 26      
# 11 - 4b + 9b = 26
#           5b = 26 - 11
#            b = 15/5 = 3
# mencari nilai a = 11 - 4 * 3 = 11 - 12 = -1
# S8 = 8/2 (2.-1+7*3)

a =-1
b = 3

def suku1 (a,n,b):
    return a + (n-1)*b
hasil1= suku1 (-1,1,3)
def suku2 (a,n,b):
    return a + (n-1)*b
hasil2= suku2 (-1,2,3)
def suku3 (a,n,b):
    return a + (n-1)*b
hasil3= suku3 (-1,3,3)
def suku4 (a,n,b):
    return a + (n-1)*b
hasil4= suku4 (-1,4,3)
def suku5 (a,n,b):
    return a + (n-1)*b
hasil5= suku5 (-1,5,3)
def suku6 (a,n,b):
    return a + (n-1)*b
hasil6= suku6 (-1,6,3)
def suku7 (a,n,b):
    return a + (n-1)*b
hasil7= suku7 (-1,7,3)
def suku8 (a,n,b):
    return a + (n-1)*b
hasil8= suku8 (-1,8,3)
# hasil
print ("berikut deretan sukunya")
print (hasil1)
print (hasil2)
print (hasil3)
print (hasil4)
print (hasil5)
print (hasil6)
print (hasil7)
print (hasil8)

print("2. Deret aritmatika")
a =-1
b = 3
def jumlah (n,a,b):
    return n/2 * (2 * a + ( n - 1 )*b)
hasilj= jumlah (8,-1,3)
print ("jumlah dari 8 deret pertama adalah ", hasilj )
print()

print ("3. Merubah uang dollar ke uang rupiah")
a=35   # us dollar
b=15102   # kurs tgl praktikum
print ("jadi, US$35 menukar kedalam rupiah adalah : ", a * b)
print()


print ("4. menghitung berapa banyak cara menghitung tim")
# diket : 
import math
def kombinasi(n, r):
    return math.comb(n, r)
# Total orang dan jumlah yang ingin dipilih
n = 7
r = 4
# Menghitung jumlah cara
jumlah_cara = kombinasi(n, r)
print(f"Jumlah cara untuk memilih {r} orang dari {n} orang adalah: {jumlah_cara}")
print()

# Soal
def jumlah (p,l,t):
    return p * l * t
hasilj= jumlah (20,13,7)
print ("hasil dari volume balok adalah : ", hasilj )




