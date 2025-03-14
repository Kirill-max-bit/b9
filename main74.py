text = "аббббба"
has_five_consecutive = any(text[i:i+5] == text[i] * 5 for i in range(len(text)
                                                                     - 4))
print(f"Есть ли 5 одинаковых символов подряд? {has_five_consecutive}")
