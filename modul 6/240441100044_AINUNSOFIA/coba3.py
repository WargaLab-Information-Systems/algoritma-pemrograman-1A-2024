#membuat list untuk menyimpan data
data = []
#fungsi untuk menerima data pengiriman barang
def pengirimanbarang():
    print('Untuk melakukan pengiriman silahkan masukkan data di bawah ini')
    nama = str(input('Masukkan nama barang: '))
    id = str(input('Masukkan ID barang: '))
    while True:
        print('Untuk melanjutkan pengiriman barang, diperlukan tingkat prioritas barang')
        print('Berikut perinciannya \n1.Darurat \n2.Biasa \n3.Non-Darurat')
        tingkat = int(input('Masukkan tingkat prioritas barang: '))
        if tingkat == 1:
            tingkat1 = 'Darurat'
            kirim = (nama,id,tingkat1)
            data.insert(0,kirim)
            print('ACC,Barang akan dikirim secepatnya')
            break
        elif tingkat == 2:
            tingkat2 = 'Biasa'
            kirim = (nama,id,tingkat2)
            #for i in range(len(data)):
            if len(data) == 1 and data[0][2] == 'Darurat':
                data.append(kirim)
            elif len(data) == 1 and data[0][2] == 'Non-Darurat':
                data.insert(0,kirim)
            elif data[-1][2] == 'Darurat':
                data.append(kirim)
            elif data[-1][2] == 'Non-Darurat' or data[0][2] == 'Darurat':
                data.insert(len(data)//2,kirim)
            else:
                data.insert(len(data)//2,kirim)
            print('ACC,Barang akan dikirim secepatnya')
            break
        elif tingkat == 3:
            tingkat3 = "Non-Darurat"
            kirim = (nama, id, tingkat3)
            data.append(kirim)
            print('ACC,Barang akan dikirim secepatnya')
            break
        else:
            print('masukkan tingkat yang sesuai')

#membuat fungsi untuk menampilkan data pengiriman barang
def databarang():
    if not data:
          print('Data pengiriman barang di YUTIEM Dilivery masih kosong')
    else:
         print('\nBerikut data pengiriman barang di YUTIEM Dilivery')
         for kirim in data:
            print('Nama barang',kirim[0],'dengan ID',kirim[1],'dan tingkat prioritas',kirim[2]) 


print('Selamat datang YUTIEM Dilivery')
while True:
    pengirimanbarang()
    databarang()

    isilagi = str(input('\nApakah kamu ingin mengisi data lagi?(y/n):'))
    if isilagi != 'y':
         print('terimakasih')
         break