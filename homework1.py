# Task1
# Користувач вводить три цифри з клавіатури. Необхідно знайти сумму чисел та добуток. Результат вивести на екран

n1 = int(input("Enter the first digit number: "))
n2 = int(input("Enter the second digit number: "))
n3 = int(input("Enter the third digit number: "))
number_sum = n1 + n2 + n3
number_mult = n1 * n2 * n3
print(f"sum: {number_sum}")
print(f"mult: {number_mult}")
# Task2
# Напишіть програму, яка обчислює площу ромба. Корситувач вводить довжину двох ййого діагоналей
# Площа ромба дорівнює половині видобутку його діагоналей
d1 = int(input("Enter the first diagonal: "))
d2 = int(input("Enter the second diagonal: "))
a1 = (d1 * d2) / 2
print("Area:",a1)
