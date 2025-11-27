import bangun_ruang as br
import bangun_datar as bd

kubus = br.kubus(4)
print(f"Luas kubus : {kubus}")

balok = br.balok(4, 5, 6)
print(f"Luas balok : {balok}")

bola = br.bola(7)
print(f"Luas bola : {bola}")

tabung = br.tabung(7, 10)
print(f"Luas tabung : {tabung}")

kerucut = br.kerucut(7, 10)
print(f"Luas kerucut : {kerucut}")


persegi = bd.persegi(4)
print(f"Luas persegi : {persegi}")

segitiga = bd.segitiga(4, 5)
print(f"Luas segitiga : {segitiga}")

lingkaran = bd.lingkaran(7)
print(f"Luas lingkaran : {lingkaran}")

ketupat = bd.ketupat(10, 12)
print(f"Luas ketupat : {ketupat}")

jajargenjang = bd.jajargenjang(4, 5)
print(f"Luas jajargenjang : {jajargenjang}")