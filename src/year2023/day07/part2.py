from src.common.common import get_lines
from functools import total_ordering


CARD_VALUE = {
    "A": 15,
    "K": 14,
    "Q": 13,
    "J": -1,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}


def simplify_cards(cards):
    return tuple(CARD_VALUE[card] for card in cards)


def find_hand_type(cards):
    counts = {}
    for card in cards:
        if card not in counts:
            counts[card] = 0
        counts[card] += 1
    if 'J' in counts:
        count_j = counts.pop('J')
        if len(counts):
            counts[max(counts, key=counts.get)] += count_j
        else:
            counts['A'] = count_j
    hand_type = tuple(sorted(counts.values(), reverse=True))
    match hand_type:
        case (5,):
            return 10
        case (4, 1):
            return 9
        case (3, 2):
            return 8
        case (3, 1, 1):
            return 7
        case (2, 2, 1):
            return 6
        case (2, 1, 1, 1):
            return 5
        case (1, 1, 1, 1, 1):
            return 4
    print(counts)
    raise ValueError("Unrecognizable hand type " + str(hand_type) + " for cards " + cards)


@total_ordering
class Hand:
    def __init__(self, cards, bid):
        self.original_cards = cards
        self.cards = simplify_cards(cards)
        self.bid = bid
        self.type = find_hand_type(cards)

    def __str__(self):
        return f"{self.original_cards} {self.bid} ; {self.cards} {self.type}"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if type(other) is not Hand:
            raise TypeError('expected type Hand but got ' + type(other))
        return self.type == other.type and self.cards == other.cards

    def __lt__(self, other):
        if type(other) is not Hand:
            raise TypeError('expected type Hand but got ' + type(other))
        if self.type == other.type:
            return self.cards < other.cards
        return self.type < other.type


def main():
    lines = get_lines('')

    hands = []

    for line in lines:
        cards, bid = line.split()
        hand = Hand(cards, int(bid))
        hands.append(hand)
    
    hands = list(sorted(hands))

    result = 0

    for rank, hand in enumerate(hands, 1):
        result += hand.bid * rank
    
    print(result)


if __name__ == "__main__":
    main()
