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