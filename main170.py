sentence = "Какое-нибудь слово, начинающееся на букву к, например, кот."


word_k = next((word for word in sentence.split() if word.lower().startswith('к')), None)
print("9.170", word_k)
