# pertama kita masukkan data yang tertera pada soal
# jaka
skor_jaka = 1100
Ipk_jaka = 3.5

# ira
skor_ida = 1000
Ipk_ida = 3.5

# peryaratan minimal lulus Beasiswa
skor_minimal = 1100
Ipk_minimal = 3.0

# cek pengkondisian antara jaka dan ira 
if skor_jaka > skor_minimal and Ipk_jaka > Ipk_minimal:
    print("jaka lulus persyaratan beasiswa")
elif skor_ida > skor_minimal and Ipk_ida > Ipk_minimal:
    print("ida lulus persyaratan beasiswa ")
else:
    print("jaka dan ida tidak lulus persyaratan beasiswa")