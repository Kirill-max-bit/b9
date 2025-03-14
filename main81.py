# Случай 1: слова разные
word1, word2 = "кот", "корм"
count1 = sum(1 for a, b in zip(word1, word2) if a == b)
print(f"Совпадений начальных букв (случай 1): {count1}")

# Случай 2: слова могут быть одинаковыми
word3, word4 = "кот", "кот"
count2 = len(word3) if word3 == word4 else \
      sum(1 for a, b in zip(word3, word4) if a == b)
print(f"Совпадений начальных букв (случай 2): {count2}")
