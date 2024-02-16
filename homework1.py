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

# Task3
# Користувач вводить з клавіатури число, що складається з чотирьох цифр. Потрібно знайти добуток цих чисел
number = int(input("Enter the 4-digit number: "))
n1 = number //1000
n2 = number //100 % 10
n3 = number % 100 // 10
n4 = number % 10
result = n1 * n2 * n3 * n4
print(f"result: {result}")
