belanja = int(input("Masukkan total belanja: "))
total = belanja * 0.9 if belanja > 100 else belanja
print("Total yang harus dibayar:", total)
