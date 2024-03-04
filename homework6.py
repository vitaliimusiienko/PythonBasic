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

# Task3
# Напишіть функцію, яка визначає кількість простих чисел у списку цілих. Список передається як параметр.
# Отриманий результат повертається із функції.
def prime_number(number: int) -> bool:
    prime_number = True

    for num in range(2, number):
        if number % num == 0:
            prime_number = False

    return prime_number

def prime_numbers_list(numbers:  list[int]) -> int:
    prime_numbers_counter = 0

    for num in numbers:
        if prime_number(num):
            prime_numbers_counter += 1

    print()
    return prime_numbers_counter
