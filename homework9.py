with open("text1.txt", "w") as my_file:
    my_file.write("To be, or not to be, that is the question, \n"
                  "Whether 'tis nobler in the mind to suffer The slings and arrows of outrageous fortune, \n"
                  "Or to take arms against a sea of troubles, And by opposing end them? To die: to sleep; \n"
                  "No more; and by a sleep to say we end The heart-ache and the thousand natural shocks \n"
                  "That flesh is heir to, 'tis a consummation Devoutly to be wished. To die, to sleep")

# 1. Даний текстовий файл. Необхідно створити новий файл, який потрібно переписати з першого файлу всі слова,
# що складаються не менше ніж з семи літер.]\

import re

symbol_count = 7
big_words = ''

with open("text1.txt", "r") as my_file:
    text_in_my_file = my_file.read()
    text_without_marks = re.sub(r'\W', ' ', text_in_my_file)
    print(text_without_marks)
    word_in_text = text_without_marks.split()


for word in word_in_text:
    if len(word) >= symbol_count:
        big_words += word + " "
print(big_words)


with open("text2.txt", "w") as new_file:
    new_file.write(big_words)

# 2. Даний текстовий файл. Підрахувати кількість слів у ньому.

with open("text1.txt", "r") as my_file:
    text_in_my_file = my_file.read()
    words_count = len(text_in_my_file.split())


# 3. Створіть програму, яка перевіряє текст на неприпустимі слова.
# Якщо неприпустиме слово знайдено, його слід замінити на набір символів *.

unacceptable_word = "die"
acceptable_word = "***"
count_unacceptable_word = 0

with open("text1.txt", "r") as my_file:
    text_in_my_file = my_file.read()


if unacceptable_word in text_in_my_file:
    text_in_my_file = text_in_my_file.replace(unacceptable_word, acceptable_word)
    count_unacceptable_word += 1


# За підсумками роботи програми необхідно показати статистику дій.

with open("text2.txt", "r") as my_file:
    text_in_my_file = my_file.read()
    words_count_in_text2 = len(text_in_my_file.split())


print(f"Number of words with more than 7 letters: {words_count_in_text2}")
print(f"Number of words in text1.txt: {words_count}")
print(f"number of replaced unacceptable words: {count_unacceptable_word}")
