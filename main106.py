word = "пятнадцатьбукв"
k, s = 3, 10  # Пример значений
part = word[k:s-1]
new_word = word[:k] + part[::-1] + word[s-1:]
print(new_word)
