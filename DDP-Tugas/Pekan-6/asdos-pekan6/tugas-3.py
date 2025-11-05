password = "python123"

while True:
    password_input= (input("Masukkan password: "))
    if password_input == password:
        print("Password benar")
        break
    else:
        print("Password salah")
