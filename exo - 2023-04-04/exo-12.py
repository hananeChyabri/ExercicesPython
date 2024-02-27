number = input("Nombre: ")
number = int(number)

sum_numbers = number
previous_number = None

while previous_number != number:
    previous_number = number

    number = input("Nombre: ")
    number = int(number)
    
    sum_numbers = sum_numbers + number

print("La sommme des nombres est " + str(sum_numbers))