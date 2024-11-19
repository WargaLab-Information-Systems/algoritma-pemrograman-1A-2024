#klub ekstrakurikuler
klub_renang = {'minji', 'hanni', 'danielle', 'haerin', 'hyein', 'hueningkai'}
klub_basket = {'yeonjun', 'soobin', 'beomgyu', 'taehyun', 'hueningkai', 'danielle'}
def klubrenang():
    print(f'daftar siswa yang mengikuti klub renang')
    no = 1
    for siswa in klub_renang:
        print(f'{no}. {siswa}')
        no += 1
def klubbasket():
    print(f'daftar siswa yang mengikuti klub basket')
    no = 1
    for siswa in klub_basket:
        print(f'{no}. {siswa}')
        no += 1
def kedua_klub():
    print(f'daftar siswa yang mengikuti kedua klub')
    daftar_siswa = klub_renang & klub_basket
    no = 1
    for siswa in daftar_siswa:
        print(f'{no}. {siswa}')
        no += 1

def satu_klub():
    daftar_siswa = (klub_renang.difference(klub_basket))|(klub_basket.difference(klub_renang))
    print('daftar siswa yang hanya mengikuti satu klub:')
    no = 1
    for siswa in daftar_siswa:
        print(f'{no}. {siswa}')
        no += 1
    
def semua_siswa():
    daftar_siswa = klub_renang|klub_basket
    print('daftar siswa unik yang setidaknya mengikuti satu dari kedua klub:')
    no = 1
    for siswa in daftar_siswa:
        print(f'{no}. {siswa}')
        no += 1

def jumlah_siswa():
    daftar_siswa = klub_renang|klub_basket
    print(f'jumlah siswa unik yang setidaknya mengikuti satu dari kedua klub:', len(daftar_siswa))


while True:
    print('--- DAFTAR SISWA YANG MENGIKUTI EKSTRAKURIKULER ---')
    print('1. Daftar siswa yang mengikuti klub renang')
    print('2. Daftar siswa yang mengikuti klub basket')
    print('3. Daftar siswa yang mengikuti kedua klub')
    print('4. Daftar siswa yang mengikuti satu klub')
    print('5. Daftar siswa unik yang mengikuti satu dari kedua klub')
    print('6. Jumlah siswa unik yang mengikuti satu dari kedua klub')
    print('7. Keluar')

    opsi = int(input('pilih opsi:'))
    print()
    if opsi == 1:
        klubrenang()
        print()
    elif opsi == 2:
        klubbasket()
        print()
    elif opsi == 3:
        kedua_klub()
        print()
    elif opsi == 4:
        satu_klub()
        print()
    elif opsi == 5:
        semua_siswa()
        print()
    elif opsi == 6:
        jumlah_siswa()
        print()
    elif opsi == 7:
        break
    else:
        print('opsi yang dipilih tidak valid')
        print()
    
