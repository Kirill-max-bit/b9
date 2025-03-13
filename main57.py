sentence = "Это пример предложения с буквами и."
for i in range(1, len(sentence), 2):  # Начинаем с индекса 1 (второй символ)
    if sentence[i] == "и":
        print(sentence[i])
