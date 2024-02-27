number = input("Nombre entre 1 et 10: ")
number = int(number)

while number < 1 or number > 10:
    number = input("Nombre entre 1 et 10: ")
    number = int(number)