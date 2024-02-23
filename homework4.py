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
        print("Please enter the text")
except Exception as error:
    print(f"Exception occurred: {error}")
finally:
    print(f"number: {d['num']}", f"letters: {d['let']}")

# Task2
# 2. Користувач вводить з клавіатури рядок та символ для пошуку.
# Порахуйте скільки разів у рядку зустрічається потрібний символ.
# Отримане число виведіть на екран.
text = 0
symbol = 0
try:
    while True:
        text = input("Enter your text: ")
        symbol = input("Enter the symbol for search: ")
        if text and symbol:
            break
        print("Please enter the text and symbol")
except Exception as error:
    print(f"Exception occurred: {error}")
finally:
    print(text.count(symbol))

# Task3
# Користувач вводить з клавіатури рядок, слово для пошуку, слово для заміни.
# Зробіть у рядку заміну одного слова на інше.
# Отриманий рядок на екрані.
n_text = 0
try:
    while True:
        text = input("Enter the text: ")
        s_word = input("Enter the word for search: ")
        if s_word in text:
            break
        print("word for search not found in text")
    r_word = input("Enter the word to replace: ")
    n_text = text.replace(s_word, r_word)
except Exception as error:
    print(f"Exception occurred: {error}")
finally:
    print(n_text)
# Task4
# Дано рядок. (зробити зрізи)
# - Спершу виведіть третій символ цього рядка.
# - У другому рядку виведіть передостанній символ цього рядка.
# - У третьому рядку виведіть перші п'ять символів цього рядка.
# - У четвертому рядку виведіть весь рядок, крім двох останніх символів.
# - У п'ятому рядку виведіть усі символи з парними індексами
# (вважаючи, що індексація починається з 0, тому символи виводяться з першого).
# - У шостому рядку виведіть усі символи з непарними індексами, тобто, починаючи з другого символу рядка.
# - У сьомому рядку виведіть усі символи у зворотному порядку.
# - У восьмому рядку виведіть усі символи рядка через один у зворотному порядку, починаючи з останнього.
# - У дев'ятому рядку виведіть довжину цього рядка.
text = "Крапка також може зустрічатися в літералах із плаваючою комою та уявних літералах."
print(text[2])
print(text[-2])
print(text[0:4])
print(text[:-2])
print(text[::2])
print(text[1::2])
print(text[::-1])
print(text[::-2])
print(len(text))