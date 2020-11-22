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

def update_dictionary(d, key, value):
    if d.get(key) is None:
        k = 2 * key
    else:
        k = key
    if d.get(k) is None:
        d.update({k: [value]})
    else:
        d[k].append(value)


d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)  # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)  # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)  # {2: [-1, -2, -3]}
