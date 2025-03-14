sentence = "Напечатать все слова, которые встречаются в нем по одному разу."


from collections import Counter
word_counts = Counter(sentence.split())
unique_words = [word for word, count in word_counts.items() if count == 1]
print("9.175", unique_words)
