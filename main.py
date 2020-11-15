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

a = float(input())
b = float(input())
operation = input()
if operation == "+":
    print(a + b)
elif operation == "-":
    print(a - b)
elif operation == "*":
    print(a * b)
elif operation == "pow":
    print(a ** b)
elif operation == "/" or operation == "mod" or operation == "div":
    if b == 0:
        print("Деление на 0!")
    else:
        if operation == "/":
            print(a / b)
        elif operation == "mod":
            print(a % b)
        else:
            print(a // b)
