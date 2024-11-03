n = int(input("masukkan nomor: "))
wadah = ""
while (n>0) :
    r=n%2
    wadah=str(r)+wadah
    n=n//2
print (wadah)
for i in range(1, len(wadah)+1):
    print (wadah[:i])
        
