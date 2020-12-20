# 3.4.1 CSv
# Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе
# Чикаго с 2001 года по настоящее время.
# Одним из атрибутов преступления является его тип – Primary Type.
# Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в
# 2015 году.
# Файл с данными: Crimes.csv
import csv
crimes = {}
with open("Crimes.csv", "r") as inf:
    reader = csv.reader(inf)
    for row in reader:
        if "2015" in row[2]:
            if row[5] not in crimes:  # first entry in the dict
                crimes[row[5]] = 1
            else:
                crimes[row[5]] += 1
for key, value in crimes.items():
    if value == max(crimes.values()):
        print(key, value)
        break
