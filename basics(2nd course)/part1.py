# 1.2.1 Реализуйте программу, которая будет вычислять количество различных объектов в списке.
# Два объекта a и b считаются различными, если a is b равно False. Вашей программе доступна
# переменная с названием objects, которая ссылается на список, содержащий не более 100 объектов.
# Выведите количество различных объектов в этом списке.

# objects = [1, True, 1, 2, 3, False, 'end']
# result = set()
# ans = 0
# for obj in objects:
#     if id(obj) not in result:
#         result.add(id(obj))
#         ans += 1
# print(ans)
# ----------------------------------------------------------------------------------------------

# 1.3.1 Напишите реализацию функции closest_mod_5, принимающую в качестве единственного
# аргумента целое число x и возвращающую самое маленькое целое число y, такое что:
#     y больше или равно x
#     y делится нацело на 5
# Формат того, что ожидается от вас в качестве ответа:
# def closest_mod_5(x):
#    if x % 5 == 0:
#        return x
#    return "I don't know :("
#
# def closest_mod_5(x):
#     if x % 5 == 0:
#         return x
#     else:
#         return x + (5 - (x % 5))
#
#
# print(closest_mod_5(8))
# --------------------------------------------------------------------------------------------------
# 1.3.2 В результате каких вызовов данная функция вернет число 31?
# def s(a, *vs, b=10):
#     res = a + b
#     for v in vs:
#         res += v
#     return res
#
#
# print('s(11, 10, 10): ', s(11, 10, 10))
# print('s(11, 10): ', s(11, 10))
# print('s(5, 5, 5, 5, 1): ', s(5, 5, 5, 5, 1))
# print('s(21): ', s(21))
# print('s(11, b=20): ', s(11, b=20))
# # print('s(b=31): ', s(b=31))
# print('s(0, 0, 31): ', s(0, 0, 31))
# print('s(11, 10, b=10): ', s(11, 10, b=10))
# # print('s(b=31, 0): ', s(b=31, 0))
# --------------------------------------------------------------------------------------------

# 1.3.1 Сочетанием из n элементов по k называется подмножество этих n элементов размера k.
# Два сочетания называются различными, если одно из сочетаний содержит элемент, который не
# содержит другое. Числом сочетаний из n по k называется количество различных сочетаний из
# n по k. Обозначим это число за C(n, k).
# # Пример:
# Пусть n = 3, т. е. есть три элемента (1, 2, 3). Пусть k = 2.
# Все различные сочетания из 3 элементов по 2: (1, 2), (1, 3), (2, 3).
# Различных сочетаний три, поэтому C(3, 2) = 3.
# Несложно понять, что C(n, 0) = 1, так как из n элементов выбрать 0 можно единственным образом,
# а именно, ничего не выбрать. Также несложно понять, что если k > n, то C(n, k) = 0, так как
# невозможно, например, из трех элементов выбрать пять.
# # Для вычисления C(n, k) в других случаях используется следующая рекуррентная формула:
# C(n, k) = C(n - 1, k) + C(n - 1, k - 1).
# # Реализуйте программу, которая для заданных n и k вычисляет C(n, k).
# # Вашей программе на вход подается строка, содержащая два целых числа n и k (1 ≤ n ≤ 10, 0 ≤ k ≤ 10).
# Ваша программа должна вывести единственное число: C(n, k).
# Считать два числа n и k вы можете, например, следующим образом:  n, k = map(int, input().split())
# def count_lots(n, k):
#     if k > n:
#         return 0
#     elif k == 0:
#         return 1
#     else:
#         return count_lots(n - 1, k) + count_lots(n - 1, k - 1)
#
#
# n, k = map(int, input().split())
# print(count_lots(n, k))
# --------------------------------------------------------------------------------------------------

