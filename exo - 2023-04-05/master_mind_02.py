from random import randint
CODE_LENGTH = 4

letters = ["🔵", 'b', 'c', 'd', 'e', 'f', ]

code = []

while len(code) < CODE_LENGTH:
    index = randint(0, len(letters) - 1)
    code.append(letters[index])

print(code)