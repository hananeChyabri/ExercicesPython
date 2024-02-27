tab = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

for line in range(3):
    txt = ""
    for column in range(4):
        division = tab[line][column] / 2
        txt = txt + str(division) + "   "
    print(txt)