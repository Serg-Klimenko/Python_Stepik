# 3.4.2 JSON
# Вам дано описание наследования классов в формате JSON.
# Описание представляет из себя массив JSON-объектов, которые соответствуют классам.
# У каждого JSON-объекта есть поле name, которое содержит имя класса, и поле parents,
# которое содержит список имен прямых предков.
# Пример:
# [{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
# Эквивалент на Python:
# class A:
#     pass
# class B(A, C):
#     pass
# class C(A):
#     pass
# Гарантируется, что никакой класс не наследуется от себя явно или косвенно, и что никакой
# класс не наследуется явно от одного класса более одного раза.
# Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в
# следующем формате.
# <имя класса> : <количество потомков>
# Выводить классы следует в лексикографическом порядке.

# inp = json.loads("""[{"name": "G", "parents": ["ZZZ"]},
#                      {"name": "TH", "parents": ["ZZZ"]},
#                      {"name": "G", "parents": ["ZY"]},
#                      {"name": "G", "parents": ["F"]},
#                      {"name": "A", "parents": []},
#                      {"name": "B", "parents": ["A"]},
#                      {"name": "C", "parents": ["A"]},
#                      {"name": "D", "parents": ["B", "C"]},
#                      {"name": "E", "parents": ["D"]},
#                      {"name": "F", "parents": ["D"]},
#                      {"name": "X", "parents": []},
#                      {"name": "Y", "parents": ["X", "A"]},
#                      {"name": "Z", "parents": ["X"]},
#                      {"name": "V", "parents": ["Z", "Y"]},
#                      {"name": "W", "parents": ["V"]}]""")
import json
inp = json.loads(input())
child = {}
# parse JSON data to dictionary parrent : [childs]
for line in inp:
    child.setdefault(line["name"], [line["name"]])  # parent: [parrent] for classes without child
    for parrent in line["parents"]:
        if parrent not in child:
            child.setdefault(parrent, [parrent, line["name"]])
        else:
            child[parrent].append(line["name"])
# search and add childs to parrent
for key in child:
    for i in child[key]:
        if i in child.keys():
            child[key] += child[i][1:]
# count uniqe childs in every parrent
for key, value in sorted(child.items()):
    print(f"{key} : {len(set(child[key]))}")

# A : 10
# B : 5
# C : 5
# D : 4
# E : 1
# F : 2
# G : 1
# TH : 1
# V : 2
# W : 1
# X : 5
# Y : 3
# Z : 3
# ZY : 2
# ZZZ : 3