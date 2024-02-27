# function
def reverse_word(word):
    r_word = ""

    for index in range(len(word)-1,-1,-1):
        r_word = r_word + word[index]

    return word

# main program

word = input("Donner un mot: ")
print(reverse_word(word))
