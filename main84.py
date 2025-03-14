sentence = "Привет, мир"
for i in range(len(sentence) - 1):
    if sentence[i] == sentence[i + 1]:
        print(f"Первая пара: '{sentence[i]}{sentence[i+1]}' на позициях {i+1} \
               и {i+2}")
        break
else:
    print("Одинаковых соседних символов нет")
