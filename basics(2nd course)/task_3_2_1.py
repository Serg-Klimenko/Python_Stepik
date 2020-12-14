# 3.2.1 Регулярные выражения
# Вам дана последовательность строк.
# Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.
# 3.2.2
# Выведите строки, содержащие "cat" в качестве слова.
# Примечание: Для работы со словами используйте группы символов \b и \B.
import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    pattern_task1 = r"(cat.*){2}"
    pattern_task2 = r"\bcat\b"
    if re.search(pattern_task2, line) is not None:
        print(line)
