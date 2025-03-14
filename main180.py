sentence1 = "слово1 слово2 слово3 слово1"
sentence2 = "слово2 слово4 слово5"


words1 = sentence1.split()
words2 = set(sentence2.split())
result = {word: word in words2 for word in words1}
print("9.180", result)
