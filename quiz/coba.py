nama_kendaraan = input("masukkan nama kendaraan (mobil/motor): ")
jenis_bensin = input("masukkan jenis bensin (pertalite/pertamax/pertamax turbo): ")
kota_dituju = input("masukkan kota tujuan (jakarta/bogor/depok/bekasi/tangerang): ")


if jenis_bensin == "pertalite":
    harga_per_liter = 10000
    jarak_per_liter = 12
elif jenis_bensin == "pertamax":
    harga_per_liter = 14000
    jarak_per_liter = 13
elif jenis_bensin == "pertamax turbo":
    harga_per_liter = 17000
    jarak_per_liter = 13.5
else:
    print("Jenis bensin tidak dikenali.")