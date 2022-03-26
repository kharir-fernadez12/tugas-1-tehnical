panjang = int(input("Masukan jumlah angka: "))
list = []

for i in range(panjang):
    isilist = int(input("Masukan angka: "))
    list.append(isilist)

print(f"Hasil penjumlahan: {sum(list)}")
