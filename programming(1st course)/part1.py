# This is a sample Python script.
# 1.  Площадь треугольника по переданным длинам трёх его сторон по формуле Герона
# a = int(input())
# b = int(input())
# c = int(input())
# p = (a + b +c) / 2
# print((p*(p-a)*(p-b)*(p-c)) ** 0.5)

# 2. выводит True, если переданное значение попадает в интервал (−15,12]∪(14,17)∪[19,+∞) и False в противном случае
# a = int(input())
# if (a > -15 and a <= 12) or a == 15 or a == 16 or a >= 19:
#     print('True')
# else:
#     print("False")

# 3. Напишите простой калькулятор, который считывает с пользовательского ввода три строки:
# первое число, второе число и операцию, после чего применяет операцию к введённым числам
# ("первое число" "операция" "второе число") и выводит результат на экран.
# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.
# # Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".
# # Обратите внимание, что на вход программе приходят вещественные числа.

# a = float(input())
# b = float(input())
# operation = input()
# if operation == "+":
#     print(a + b)
# elif operation == "-":
#     print(a - b)
# elif operation == "*":
#     print(a * b)
# elif operation == "pow":
#     print(a ** b)
# elif operation == "/" or operation == "mod" or operation == "div":
#     if b == 0:
#         print("Деление на 0!")
#     else:
#         if operation == "/":
#             print(a / b)
#         elif operation == "mod":
#             print(a % b)
#         else:
#             print(a // b)

# 4. Комнаты бывают треугольные, прямоугольные и круглые. Чтобы быстро вычислять площадь, требуется
# написать программу, на вход которой подаётся тип фигуры комнаты и соответствующие параметры,
# которая бы выводила площадь получившейся комнаты.
# Для числа π используют значение 3.14.
# # Формат ввода:
# # треугольник
# a # b # c # # где a, b и c — длины сторон треугольника
#
# прямоугольник
# a # b # # где a и b — длины сторон прямоугольника
#
# круг
# r # # где r — радиус окружности

# figure = input()
# if figure == "треугольник":
#     a = float(input())
#     b = float(input())
#     c = float(input())
#     p = (a + b + c) / 2
#     print((p*(p-a)*(p-b)*(p-c)) ** 0.5)
# elif figure == "прямоугольник":
#     a = float(input())
#     b = float(input())
#     print(a * b)
# elif figure == "круг":
#     a = float(input())
#     print(3.14 * a * a)

# 5. Напишите программу, которая получает на вход три целых числа, по одному числу в строке,
# и выводит на консоль в три строки сначала максимальное, потом минимальное, после чего
# оставшееся число.
# # На ввод могут подаваться и повторяющиеся числа.

# maxNum = int(input())
# minNum = int(input())
# lastNum = int(input())
#
# if minNum > maxNum:
#     minNum, maxNum = maxNum, minNum
# if lastNum > maxNum:
#     lastNum, maxNum = maxNum, lastNum
# if lastNum < minNum:
#     lastNum, minNum = minNum, lastNum
# print("%d\n%d\n%d" % (maxNum, minNum, lastNum))

# 6. Напишите программу, считывающую с пользовательского ввода целое число n (неотрицательное),
# выводящее это число в консоль вместе с правильным образом изменённым словом "программист",
# для того, чтобы робот мог нормально общаться с людьми, например: 1 программист, 2 программиста,
# 5 программистов.

# result = input()
# digit = int(result)
# result += " программист"
# if 11 <= digit % 100 <= 14:
#     result += "ов"
# else:
#     if digit > 20:
#         digit %= 10
#     if digit != 1:
#         if 2 <= digit <= 4:
#             result += "а"
#         else:
#             result += "ов"
# print(result)

# 7. Билет считается счастливым, если сумма первых трех цифр совпадает с суммой последних трех цифр номера билета.
# Написать программу, которая проверит равенство сумм и выведет "Счастливый", если суммы совпадают,
# и "Обычный", если суммы различны.
# # На вход программе подаётся строка из шести цифр.
# # Выводить нужно только слово "Счастливый" или "Обычный", с большой буквы

str = int(input())
num1 = str // 1000
num2 = str % 1000

if num1 // 100 + num1 // 10 % 10 + num1 % 10 == num2 // 100 + num2 // 10 % 10 + num2 % 10:
    print("Счастливый")
else:
    print("Обычный")