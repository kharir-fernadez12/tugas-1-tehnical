list5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"Original List: {list5}")

print(f"Bilangan Genap: \n {list(filter(lambda x: x%2 ==  0, list5))}")
print(f"Bilangan Genap: \n {list(filter(lambda x: x%2 !=  0, list5))}")
