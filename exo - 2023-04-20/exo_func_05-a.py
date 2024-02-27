# function
def count_character(word, character):
    count = 0
    for char in word:
        if char == character:
            count = count + 1
    return count



# main program
print(count_character("retard", "r"))
