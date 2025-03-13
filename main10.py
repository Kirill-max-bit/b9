city1 = input("Введите название первого города: ")
city2 = input("Введите название второго города: ")
city3 = input("Введите название третьего города: ")
cities = [city1, city2, city3]
longest = max(cities, key=len)
shortest = min(cities, key=len)
print(f"Самое длинное название: {longest}")
print(f"Самое короткое название: {shortest}")
