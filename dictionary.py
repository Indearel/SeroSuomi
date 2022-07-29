
def add_to_dictionary():
    new_word = input('Hello, what do you want to add ?')

    f = open("../SeroSuomi/dictionary.txt", "a")
    f.write(str(new_word) + '\n')
    f.close()