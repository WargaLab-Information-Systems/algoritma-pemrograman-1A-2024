def deret_aritmatika():
    # diketahui
    u5 = 11
    # persamaan1: a+4b = 11
    # a = 11-4b

    jumlah_u8_dan_u12 = 52
    # persamaan2: 2a+18b = jumlah_u8_dan_u12
    # 2 (11-4b) + 18b = jumlah_u8_dan_u12 (subtisusi a)

    b = (jumlah_u8_dan_u12 - 22) / 10 
    a = 11 - 4 * b 
    
    # menghitung jumlah 8 suku pertama 
    S8 = 8 / 2 * (2 * a + 7 * b)
    
    # output dari S8
    print(f"Jumlah nilai dari 8 suku pertama adalah: {S8} ")

# memanggil fungsi (def)
deret_aritmatika()