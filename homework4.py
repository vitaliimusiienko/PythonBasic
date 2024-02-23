# Task1
# Користувач вводить рядок з клавіатури. Порахуйте кількість літер, цифр у рядку.
# Виведіть обидві кількості на екран. (використовувати цикл)
# d = 0
# try:
#     while True:
#         text = input("Enter your text: ")
#         d = {'let': 0, 'num': 0}
#         for i in text:
#             if i.isalpha():
#                 d['let'] += 1
#             elif i.isdigit():
#                 d['num'] += 1
#         if text:
#             break
#         print("Please enter the text")
# except Exception as error:
#     print(f"Exception occurred: {error}")
# finally:
#     print(f"number: {d['num']}", f"letters: {d['let']}")

# Task2
# 2. Користувач вводить з клавіатури рядок та символ для пошуку.
# Порахуйте скільки разів у рядку зустрічається потрібний символ.
# Отримане число виведіть на екран.
# text = 0
# symbol = 0
# try:
#     while True:
#         text = input("Enter your text: ")
#         symbol = input("Enter the symbol for search: ")
#         if text and symbol:
#             break
#         print("Please enter the text and symbol")
# except Exception as error:
#     print(f"Exception occurred: {error}")
# finally:
#     print(text.count(symbol))

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
    print(n_text)
except Exception as error:
    print(f"Exception occurred: {error}")
finally:
    print(n_text)



