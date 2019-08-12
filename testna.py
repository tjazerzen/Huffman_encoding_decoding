sentences_file = open("data.txt", "r")
sentences = sentences_file.readlines()
for number, sentence in enumerate(sentences, 1):
    print(number, sentence)


sentences_file.close()