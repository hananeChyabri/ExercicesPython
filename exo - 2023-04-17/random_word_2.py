from random import choice

def random_letter():
    letters = ["a", "h", "k", "o", "n", "s", "t"]
    return choice(letters)

def random_word(word_length):
    txt = ""
    for i in range(word_length):
        letter = random_letter()
        txt = txt + letter
    return txt

num_letters = int(input("Combien de lettres ? "))
print(random_word(num_letters))
