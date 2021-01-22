# task 5.2 Old LCD calculator
# Напишите программу, которая выводит число в стиле LCD калькулятора.
# На вход программе подаётся последовательность цифр, которую нужно вывести на
# экран в специальном стиле (см. пример).
# Размер всех цифр 4 символа в ширину и 7 символов в высоту. Между цифрами в выводе
# должен быть один пустой столбец. Перед первой цифрой не должно быть пробелов.
# Выведенные цифры должны быть обведены рамочкой, в углах которой находится символ
# x ("икс"), горизонтальная линия создаётся из символа - ("дефис"), а вертикальная
# -- из символа вертикальной черты: |.
# Формат ввода:
# Строка произвольной длины (минимум один символ), содержащая последовательность
# цифр.
# Формат вывода:
# 9 строк, содержащих цифры, записанные в указанном в задании формате.
#  Sample Output:
# x-------------------------------------------------x
# | --        --   --        --   --   --   --   -- |
# ||  |    |    |    | |  | |    |       | |  | |  ||
# ||  |    |    |    | |  | |    |       | |  | |  ||
# |           --   --   --   --   --        --   -- |
# ||  |    | |       |    |    | |  |    | |  |    ||
# ||  |    | |       |    |    | |  |    | |  |    ||
# | --        --   --        --   --        --   -- |
# x-------------------------------------------------x

digits = [
    [" -- ", "|  |", "|  |", "    ", "|  |", "|  |", " -- "],  # 0
    ["    ", "   |", "   |", "    ", "   |", "   |", "    "],  # 1
    [" -- ", "   |", "   |", " -- ", "|   ", "|   ", " -- "],  # 2
    [" -- ", "   |", "   |", " -- ", "   |", "   |", " -- "],  # 3
    ["    ", "|  |", "|  |", " -- ", "   |", "   |", "    "],  # 4
    [" -- ", "|   ", "|   ", " -- ", "   |", "   |", " -- "],  # 5
    [" -- ", "|   ", "|   ", " -- ", "|  |", "|  |", " -- "],  # 6
    [" -- ", "   |", "   |", "    ", "   |", "   |", "    "],  # 7
    [" -- ", "|  |", "|  |", " -- ", "|  |", "|  |", " -- "],  # 8
    [" -- ", "|  |", "|  |", " -- ", "   |", "   |", " -- "],  # 9
]
# input numbers
numbers = list(input())
length = len(numbers)  # count of digits
# header of table - 4 chars for 1 digit + 1 char for space
print("x", "-" * (5 * length - 1), "x", sep="")
# loof for string of digit from 0 to 7
for num in range(7):
    print("|", end="")
    # loop for digit in entered string
    pos = 0
    for line in numbers:
        print(digits[int(line)][num], end="")
        if pos < length - 1:
            print(" ", end="")
        else:
            print("|")
        pos += 1
# footer of table
print("x", "-" * (5 * length - 1), "x", sep="")