lista = ["sokin", "sini", 3, 4, 3.14]
listb = []
#akses list
print (lista[3] )
print (lista[1:3])
print (lista[4] )
#ubah elemen list
lista[3] = "ngab"
print(lista)
lista[3:5] = [5, "kite"]
print(lista)
#tambah elemen list
listb=(lista[2:4] + ["ngupiii"] + [11,22,33])
print(listb)
gabungan=(lista + listb)
print(gabungan)