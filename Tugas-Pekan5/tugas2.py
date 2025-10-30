namahari = (input("Masukkan nama hari: "))

match namahari:
    case ("sabtu" | "minggu") :
        print("ini hari libur, hore!")
    case ("senin" | "selasa" | "rabu" | "kamis") :
        print("Hari kerja, Semangat!")
    case "jumat" :
        print("besok libur!")
    case _:
        print("Nama hari tidak valid")