import re
import math
from src.common.common import get_lines


def round_to(x, base):
    return base * math.ceil(x / base)


lines = get_lines()

depart_time = int(lines[0])

buses = list(map(int, re.findall(r'\d+', lines[1])))

min_id, min_time = min([(bus, round_to(depart_time, bus)) for bus in buses], key=lambda tup: tup[1])

wait_time = min_time - depart_time

print(wait_time * min_id)
