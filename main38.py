word = "программист"
third = len(word) // 3
new_word = word[third:2*third] + word[2*third:] + word[:third]
print("Результат:", new_word)


word = "программист"
third = len(word) // 3
new_word = word[2*third:] + word[:third] + word[third:2*third]
print("Результат:", new_word)
