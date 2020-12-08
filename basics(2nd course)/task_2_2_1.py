# 2.2 Работа с кодом: модули и импорт
# В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день.
# Во второй строке дано одно число days -- число дней.
# Вычислите и выведите год, месяц и день даты, которая наступит, когда с момента исходной даты
# date пройдет число дней, равное days.
# Примечание:
# Для решения этой задачи используйте стандартный модуль datetime.
# Вам будут полезны класс datetime.date для хранения даты и класс datetime.timedelta для прибавления дней к дате.
import datetime
line = [int(_) for _ in input().split()]
print(str(datetime.date(line[0], line[1], line[2]) + datetime.timedelta(days=int(input()))).replace('-', ' '))