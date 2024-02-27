# function
def sum_grid(table):
    sum_number = 0

    for line in range(len(table)):
        for column in range(len(table[line])):
            sum_number = sum_number + table[line][column]
    print(sum_number)
# main program

grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sum_grid(grid)
