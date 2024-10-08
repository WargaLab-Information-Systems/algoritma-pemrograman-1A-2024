Orang1 = "jaka"
Orang2 = "ida"

# skor jaka
skor_jaka = 1100
ipk_jaka = 3.5
# skor ida
skor_ida = 1000
ipk_ida = 3.5
# syarat skor
syarat_skor = 1100
syarat_ipk = 3.0

# perintah if else
if skor_jaka > syarat_skor and ipk_jaka > syarat_ipk:
    print(f"{Orang1} lulus beasiswa")
else:
    print(f"{Orang1} tidak lulus beasiswa karena nilainya kurang")

# perintah if else
if skor_ida > syarat_skor and ipk_ida > syarat_ipk:
    print(f"{Orang2} lulus beasiswa")
else:
    print(f"{Orang2} tidak lulus beasiswa karena nilainya kurang")
    