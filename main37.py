word = "программирование"
half = len(word) // 2
new_word = word[half:] + word[:half]
print("Результат:", new_word)
