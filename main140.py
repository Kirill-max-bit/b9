text = "Пример текста с цифрами 123 и 456."
count = sum(1 for char in text if char.isdigit())
print("Количество цифр:", count)
