fruits = ['coconut', 'banana', 'lemon', 'pear', 'avocado', 'tomato']

index = input("Donne index entre 0 et " + str(len(fruits) - 1)+ ": ")
index = int(index)

while index < 0 or index >= len(fruits):
    index = input("Donne index entre 0 et " + str(len(fruits) - 1)+ ": ")
    index = int(index)

print(fruits)
print(fruits[:index])
print(fruits[index:])

