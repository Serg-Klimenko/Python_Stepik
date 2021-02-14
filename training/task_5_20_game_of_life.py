# 5.20 Game of life
# Напишите программу, вычисляющую следующее состояние поля для Game of life.
#    в пустой (мёртвой) клетке, рядом с которой ровно три живые клетки, зарождается
#    жизнь;
#    если у живой клетки есть две или три живые соседки, то эта клетка продолжает
#    жить; в противном случае, если соседей меньше двух или больше трёх, клетка
#    умирает («от одиночества» или «от перенаселённости»)
#
# Поле представляет собой прямоугольник, причём для крайних клеток поля соседними
# являются клетки с противоположного конца (поле представляет собой тор).
#
# Формат ввода:
# На первой строке указаны два целых числа через пробел -- высота и ширина поля.
# В следующих строках подаётся состояние поля. Точка "." обозначает мёртвую клетку, символ "X" − живую.
# Формат вывода:
# Следующее состояние поля, используя те же обозначения, что использовались на
# вводе.
# input col, row from console
n, m = (int(x) for x in input().split())
# init matrix n*m
life_field = [["." for j in range(m)] for i in range(n)]
# init result matrix
next_life_field = [["." for j in range(m)] for i in range(n)]
# input fields string
for i in range(n):
    row = input()
    for j in range(m):
        if row[j] == "X":
            life_field[i][j] = "X"
            next_life_field[i][j] = "X"
# next step of game
for i in range(n):
    for j in range(m):
        # calculate neighbour ceil
        count = 0  # count of neighbour life cell
        for i1 in range(i - 1, i + 2):
            for j1 in range(j - 1, j + 2):
                if life_field[i1 % n][j1 % m] == "X":
                    count += 1
        if life_field[i][j] == "." and count == 3:  # dead cell & 3 live cell
            next_life_field[i][j] = "X"
        elif life_field[i][j] == "X" and (count < 3 or count > 4):  # live cell
            next_life_field[i][j] = "."
# output matrix
for i in range(n):
    print(*next_life_field[i], sep="")
