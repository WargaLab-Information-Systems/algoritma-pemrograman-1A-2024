klub_basket = {'Hilya', 'Febby', 'Arinda', 'Noval', 'Khofifah'}
klub_renang = {'Febby', 'Arinda', 'Khofifah', 'Rio', 'Putra'}

print("\nSiswa yang mengikuti kedua klub:")
print(klub_basket&klub_renang) #intersection(irisan)
 
print("\nSiswa yang hanya mengikuti satu klub:")
print(klub_basket-klub_renang) #diference(selisih)

print("\nsiswa unik yang mengikuti setidaknya satu dari kedua klub tersebut:")
print(klub_basket|klub_renang) #union(gabungan)

print("\njumlah siswa unik yang mengikuti setidaknya satu dari kedua klub:")
print(len(klub_basket|klub_renang)) #len(menghitung jumlah elemen hasil gabungan)