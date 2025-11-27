# Input dari pengguna
kendaraan = input("Masukkan nama kendaraan (misal: mobil, motor): ")
bensin = input("Masukkan jenis bensin (Pertalite, Pertamax, Pertamax Turbo): ")
tujuan = input("Masukkan kota tujuan (Jakarta, Bekasi, Depok, Tangerang, Bogor): ")

# Tentukan harga dan jarak tempuh bensin berdasarkan input jenis bensin
if bensin == "pertalite":
    harga_liter = 10000
    jarak_liter = 12
elif bensin == "pertamax":
    harga_liter = 14000
    jarak_liter = 13
elif bensin == "pertamax turbo":
    harga_liter = 17000
    jarak_liter = 13.5
else:
    print("Jenis bensin tidak dikenali.")

# Tentukan jarak kota tujuan
if tujuan == "jakarta":
    jarak_kota = 20
elif tujuan == "bekasi":
    jarak_kota = 35.7
elif tujuan == "depok":
    jarak_kota = 5
elif tujuan == "tangerang":
    jarak_kota = 99
elif tujuan == "bogor":
    jarak_kota = 120.6
else:
    print("Kota tujuan tidak dikenali.")

# Hitung pemakaian bensin (liter) dan total biaya
pemakaian_bensin = jarak_kota / jarak_liter
total_harga_bensin = pemakaian_bensin * harga_liter

# Output hasil
print("\n--- Rincian Perjalanan ---")
print(f"Nama Kendaraan      : {kendaraan}")
print(f"Jenis Bensin        : {bensin}")
print(f"Kota Tujuan         : {tujuan}")
print(f"Jarak ke Kota       : {jarak_kota} KM")
print(f"Pemakaian Bensin    : {pemakaian_bensin:.2f} liter")
print(f"Total Harga Bensin  : Rp {total_harga_bensin:}")
