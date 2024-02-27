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
    for index_both in range(CODE_LENGTH):
        if code[index_both] == guess[index_both]:
            good_answers.append(index_both)
    
    print(str(len(good_answers)) + " lettres bien placées")

    # ICI !
    wrong_places = []
    for index_guess in range(len(guess)):
        for index_code in range(len(code)):
            if guess[index_guess] == code[index_code]:
                if index_code not in good_answers and index_guess not in good_answers and index_code not in wrong_places:
                    wrong_places.append(index_code)
                    break
    
    print(str(len(wrong_places)) + " lettres mal placées")

    