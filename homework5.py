# Task1
# У списку цілих, заповненому випадковими числами обчислити:
# ■ Суму негативних чисел;
# ■ Суму парних чисел;
# ■ Суму непарних чисел;
# ■ Добуток елементів з кратними індексами 3;
# ■ Добуток елементів між мінімальним та максимальним елементом;
# ■ Суму елементів, що знаходяться між першим та останнім позитивними елементoм
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
mult_index_numbers = 1
for i in index3_num:
    mult_index_numbers *= i

mult_min_max_numbers = 0
min_number_index = numbers.index(min(numbers))
max_number_index = numbers.index(max(numbers))

if min_number_index > max_number_index:
    min_number_index, max_number_index = max_number_index, min_number_index

num_size_min_max = numbers[min_number_index + 1: max_number_index]
mult_min_max_numbers = 1
for i in num_size_min_max:
    mult_min_max_numbers *= i

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

# Task2
# Є список цілих, заповнений випадковими числами.
# На підставі даних цього масиву потрібно:
# ■ Створити список цілих, що містить лише парні числа з першого списку;
# ■ Створити список цілих, що містить лише непарні числа з першого списку;
# ■ Створити список цілих, що містить лише негативні числа з першого списку;
# ■ Створити список цілих, що містить лише позитивні числа з першого списку.
numbers = []
num_size = 10
numbers_even = []
numbers_odd = []
numbers_negative = []
numbers_positive = []

for i in range(num_size):
    numbers.append(random.randint(-10, 10))
print(numbers)

i = 0

for i in range(num_size):
    if numbers[i] % 2 == 0:
        numbers_even.append(numbers[i])
    if numbers[i] % 2 != 0:
        numbers_odd.append(numbers[i])
    if numbers[i] < 0:
        numbers_negative.append(numbers[i])
    if numbers[i] > 0:
        numbers_positive.append(numbers[i])

print(f"even: {numbers_even}")
print(f"odd: {numbers_odd}")
print(f"negative: {numbers_negative}")
print(f"positive: {numbers_positive}")
