# nilai_mahasiswa = {
#     'davin' : '85',
#     'razan' : '20',
#     'dika' : '10',
# }

# print(nilai_mahasiswa.keys())

# print(nilai_mahasiswa.values())

# print(nilai_mahasiswa.items())

# for key,values in nilai_mahasiswa.items():
#     print(f'nama={key},nilai = {values}')


# #update
# nilai_mahasiswa['dika'] = 15
# print(nilai_mahasiswa)


# nilai_mahasiswa['eka'] = 13
# print(nilai_mahasiswa)


# #update yg lain
# nilai_mahasiswa.update({'eka':'50'})
# print(nilai_mahasiswa)

# #hapus/delete
# del nilai_mahasiswa['dika']
# print(nilai_mahasiswa)


#SET adalah data yg tidak memiliki urutan dan tidak memiliki elemen duplikat
A = {1,1,3,5,20,22,4,2,2}
B = {2,3,1,3,22,2,4,5,90}
# print(A)
# print(B)

#set memiliki 3 operasi , union(gabungan), intersection(irisan), selisih(different)

# print(A.union(B))
print(A|B)


# print(A.intersection(B))



# print(B.difference(A))

#tambah
# A.add(8)
# print(A)

# #hapus
# A.remove(9)
# print(A)

# kesimpulan dari bljr dictionary() dan set(himpunan)

# value itu tidak harus angka
