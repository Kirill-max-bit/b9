word1, word2 = "процессор", "информация"


common_letters = set(word1).intersection(word2)


result = []
for letter in common_letters:
    if word1.count(letter) == 1 and word2.count(letter) == 1:
        result.append(letter)


print("Буквы, встречающиеся в обоих словах один раз:", " ".join(result))
