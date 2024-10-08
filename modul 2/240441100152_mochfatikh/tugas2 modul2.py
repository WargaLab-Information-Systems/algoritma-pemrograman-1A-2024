#diketahui skor jaka
skor_jaka = 1100
ipk_jaka =3.5

skor_ida = 1000
ipk_ida  =3.0

syarat_skor = 1100
syarat_ipk =3.0

if skor_jaka >=syarat_skor and ipk_jaka >= syarat_ipk:
    print("jaka lulus")
else:
    print("jaka tidak lulus karena kehilangan nilainya kurang")
if skor_ida >=syarat_skor and ipk_ida >=syarat_ipk:
    print("ida lulus")
else:
    print("ida tidak lulus karena nilainya kurang")