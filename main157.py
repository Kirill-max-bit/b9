word1 = "процессор"
word2 = "информация"
unique_letters = set(word1)
result = ["да" if letter in word2 else "нет" for letter in unique_letters]
print("Результат:", " ".join(result))
