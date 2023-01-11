var1 = "Hallo Python"
var2 = "Programming with Python"
print(var1)
print(var2)
print(var1[11])
print(var2[12:16])

print(var1[0:5], "World")
print(var1 + " " + var2)

print((var1 + " ") * 3)
print(len(var1))

positional_order = ("{2}, {1}, dan {0}".format("Budi", "Galih", "Ratna"))
print(positional_order)

print("|{:<20}|{:^20}|{:>20}|".format("NIM", "Nama", "Prodi"))
print("|{:<20}|{:^20}|{:>20}|".format("12221326", "Agis Sukmayadi", "Sistem Informasi"))


bsi = "Universitas Bina Sarana Informatika"
print(" - ".join(bsi.split()))
print(bsi.lower())
print(bsi.upper())
print(bsi.split())
print(bsi.startswith("U"))
print(bsi.endswith("U"))
print(bsi.replace("Bina Sarana Informatika", "BSI"))