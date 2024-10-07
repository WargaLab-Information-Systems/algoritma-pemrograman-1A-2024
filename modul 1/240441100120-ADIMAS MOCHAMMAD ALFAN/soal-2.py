suku5 = 11
suku8_dan_suku12 = 52
 
# mencari suku pertama dan beda suku menggunakan sistem persamaan
# suku ke-5 = 11
# hasil jumlah suku ke-8 dan suku ke-12 = 52
# hasil rumus dereta aritmatika a + 4b =11,2a + 11b = 52
# sistem persamaan yaitu a + 4b = 11, menjadi a = 11 - 4b
# a disubstitusi ke dalam 2a + 18b =52, menjadi 2(11 - 4b) + 18b = 52
# disederhanakan 22 + (8b + 18b) = 52 jadi 10b = 30 => b = 3
# substitusi b ke dalam a = 11 - 4b, menjadi a = 11 - 12 => a = -1
# dihitung dengan metode sistem persamaan menjadi a =-1 b =3 
 
a = -1  # a = suku pertama
b = 3   # b = beda suku
n = 8   # jumlah suku ke-8

# mencari hasil jumlah 8 suku pertama
jumlah_8suku =int(n/2 *(2*a+(n-1)*b))
print("jumlah nilai 8 suku pertama dari deret aritmatika adalah :", jumlah_8suku)