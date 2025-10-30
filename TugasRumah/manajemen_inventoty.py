inventory = ["pedang", "perisai", "roti"]
command = input("perintah: ").split()

match command:
    case ["ambil", item]:
        inventory.append(item)
        print("kamu mengambil", item)
    case ["buang", item]:
        if item in inventory:
            inventory.remove(item)
            print("kamu membuang", item)
        else:
            print(f"Item '{item}' tidak ada di inventory.")
    case ["lihat"]:
        print("inventory kamu:", inventory)
    case _:
        print("Perintah tidak valid. Gunakan format: 'ambil <item>' atau 'buang <item>'.")
print("Inventory akhir:", inventory)
