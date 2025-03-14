word = "молоко"
if "о" in word:
    new_word = word.replace("о", "", 1)
print(new_word)


word = "молоко"
if "л" in word:
    new_word = word[::-1].replace("л", "", 1)[::-1]
print(new_word)
