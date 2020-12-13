# 3.1.2 Стандартные методы и функции для строк
# Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.
# Выведите одно число – количество вхождений строки t в строку s.

s = input()
t = input()
start_slice = 0
count = 0
while start_slice < len(s):
    if s.find(t, start_slice) == -1:
        break
    else:
        count += 1
        start_slice = s.index(t, start_slice) + 1
print(count)
