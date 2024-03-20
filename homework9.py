# 1. Даний текстовий файл. Необхідно створити новий файл, який потрібно переписати з першого файлу всі слова,
# що складаються не менше ніж з семи літер.
try:
    my_file = open("text1.txt", "w")
    try:
        my_file.write("To be, or not to be, that is the question, "
                      "Whether 'tis nobler in the mind to suffer The slings and arrows of outrageous fortune,\n "
                      "Or to take arms against a sea of troubles, And by opposing end them? To die: to sleep;\n"
                      "No more; and by a sleep to say we end The heart-ache and the thousand natural shocks\n"
                      "That flesh is heir to, 'tis a consummation Devoutly to be wish'd. To die, to sleep")
    except Exception as e:
        print(e)
    finally:
        my_file.close()

except Exception as e:
    print(e)

# 2. Даний текстовий файл. Підрахувати кількість слів у ньому.
#
# 3. Створіть програму, яка перевіряє текст на неприпустимі слова.
#
# Якщо неприпустиме слово знайдено, його слід замінити на набір символів *.
#
# За підсумками роботи програми необхідно показати статистику дій.
