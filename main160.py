word1 = "процессор"
word2 = "процесс"
can_form = set(word2).issubset(set(word1))
print("Можно ли составить второе слово из букв первого (вариант 1):", can_form)
