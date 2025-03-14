sentence = "Это предложение с буквой и_"
letter = "т"
index = sentence.rfind("и")
if index != -1:
    new_sentence = sentence[:index] + letter + sentence[index:]
print(new_sentence)
