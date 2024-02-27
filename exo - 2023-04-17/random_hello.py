from random import randint

def random_greeting():
    greetings = ["Bonjour", "Hello", "Ola", "Ciao"]
    index = randint(0, len(greetings) - 1)
    print(greetings[index])

for i in range(100):
    random_greeting()
