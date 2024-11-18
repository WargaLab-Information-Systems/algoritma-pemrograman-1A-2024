input_kata = str(input("masukkan kata palindrom: "))
def cek_palindrom (input_kata):
    if input_kata == input_kata [:-1]:
        print(f"{input_kata} adalah kata palindrom")
    else:
        print(f"{input_kata} bukan kata palindrom")
    return input_kata
x = input_kata
print(cek_palindrom(x))