# 1.4.1 Реализуйте программу, которая будет эмулировать работу с пространствами имен. Необходимо
# реализовать поддержку создания пространств имен и добавление в них переменных.
# В данной задаче у каждого пространства имен есть уникальный текстовый идентификатор – его имя.
# Вашей программе на вход подаются следующие запросы:
#     create <namespace> <parent> –  создать новое пространство имен с именем <namespace> внутри
#                                       пространства <parent>
#     add <namespace> <var> – добавить в пространство <namespace> переменную <var>
#     get <namespace> <var> – получить имя пространства, из которого будет взята переменная
#                               <var> при запросе из пространства <namespace>, или None, если
#                               такого пространства не существует
# Рассмотрим набор запросов
#     add global a
#     create foo global
#     add foo b
#     create bar foo
#     add bar a
# Структура пространств имен описанная данными запросами будет эквивалентна структуре пространств
# имен, созданной при выполнении данного кода
# a = 0
# def foo():
#   b = 1
#   def bar():
#     a = 2
# В основном теле программы мы объявляем переменную a, тем самым добавляя ее в пространство
# global. Далее мы объявляем функцию foo, что влечет за собой создание локального для нее
# пространства имен внутри пространства global. В нашем случае, это описывается командой
# create foo global. Далее мы объявляем внутри функции foo функцию bar, тем самым создавая
# пространство bar внутри пространства foo, и добавляем в bar переменную a.
# Добавим запросы get к нашим запросам
#     get foo a
#     get foo c
#     get bar a
#     get bar b
# Представим как это могло бы выглядеть в коде
# a = 0
# def foo():
#   b = 1
#   get(a)
#   get(c)
#   def bar():
#     a = 2
#     get(a)
#     get(b)
# Результатом запроса get будет имя пространства, из которого будет взята нужная переменная.
# Например, результатом запроса get foo a будет global, потому что в пространстве foo не объявлена
# переменная a, но в пространстве global, внутри которого находится пространство foo, она объявлена.
# Аналогично, результатом запроса get bar b будет являться foo, а результатом работы get bar a
# будет являться bar.
# Результатом get foo c будет являться None, потому что ни в пространстве foo, ни в его внешнем
# пространстве global не была объявлена переменная с.
# Более формально, результатом работы get <namespace> <var> является
#     <namespace>, если в пространстве <namespace> была объявлена переменная <var>
#     get <parent> <var> – результат запроса к пространству, внутри которого было создано
#                           пространство <namespace>, если переменная не была объявлена
#     None, если не существует <parent>, т. е. <namespace> – это global
# Формат входных данных
# В первой строке дано число n (1 ≤ n ≤ 100) – число запросов.
# В каждой из следующих n строк дано по одному запросу.
# Запросы выполняются в порядке, в котором они даны во входных данных.
# Имена пространства имен и имена переменных представляют из себя строки длины не более 10,
# состоящие из строчных латинских букв.
# Формат выходных данных
# Для каждого запроса get выведите в отдельной строке его результат.
# namespaces = {'global': ['global']}
# for i in range(int(input())):
#     s = input().split()
#     if s[0] == 'create':
#         namespaces.setdefault(s[1], [])
#         namespaces[s[1]].append(s[2])
#     elif s[0] == 'add':
#         namespaces[s[1]].append(s[2])
#     else:
#         result = 'None'
#         if s[2] in namespaces[s[1]]:
#             result = s[1]
#         else:
#             key = s[1]
#             while key != 'global' and s[2] not in namespaces[[key][0]]:
#                 key = namespaces[key][0]
#                 if s[2] in namespaces[[key][0]]:
#                     result = key
#                     break
#         print(result)
# ------------------------------------------------------------------------------------------------
# 1.5.1
# Реализуйте класс MoneyBox, для работы с виртуальной копилкой.
# Каждая копилка имеет ограниченную вместимость, которая выражается целым числом – количеством
# монет, которые можно положить в копилку. Класс должен поддерживать информацию о количестве
# монет в копилке, предоставлять возможность добавлять монеты в копилку и узнавать, можно ли
# добавить в копилку ещё какое-то количество монет, не превышая ее вместимость.
# # Класс должен иметь следующий вид
#
# class MoneyBox:
#     def __init__(self, capacity):
#     # конструктор с аргументом – вместимость копилки
#
#     def can_add(self, v):
#         # True, если можно добавить v монет, False иначе
#
#     def add(self, v):
#         # положить v монет в копилку
#
# При создании копилки, число монет в ней равно 0.
# Примечание:
# Гарантируется, что метод add(self, v) будет вызываться только если can_add(self, v) – True
# class MoneyBox:
#     def __init__(self, capacity):
#         self.count = 0
#         self.capacity = capacity
#
#     def can_add(self, v):
#         if self.count + v > self.capacity:
#             return False
#         else:
#             return True
#
#     def add(self, v):
#         self.count += v
# ----------------------------------------------------------------------------------------------

# 1.5.2
# Вам дается последовательность целых чисел и вам нужно ее обработать и вывести на экран сумму
# первой пятерки чисел из этой последовательности, затем сумму второй пятерки, и т. д.
# Но последовательность не дается вам сразу целиком. С течением времени к вам поступают её
# последовательные части. Например, сначала первые три элемента, потом следующие шесть, потом
# следующие два и т. д.
# Реализуйте класс Buffer, который будет накапливать в себе элементы последовательности и выводить
# сумму пятерок последовательных элементов по мере их накопления.
# Одним из требований к классу является то, что он не должен хранить в себе больше элементов,
# чем ему действительно необходимо, т. е. он не должен хранить элементы, которые уже вошли в
# пятерку, для которой была выведена сумма.
# Класс должен иметь следующий вид
# class Buffer:
#    def __init__(self):
#        # конструктор без аргументов
#
#    def add(self, *a):
#        # добавить следующую часть последовательности
#
#    def get_current_part(self):
#        # вернуть сохраненные в текущий момент элементы последовательности в порядке,
#        в котором они были добавлены
#
# Пример работы с классом
# buf = Buffer()
# buf.add(1, 2, 3)
# buf.get_current_part() # вернуть [1, 2, 3]
# buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
# buf.get_current_part() # вернуть [6]
# buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
# buf.get_current_part() # вернуть []
# buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и
#                                                                 четвертой пятерки
# buf.get_current_part() # вернуть [1]
# Обратите внимание, что во время выполнения метода add выводить сумму пятерок может
# потребоваться несколько раз до тех пор, пока в буфере не останется менее пяти элементов.
# class Buffer:
#     def __init__(self):
#         self.buffer = []
#
#     def add(self, *a):
#         self.buffer.extend(a)
#         while len(self.buffer) >= 5:
#             print(sum(self.buffer[:5]))
#             self.buffer = self.buffer[5:]
#
#     def get_current_part(self):
#         print(self.buffer) # change print to return
#
#
# buf = Buffer()
# buf.add(1, 2, 3)
# buf.get_current_part() # вернуть [1, 2, 3]
# buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
# buf.get_current_part() # вернуть [6]
# buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
# buf.get_current_part() # вернуть []
# buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
# buf.get_current_part() # вернуть [1]
# --------------------------------------------------------------------------------------------

