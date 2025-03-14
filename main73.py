sentence = "Мама мыла раму с Таней"
last_s = sentence.rfind('с')
last_t = sentence.rfind('Т')
if last_s > last_t:
    print("Буква 'с' встречается позже")
elif last_t > last_s:
    print("Буква 'Т' встречается позже")
else:
    print("Буквы 'с' и 'Т' либо совпадают по последнему вхождению")
print(f"Позиция 'с': {last_s}, позиция 'Т': {last_t}")
