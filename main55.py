sentence = "Пример предложения с символами п и с."
char1, char2 = "п", "с"
for char in sentence:
    if char in (char1, char2):
        print(char)
