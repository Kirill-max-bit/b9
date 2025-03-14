sequence1 = "aaaab"
count1 = 0
for char in sequence1:
    if char == sequence1[0]:
        count1 += 1
    else:
        break
print(f"Количество одинаковых символов в начале (случай 1): {count1}")

# Случай 2: все могут быть одинаковыми
sequence2 = "aaaa"
count2 = len(sequence2) if all(char == sequence2[0] for char in sequence2) \
    else next(i for i, char in enumerate(sequence2) if char != sequence2[0])

print(f"Количество одинаковых символов в начале (случай 2): {count2}")
