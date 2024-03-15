# Написати валідації за допомогою регулярних виразів та протестувати на рiзних кейсах:
# - домашній номер телефону (тільки цифри та довжина номера)
import re


while True:

    home_phone_number = input("Enter your home phone number: ")
    result = re.match(r'^([0-9]{6})$', home_phone_number)

    if bool(result) is False:
        print("Incorrect home phone number, please enter again")
    if bool(result) is True:
        break

print("Your home phone number correct! Enjoy")


# - Мобільний номер телефону (тільки цифри, можлива наявність плюса, довжина номера)

while True:

    phone_number = input("Enter your phone number: ")
    result = re.match(r'^[+]?[380]\d{11}$', phone_number)

    if bool(result) is False:
        print("Incorrect phone number, please enter again")
    if bool(result) is True:
        break

print("Your phone number correct! Enjoy")

# - email (наявність @, домену: gmail.com наприклад, мінімальна довжина та максимальна на ваш вибір)

while True:

    email = input("Enter your email: ")
    result = re.match(r'^[0-9a-zA-Z]+[._]?[0-9a-zA-Z]+[@][0-9a-zA-Z]{3,}[.][0-9a-zA-Z]{2,}$', email)

    if bool(result) is False:
        print("Incorrect email, please enter again")
    if bool(result) is True:
        break

print("Your email correct! Enjoy")

# - ПІБ клієнта (3 слова, мінімальна довжина 2 символи, максимальна довжина 20)

while True:

    full_name = input("Enter your full name: ")
    result = re.match(r'^[a-zA-ZА-Яа-яёЁїЇіІєЄґҐ]{2,20}\s[a-zA-ZА-Яа-яёЁїЇіІєЄґҐ]{2,20}\s[a-zA-ZА-Яа-яёЁїЇіІєЄґҐ]{2,20}$', full_name)

    if bool(result) is False:
        print("Incorrect full name, please enter again")
    if bool(result) is True:
        break

print(f"Thank you {full_name}!")