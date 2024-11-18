hari = {
    1: "Senin",
    2: "Selasa",
    3: "Rabu",
    4: "Kamis",
    5: "Jumat",
    6: "Sabtu",
    7: "Minggu"
}

print("Masukkan nomor hari (1-7):")
nomor = int(input())
if nomor in hari:
    print("Hari ke-", nomor, "adalah:", hari[nomor])
else:
    print("Nomor hari tidak valid")
    