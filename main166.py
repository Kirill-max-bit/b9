sentence = "мама мыла раму"
words = sentence.split()
words[0], words[-1] = words[-1], words[0]
new_sentence = " ".join(words)
print("Предложение с заменой слов:", new_sentence)
