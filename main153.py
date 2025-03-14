from itertools import groupby

text = "ааббббввггггг"
max_count = max(len(list(group)) for _, group in groupby(text))
print("Максимальное количество одинаковых символов подряд:", max_count)
