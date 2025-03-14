sentence = "Чудо или щука"
pos_chu = sentence.find('чу')
pos_shchu = sentence.find('щу')
has_comb = pos_chu != -1 or pos_shchu != -1
first_pos = min(pos_chu, pos_shchu) + 1 if has_comb else -1
print(f"Есть ли 'чу' или 'щу'? {has_comb}")
if has_comb:
    print(f"Позиция первой буквы: {first_pos}")
