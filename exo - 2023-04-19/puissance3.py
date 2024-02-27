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


def check_diagonale(tableau, line, column):
    if column < 3 and line < 3:
        if (tableau[line + 1][column + 1] == tableau[line][column]
        and tableau[line + 2][column + 2] == tableau[line][column]):
            return True
    if column > 1 and line > 1:
        if (tableau[line - 1][column - 1] == tableau[line][column]
        and tableau[line - 2][column - 2] == tableau[line][column]):
            return True
        
    if (column > 0 and column < 4 
    and line > 0 and line < 4):
        if (tableau[line + 1][column + 1] == tableau[line][column]
        and tableau[line - 1][column - 1] == tableau[line][column]):
            return True
        
    if column < 3 and line > 1:
        if (tableau[line - 1][column + 1] == tableau[line][column]
        and tableau[line - 2][column + 2] == tableau[line][column]):
            return True
    if column > 1 and line < 3:
        if (tableau[line + 1][column - 1] == tableau[line][column]
        and tableau[line + 2][column - 2] == tableau[line][column]):
            return True
        
    if (column > 0 and column < 4 
    and line > 0 and line < 4):
        if (tableau[line + 1][column - 1] == tableau[line][column]
        and tableau[line - 1][column + 1] == tableau[line][column]):
            return True
    

def check_full(tableau):
    return '.' not in tableau[0]

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
    diagonal = check_diagonale(tableau, line, column)

    # 5 - Return True si un des checks a réussi, sinon False

    return (vertical or horizontal or diagonal)

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
    ["X","X","X","X","."],
    [".",".",".",".","X"],
    [".",".",".",".","X"],
    [".",".",".",".","X"],
    [".",".",".",".","X"],
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
        if check_full(grid):
            grid = [[".",".",".",".","."],
                    [".",".",".",".","."],
                    [".",".",".",".","."],
                    [".",".",".",".","."],
                    [".",".",".",".","."]]
        # Changement de player
        current_player = (current_player % 2) + 1


display_tableau(grid)

print(f"Bravo joueur {winner} ! Vous avez gagné !")


