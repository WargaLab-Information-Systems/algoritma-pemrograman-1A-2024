klub_basket = {"naisa","windy", "yesica", "yeyen", "ainun", "eka"}
klub_renang = {"rendy", "dian","ainun", "wawan", "yeyen",  "farih"}

print(f"berikut adalah nama siswa yang mengikuti kedua klub : {klub_renang&klub_basket}")
print(f"berikut adalah nama siswa yang mengikuti satu klub : {klub_renang-klub_basket}{klub_basket-klub_renang}")
print(f"berikut adalah nama siswa unik yang mengikuti kedua klub: {klub_basket|klub_renang}")
print(f"berikut data dari jumlah siswa yang mengikuti setidaknya satu dari kedua klub sebanyak {len(klub_renang|klub_basket)} siswa")