import re
import math
from src.common.common import get_lines


lines = get_lines()

buses = [(idx, int(bus)) for idx, bus in enumerate(lines[1].split(',')) if bus != 'x']

print(buses)

t = 100000000000000

try:
    while True:
        all_good = True
        for idx, bus in buses:
            if (t + idx) % bus != 0:
                all_good = False
                break
        if all_good:
            print(t)
            break
        t += buses[0][1]
except KeyboardInterrupt:
    print(t)
