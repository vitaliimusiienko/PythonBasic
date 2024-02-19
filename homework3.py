# Task1
# Користувач вводить з клавіатури номер дня тижня (1-7). Необхідно вивести на екран назву дня тижня.
# Наприклад якщо 1, на екрані напис понеділок, 2 - вівторок тощо.

try:
    action = int(input("Enter a number from 1 to 7 to display the name of the day of the week: "))
    if action == 1:
        print("Monday")
    elif action == 2:
        print("Tuesday")
    elif action == 3:
        print("Wednasday")
    elif action == 4:
        print("Thurday")
    elif action == 5:
        print("Friday")
    elif action == 6:
        print("Suturday")
    elif action == 7:
        print("Sunday")
    else:
        print("Incorrect action!")
except ValueError as error:
    print("Enter only the indicated numbers")
    print(f"VallueError: {error}")
except Exception as error:
    print(f"Exception occurred: {error}")
finally:
    print("End the first program")

# Task2
# Користувач вводить два числа. Визначити, чи рівні ці числа, і якщо ні,
# вивести іх на екран в порядку зростання
try:
    n1 = int(input("Enter the first digit number: "))
    n2 = int(input("Enter the second digit number: "))
    if n1 == n2:
        print("They are equal")
    elif n1 > n2:
        print(f"{n2}, {n1}")
    elif n2 > n1:
        print(f"{n1}, {n2}")
    else:
        print("Enter the correct values")
except ValueError as error:
    print("Enter only the numbers")
    print(f"VallueError: {error}")
except Exception as error:
    print(f"Exception occurred: {error}")
finally:
    print("End the second program")


# Task3
# Користувач вводить два числа та математичну дію: +-* або /
# залежно від введенної математичної дії вивести результат
try:
    n1 = int(input("Enter the first digit number: "))
    n2 = int(input("Enter the second digit number: "))
    action = input("Enter what mathematical operation you want to perform: ")
    if action == "+":
        result = n1 + n2
    elif action == "-":
        result = n1 - n2
    elif action == "*":
        result = n1 * n2
    elif action == "/":
        result = n1 / n2
    else:
        print(f"{action} is not valid operation"
              f"please enter the commands +-* or /")
    print(f"{result}")
except ValueError as error:
    print("Enter only the numbers")
    print(f"VallueError: {error}")
except ZeroDivisionError as error:
    print(f"ZeroDivisionError occurred: {error}")
except Exception as error:
    print(f"Exception occurred: {error}")
finally:
    print("End the third program")
