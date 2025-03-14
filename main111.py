word = "пример"
length = len(word)
if length % 2 == 1:
    middle = length // 2
    new_word = word[:middle] + word[middle+1:]
else:
    middle = length // 2
    new_word = word[:middle-1] + word[middle+1:]
print(new_word)
