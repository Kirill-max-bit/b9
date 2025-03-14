text = "1 2 3 4 5"
digits = [int(char) for char in text if char.isdigit()]
sum_digits = sum(digits)
print("Сумма цифр:", sum_digits)
