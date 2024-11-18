desimal = int(input("Masukkan bilangan desimal: "))
biner = "" #untuk mengkonversi bentuk desimal

while desimal> 0: #akan berjalan jika desimal lebih dari 0
    biner = str(desimal % 2) + biner #Sisa hasil bagi dari n dibagi 2 (yaitu n % 2) dihitung dan ditambahkan di awal string biner. Sisa ini bisa 0 atau 1, sesuai dengan cara kerja bilangan biner.
    desimal = desimal // 2 #dibagi 2 menggunakan pembagian bulat untuk memperkecil nilai dan melanjutkan ke proses konversi. proses berjalan smpai desimal bernilai 0

print("bilangan biner :", biner)
print("Hasil konversi dalam bentuk segitiga: ") #mengkonversi ke
for i in range(1, len(biner) + 1): #Fungsi len() dalam Python digunakan untuk menghitung dan mengembalikan jumlah elemen dalam suatu objek
    print(biner[:i]) #mengambil potongan string biner dari awal hingga indeks ke-i, menciptakan tampilan segitiga yang menyajikan bagian dari bilangan biner pada setiap baris.
#Fungsi len() dalam Python digunakan untuk menghitung dan mengembalikan jumlah elemen dalam suatu objek