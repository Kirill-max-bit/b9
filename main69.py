def count_sentences(text):
    sentences = [s for s in text.replace("?", ".").replace("!", ".").split(".")
                 if s.strip()]
    return len(sentences)


text = "Я иду. Ты дома? Да!"
print(count_sentences(text))
