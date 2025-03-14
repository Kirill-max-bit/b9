word1, word2, word3 = "мама", "папа", "рама"
unique_letters = set(word1) ^ set(word2) ^ set(word3)
result = " ".join(unique_letters)
print("Буквы, которые есть только в одном из слов (вариант 2):", result)
