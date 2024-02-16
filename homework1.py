# Task1
# Користувач вводить три цифри з клавіатури. Необхідно знайти сумму чисел та добуток. Результат вивести на екран

n1 = int(input("Enter the first digit number: "))
n2 = int(input("Enter the second digit number: "))
n3 = int(input("Enter the third digit number: "))
number_sum = n1 + n2 + n3
number_mult = n1 * n2 * n3
print(f"sum: {number_sum}")
print(f"mult: {number_mult}")