sentence = "Мама мыла раму"
vowels = "аеёиоуыэюя"
count = sum(1 for char in sentence.lower() if char in vowels)
print(f"Количество гласных букв: {count}")
