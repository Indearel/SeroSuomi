
def add_to_dictionary():
    new_word = input('Moi, mitä haluat lisätä ?')

    f = open("../SeroSuomi/dictionary.txt", "a")
    f.write(str(new_word) + '\n')
    f.close()