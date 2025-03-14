text = "чяс щяс"
words = text.split()
corrected = [word.replace('чя', 'ча').replace('щя', 'ща') for word in words]
print(f"Исправленный текст: {' '.join(corrected)}")
