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

# Task6
# Напишіть функцію, яка обчислює ступінь кожного елемента списку цілих.
# Значення для ступеня передається як параметр, список також передається як параметр.
# Функція повертає новий список, який містить отримані результати.

def pow_numbers(numbers: list[int], pow: int) -> list[int]:
    new_numbers = []
    for number in numbers:
        new_number = number ** pow
        new_numbers.append(new_number)
    return new_numbers


numbers = [random.randint(1, 20) for _ in range(10)]
numbers2 = [random.randint(1, 20) for _ in range(10)]


choice = input("Enter what you want: \n"
               "Calculate the product of the elements of a list of integers press 1: \n"
               "Find the minimum in a list of integers press 2: \n"
               "Determine the number of primes in a list of integers press 3: \n"
               "Remove the given integer from the list press 4: \n"
               "Get a list containing the elements of both lists press 5: \n"
               "Calculate the power of each element of a list of integers press 6: ")

print(numbers)


try:
    match choice:
        case "1":
            result = mult_number(numbers)
            print(result)
        case "2":
            result = min_nums(numbers)
            print(f"Minimal: {result}")
        case "3":
            result = prime_numbers_list(numbers)
            print(f"Prime numbers: {result}")
        case "4":
            number = int(input("Enter the number you want to delete: "))
            result = delete_item(numbers, number)
            print(f"Number of deleted objects: {result}")
        case "5":
            print(numbers2)
            result = consolidated_list(numbers, numbers2)
            print(result)
        case "6":
            pow = int(input("Enter the power of the number: "))
            result = pow_numbers(numbers, pow)
            print(result)
        case _:
            print("Incorrect choice, enter a number from 1 to 6")
except Exception as error:
    print(f"Exception occurred: {error}")