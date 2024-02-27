# function
def reverse_word(word):
    r_word = ""

    for char in word[::-1]:
        r_word = char + r_word

    return r_word

# main program

word = input("Donner un mot: ")
print(reverse_word(word))
