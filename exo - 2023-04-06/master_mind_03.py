from random import randint
CODE_LENGTH = 4

letters = ["a", 'b', 'c', 'd', 'e', 'f', ]

code = []

# while len(code) < CODE_LENGTH:
for i in range(CODE_LENGTH):
    index = randint(0, len(letters) - 1)
    code.append(letters[index])

print(code)

guess = input("Entrez un code de " + str(CODE_LENGTH) + " lettres parmis " + str(letters))

while len(guess) != CODE_LENGTH:
    guess = input("Entrez un code de " + str(CODE_LENGTH) + " lettres parmis " + str(letters))

guess = list(guess)
