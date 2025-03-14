text = "Пример текста с цифрами 123 и 456."
sum_digits = sum(int(char) for char in text if char.isdigit())
print("Сумма цифр:", sum_digits)


text = "Пример текста с цифрами 123 и 456."
max_digit = max(int(char) for char in text if char.isdigit())
print("Максимальная цифра:", max_digit)
