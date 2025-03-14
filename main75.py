sentence1 = "Привет, мир!"
comma_index = sentence1.index(',')
result1 = sentence1[:comma_index]
print(f"Символы до первой запятой (случай 1): '{result1}'")


sentence2 = "Привет мир"
comma_index = sentence2.find(',')
result2 = sentence2[:comma_index] if comma_index != -1 else sentence2
print(f"Символы до первой запятой (случай 2): '{result2}'")
