word1, word2, word3 = "мама", "папа", "рама"
all_letters = word1 + word2 + word3
unique_letters = [letter for letter in set(all_letters)
                  if all_letters.count(letter) == 1]
print("Неповторяющиеся буквы:", " ".join(unique_letters))
