# data mahasiswa
nama1 = "jaka"
nilai1 = 1100
ipk1 = 3.5

nama2 = "ida"
nilai2 = 1000
ipk2 = 3.0

#persyaratan beasiswa
syarat_nilai = 1100
syarat_ipk = 3.0

#menampilkan hasil
#jaka
if nilai1 > syarat_nilai and ipk1 >= syarat_ipk :
    print(f"{nama1} memenuhi persyaratan beasiswa")
else:
    print(f"{nama1} tidak memenuhi persyaratan beasiswa")
#ida
if nilai2 > syarat_nilai and ipk1 >= syarat_ipk :
    print(f"{nama2} memenuhi persyaratan beasiswa")
else:
    print(f"{nama2} tidak memenuhi persyaratan beasiswa")