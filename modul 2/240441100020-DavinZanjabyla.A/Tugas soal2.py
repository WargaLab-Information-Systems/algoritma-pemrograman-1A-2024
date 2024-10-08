# skor_ida = 1000
# skor_jaka = 1000
# ipk_ida = 3.5
# ipk_jaka = 3.5

skor_ida = int(input("masukan skor ida : "))
ipk_ida = int(input("masukan ipk ida : "))
if skor_ida >= 1000 and ipk_ida >= 3:
    print('ida lolos mendapatkan beasiswa')
else:
    print('ida tidak lolos seleksi penerimaan beasiswa')

skor_jaka = int(input("masukan skor jaka : "))
# ipk_ida = int(input("masukan ipk ida : "))
ipk_jaka = int(input("masukan ipk jaka : "))

# if skor_ida >= 1000 and ipk_ida >= 3:
#     print('ida lolos mendapatkan beasiswa')
# else:
#     print('ida tidak lolos seleksi penerimaan beasiswa')

if skor_jaka <= 1100 or ipk_jaka >= 3:
    print('jaka lolos mendapatkan beasiswa')
else:
    print('jaka tidak lolos seleksi penerimaan beasiswa')

