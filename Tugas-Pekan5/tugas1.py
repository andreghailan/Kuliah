command = input("Masukkan perintah (run/stop/pause) : " )
match command:
    case "run":
        print("Program sedang berjalan")
    case "stop":
        print("program dihentikan")
    case "pause":
        print("program dijeda")
    case _:
        print("command tidak dikenali")