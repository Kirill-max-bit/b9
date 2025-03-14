sentence = "Дано предложение с словами, которые начинаются и оканчиваются на."

print("а)", [word for word in sentence.split()
             if word[0].lower() == word[-1].lower()])

print("б)", [word for word in sentence.split()
             if word.lower().count('е') == 3])

print("в)", [word for word in sentence.split()
             if 'о' in word.lower()])
