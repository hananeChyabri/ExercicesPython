from random import randint
# function


def create_word(n, possibilities):
    word = ""

    for _ in range(n):
        index = randint(0, len(possibilities) - 1) 
        word += possibilities.pop(index)

    return word

# main program
print(create_word(4, ["p","y","t","h","o","n","!","?"]))
