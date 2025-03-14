sentence = "Пример  текста   с    пробелами."
max_spaces = max(len(s) for s in sentence.split(" ") if s == "")
print("Максимальное количество пробелов подряд:", max_spaces)
