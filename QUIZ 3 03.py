list3 = [6, 5, 3, 9]
list4 = [0, 1, 7, 7]

zipped = zip(list3, list4)

jumlah = [x + y for (x, y) in zipped]
print(jumlah)
