print("=== Selamat datang di Toko Penyewaan DVD Juminten ===")

while True:
  print("Silakan masukkan lama waktu penyewaan (dalam hari): ")
  lama_sewa = int(input())

  # denda per hari
  denda_per_hari = 2500
  
  # denda tambahan untuk setiap 5 hari keterlambatan
  denda_tambahan = 5500

  # Menghitung total denda keterlambatan
  if 0 < lama_sewa <= 5:
    total_denda = 0
    print("kerenn anda tidak telat dalam pengembalian DVD")
    print("Jangan lupa datang kembali dan Terima kasih!")

  else:
    keterlambatan = lama_sewa - 5
    total_denda = keterlambatan * denda_per_hari
    if keterlambatan >= 5:
      total_denda += (keterlambatan // 5) * denda_tambahan
  
    print(f"Total denda keterlambatan anda sebesar : Rp.{total_denda}")
    print("Tolong Segera Dilunasi sekarang!!")
    print("Terima kasih")
  
  jawab = str(input("Apakah Anda ingin menghitung kembali ? {y/n} : "))
  
  if jawab == "y" or jawab == "ya":
    continue
  elif jawab == "n" or jawab == "tidak":
    break
  else: 
    print("maaf inputan anda invalid")
    break