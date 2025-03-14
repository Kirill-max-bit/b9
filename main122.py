word = "информация_"
letter = "т"  # Заданная буква
index = word.find("и")  # Находим первую "и"
if index != -1:
    new_word = word[:index+1] + letter + word[index+1:]
print(new_word)
