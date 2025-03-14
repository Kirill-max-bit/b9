def count_ro(sentence):
    return sentence.count("ро")


sentence = "просторок"
print(count_ro(sentence))


def count_pair(sentence, pair):
    return sentence.count(pair)


sentence = "просторок"
pair = "ст"
print(count_pair(sentence, pair))  


def count_substring(sentence, substring):
    return sentence.count(substring)


sentence = "просторок"
substring = "оро"
print(count_substring(sentence, substring))
