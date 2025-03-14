from collections import Counter

sentence1 = "слово1 слово2 слово3 слово1"
sentence2 = "слово2 слово4 слово5"

words1 = sentence1.split()
words2 = sentence2.split()

counter1 = Counter(words1)
counter2 = Counter(words2)


result = [word for word in set(words1 + words2)
          if (counter1.get(word, 0) + counter2.get(word, 0)) == 1]
print("9.183", result)
