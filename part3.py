# 1. Пример функции
# def f(x):
#     if x <= -2:
#         res = 1 - (x + 2) ** 2
#     elif x > 2:
#         res = (x - 2) ** 2 + 1
#     else:
#         res = - x / 2
#     return res
#
#
# n = float(input())
# print(f(n))

# 2. Напишите функцию modify_list(l), которая принимает на вход список целых чисел,
# удаляет из него все нечётные значения, а чётные нацело делит на два.
# Функция не должна ничего возвращать, требуется только изменение переданного списка


# def modify_list(l):
#     for x in range(len(l) - 1, -1, -1):
#         if l[x] % 2 == 0:
#             l[x] = l[x] // 2
#         else:
#             l.pop(x)
#
#
# lst = [10, 5, 8, 3]
# modify_list(lst)
# print(lst)

# 3.2.1 Напишите функцию update_dictionary(d, key, value), которая принимает на вход словарь d
# и два числа: key и value.
# Если ключ key есть в словаре d, то добавьте значение value в список, который хранится по этому ключу.
# Если ключа key нет в словаре, то нужно добавить значение в список по ключу 2∗key. Если и ключа
# 2∗key нет, то нужно добавить ключ 2∗key в словарь и сопоставить ему список из переданного элемента [value].
# Требуется реализовать только эту функцию, кода вне её не должно быть.
# Функция не должна вызывать внутри себя функции input и print.

# def update_dictionary(d, key, value):
#     if d.get(key) is None:
#         k = 2 * key
#     else:
#         k = key
#     if d.get(k) is None:
#         d.update({k: [value]})
#     else:
#         d[k].append(value)
#
#
# d = {}
# print(update_dictionary(d, 1, -1))  # None
# print(d)  # {2: [-1]}
# update_dictionary(d, 2, -2)
# print(d)  # {2: [-1, -2]}
# update_dictionary(d, 1, -3)
# print(d)  # {2: [-1, -2, -3]}

# 3.2.2 Программа должна считывать одну строку со стандартного ввода и выводить для каждого
# уникального слова в этой строке число его повторений (без учёта регистра) в формате "слово количество"
# Порядок вывода слов может быть произвольным, каждое уникальное слово должно выводиться только один раз.

# s = [i.lower() for i in input().split()]
# result = {}
# for x in s:
#     result.setdefault(x)
#     if result[x] is None:
#         result[x] = 1
#     else:
#         result[x] += 1
# for x in result:
#     print(x, result[x])

# 3.4.1 Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью
# кодирования повторов, и производит обратную операцию, получая исходный текст.
# Запишите полученный текст в файл и прикрепите его, как ответ на это задание.
# В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.
# пример текста - Y1L7B13a10D10K3h17a1l3X16v3H20m9p16P9y2t5Q17J6t15U5f14E13u11c3q7
# numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
# with open("input.txt") as inf:
#     s = inf.readline().strip()
# i = len(s) - 1
# res = ""
# while i > 0:
#     if s[i - 1] not in numbers:
#         res = s[i - 1] * int(s[i]) + res
#     else:
#         res = s[i - 2] * int(s[i - 1] + s[i]) + res
#         i -= 1
#     i -= 2
# with open("output.txt", "w") as ouf:
#     ouf.write(res)

# 3.4.2 Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки)
# и выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось.
# Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).
# В качестве ответа укажите вывод программы, а не саму программу.
# Слова, написанные в разных регистрах, считаются одинаковыми.
# Пример текста - abc a bCd bC AbC BC BCD bcd ABC
# result = {}
# with open("input.txt") as inf:
#     for line in inf:
#         line = line.lower().strip().split()
#         for word in line:
#             result.setdefault(word)
#             if result[word] is None:
#                 result[word] = 1
#             else:
#                 result[word] += 1
# for x, y in result.items():
#     if y == max(result.values()):
#         print(x, y)
#         break

# 3.4.3 Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк,
# где в каждой строке записана следующая информация:
# Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку
# Поля внутри строки разделены точкой с запятой, оценки — целые числа.
# Напишите программу, которая считывает исходный файл с подобной структурой и для каждого абитуриента
# записывает его среднюю оценку по трём предметам на отдельной строке, соответствующей этому абитуриенту,
# в файл с ответом.
# Также вычислите средние баллы по математике, физике и русскому языку по всем абитуриентам и добавьте
# полученные значения, разделённые пробелом, последней строкой в файл с ответом.
# В качестве ответа на задание прикрепите полученный файл со средними оценками по каждому ученику и одной
# строкой со средними оценками по трём предметам.

# sum_m, sum_f, sum_r, count = 0, 0, 0, 0
# with open("input.txt", encoding="utf-8") as inf, open("output.txt", "w") as ouf:
#     for line in inf:
#         line = line.strip().split(";")
#         if len(line) > 1:
#             ouf.writelines(str((int(line[1]) + int(line[2]) + int(line[3])) / 3) + "\n")
#             sum_m += int(line[1])
#             sum_f += int(line[2])
#             sum_r += int(line[3])
#             count += 1
#     ouf.write(str(sum_m / count) + " " + str(sum_f / count) + " " + str(sum_r / count))

# import sys
# print(*sys.argv[1:])

# 3.6.1 Скачайте файл. В нём указан адрес другого файла, который нужно скачать с использованием модуля
# requests и посчитать число строк в нём. Используйте функцию get для получения файла (имеет смысл
# вызвать метод strip к передаваемому параметру, чтобы убрать пробельные символы по краям).
# После получения файла вы можете проверить результат, обратившись к полю text. Если результат работы
# скрипта не принимается, проверьте поле url на правильность. Для подсчёта количества строк разбейте
# текст с помощью метода splitlines.
import requests
with open("input.txt") as inf:
    file_name = inf.readline().strip()
r = requests.get(file_name)
print(len(r.text.splitlines()))

