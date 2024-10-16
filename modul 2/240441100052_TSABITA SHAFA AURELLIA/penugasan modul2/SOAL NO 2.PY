# SOAL NO 2
# skor_jaka = 1100
# ipk_jaka = 3.5
# skor_ida = 1000
# ipk_ida = 3.5

skor_jaka = int(input("Masukkan skor Jaka: "))
ipk_jaka = float(input("Masukkan IPK Jaka: "))

skor_ida = int(input("Masukkan skor Ida: "))
ipk_ida = float(input("Masukkan IPK Ida: "))

skor_minimal = 1100
ipk_minimal = 3.0

if skor_jaka > skor_minimal and ipk_jaka >= ipk_minimal:
    print("Jaka lulus persyaratan beasiswa.")
else:
    print("Jaka tidak lulus persyaratan beasiswa.")

if skor_ida > skor_minimal and ipk_ida >= ipk_minimal:
    print("Ida lulus persyaratan beasiswa.")
else:
    print("Ida tidak lulus persyaratan beasiswa.")