text = "1 2 -3 4 -5"
digits = [int(char) for char in text.split() if char.lstrip('-').isdigit()]
algebraic_sum = sum(digits)
print("Алгебраическая сумма:", algebraic_sum)
