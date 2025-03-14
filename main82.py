sentence = "   кот дома"
first_word = sentence.lstrip().split()[0]
count_o = first_word.count('о')
print(f"Количество 'о' в первом слове: {count_o}")
