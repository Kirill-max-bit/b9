word = "прроцесор"
correct_word = word.replace("рр", "р").replace("сор", "ссор")
print(correct_word)


phrase = "теекстовыйфайл"
correct_phrase = phrase.replace("ее", "е").replace("ый", "ый ")
print(correct_phrase)


phrase = "програма и аллгоритм"
correct_phrase = phrase.replace("грама", "грамма").replace("лл", "л")
print(correct_phrase)


phrase = "процесор и паммять"
correct_phrase = phrase.replace("сор", "ссор").replace("мм", "м")
print(correct_phrase)
