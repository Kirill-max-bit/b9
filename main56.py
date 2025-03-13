sentence = "В этом предложении есть буквосочетания нн."
for i in range(len(sentence) - 1):
    if sentence[i] == "н" and sentence[i + 1] == "н":
        print("нн")
