from src.common.common import get_lines


class Node:
    def __init__(self, value):
        self.value = value
        self.incoming = set()
        self.outgoing = set()
    
    def __eq__(self, other):
        return self.value == other.value
    
    def __hash__(self):
        return hash(self.value)


class DirectedGraph:
    def __init__(self):
        self.nodes = {}
    
    def add_edge(self, start, end):
        start_node = self.get_node(start)
        end_node = self.get_node(end)
        if end_node not in start_node.outgoing:
            start_node.outgoing.add(end_node)
        if start_node not in end_node.incoming:
            end_node.incoming.add(start_node)
    
    def remove_edge(self, start, end):
        start_node = self.get_node(start)
        end_node = self.get_node(end)
        if end_node in start_node.outgoing:
            start_node.outgoing.remove(end_node)
        if start_node in end_node.incoming:
            end_node.incoming.remove(start_node)
    
    def get_node(self, value):
        if value not in self.nodes:
            self.nodes[value] = Node(value)
        return self.nodes[value]
    
    def find_source(self):
        for node in self.nodes.values():
            if len(node.incoming) == 0:
                return node
        return None
    
    def find_target(self):
        for node in self.nodes.values():
            if len(node.outgoing) == 0:
                return node
        return None

    def kahn(self):
        L = []
        S = set()

        for node in self.nodes.values():
            if len(node.incoming) == 0:
                S.add(node.value)
        
        while len(S) >= 1:
            n = S.pop()
            node = self.get_node(n)
            L.append(n)
            for out in set(node.outgoing):
                self.remove_edge(n, out.value)
                if len(out.incoming) == 0:
                    S.add(out.value)
        
        for node in self.nodes.values():
            if len(node.incoming) >= 1 or len(node.outgoing) >= 1:
                raise ValueError("graph has at least one cycle")
        
        return L


def parse_input(lines):
    rules = set()
    updates = []

    for line in lines:
        if '|' in line:
            l, r = line.split('|')
            rules.add((int(l), int(r)))
        if ',' in line:
            pages = [int(p) for p in line.split(',')]
            updates.append(pages)
    
    return rules, updates


def filter_used_rules(rules, pages):
    result = []
    for x, y in rules:
        if x in pages and y in pages:
            result.append((x, y))
    return result


def build_graph(rules):
    graph = DirectedGraph()

    for x, y in rules:
        graph.add_edge(x, y)

    return graph


def transform_to_pump(pairs):
    comps = set(x for p in pairs for x in p)
    components = '\n'.join(f"component {x}" for x in comps)
    arrows = '\n'.join(f"{x} -> {y}" for x, y in pairs)
    return f"\n\n\n{components}\n\n{arrows}\n\n\n"


def print_pump(rules, updates):
    print("@startuml")

    for pages in updates:
        print(transform_to_pump(filter_used_rules(rules, pages)))
        print("newpage")
    
    print("@enduml")


def main():
    lines = get_lines('')

    rules, updates = parse_input(lines)

    total = 0

    for pages in updates:
        current_rules = filter_used_rules(rules, pages)
        illegal = False
        for i in range(len(pages)):
            for j in range(i + 1, len(pages)):
                if (pages[j], pages[i]) in current_rules:
                    illegal = True
                    break
            if illegal:
                break
        if illegal:
            g = build_graph(current_rules)
            result = g.kahn()
            ordered = sorted(pages, key=lambda x: result.index(x))
            total += ordered[len(pages) // 2]

    print(total)


if __name__ == "__main__":
    main()
