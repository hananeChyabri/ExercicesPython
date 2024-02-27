from random import randint
# function


def create_word():
    possibilities= ["a", "i", "l", "n", "o","r", "s", "t"]
    word = ""

    for _ in range(5):
        index = randint(0, len(possibilities) - 1) 
        word += possibilities.pop(index)

    return word

# main program
print(create_word())
