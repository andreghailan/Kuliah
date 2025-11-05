nama_teman = []

for i in range(5):
    nama = input(f"Masukkan nama teman ke-{i+1}: ")
    nama_teman.append(nama)
print("Daftar nama teman:")
for nama in nama_teman:
    print(nama)
