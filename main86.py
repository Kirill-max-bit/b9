text = "жираф шишка"
words = text.split()
is_correct = all('жы' not in word and 'шы' not in word for word in words)
print(f"Правильно ли записаны 'жи' и 'ши'? {is_correct}")
