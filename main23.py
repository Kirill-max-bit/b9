word = input("Введите слово: ")
m = int(input("Введите начальный индекс (m): "))
n = int(input("Введите конечный индекс (n): "))
part = word[m - 1:n]
print("Часть слова:", part)
