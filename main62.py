sentence = "Это предложение содержит несколько букв а."
total_letters = len(sentence)
count_a = sentence.count("а")
percentage = (count_a / total_letters) * 100
print(f"{percentage:.2f}%")
