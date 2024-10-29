nomer = int(input("masukkan bilangan bulat:"))
strnomer = str(nomer)
strbalik = ""
#strbalik berfungsi mengembalikan string dengan urutan karakter yang terbalik
for i in range(len(strnomer)-1,-1,-1):
    strbalik+=strnomer[i]
    
print(strbalik)
#len adalah fungsi bawaan dalam python yang digunakan untuk mencari panjang string