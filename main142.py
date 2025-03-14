text = "   Пример текста с цифрами 123 и 456."
# Убираем пробелы в начале
text = text.lstrip()
max_digit = max(char for char in text if char.isdigit())
index = text.find(max_digit) + 1  # Порядковый номер (начиная с 1)
print("Порядковый номер максимальной цифры:", index)
