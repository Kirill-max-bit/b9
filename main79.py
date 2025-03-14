text = "Привет, мир! Как дела?"
first_sentence = text.split('.')[0]
# Случай 1: известно, что 'и' есть
count_i1 = first_sentence.count('и')
print(f"Количество 'и' в первом предложении (случай 1): {count_i1}")
# Случай 2: 'и' может не быть
count_i2 = first_sentence.count('и') if 'и' in first_sentence else 0
print(f"Количество 'и' в первом предложении (случай 2): {count_i2}")
