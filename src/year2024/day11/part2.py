from src.common.common import get_lines
import math


class Node:
    def __init__(self, value: int):
        self.value = value
        self.next: Node = None
        self.prev: Node = None
    
    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return str(self)


class LinkedList:
    def __init__(self):
        self.head: Node = None
        self.size = 0

    def add_after(self, ref: Node, to_add: Node):
        if to_add.next is not None or to_add.prev is not None:
            raise ValueError("added node cannot have next or prev")

        orig_next = ref.next

        ref.next = to_add
        to_add.prev = ref

        if orig_next is not None:
            to_add.next = orig_next
            orig_next.prev = to_add

        self.size += 1
    
    def __iter__(self):
        return LinkedListIterator(self)
    
    def __str__(self):
        return f"[{self.head}]({self.size})"
    
    def __repr__(self):
        return str(self)


def count_digits(num):
    return math.floor(math.log10(num)) + 1


class LinkedListIterator:
    def __init__(self, linked_list: LinkedList):
        self.linked_list = linked_list
        self.current = linked_list.head
    
    def __next__(self):
        if self.current is None:
            raise StopIteration
        to_return = self.current
        self.current = self.current.next
        return to_return


def main():
    lines = get_lines('')

    numbers = [int(x) for x in lines[0].split()]

    stones = LinkedList()

    last = None
    for n in numbers:
        if last is None:
            stones.head = Node(n)
            last = stones.head
            stones.size += 1
        else:
            to_add = Node(n)
            stones.add_after(last, to_add)
            last = to_add

    for i in range(75):
        print(i, stones.size)

        for node in stones:
            if node.value == 0:
                node.value = 1
                continue
            
            digits_len = count_digits(node.value)
            if digits_len % 2 == 0:
                mul = 10 ** (digits_len // 2)
                left = node.value // mul
                right = node.value % mul
                node.value = left
                stones.add_after(node, Node(right))
                continue
            
            node.value *= 2024
    
    print(stones.size)


if __name__ == "__main__":
    main()
