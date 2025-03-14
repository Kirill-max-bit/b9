# Случай 1: запятая есть
sentence1 = "Анна, привет"
comma_index = sentence1.index(',')
count_n1 = sentence1[:comma_index].count('н')
print(f"Количество 'н' до запятой (случай 1): {count_n1}")

# Случай 2: запятой может не быть
sentence2 = "Анна привет"
comma_index = sentence2.find(',')
count_n2 = sentence2[:comma_index].count('н') if comma_index != -1 else \
      sentence2.count('н')
print(f"Количество 'н' до запятой (случай 2): {count_n2}")
