word = "пример"
word = list(word)
for i in range(0, len(word) - 1, 2):
    word[i], word[i+1] = word[i+1], word[i]
word = "".join(word)
print(word)
