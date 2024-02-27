# function
def remove_vowel(word):
    new_word = ""

    for char in word:
        if char not in ["a", "e", "i", "o", "u", "y"]:
            new_word = new_word + char
    return new_word



# main program
print(remove_vowel("retard"))
