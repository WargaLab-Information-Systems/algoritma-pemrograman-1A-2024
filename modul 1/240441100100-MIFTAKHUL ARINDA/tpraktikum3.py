usd = 35 # uang dollar suraji
kurs = 15102.10 # kurs tgl 25 september

# menghitung dengan menggunakan fungsi
def hitung_rupiah(usd, kurs):
    rupiah = usd * kurs
    return rupiah

# memanggil fungsi
uang_rupiah = hitung_rupiah(usd, kurs)

# output 
print(f"uang yang didapatkan Suraji setelah menukarkan uang adalah {uang_rupiah} ")