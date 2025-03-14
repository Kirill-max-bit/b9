word = "пример"
m, n = 2, 5
word = list(word)
word[m-1], word[n-1] = word[n-1], word[m-1]
word = "".join(word)
print(word)
