sentence = "Верно ли, что самое длинное слово имеет больше 10 символов?"


longest_word = max(sentence.split(), key=len)
is_longer_than_10 = len(longest_word) > 10
print("9.173", is_longer_than_10)
