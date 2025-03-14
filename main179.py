words = ["первое", "второе", "третье", "око", "дед"]

# а) Слова без повторяющихся букв
words_a = [word for word in words if len(set(word)) == len(word)]
print("а)", words_a)

# б) Симметричные слова
words_b = [word for word in words if word == word[::-1]]
print("б)", words_b)
