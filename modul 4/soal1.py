lebar_belah_ketupat = int(input('Input lebar belah ketupat: '))
karakter = input("Masukkan karakter untuk pola misalnya X atau O: ")

if karakter =="o":  
  for i in range(lebar_belah_ketupat):
    for j in range(lebar_belah_ketupat-i):
      print(' ',end='')
      
    for k in range(i+1):
      print( "o",end='')
    print()
 
  for i in range(1,lebar_belah_ketupat):
    for j in range(i+1):
      print(' ',end='')
      
    for k in range(lebar_belah_ketupat-i):
      print( "o",end='')
    print()
elif karakter =="x":  
  for i in range(lebar_belah_ketupat):
    for j in range(lebar_belah_ketupat-i):
      print(' ',end='')
      
    for k in range(i+1):
      print( "x",end='')
    print()
 
  for i in range(1,lebar_belah_ketupat):
    for j in range(i+1):
      print(' ',end='')
      
    for k in range(lebar_belah_ketupat-i):
      print( "x",end='')
    print()
else:
  print("bukan karakter yang di inginkan")  