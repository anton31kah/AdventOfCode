from src.common.common import get_lines
from collections import defaultdict
import re


class Robot:
    def __init__(self, position: tuple[int, int], speed: tuple[int, int], boundaries: tuple[int, int]):
        # col,row
        self.position = position
        self.speed = speed
        self.boundaries = boundaries

    @staticmethod
    def parse_line(line: str, boundaries: tuple[int, int]):
        x, y, dx, dy = map(int, re.findall(r'-?\d+', line))
        return Robot((x, y), (dx, dy), boundaries)
    
    def move(self):
        x, y = self.position
        dx, dy = self.speed
        bx, by = self.boundaries
        nx, ny = (x + dx) % bx, (y + dy) % by
        self.position = nx, ny
        return self.position
    
    def quadrant(self):
        x, y = self.position
        bx, by = self.boundaries
        qx, qy = bx // 2, by // 2
        if x < qx:
            if y < qy:
                return 1
            elif y >= by - qy:
                return 2
        elif x >= bx - qx:
            if y < qy:
                return 3
            elif y >= by - qy:
                return 4
        
        return None


def print_robots(robots: list[Robot], boundaries: tuple[int, int]):
    positions = set(robot.position for robot in robots)
    bx, by = boundaries
    for y in range(by):
        for x in range(bx):
            if (y, x) in positions:
                print('x', end='')
            else:
                print('.', end='')
        print()
    print()
    print()


def main():
    example = False
    lines = get_lines('S' if example else '')
    boundaries = (11, 7) if example else (101, 103)
    
    robots = [Robot.parse_line(line, boundaries) for line in lines]

    print('initial')
    print_robots(robots, boundaries)

    for i in range(10000):
        for robot in robots:
            robot.move()
        
        print(f'after {i + 1} seconds')
        print_robots(robots, boundaries)
    
    quadrants = defaultdict(int)

    for robot in robots:
        quadrants[robot.quadrant()] += 1
    
    total = 1

    for quadrant, amount in quadrants.items():
        if isinstance(quadrant, int) and 1 <= quadrant <= 4:
            total *= amount
    
    print(total)


if __name__ == "__main__":
    main()
