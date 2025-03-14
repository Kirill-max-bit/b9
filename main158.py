word1 = "процессор"
word2 = "информация"
unique_to_word1 = set(word1) - set(word2)
unique_to_word2 = set(word2) - set(word1)
result = list(unique_to_word1) + list(unique_to_word2)
print("Буквы, которые есть только в одном из слов:", " ".join(result))
