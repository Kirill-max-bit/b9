from collections import Counter

sentence = "В предложении только два слова одинаковые, например, слово слово."

word_counts = Counter(sentence.split())
duplicate_words = [word for word, count in word_counts.items() if count == 2]
print("9.177", duplicate_words)
