from random import randint

to_guess = randint(1, 10)

user_number = None
tentatives = 0

while user_number != to_guess and tentatives < 3:
    user_number = input("Donne un nombre de 1 à 10: ")
    user_number = int(user_number)
    
    tentatives = tentatives + 1

    if user_number < to_guess:
        print("Ton chiffre est trop petit.")
    elif user_number > to_guess:
        print("Ton chiffre est trop grand.")

if user_number == to_guess:
    print("Bravo tu as deviné.")
else:
    print("Tu as perdu. La bonne réponse était " + str(to_guess) + ".")
