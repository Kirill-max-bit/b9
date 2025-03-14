sentence = "Дано предложение с словами, которые начинаются и оканчиваются на одну букву, например, слово око."

# а) Слова, начинающиеся и оканчивающиеся на одну и ту же букву
words_a = [word for word in sentence.split() if word[0].lower() == word[-1].lower()]
print("а)", words_a)

# б) Слова, которые содержат ровно три буквы "е"
words_b = [word for word in sentence.split() if word.lower().count('е') == 3]
print("б)", words_b)

# в) Слова, которые содержат хотя бы одну букву "о"
words_c = [word for word in sentence.split() if 'о' in word.lower()]
print("в)", words_c)
