# mylist.append('orange')
# mylist = ['apple', 'banana', 'cherry']
# mylist.insert(1, 'kiwi')
# mylist.remove('banana')
# mylist.sort()
# poplist = mylist.pop(3)
# print(mylist)
# print(poplist)

# list1 = ['a', 'b', 'c']
# list2 = [1, 2, 3]
# gabungan = list1 *3
# print(gabungan)

lang = input("Masukkan bahasa pemrograman yang kamu suka: ")
match lang:
    case "python":  
        print("Kamu akan jago python")
    case "javascript":
        print("Kamu akan jago javascript")
    case _:
        print("Belajar Lagi DEKKK")