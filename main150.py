import re

text = "Пример текста с числами 123 и 45.6, а также -7."
numbers = [float(num) for num in re.findall(r"-?\d+\.?\d*", text)]
sum_numbers = sum(numbers)
print("Сумма всех чисел:", sum_numbers)
