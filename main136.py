word = "пример"
s, k = 4, 2
letter = word[s-1]
new_word = word[:k-1] + letter + word[k-1:s-1] + word[s:]
print(new_word)
