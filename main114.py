word = "программирование"
unique_letters = []
for letter in word:
    if letter not in unique_letters:
        unique_letters.append(letter)
new_word = "".join(unique_letters)
print(new_word)
