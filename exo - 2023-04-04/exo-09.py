from random import randint

d1 = randint(1, 6)
d2 = randint(1, 6)
d3 = randint(1, 6)

print(str(d1) + " - " + str(d2) + " - " + str(d3))

while d1 != d2 or d1 != d3:
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    d3 = randint(1, 6)

    print(str(d1) + " - " + str(d2) + " - " + str(d3))



