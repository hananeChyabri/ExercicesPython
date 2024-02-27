grid = [
    ["a", "b", "c", "d"],
    ["e", "f", "g", "h"],
    ["i", "j", "k", "l"],
]

for line in range(3):
    txt = ""
    for column in range(4):
        txt = txt + grid[line][column]
    print(txt + "\n")
