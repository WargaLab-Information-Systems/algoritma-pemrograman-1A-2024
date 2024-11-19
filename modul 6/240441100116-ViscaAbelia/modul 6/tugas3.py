#PENGIRIMAN BARANG
Barang = []
while True:
    print('-Pengiriman Barang-')
    NamaBarang = input('masukkan nama barang : ')
    ID_Barang = int(input('masukkan ID barang : '))
    TingkatPrioritas = input('masukkan tingkat prioritas (darurat/biasa/non-darurat) : ')
    DataBarang = [NamaBarang, ID_Barang, TingkatPrioritas]
    if TingkatPrioritas == 'darurat':
        Barang.insert(0, DataBarang)
    elif TingkatPrioritas == 'biasa':
        tengah = len(NamaBarang) // 2
        Barang.insert(tengah, DataBarang)
    elif TingkatPrioritas == 'non-darurat':
        Barang.append(DataBarang)
    else:
        print('jawaban tidak sesuai')
    
    for i in range(len(Barang)):
        data = Barang[i]
        print(f'ID barang : {data[0]}, Nama Barang : {data[1]}, Tingkat Prioritas : {data[2]}')
        
    IsiLagi = input('apakah anda ingin mengisi data lagi? (iya/tidak) ')
    if IsiLagi == 'tidak':
        break