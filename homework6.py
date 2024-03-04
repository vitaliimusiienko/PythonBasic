# Task1
# Напишіть функцію, яка обчислює добуток елементів списку цілих. Список передається як параметр.
# Отриманий результат повертається із функції.
import random

def mult_number(numbers: list[int]) -> int:
    multiplication_numbers = 1

    for number in numbers:
        if int(number):
            multiplication_numbers *= number

    return multiplication_numbers

