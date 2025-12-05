usia = float(input("Masukkan usia kamu : "))
if usia >= 60  :
    print("Kategori : Lansia")
elif usia >= 18 and usia <60 :
    print("Kategori : Dewasa")
elif usia >= 13 and usia <17 :
    print("Kategori : Remaja")
elif usia >= 5 and usia <12 :
    print("Kategori : Anak-anak")
elif usia <= 0 :
    print("Usia tidak valid")
else:
    print("Kategori : Balita")