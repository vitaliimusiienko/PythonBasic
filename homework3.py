# Task1
# Користувач вводить з клавіатури номер дня тижня (1-7). Необхідно вивести на екран назву дня тижня.
# Наприклад якщо 1, на екрані напис понеділок, 2 - вівторок тощо.
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
# то вивести їх на екран в прорядку зростання

try:
    n1 = int(input("Enter the first digit number: "))
    n2 = int(input("Enter the second digit number: "))
    if n1 > n2:
        print(f"{n2}, {n1}")
    elif n2 > n1:
        print(f"{n1}, {n2}")
    else:
        print("They are equal")
except ValueError as error:
    print("Enter only the numbers")
    print(f"VallueError: {error}")
except Exception as error:
    print(f"Exception occurred: {error}")
finally:
    print("End the second program")

