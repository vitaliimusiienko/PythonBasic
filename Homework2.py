"""Task1
Користувач вводить три цифри з клавіатури. Залежно від вибору користувача програма виводить
на екран максимум з трьох, мінімум іх трьох або середноарифметичне трьох чисел"""

n1 = int(input("Enter first digit number"))
n2 = int(input("Enter second digit number"))
n3 = int(input("Enter third digit number"))

c1 = int(input("Choice what you want "
               "Enter 1 Maximum of three numbers. "
               "Enter 2 Minimum of three numbers. "
               "Enter 3 Arithmetic mean of thee numbers: "))

if 0 < c1 < 2:
    print(f"Maximum: {max(n1, n2, n3)}")
elif 1 < c1 < 3:
    print(f"Minimum: {min(n1, n2, n3)}")
elif 2 < c1 < 4:
    print(f"Arifmetic mean: {(n1 + n2 + n3) / 3}")
else:
    print("Incorrect choice")
# """Task2
# Користувач вводить з клавіатури кількість метрів.
# Залежно від вибору користувача програма переводть метри в милі, дюйми чи ярди"""
m1 = int(input("Enter the lenght in meters: "))
c1 = int(input("Choice what you want to transfer metters to: "
               "Enter 1 in miles. "
               "Enter 2 in inches. "
               "Enter 3 in yards: "))
m2 = m1 / 1609
m3 = m1 * 39.37
m4 = m1 * 1.094
if 0 < c1 < 2:
    print(f"Miles: {m2}")
elif 1 < c1 < 3:
    print(f"Inches: {m3}")
elif 2 < c1 < 4:
    print(f"Yards: {m4}")
else:
    print("Incorrect choice")