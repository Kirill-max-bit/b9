sentence = "Преобразовать каждое слово по правилам."

# а) Заменить первую встреченную букву "а" на "о"
words_a = [word.replace('а', 'о', 1) if 'а' in word else word for word in sentence.split()]
print("а)", words_a)

# б) Удалить из слова все вхождения последней буквы (кроме нее самой)
words_b = [word.replace(word[-1], '') + word[-1] for word in sentence.split()]
print("б)", words_b)

# в) Оставить в слове только первые вхождения каждой буквы
words_c = [''.join(sorted(set(word), key=word.index)) for word in sentence.split()]
print("в)", words_c)

# г) В самом длинном слове удалить среднюю (средние) буквы
longest_word = max(sentence.split(), key=len)
middle = len(longest_word) // 2
if len(longest_word) % 2 == 0:
    new_word = longest_word[:middle-1] + longest_word[middle+1:]
else:
    new_word = longest_word[:middle] + longest_word[middle+1:]
words_d = [new_word if word == longest_word else word for word in sentence.split()]
print("г)", words_d)
