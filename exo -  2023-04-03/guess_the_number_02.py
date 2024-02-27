from random import randint

to_guess = randint(1, 10)

user_number = input("Donne un nombre de 1 à 10: ")
user_number = int(user_number)

if user_number < to_guess:
    print("Ton chiffre est trop petit.")
elif user_number > to_guess:
    print("Ton chiffre est trop grand.")
else:
    print("Bravo tu as deviné.")
