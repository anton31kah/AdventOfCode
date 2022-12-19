from cachetools import cached, LRUCache
from cachetools.keys import hashkey
from src.common.common import get_lines


class Material:
    def __init__(self, ore=0, clay=0, obsidian=0, geode=0):
        self.ore = ore
        self.clay = clay
        self.obsidian = obsidian
        self.geode = geode

    @classmethod
    def create(cls, material_name: str, amount=1):
        match material_name:
            case 'ore':
                return Material(ore=amount)
            case 'clay':
                return Material(clay=amount)
            case 'obsidian':
                return Material(obsidian=amount)
            case 'geode':
                return Material(geode=amount)

        raise ValueError('Invalid material name', material_name)

    @classmethod
    def __validate(cls, obj, operation=''):
        if not isinstance(obj, Material):
            raise ValueError('Cannot perform operation', operation,
                             'on two different types:', Material, 'and', type(obj))

    def __add__(self, other):
        Material.__validate(other)

        return Material(
            ore=self.ore + other.ore,
            clay=self.clay + other.clay,
            obsidian=self.obsidian + other.obsidian,
            geode=self.geode + other.geode,
        )

    def __sub__(self, other):
        Material.__validate(other)

        return Material(
            ore=self.ore - other.ore,
            clay=self.clay - other.clay,
            obsidian=self.obsidian - other.obsidian,
            geode=self.geode - other.geode,
        )

    def __ge__(self, other):
        Material.__validate(other)

        return self.ore >= other.ore \
            and self.clay >= other.clay \
            and self.obsidian >= other.obsidian \
            and self.geode >= other.geode

    def __hash__(self) -> int:
        return hash((self.ore, self.clay, self.obsidian, self.geode))

    def __str__(self):
        attributes = [
            ('ore', self.ore),
            ('clay', self.clay),
            ('obsidian', self.obsidian),
            ('geode', self.geode)
        ]
        return ' '.join(f'{value} {key}' for key, value in attributes if value > 0)

    def __repr__(self):
        return str(self)


class Robot:
    def __init__(self, cost: Material, produces: Material):
        self.cost = cost
        self.produces = produces

        _, robot_type = str(produces).split(' ')
        self.type = robot_type

    def __str__(self):
        return f'{self.type} robot costs {self.cost}'

    def __repr__(self):
        return str(self)


class Blueprint:
    def __init__(self, blueprint_id: int, available_robots: list[Robot], blueprint_robots: list[Robot]):
        self.blueprint_id = blueprint_id
        self.available_robots = available_robots
        self.blueprint_robots = blueprint_robots


def parse_blueprint(line: str) -> Blueprint:
    blueprint_id, robots = line.split(': ')

    _, blueprint_id = blueprint_id.split(' ')
    blueprint_id = int(blueprint_id)

    robots = robots.split('.')
    processed_robots: list[Robot] = []

    for robot in robots:
        robot = robot.strip()
        if len(robot) == 0:
            continue

        robot_type, robot_cost = robot.split(' robot costs ')

        _, robot_type = robot_type.split('Each ')
        robot_type = Material.create(robot_type, 1)

        robot_cost = robot_cost.split(' and ')
        costs = []

        for cost in robot_cost:
            cost_amount, cost_type = cost.split(' ')
            costs.append(Material.create(cost_type, int(cost_amount)))

        robot_cost = sum(costs, start=Material())

        processed_robots.append(Robot(robot_cost, robot_type))

    available = []
    for robot in processed_robots:
        if robot.produces.ore > 0:
            available.append(robot)

    return Blueprint(blueprint_id, available, processed_robots)


def hash_robots(robots: list[Robot]):
    count = {}
    for robot in robots:
        if robot.type not in count:
            count[robot.type] = 0
        count[robot.type] += 1
    return frozenset(count.items())


@cached(cache=LRUCache(maxsize=1_000_000), key=lambda minutes, material, available_robots, blueprint_robots, path: hashkey(minutes, material, hash_robots(available_robots)))
def play(minutes: int, material: Material, available_robots: list[Robot], blueprint_robots: list[Robot], path: list[str]):
    if minutes <= 0:
        return material.geode, path

    options = []

    robots_that_can_be_built = {}

    for robot in blueprint_robots:
        if material >= robot.cost:
            robots_that_can_be_built[robot.type] = robot

    # print(minutes, len(robots_that_can_be_built))

    for robot_to_build in robots_that_can_be_built.values():
        new_material = material + Material() - robot_to_build.cost

        for robot in available_robots:
            new_material += robot.produces

        debug_line = f'[{minutes}] Built {robot_to_build.type}, {material} -> {new_material}, {hash_robots(available_robots)}'
        options.append(play(minutes - 1, new_material, available_robots + [robot_to_build], blueprint_robots, path + [debug_line]))

    if 'geode' not in robots_that_can_be_built:
        # no robot built
        new_material = material + Material()

        for robot in available_robots:
            new_material += robot.produces

        debug_line = f'[{minutes}] Built nothing, {material} -> {new_material}, {hash_robots(available_robots)}'
        options.append(play(minutes - 1, new_material, available_robots + [], blueprint_robots, path + [debug_line]))

    return max(options, key=lambda t: t[0])


def main():
    lines = get_lines('S')

    blueprints: list[Blueprint] = []

    for line in lines:
        blueprint = parse_blueprint(line)
        blueprints.append(blueprint)

    total_quality = 0

    for blueprint in blueprints:
        # material = Material()
        # for minute in range(24):
        #     built_robots = []

        #     for robot in robots:
        #         if material >= robot.cost:
        #             material -= robot.cost
        #             built_robots.append(robot)

        #     for robot in robots:
        #         for _ in range(robot.amount):
        #             material += robot.produces

        #     print('  minute', minute + 1, material)

        #     for robot in built_robots:
        #         robot.amount += 1

        geode, path = play(24, Material(), blueprint.available_robots, blueprint.blueprint_robots, [])
        for line in path:
            print(line)

        print('blueprint', blueprint.blueprint_id, geode)
        total_quality += geode * blueprint.blueprint_id
        exit()

    print(total_quality)


if __name__ == "__main__":
    main()
