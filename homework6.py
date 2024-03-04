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

# Task2
# Напишіть функцію для знаходження мінімуму у списку цілих. Список передається як параметр.
# Отриманий результат повертається із функції

def min_nums(numbers: list[int]) -> int:
    minimal_number = 0

    for number in numbers:
        if int(number):
            minimal_number = min(numbers)

    return minimal_number
