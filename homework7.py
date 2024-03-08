# Task1
# Написати рекурсивну функцію знаходження ступеня числа
def pow_number(number: int, power: int):
    if power == 1:
        return number
    if power != 1:
        return number * pow_number(number, power - 1)

print(pow_number(3, 4))