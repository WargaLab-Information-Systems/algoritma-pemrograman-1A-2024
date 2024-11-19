klub_basket = {'yesika', 'rendy', 'yeyen', 'dian', 'eka', 'ainun'}
klub_renang = {'ainun', 'jefri', 'bita', 'hilmy', 'naisa', 'dian'}

siswa2klub= (klub_basket & klub_renang)
print('Siswa yang mengikuti 2 klub adalah')
angka = 0
for siswa in siswa2klub:
    angka += 1
    print(f'{angka} {siswa}')

siswa1klub = (klub_basket - klub_renang) | (klub_renang - klub_basket)
print('Siswa yang mengikuti 1 klub adalah')
angka = 0
for siswa in siswa1klub:
    angka += 1
    print(f'{angka} {siswa}')

siswaunik = (klub_basket | klub_renang)
print(f'Siswa unik yang setidaknya mengikuti satu dari kedua klub adalah')
angka = 0
for siswa in siswaunik:
    angka += 1
    print(f'{angka} {siswa}')

jumlah_siswa_unik = len(siswaunik)
print(f'Jumlah siswa unik adalah : {jumlah_siswa_unik}')

