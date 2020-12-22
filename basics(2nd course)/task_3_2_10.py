# 3.2.10 Регулярные выражения
# Вам дана последовательность строк.
# Выведите строки, содержащие двоичную запись числа, кратного 3.
# 0011      0001 0010
# 0110      0001 0101
# 1001      0001 1000
# 1100      0001 1011
# 1111      0001 1110
#

import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    if re.search(r"[^01]", line) is None:
        even = re.findall(r"(\d)(?:\d)?", line[::-1])
        sum_even = len(re.sub(r"(0)", "", "".join(even)))
        odd = re.findall(r"(?:\d)(\d)?", line[::-1])
        sum_odd = len(re.sub(r"(0)", "", "".join(odd)))
        if (sum_odd - sum_even) % 3 == 0:
            print(line)
