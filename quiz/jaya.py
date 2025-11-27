kendaraan = input("masukkan nama kendaraan (mobil/motor): ")
bensin = input("masukkan jenis bensin (pertalite/pertamax/pertamax turbo): ")
tujuan = input("masukkan kota tujuan (jakarta/bogor/depok/bekasi/tangerang): ")

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

pemakaian_bensin = jarak_kota / jarak_liter
total_harga_bensin = pemakaian_bensin * harga_liter

print("\n--- Rincian Perjalanan ---")
print(f"Nama Kendaraan      : {kendaraan}")
print(f"Jenis Bensin        : {bensin}")
print(f"Kota Tujuan         : {tujuan}")
print(f"Jarak ke Kota       : {jarak_kota} KM")
print(f"Pemakaian Bensin    : {pemakaian_bensin:.2f} liter")
print(f"Total Harga Bensin  : Rp {total_harga_bensin:.0f}")