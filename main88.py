sentence = "Привет, мир, как дела"
first_comma = sentence.index(',')
second_comma = sentence.find(',', first_comma + 1)
result = sentence[first_comma + 1:second_comma] if second_comma != -1 else \
      sentence[first_comma + 1:]
print(f"Между запятыми: '{result.strip()}'")
