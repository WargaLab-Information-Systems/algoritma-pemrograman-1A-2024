def reverse_integer(num):
    reversed_num = int(str(num)[::-1])  
    return reversed_num

user_input = input("Masukkan angka bulat: ")

if user_input.isdigit() or (user_input[0] == '-' and user_input[1:].isdigit()):
    number = int(user_input)
    reversed_number = reverse_integer(number)
    print("Angka yang dibalik: ", reversed_number)
else:
    print("Input tidak valid! Harap masukkan angka bulat.")
