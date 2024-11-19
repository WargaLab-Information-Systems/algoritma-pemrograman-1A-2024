# dict akses berdasarkan identifier
# ada key sama value

# key
nilai_mahasiswa = {
    "Davin" : "85",
    "Razan" : "20",
    "Dika" : "10"
}

print(nilai_mahasiswa.keys())

print(nilai_mahasiswa.values())

print(nilai_mahasiswa.items())

for key,value in nilai_mahasiswa.items():
    print(f"nama = {key}, nilai = {value}")

# Tambah & Update
nilai_mahasiswa["Dika"] = 15

print(nilai_mahasiswa)

nilai_mahasiswa["Eka"] = 13

print(nilai_mahasiswa)

# Update yang lainnya
nilai_mahasiswa.update({"Eka":"50"})
print(nilai_mahasiswa)

# Hapus
del nilai_mahasiswa["Dika"]
print(nilai_mahasiswa)

# Set adalah data yang tidak memiliki urutan dan tidak memiliki elemen duplikat

A = {1,1,3,5,4,2,2,30,40}
B = {2,3,1,3,2,4,5,90}

print(A)
print(B)

# Set memiliki 3 operasi
# Union (gabungan)
# Intersection (Irisan)
# Difference (Perbedaan)

print(A.union(B))
print(A|B)

print(A.intersection(B))

print(A.difference(B))

print(B.difference(A))
print(A-B)

# Tambah
A.add(8)
print(A)

# Hapus
A.remove(3)
print(A)