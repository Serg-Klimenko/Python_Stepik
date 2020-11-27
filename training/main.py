# 5.12 Command handler
# Напишите программу, имитирующую обработчик команд от пользователя.
# Программа должна выводить оповещение о своём состоянии в следующем формате:
# Когда пользователь вводит команду, содержимое которой обозначим как <command>, программа должна
# вывести фразу
# Processing "<command>" command...
# Например, пользователь ввёл Come to me, в таком случае должна быть выведена строка
# Processing "Come to me" command...
# Считывание команд должно продолжаться до ввода команды End, при этом программа должна вывести сообщение
# Good bye! и завершиться
# Для считывания команд используйте функцию input без аргументов.
# Формат ввода:
# Последовательность команд, каждая на отдельной строке. Команда состоит из символов латинского
# алфавита, пробелов и символов табуляции. Гарантируется отсутствие пробельных символов в начале и
# конце строки. Последняя команда всегда End.
#
# Формат вывода:
# Сообщения об обработке команд, как указано в задании, по одному сообщению на строку.

while True:
    command = input()
    if command == 'End':
        print('Good bye!')
        break
    else:
        print('Processing \"' + command + '\" command...')
