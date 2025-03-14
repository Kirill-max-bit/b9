sentence = "Мама мыла раму"
m_count = sentence.lower().count('м')
n_count = sentence.lower().count('н')
if m_count > n_count:
    print("Букв 'м' больше")
elif n_count > m_count:
    print("Букв 'н' больше")
else:
    print("Букв 'м' и 'н' поровну")
print(f"м: {m_count}, н: {n_count}")
