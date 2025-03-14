text = "Пример текста с цифрами 12345 и 678."
digits = "".join(char for char in text if char.isdigit())
number = int(digits) if digits else 0
print("Число из цифр:", number)
