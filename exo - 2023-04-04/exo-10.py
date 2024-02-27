
number = input("Nombre: ")
number = int(number)

greater = number
lower = number

while number != 0:
    number = input("Nombre: ")
    number = int(number)

    if number > greater:
        greater = number
    elif number < lower:
        lower = number

print("Plus grand: " + str(greater))
print("Plus petit: " + str(lower))

