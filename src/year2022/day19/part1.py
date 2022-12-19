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

    def __add__(self, other):
        if not isinstance(other, Material):
            raise ValueError('Cannot add two different types:',
                             Material, 'and', type(other))

        return Material(
            ore=self.ore + other.ore,
            clay=self.clay + other.clay,
            obsidian=self.obsidian + other.obsidian,
            geode=self.geode + other.geode,
        )

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
    def __init__(self, cost: Material, produces: Material, amount: int):
        self.cost = cost
        self.produces = produces
        self.amount = amount

    def __str__(self):
        _, robot_type = str(self.produces).split(' ')
        plural = "s" if self.amount > 1 else ""
        return f'{self.amount} {robot_type} robot{plural} costs {self.cost}'


def parse_blueprint(line: str) -> tuple[int, list[Robot]]:
    blueprint_id, robots = line.split(': ')

    _, blueprint_id = blueprint_id.split(' ')
    blueprint_id = int(blueprint_id)

    robots = robots.split('.')
    processed_robots: list[Robot] = []

    for robot in robots:
        robot = robot.strip()
        robot_type, robot_cost = robot.split(' robot costs ')

        _, robot_type = robot_type.split('Each ')
        robot_type = Material.create(robot_type, 1)

        robot_cost = robot_cost.split(' and ')
        costs = []

        for cost in robot_cost:
            cost_amount, cost_type = cost.split(' ')
            costs.append(Material.create(cost_type, int(cost_amount)))

        robot_cost = sum(costs, start=Material())

        processed_robots.append(Robot(robot_cost, robot_type, 0))

    for robot in processed_robots:
        if robot.produces.ore > 0:
            robot.amount = 1

    return blueprint_id, processed_robots


def main():
    lines = get_lines('')

    blueprints = {}

    for line in lines:
        blueprint_id, robots = parse_blueprint(line)
        blueprints[blueprint_id] = robots

    print(blueprints)

    print(0)


if __name__ == "__main__":
    main()
