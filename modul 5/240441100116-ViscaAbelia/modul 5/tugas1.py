#fungsi calculate_discount
def calculate_discount():
    Total_belanja = int(input('berapa total belanja anda? '))
    Tanya_keanggotaan = input('apakah anda memiliki keanggotaan? (iya/tidak) ')
    if Tanya_keanggotaan == 'tidak' and Total_belanja > 1000000:
        Diskon = 5/100 * Total_belanja
        Total_belanja -= Diskon
    elif Tanya_keanggotaan == 'tidak':
        Diskon = 0
    else:
        Keanggotaan = input('keanggotaan apa yang anda miliki? (gold, silver, bronze) ')
        if Total_belanja > 1000000 and Keanggotaan == 'gold':
            Diskon = 20/100 * Total_belanja
            Total_belanja -= Diskon
        elif Total_belanja > 1000000 and Keanggotaan == 'silver':
            Diskon = 15/100 * Total_belanja
            Total_belanja -= Diskon
        elif Total_belanja > 1000000 and Keanggotaan == 'bronze':
            Diskon = 10/100 * Total_belanja
            Total_belanja -= Diskon
        else:
            if Keanggotaan == 'gold':
                Diskon = 15/100 * Total_belanja
                Total_belanja -= Diskon
            elif Keanggotaan == 'silver':
                Diskon = 10/100 * Total_belanja
                Total_belanja -= Diskon
            elif Keanggotaan == 'bronze':
                Diskon = 5/100 * Total_belanja
                Total_belanja -= Diskon
            else:
                Diskon = 0
    print(f'Anda mendapatkan diskon {Diskon}')
    print(f'total yang harus anda bayar adalah Rp.{Total_belanja}')                
calculate_discount()
