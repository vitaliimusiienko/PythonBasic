# Task1
# Користувач вводить з клавіатури номер дня тижня (1-7). Необхідно вивести на екран назву дня тижня.
# Наприклад якщо 1, на екрані напис понеділок, 2 - вівторок тощо.
# Task1
# Користувач вводить з клавіатури номер дня тижня (1-7). Необхідно вивести на екран назву дня тижня.
# Наприклад якщо 1, на екрані напис понеділок, 2 - вівторок тощо.
action = int(input("Enter a number from 1 to 7 to display the name of the day of the week: "))
if action == 1:
    print("Monday")
if action == 2:
    print("Tuesday")
if action == 3:
    print("Wednasday")
if action == 4:
    print ("Thurday")
if action == 5:
    print("Friday")
if action == 6:
    print("Suturday")
if action == 7:
    print("Sunday")
else:
    print("Incorrect action!")