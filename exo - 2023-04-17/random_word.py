from random import choice

def random_letter():
    letters = ["a", "b", "c", "d", "e"]
    return choice(letters)

txt = ""
for i in range(5):
    l = random_letter()
    txt = txt + l

print(txt)
