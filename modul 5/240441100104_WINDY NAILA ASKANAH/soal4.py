kata = input("masukkan kata yang ingin di periksa : ")
def palindrom(kata):
    return kata == kata[::-1]
if palindrom(kata):
    print("kata ini palindrom atau true")
else:
    print("kata ini bukan palindrom atau false")