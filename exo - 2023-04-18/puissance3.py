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


def check_vertical(tableau, line, column):
    if line <= 2:
        if tableau[line][column] == tableau[line+1][column] and tableau[line][column] == tableau[line+2][column]:
            return True

    return False

def check_horizontal(tableau, line, column):
    if column <= 2:
        if tableau[line][column] == tableau[line][column+1] and tableau[line][column] == tableau[line][column+2]:
            return True
    
    if column >= 2:
        if tableau[line][column] == tableau[line][column-1] and tableau[line][column] == tableau[line][column-2]:
            return True
    
    if column > 0 and column < 4:
        if tableau[line][column] == tableau[line][column-1] and tableau[line][column] == tableau[line][column+1]:
            return True
    
    return False

def check_winner(tableau, column):
    
    # 1 - Determiner la position du dernier token joué
    line = 0
    for i in range(len(tableau)):
        if tableau[i][column] != ".":
            line = i
            break

    # 2 - Check vertical
    vertical = check_vertical(tableau, line, column)

    # 3 - Check horizontal
    horizontal = check_horizontal(tableau, line, column)
    # 4 - Check diagonal

    # 5 - Return True si un des checks a réussi, sinon False
    return False

def place_token_for(tableau, player, column):
    
    for line in range(4, -1, -1):
        if tableau[line][column] == ".":
            if player == 1:
                tableau[line][column] = "O"
            else:
                tableau[line][column] = "X"
            break


def place_token_while(tableau, player, column):
    line = len(tableau) - 1
    while line > -1 and tableau[line][column] != ".":
        line -= 1  # Idem que : line = line - 1

    if line >= 0:
        if player == 1:
            tableau[line][column] = "O"
        else:
            tableau[line][column] = "X"



grid = [
    [".",".",".",".","."],
    [".",".",".",".","."],
    [".",".",".",".","."],
    [".",".",".",".","."],
    [".",".",".",".","."],
]

display_tableau(grid)

winner = None
current_player = 1

while winner == None:
    # current_player va joueur
    print(current_player)

    display_tableau(grid)
    col = int(input("Colonne (0-4) : "))
    place_token_for(grid, current_player, col)


    # vérifier si on a un gagnant
    if check_winner(grid, col):
        winner = current_player
    else:
        # Changement de player
        current_player = (current_player % 2) + 1
        # Equivalent à:
        # if current_player == 1:
        #     current_player = 2
        # else:
        #     current_player = 1


display_tableau(grid)

print(f"Bravo joueur {winner} ! Vous avez gagné !")


