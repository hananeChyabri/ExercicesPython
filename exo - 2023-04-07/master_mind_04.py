from random import randint
CODE_LENGTH = 4

letters = ["a", 'b', 'c', 'd', 'e', 'f', ]

code = []

# while len(code) < CODE_LENGTH:
for i in range(CODE_LENGTH):
    index = randint(0, len(letters) - 1)
    code.append(letters[index])

print(code)

guess = None  # good_answers = []

while guess != code:  # len(good_answers) != CODE_LENGTH
    guess = input("Entrez un code de " + str(CODE_LENGTH) + " lettres parmis " + str(letters))

    while len(guess) != CODE_LENGTH:
        guess = input("Entrez un code de " + str(CODE_LENGTH) + " lettres parmis " + str(letters))

    guess = list(guess)


    good_answers = []
    for index in range(CODE_LENGTH):
        if code[index] == guess[index]:
            good_answers.append(index)
    
    print(str(len(good_answers)) + " lettres bien placées")

    # ICI !
