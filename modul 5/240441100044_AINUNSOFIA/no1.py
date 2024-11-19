def calculate_diskon():
    diskonanggota = 0
    if anggota == 1:
        diskonanggota += 0.15
        print ('kamu mendapat diskon keanggotaan 15%')
    elif anggota == 2:
        diskonanggota += 0.10
        print ('kamu mendapat diskon keanggotaan 10%')
    elif anggota == 3:
        diskonanggota += 0.05
        print ('kamu mendapat diskon keanggotaan 5%')
    else:
        diskonanggota += 0
        print ('kamu tidak mendapat diskon keanggotaan')


    diskonbelanja = 0
    if belanja > 1000000:
        diskonbelanja += 0.05
        print ('kamu mendapat diskon belanja 5%')
    else:
        diskonbelanja += 0
        print ('kamu tidak mendapat diskon belanja')

    jumlahdiskon = diskonbelanja + diskonanggota
    print('jumlah diskon yang kamu peroleh',jumlahdiskon)
    potonganharga = jumlahdiskon * belanja
    print("ptongan harga yang kamu peroleh",potonganharga)
    totalharga = belanja - potonganharga
    return totalharga


print('selamat datang di toko kami,selamat berbelanja')
print('berikut perincian kode keanggotaan kami')
print(' 1. gold')
print(' 2. silver')
print(' 3. bornze')
print(' 4. tidak ada')
anggota = int(input('masukkan kode keanggotaan mu : '))
belanja = float(input('masukkan total belanja mu : '))
print('total belanja setelah diskon', calculate_diskon())