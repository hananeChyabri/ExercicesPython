def display_tableau(tableau):
    for line in range(len(tableau)):
        #txt = str(line) + " "
        txt = f"{line} "

        for column in range(len(tableau[0])):
            txt = txt + tableau[line][column] + " "
        print(txt)
    
    col_numbers = "  "
    for i in range(len(tableau[0])):
        col_numbers = col_numbers + str(i) + " "
    print(col_numbers)

def check_winner(tableau, player):
    if player == 1:
        return True
    return False

grid = [
    [".",".",".",".","."],
    [".",".",".",".","."],
    [".",".",".",".","."],
    [".",".",".",".","."],
    [".",".",".",".","."],
]

display_tableau(grid)

winner = None
current_player = 0

while winner == None:
    # current_player va joueur
    print(current_player)
    # vérifier si on a un gagnant
    if check_winner(grid, current_player):
        winner = current_player
    else:
        current_player = (current_player + 1) % 2

