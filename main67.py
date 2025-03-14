def count_words_967(sentence, trim_spaces=True):
    if trim_spaces:
        sentence = sentence.strip()
    return len(sentence.split())


sentence1 = "я   иду    домой"
sentence2 = "   я   иду    домой"
print("Случай 1:", count_words_967(sentence1, False))
print("Случай 2:", count_words_967(sentence2, True))
