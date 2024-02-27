from random import choice
# function


def create_word():
    possibilities= ["a", "i", "l", "n", "o","r", "s", "t"]
    word = ""

    for _ in range(5):
        char = choice(possibilities)
        word += char
        possibilities.remove(char)
    return word

# main program
print(create_word())
