word = "анаграмма"
a_index = word.find("а")
o_index = word.rfind("о")
if a_index != -1 and o_index != -1:
    word = list(word)
    word[a_index], word[o_index] = word[o_index], word[a_index]
    word = "".join(word)
print(word)
