# 2.1.1 Ошибки и исключения
# напишите программу, которая будет определять обработку каких исключений можно удалить из кода.
# Формат входных данных
# В первой строке входных данных содержится целое число n - число классов исключений.
# В следующих n строках содержится описание наследования классов. В i-й строке указано от каких
# классов наследуется i-й класс. Обратите внимание, что класс может ни от кого не наследоваться.
# Гарантируется, что класс не наследуется сам от себя (прямо или косвенно), что класс не наследуется
# явно от одного класса более одного раза.
# В следующей строке содержится число m - количество обрабатываемых исключений.
# Следующие m строк содержат имена исключений в том порядке, в каком они были написаны у Антона в коде.
# Гарантируется, что никакое исключение не обрабатывается дважды.
# Формат выходных данных
# Выведите в отдельной строке имя каждого исключения, обработку которого можно удалить из кода,
# не изменив при этом поведение программы. Имена следует выводить в том же порядке, в котором они
# идут во входных данных.
classes = {}


def is_parent(child, exeptions):
    if child in classes.keys() and classes[child] in exeptions:
        return True
    else:
        while classes[child] and child in classes.keys():
            for j in classes[child]:
                if j in classes.keys() and is_parent(j, exeptions):
                    return True
    return False


for _ in range(int(input())):
    line = input().replace(':', ' ').split()
    classes.setdefault(line[0], [])
    if len(line) > 1:
        classes[line[0]] = line[1:]
exeptions = []
for _ in range(int(input())):
    exeption = input()
    exeptions.append(exeption)
    if exeption not in exeptions and is_parent(exeption, exeptions):
        print(exeption)

#        and classes[exeption] in exeptions:
#        print(exeption)
