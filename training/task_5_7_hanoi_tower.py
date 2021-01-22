# 5.7 Hanoi Tower
# Ханойская башня -- одна из широко известных головоломок, условие которой состоит
# в следующем:
# Имеется три стержня (пронумеруем их числами 1, 2 и 3). На первом стержне находится
# n колец с радиусами от 1 до n. Кольца отсортированы по радиусу, и наибольшее
# кольцо лежит ниже всех.
# Вам требуется найти и записать алгоритм переноса всех n колец с первого стержня
# на третий по следующим правилам:
# за один ход можно переносить только одно кольцо;
# нельзя класть большее кольцо на меньшее.
# Программа должна вывести на экран кратчайшую последовательность действий,
# необходимую для того, чтобы перенести все кольца с первого стержня на третий.
# Формат ввода:
# Строка, содержащая положительное целое число n n n.
# Формат вывода:
# Порядок действий для решения головоломки. Каждое действие записывается на
# отдельной строке. Действие записывается в формате "номер стержня, с которого
# снимаем кольцо" - "номер стержня, на который надеваем кольцо"
def hanoi_tower(level, base=1, goal=3):
    if level == 1:
        print(f"{base} - {goal}")
        return
    tmp = 6 - base - goal
    hanoi_tower(level - 1, base, tmp)
    print(f"{base} - {goal}")
    hanoi_tower(level - 1, tmp, goal)


n = int(input())
hanoi_tower(n)
