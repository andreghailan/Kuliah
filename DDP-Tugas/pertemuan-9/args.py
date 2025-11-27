def bilangan_ganjil(ganjil):
  for angka in range(1, ganjil + 1):
    if angka % 2 != 0:
      print(angka, end=" ")
  print()

bilangan_ganjil(20)
