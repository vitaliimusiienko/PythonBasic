# Task1
# У списку цілих, заповненому випадковими числами обчислити:
# ■ Суму негативних чисел;
# ■ Суму парних чисел;
# ■ Суму непарних чисел;
# ■ Добуток елементів з кратними індексами 3;
# ■ Добуток елементів між мінімальним та максимальним елементом;
# ■ Суму елементів, що знаходяться між першим та останнім позитивними елементoм
from functools import reduce
from operator import mul
import random
numbers = []
num_size = 10
for i in range(num_size):
    numbers.append(random.randint(-10, 10))
print(numbers)
negative_num_sum = 0
for number in numbers:
    if number < 0:
        negative_num_sum += number
even_numbers = 0
for number in numbers:
    if number % 2 == 0:
        even_numbers += number
odd_numbers = 0
for number in numbers:
    if number % 2 != 0:
        odd_numbers += number
index3_num = numbers[3::3]
mult_index_numbers = reduce(mul, index3_num)
mult_min_max_numbers = 0
min_number_index = numbers.index(min(numbers))
max_number_index = numbers.index(max(numbers))
if min_number_index > max_number_index:
    min_number_index, max_number_index = max_number_index, min_number_index
num_size_min_max = numbers[min_number_index + 1: max_number_index]
mult_min_max_numbers = reduce(mul, num_size_min_max)
first_positive_index = 0
last_positive_index = 0
sum_positive_num = 0
for i in range(num_size):
    if numbers[i] > 0:
        first_positive_index = i
        break
for i in range(num_size - 1, -1, -1):
    if numbers[i] > 0:
        last_positive_index = i
        break
for i in range(first_positive_index + 1, last_positive_index):
    sum_positive_num += numbers[i]
print(f"The sum of negative numbers: {negative_num_sum}")
print(f"The sum of even numbers: {even_numbers}")
print(f"The sum of odd numbers: {odd_numbers}")
print(f"Multiplication of elements with multiple indices 3: {mult_index_numbers}")
print(f"Multiplication of elements between the minimum and maximum element: {mult_min_max_numbers}")
print(f"The sum of the elements between the first and the last positive element: {sum_positive_num}")
