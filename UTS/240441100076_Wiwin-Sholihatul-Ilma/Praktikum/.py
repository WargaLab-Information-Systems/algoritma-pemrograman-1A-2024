makan = input("Apakah anda sudah makan: (ya/tidak)")
mandi = input("Apakah anda sudah mandi: (ya/tidak)")
transportasi = input("Jalan kaki atau Menggunakan motor: ")

waktu_makan = 15
waktu_mandi = 10
jalan_kaki = 30
motor = 15
persiapan = waktu_makan + waktu_mandi
perjalanan1 = persiapan + jalan_kaki
perjalanan2 = persiapan + motor
batas_waktu = 60

total_perjalanan1 = persiapan + perjalanan1 
total_perjalanan2 = persiapan + perjalanan2
print(total_perjalanan1)
print(total_perjalanan2)

if makan == "tidak":
    print("Silahkan makan")
elif mandi == "ya":
    print("Silahkan mandi")
else:
    print("Silahkan pilih transportasi", transportasi)

if batas_waktu < 50:
    print("Anda tepat waktu")
elif batas_waktu < 40:
    print("Anda tepat waktu")
else:
    print("Anda terlambat")