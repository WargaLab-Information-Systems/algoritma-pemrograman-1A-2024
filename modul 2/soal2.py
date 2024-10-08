# Persyaratan beasiswa
skor_minimum = 1100
ipk_minimum = 3.0

#DATA JAKA
jaka_nama = "Jaka"
jaka_skor = 1100
jaka_ipk = 3.5

#CEK KELULUSAN JAKA
if jaka_skor >= skor_minimum and jaka_ipk >= ipk_minimum:
    print(f"{jaka_nama} lulus persyaratan beasiswa.")
    print(f"selamat untuk mahasiswa {jaka_nama}")
else:
    print(f"{jaka_nama} tidak lulus persyaratan beasiswa.")
    print("jangan pantang menyerah naikkan lagi di semester kedepannya")

#DATA IDA
ida_nama = "Ida"
ida_skor = 1000
ida_ipk = 3.5

#CEK KELULUSAN IDA
if ida_skor >= skor_minimum and ida_ipk >= ipk_minimum:
    print(f"{ida_nama} lulus persyaratan beasiswa.")
    print(f"selamat untuk mahasiswa {ida_nama}")
else:
    print(f"{ida_nama} tidak lulus persyaratan beasiswa.")
    print("jangan pantang menyerah naikkan lagi di semester kedepannya")
