# function
def remove_vowel(word):

    for char in ["a", "e", "i", "o", "u", "y"]:
        word = word.replace(char, "")
    return word


# main program
print(remove_vowel("retard"))
