# Task1
# Написати рекурсивну функцію знаходження ступеня числа

def pow_number(number: int, power: int) -> int:
    if power == 1:
        return number
    if power != 1:
        return number * pow_number(number, power - 1)

number = 3
power = 4
print(pow_number(number, power))
# pow_number(3, 4) -> pow_number(3, 3)
# pow_number(3, 3) -> pow_number(3, 2)
# pow_number(3, 2) -> pow_number(3, 1)

# Task2
# Написати рекурсивну функцію, яка виводить N зірок у ряд, число N задає користувач

def show_symbols(symbol, symbol_counter: int):
    if symbol_counter <= 0:
        return

    print(symbol, end=" ")
    show_symbols(symbol,symbol_counter - 1)
symbol = "*"
symbol_counter = 4
show_symbols(symbol, symbol_counter)
print(end="\n")
# show_symbols("*", 4) -> show_symbols("*", 3)
# show_symbols("*", 3) -> show_symbols("*", 2)
# show_symbols("*", 2) -> show_symbols("*", 1)
# show_symbols("*", 1) -> show_symbols("*", 0)

# Task3
# Написати рекурсивну функцію, яка обчислює сумму всіх чисел в діапазоні від a до b.
# Користувач вводить a та b. Проілюструйте роботу функції

def sum_numbers(number2: int) -> int:
    if number2 == number1:
        return number1
    return number2 + sum_numbers(number2 - 1)


number1 = 2
number2 = 5

if number1 > number2:
    number1, number2 = number2, number1
print(sum_numbers(number2))

# sum_numbers(5) -> sum_numbers(4)
# sum_numbers(4) -> sum_numbers(3)
# sum_numbers(3) -> sum_numbers(2)
# sum_numbers(2) = number1
