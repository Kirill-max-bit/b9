word = "абвгдеёжзий"
new_word = "".join([word[i] + word[-(i+1)] for i in range(6)])
print(new_word)
