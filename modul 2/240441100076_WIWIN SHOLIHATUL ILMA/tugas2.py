# Data Jaka
skor_jaka = 1100
ipk_jaka = 3.5

# Data Ida
skor_ida = 1000
ipk_ida = 3.5

# Persyaratan Beasiswa
skor_minimum = 1100
ipk_minimum = 3.0

# Cek kelayakan jaka
if skor_jaka > skor_minimum and ipk_jaka >= ipk_minimum:
    print("Jaka lulus persyaratan beasiswa")
else: 
    print("Jaka tidak lulus persyaratan beasiswa")

# Cek kelayakan ida
if skor_ida > skor_minimum and ipk_ida >= ipk_minimum:
    print("Ida lulus persyaratan beasiswa")
else:
    print("Ida tidak lulus persyaratan beasiswa")