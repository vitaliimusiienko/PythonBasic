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

# Task4
# Напишіть функцію, яка видаляє зі списку ціле задане число.
# З функції потрібно повернути кількість видаленних елементів.

def delete_item(numbers: list[int], number: int) -> int:
    delete_item_counter = 0
    for item in numbers:
        if item == number:
            numbers.remove(item)
            delete_item_counter += 1

    return delete_item_counter

# Task5
# Напишіть функцію, яка отримує два списки як параметр і повертає список,
# що містить елементи обох списків
def consolidated_list(numbers: list[int], numbers2: list[int]) -> list[int]:
    for number in numbers2:
        numbers.append(number)

    return numbers
