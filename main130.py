word = "пример"
s, k = 2, 4
letter = word[s-1]
new_word = word[:s-1] + word[s:k] + letter + word[k:]
print(new_word)
