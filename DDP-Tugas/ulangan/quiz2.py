nama_pembeli = input("Masukan Nama Pembeli: ")
no_hp = input("Masukan No Hp Pembeli: ")
pesan_menu = input("Pesan Menu Apa? (makanan atau minuman): ")
if pesan_menu == "makanan":
    print("Menu Makanan:")
    print("1. Nasi Goreng - Rp. 15.000")
    print("2. Mie Goreng - Rp. 12.000")
    print("3. Ayam Geprek - Rp. 18.000")
    menu_pilihan = input("Masukkan pesanan : ")
    jumlah_pesanan = int(input("Masukkan Jumlah Pesanan: "))
    
    if menu_pilihan == "nasi goreng":
        harga_satuan = 15000
    elif menu_pilihan == "mie goreng":
        harga_satuan = 12000
    elif menu_pilihan == "ayam geprek":
        harga_satuan = 18000
    else:
        print("Menu tidak tersedia.")
        exit()
elif pesan_menu == "minuman":
    print("Menu Minuman:")
    print("1. Aneka Jus - Rp. 15.000")
    print("2. Soft Drink - Rp. 10.000")
    print("3. Sweet Ice Tea - Rp. 5.000")
    menu_pilihan = input("Masukkan pesanan (Aneka Jus/Soft Drink/Sweet Ice Tea): ")
    jumlah_pesanan = int(input("Masukkan Jumlah Pesanan: "))
    
    if menu_pilihan == "aneka jus":
        harga_satuan = 15000
    elif menu_pilihan == "soft drink":
        harga_satuan = 10000
    elif menu_pilihan == "sweet ice tea":
        harga_satuan = 5000
    else:
        print("Menu tidak tersedia.")
        exit()
else:
    print("Pilihan menu tidak valid.")
    exit()
total_harga = harga_satuan * jumlah_pesanan
print("\n--- Struk Pembayaran ---")
print("Nama Pembeli: {}".format(nama_pembeli))
print("No Hp Pembeli: {}".format(no_hp))
print("Menu yang di Pesan: {}".format(menu_pilihan.title()))
print("Jumlah Pesanan: {}".format(jumlah_pesanan))
print("Harga yang harus di bayarkan: Rp. {}".format(total_harga))