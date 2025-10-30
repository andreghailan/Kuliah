print("===== Menghitung Luas dan Keliling Tabung =====")
phi = 22/7
Jari = float(input("Masukkan Jari-Jari alas tabung : "))
luas = float(input("Masukkan Luas alas tabung : "))
tinggi = float(input("Masukkan Tinggi tabung : "))
luas_permukaan = 2 * phi * Jari * (Jari + tinggi)

Keliling = 2 * phi * Jari
print("--------------------------------")
print("Keliling tabung adalah : ", Keliling)
print("Luas permukaan tabung adalah : ", luas_permukaan)