# 3.2.1 Регулярные выражения
# Вам дана последовательность строк.
# Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.
import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    if re.search(r"(cat.*){2}", line) is not None:
        print(line)
