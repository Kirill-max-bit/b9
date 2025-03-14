sentence = "В предложении только два слова одинаковые, например, слово слово."

# Найти одинаковые слова
from collections import Counter
word_counts = Counter(sentence.split())
duplicate_words = [word for word, count in word_counts.items() if count == 2]
print("9.177", duplicate_words)
