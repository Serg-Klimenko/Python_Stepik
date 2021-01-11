# 5.11 Jolly jumpers
# Последовательность n>0 n \gt 0 n>0 целых чисел называется jolly jumper в случае,
# если значения абсолютных разностей последовательных элементов принимают все
# возможные значения между 1 1 1 и n−1 n-1 n−1.
# Например, последовательность 1 -3 -4 -1 1 является jolly jumper последовательностью,
# так как абсолютные разности равны 4 1 3 2, соответственно, а n−1=4 n-1 = 4 n−1=4.
# Будем считать, что последовательность из одного числа является jolly jumper.
# Напишите программу, которая проверяет, является ли введённая последовательность
# jolly jumper.
# Формат ввода:
# Строка, содержащая 1≤n≤10000 1 \le n \le 10000 1≤n≤10000 целых чисел, разделённых
# пробелом.
# Формат вывода:
# Одна строка, содержащая "Jolly" (без кавычек), если последовательность является
# jolly jumper и "Not jolly" в противном случае.
lst = [int(_) for _ in input().split()]
result = []  # list of difference of elements
# calculate difference of n and n+1 elements
for k in range(0, len(lst) - 1):
    result += [abs(lst[k] - lst[k + 1])]
message = "Jolly"
# sort list of difference
result.sort()
# change difference between n and n-1 elements
for pos in range(1, len(result)):
    if result[pos] - result[pos - 1] != 1:
        message = "Not jolly"
        break
print(message)
