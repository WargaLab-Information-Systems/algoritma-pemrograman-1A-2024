#fungsi data panitia
def datapanitia():
    data1 = ('2401', 'Jefri', 'Madura', 'Humas', 'CO')
    data2 = ('2402', 'Windy', 'Bojonegoro', 'Acara', 'Anggota')
    data3 = ('2403', 'Jihar', 'Sidoarjo', 'PDD', 'CO')
    data4 = ('2404', 'Hilya', 'Gresik', 'Konsumsi', 'Anggota')
    data5 = ('2405', 'Farhan', 'Pasuruan', 'Perkab', 'CO')
    data = [data1, data2, data3, data4, data5]
    return data


#fungsi untuk mencari data
def caridata(listdata, atb):
    hasil = []
    for i in listdata:
        if (atb.lower() in i[0].lower() or atb.lower() in i[1].lower() or atb.lower() in i[2].lower() or atb.lower() in i[3].lower() or atb.lower() in i[4].lower()):   
            hasil.append(i)
    return hasil


#fungsi untuk menampilkan data
def tampilkandata(listdata):
    for i in listdata:
        print(f'NIP: {i[0]}, Nama: {i[1]}, Alamat: {i[2]}, Departemen: {i[3]}, Jabatan: {i[4]}')

#nyummi, aplikasikan fungsi yg sdh dibuat
print('Data panitia MAKASI 2024')
listdata = datapanitia()
tampilkandata(listdata)
while True:
    tanya = input('\nApakah kamu ingin mencari data panitia?(y/g): ')
    if tanya == 'y':
        atb = input('Silahkan masukkan atribut panitia: ')
        hasil = caridata(listdata, atb)
        if hasil:
            print('\nData panitia ditemukan')
            tampilkandata(hasil)
        else:
            print('\nData tidak ditemukan')
    elif tanya == 'g':
        print('okeyy, terimakasih. MAKASI 2024 DATANG YA!')
        break
    else: 
        print('input salah!')