word1 = "мама"
word2 = "папа"
word3 = "рама"
common_letters = set(word1) & set(word2) & set(word3)
print("Общие буквы трех слов:", " ".join(common_letters))
