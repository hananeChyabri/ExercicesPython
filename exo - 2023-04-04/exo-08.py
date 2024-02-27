password = input("Mot de passe: ")
tentative = 1

while password != "Pyth0n" and tentative < 3:
    password = input("Mot de passe: ")
    tentative = tentative + 1

if password == "Pyth0n":
    print("Mot de passe valide.")
else:
    print("Mot de passe incorrect.")


