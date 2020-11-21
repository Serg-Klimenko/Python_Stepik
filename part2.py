# 1.
# res = num = int(input())
#
# while num != 0:
#     num = int(input())
#     res += num
# print(res)

# 2. Программа должна считывать размеры команд (два положительных целых числа a и b,
# каждое число вводится на отдельной строке) и выводить наименьшее число d,
# которое делится на оба этих числа без остатка.

# a = int(input())
# b = int(input())
# if a < b:
#     a, b = b, a
# d = a
# while d % b != 0:
#     d += a
# print(d)

# 3. Напишите программу, которая считывает целые числа с консоли по одному числу в строке.
# Для каждого введённого числа проверить:
# если число меньше 10, то пропускаем это число;
# если число больше 100, то прекращаем считывать числа;
# в остальных случаях вывести это число обратно на консоль в отдельной строке.
# while True:
#     a = int(input())
#     if a < 10:
#         continue
#     if a > 100:
#         break
#     print(a)

# 3. Напишите программу, на вход которой даются четыре числа a, b, c и d, каждое в своей строке.
# Программа должна вывести фрагмент таблицы умножения для всех чисел отрезка [a;b] на все числа отрезка [c;d].
# # Числа a, b, c и d являются натуральными и не превосходят 10, a≤b a \le b a≤b, c≤d c \le d c≤d.
# # Следуйте формату вывода из примера, для разделения элементов внутри строки используйте '\t' — символ табуляции.
# Заметьте, что левым столбцом и верхней строкой выводятся сами числа из заданных отрезков —
# заголовочные столбец и строка таблицы.
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# print(" ", end="\t")
# for i in range(c, d + 1):
#     print(i, end="\t")
# print()
# for i in range(a, b + 1):
#     print(i, end="\t")
#     for j in range(c, d + 1):
#         print(i * j, end="\t")
#     print()

# 4. Напишите программу, которая считывает с клавиатуры два числа a и b, считает и выводит на консоль
# среднее арифметическое всех чисел из отрезка [a;b], которые кратны числу 3.
# # В приведенном ниже примере среднее арифметическое считается для чисел на отрезке [−5;12]
# Всего чисел, делящихся на 3, на этом отрезке 6: −3,0,3,6,9,12. Их среднее арифметическое равно 4.5
# На вход программе подаются интервалы, внутри которых всегда есть хотя бы одно число, которое делится на 3.

# a = int(input())
# b = int(input())
# s = 0
# count = 0
# for i in range(a, b + 1):
#     if i % 3 == 0:
#         s += i
#         count += 1
# print(s / count)

# 5. Напишите программу, которая вычисляет процентное содержание символов G (гуанин) и C (цитозин)
# в введенной строке (программа не должна зависеть от регистра вводимых символов).
# Например, в строке "acggtgttat" процентное содержание символов G и C равно 4/10*100=40.0,
# где 4 -- это количество символов G и C,  а 10 -- это длина строки.

# s = input()
# s = s.upper()
# count = s.count('C') + s.count('G')
#
# print(count / len(s)*100)

# 6. Кодирование осуществляется следующим образом:
# s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых символов исходной строки заменяются
# на этот символ и количество его повторений в этой позиции строки.
# # Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом и выводит закодированную
# последовательность на стандартный вывод. Кодирование должно учитывать регистр символов.

# s = input()
# result = ''
# i = 0
# while i < len(s):
#     result += s[i]
#     count = 1
#     while i + count < len(s) and s[i + count] == s[i]:
#         count += 1
#     result += str(count)
#     i += count
# print(result)

# 7. Напишите программу, на вход которой подается одна строка с целыми числами. Программа должна вывести
# сумму этих чисел. Используйте метод split строки.
# a = [int(i) for i in input().split()]
# s = 0
# for i in a:
#     s += i
# print(s)

# 8. Напишите программу, на вход которой подаётся список чисел одной строкой. Программа должна
# для каждого элемента этого списка вывести сумму двух его соседей. Для элементов списка,
# являющихся крайними, одним из соседей считается элемент, находящий на противоположном конце этого списка.
# Например, если на вход подаётся список "1 3 5 6 10", то на выход ожидается список "13 6 9 15 7" (без кавычек).
# Если на вход пришло только одно число, надо вывести его же.
# Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.

# a = [int(i) for i in input().split()]
# if len(a) == 1:
#     print(a[0])
# else:
#     for i in range(len(a)):
#         print(a[i - 1] + a[(i + 1) % len(a)], end=" ")

# 9. Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран
# в одну строку значения, которые встречаются в нём более одного раза.
# Для решения задачи может пригодиться метод sort списка.
# Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.

# a = [int(i) for i in input().split()]
# a.sort()
# i = 0
# while i < len(a):
#     step = a.count(a[i])
#     if step > 1:
#         print(a[i], end=" ")
#     i += step

# sapper
# input col, row, mines from console
# col_field, row_field, quantity_mines = (int(i) for i in input().split())
# # fil matrix .
# field = [[0 for j in range(row_field)] for i in range(col_field)]
# # input x, y mine positions in the table from console
# for i in range(quantity_mines):
#     col, row = (int(i) - 1 for i in input().split())
#     field[col][row] = "*"
# # +1 to each ceil near mine
# for i in range(col_field):
#     for j in range(row_field):
#         if field[i][j] == "*":
#             for ki in range(i - 1, i + 2):
#                 for kj in range(j - 1, j + 2):
#                     if 0 <= ki < col_field and 0 <= kj < row_field and field[ki][kj] != "*":
#                         field[ki][kj] += 1
# # output matrix
# for i in range(col_field):
#     for j in range(row_field):
#         if field[i][j] == 0:
#             field[i][j] = "."
#         print(field[i][j], end=' ')
#     print()

# 10. Напишите программу, которая считывает с консоли числа (по одному в строке) до тех пор, пока сумма
# введённых чисел не будет равна 0 и сразу после этого выводит сумму квадратов всех считанных чисел.
# # Гарантируется, что в какой-то момент сумма введённых чисел окажется равной 0, после этого считывание
# продолжать не нужно.
# # В примере мы считываем числа 1, -3, 5, -6, -10, 13; в этот момент замечаем, что сумма этих чисел равна
# нулю и выводим сумму их квадратов, не обращая внимания на то, что остались ещё не прочитанные значения.

# a = int(input())
# result = a * a
# s = a
# while s != 0:
#     a = int(input())
#     s += a
#     result += a * a
# print(result)

# 11. Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ...
# (число повторяется столько раз, чему равно). На вход программе передаётся неотрицательное целое
# число n — столько элементов последовательности должна отобразить программа.
# На выходе ожидается последовательность чисел, записанных через пробел в одну строку.
# Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.

n = int(input())
num = 0
out = 0
while out < n:
    num += 1
    for i in range(num):
        print(num, end=" ")
        out += 1
        if out >= n:
            break
