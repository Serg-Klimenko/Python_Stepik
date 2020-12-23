# 5.23 Annoying input
# Напишите функцию get_int(start_message, error_message, end_message), принимающую три
# строки в качестве аргументов.
# Функция должна запрашивать у пользователя ввод до тех пор, пока не будет введено целое
# число (строка, принимаемая функцией int без ошибок).
# Перед первым запросом ввода должен быть выведен аргумент start_message, после
# каждого ошибочного ввода нужно выводить значение строки error_message и при удачном
# вводе нужно вывести строку end_message и вернуть полученное целое число из функции
# Каждое выводимое сообщение должно находиться на отдельной строке.
import re


def get_int(str_input, str_wrong, str_ok):
    x = input(f"{str_input}\n")
    while re.search(r"^-?\d+$", x) is None:
        x = input(f"{str_wrong}\n")
    print(str_ok)
    return int(x)


x = get_int('Input int number:', 'Wrong value. Input int number:', 'Thank you.')
