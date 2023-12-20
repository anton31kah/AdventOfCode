import re
from typing import Sequence
from src.common.common import get_lines
from dataclasses import dataclass


@dataclass
class Part:
    x: int
    m: int
    a: int
    s: int

@dataclass
class Compare:
    att: str
    op: str
    val: int

    def test(self, part: Part) -> bool:
        value = getattr(part, self.att, None)
        if value is None:
            raise ValueError(f"attribute {self.att} not found in object {part}")
        match self.op:
            case '>':
                return value > self.val
            case '<':
                return value < self.val
        raise ValueError("invalid sign " + self.op)

@dataclass
class Rule:
    compare: Compare

    def supports(self, part: Part) -> bool:
        return self.compare is None or self.compare.test(part)

    def test(self, part: Part) -> bool:
        raise ValueError("Abstract")

@dataclass
class ConstantRule(Rule):
    result: bool

    def test(self, part: Part) -> bool:
        return self.result

@dataclass
class RedirectRule(Rule):
    to: str
    workflows: dict[str, 'Workflow']

    def test(self, part: Part) -> bool:
        return self.workflows[self.to].test(part)

@dataclass
class Workflow:
    name: str
    rules: list[Rule]

    def test(self, part: Part) -> bool:
        for r in self.rules:
            if r.supports(part):
                return r.test(part)

@dataclass
class Node:
    value: str
    left: 'Node'
    right: 'Node'
    parent: 'Node'
    parent_link: list[Compare]


def read_input(lines):
    workflows = {}
    parts = []

    reading_workflows = True
    for line in lines:
        if not line:
            reading_workflows = False
            continue
        if reading_workflows:
            name, logic = line.split('{')
            rules_string = logic[:-1].split(',')
            rules = []
            for rule_str in rules_string:
                str_parts = re.findall(r"(\w+)(([<>])(\d+):(\w+))?", rule_str)[0]
                compare = None
                if str_parts[1]:
                    compare_att, _, compare_op, compare_value, result = str_parts
                    compare = Compare(compare_att, compare_op, int(compare_value))
                else:
                    result = str_parts[0]
                if result == 'R':
                    rules.append(ConstantRule(compare, False))
                elif result == 'A':
                    rules.append(ConstantRule(compare, True))
                else:
                    rules.append(RedirectRule(compare, result, workflows))
            workflows[name] = Workflow(name, rules)
        else:
            x, m, a, s = [int(v) for v in re.findall(r'\d+', line)]
            parts.append(Part(x, m, a, s))
    
    return workflows, parts

def empty_ranges():
    return {
        'x': range(1, 4001),
        'm': range(1, 4001),
        'a': range(1, 4001),
        's': range(1, 4001),
    }

def reverse_compare(compare: Compare) -> Compare:
    match compare.op:
        case '>':
            return Compare(compare.att, '<', compare.val + 1)
        case '<':
            return Compare(compare.att, '>', compare.val - 1)

def merge_ranges(ranges: dict[str, range], compare: Compare):
    if not compare:
        return ranges.copy()
    res = ranges.copy()
    match compare.op:
        case '>':
            res[compare.att] = range(compare.val + 1, res[compare.att].stop)
        case '<':
            res[compare.att] = range(res[compare.att].start, compare.val)
    return res

def build_tree(workflows: dict[str, Workflow]):
    root = Node('in', None, None, None, None)
    current = root
    
    else_rules: list[Compare] = []
    for rule in workflows[current.value].rules:
        if rule.compare:
            if not else_rules:
                current.left = Node(rule.result, None, None, current, rule.compare)
                else_rules.append(reverse_compare(rule.compare))
            else:
                ...
            ranges = merge_ranges(ranges, rule.compare)
            ...
        ...


def main():
    lines = get_lines('')
    workflows, parts = read_input(lines)
    total = 0
    for part in parts:
        res = workflows['in'].test(part)
        if res:
            total += part.x + part.m + part.a + part.s
    print(total)
    """
    1. build binary tree from rules
    2. at leaves, go up the tree and build ranges ([0<x<1000, 100<m<4000, ...])
    3. find a way to merge ranges and count how many can the fit
    """


if __name__ == "__main__":
    main()
