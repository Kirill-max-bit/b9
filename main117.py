def is_palindrome(s):
    s = s.replace(" ", "")
    return s == s[::-1]


sentence = "А РОЗА УПАЛА НА ЛАПУ АЗОРА"
print(is_palindrome(sentence))