# 1.6.1  Наследование классов
# Вам дано описание наследования классов в следующем формате.
# <имя класса 1> : <имя класса 2> <имя класса 3> ... <имя класса k>
# Это означает, что класс 1 отнаследован от класса 2, класса 3, и т. д.
# Или эквивалентно записи:
# class Class1(Class2, Class3 ... ClassK):
#     pass
# Класс A является прямым предком класса B, если B отнаследован от A:
# class B(A):
#     pass
# Класс A является предком класса B, если
#     A = B;
#     A - прямой предок B
#     существует такой класс C, что C - прямой предок B и A - предок C
# Например:
# class B(A):
#     pass
# class C(B):
#     pass
# A -- предок С
# Вам необходимо отвечать на запросы, является ли один класс предком другого класса
# Важное примечание:  Создавать классы не требуется.
# Мы просим вас промоделировать этот процесс, и понять существует ли путь от одного класса до другого.
# Формат входных данных
# В первой строке входных данных содержится целое число n - число классов.
# В следующих n строках содержится описание наследования классов. В i-й строке указано от
# каких классов наследуется i-й класс. Обратите внимание, что класс может ни от кого не
# наследоваться. Гарантируется, что класс не наследуется сам от себя (прямо или косвенно),
# что класс не наследуется явно от одного класса более одного раза.
#
# В следующей строке содержится число q - количество запросов.
# В следующих q строках содержится описание запросов в формате <имя класса 1> <имя класса 2>.
# Имя класса – строка, состоящая из символов латинского алфавита, длины не более 50.
# Формат выходных данных
# Для каждого запроса выведите в отдельной строке слово "Yes", если класс 1 является предком
# класса 2, и "No", если не является.
# classes = {}
#
#
# def is_parent(parent, child):
#     if child in classes.keys():
#         if child == parent or parent in classes[child]:
#             return True
#         elif not classes[child]:
#             return False
#         else:
#             for j in classes[child]:
#                 if j in classes.keys() and is_parent(parent, j):
#                     return True
#     return False
#
#
# for i in range(int(input())):
#     line = input().replace(':', ' ').split()
#     classes.setdefault(line[0], line[1:])
# for i in range(int(input())):
#     parent, child = input().split()
#     if is_parent(parent, child):
#         print('Yes')
#     else:
#         print('No')
# -------------------------------------------------------------------------------------------

# 1.6.2 Наследование классов
# Реализуйте структуру данных, представляющую собой расширенную структуру стек.
# Необходимо поддерживать добавление элемента на вершину стека, удаление с вершины стека,
# и необходимо поддерживать операции сложения, вычитания, умножения и целочисленного деления.
# Операция сложения на стеке определяется следующим образом. Со стека снимается верхний
# элемент (top1), затем снимается следующий верхний элемент (top2), и затем как результат
# операции сложения на вершину стека кладется элемент, равный top1 + top2.
# Аналогичным образом определяются операции вычитания (top1 - top2), умножения (top1 * top2)
# и целочисленного деления (top1 // top2).
# Реализуйте эту структуру данных как класс ExtendedStack, отнаследовав его от стандартного
# класса list.
# Требуемая структура класса:
# class ExtendedStack(list):
#     def sum(self):
#         # операция сложения
#     def sub(self):
#         # операция вычитания
#     def mul(self):
#         # операция умножения
#     def div(self):
#         # операция целочисленного деления
# Примечание
# Для добавления элемента на стек используется метод append, а для снятия со стека – метод pop
# Гарантируется, что операции будут совершаться только когда в стеке есть хотя бы два элемента

class ExtendedStack(list):
    def sum(self):  # операция сложения
        self.append(self.pop() + self.pop())

    def sub(self):  # операция вычитания
        self.append(self.pop() - self.pop())

    def mul(self):  # операция умножения
        self.append(self.pop() * self.pop())

    def div(self):  # операция целочисленного деления
        self.append(self.pop() // self.pop())


ex_stack = ExtendedStack([1, 2, 3, 4, -3, 3, 5, 10])
ex_stack.div()
assert ex_stack.pop() == 2
ex_stack.sub()
assert ex_stack.pop() == 6
ex_stack.sum()
assert ex_stack.pop() == 7
ex_stack.mul()
assert ex_stack.pop() == 2
assert len(ex_stack) == 0
