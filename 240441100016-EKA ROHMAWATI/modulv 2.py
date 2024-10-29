#input angka
i = int(input("Masukkan bilangan desimal: "))

# Mengonversi desimal ke biner
biner = " " #menggunakan string kosong yang akan digunakan untuk menyimpan hasil konversi dari bilangan desimal ke biner.
while i > 0: #Loop akan terus berjalan selama i (bilangan desimal yang dimasukkan) lebih besar dari 0 yang akan terus melakukan konversi hingga semua nilai dari i habis.
    sisa = i % 2  #untuk mendapatkan sisa pembagian menggunakan operasi modulus (%) untuk mendapatkan sisa dari pembagian i dengan 2 yang memberi angka 0 atau 1 merupakan digit dalam sistem biner.
    biner = str(sisa) + biner  # menambahkan sisa ke depan string biner membangun representasi biner dari angka desimal dari belakang ke depan.
    i = i // 2  # membagi desimal dengan 2 menggunakan pembagian bulat (//) untuk mengurangi nilai i untuk iterasi berikutnya.

# Menampilkan hasil dalam bentuk pola segitiga
print("Bilangan Biner: ",biner)
for i in range(len(biner)): #loop yang berjalan dari 0 hingga panjang string biner len(biner) untuk memastikan mencetak semua karakter dalam string biner yang merupakan representasi biner dari bilangan desimal
    print(biner[:i]) #loop mencetak substring dari biner yang dimulai dari indeks 0 hingga indeks i