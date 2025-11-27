
print("\nPilih operator:")
print("+  = Tambah")
print("-  = Kurang")
print("/  = Bagi")
print("*  = Kali")
print("** = Pangkat")

operator = input("Masukkan operator yang dipilih : ")

angka1 = float(input("Masukkan angka 1 : "))
angka2 = float(input("Masukkan angka 2 : "))


if operator == '+':
    hasil = angka1 + angka2
    keterangan = "tambah"
elif operator == '-':
    hasil = angka1 - angka2
    keterangan = "kurang"
elif operator == '/':
    hasil = angka1 / angka2
    keterangan = "bagi"
elif operator == '*':
    hasil = angka1 * angka2
    keterangan = "kali"
elif operator == '':
    hasil = angka1 ** angka2
    keterangan = "pangkat"
else:
    print("Operator tidak valid!")
    exit()

print("\nOutput Program :")
print("Angka pertama :", angka1)
print("Angka kedua :", angka2)
print("Pilihan Operator :", keterangan)
print(f"Hasil operator {angka1} {operator} {angka2} = {hasil} ")