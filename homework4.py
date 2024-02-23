# Task1
# Користувач вводить рядок з клавіатури. Порахуйте кількість літер, цифр у рядку.
# Виведіть обидві кількості на екран. (використовувати цикл)
d = 0
try:
    while True:
        text = input("Enter your text: ")
        d = {'let': 0, 'num': 0}
        for i in text:
            if i.isalpha():
                d['let'] += 1
            elif i.isdigit():
                d['num'] += 1
        if text:
            break
except Exception as error:
    print(f"Exception occurred: {error}")
finally:
    print(f"number: {d['num']}", f"letters: {d['let']}")

