warna = int(input("Masukan jumlah warna: "))
list_warna = []

for i in range(warna):
    isiwarna = input("Masukan warna: ")
    list_warna.append(list(isiwarna))
    
print(list_warna)