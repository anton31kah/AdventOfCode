import itertools
from src.common.common import get_lines


def read_cards(lines):
    player1_cards, player2_cards = [], []

    flag = True

    for line in lines:
        if not line:
            flag = False
            continue
        if line.endswith(':'):
            continue
        if flag:
            player1_cards.append(int(line))
        else:
            player2_cards.append(int(line))

    return player1_cards, player2_cards


def calculate_score(cards):
    score = 0
    for multiply, card in enumerate(reversed(cards), start=1):
        score += multiply * card
    return score


history = {}
games_played = 0


def play_game(game_id, cards1, cards2):
    global games_played

    game_history = history.setdefault(game_id, set())

    for round in itertools.count(start=1):
        if not cards1 or not cards2:
            if cards1:
                return 1, cards1
            else:
                return 2, cards2

        # <history>
        round_cards = (tuple(cards1), tuple(cards2))

        if round_cards in game_history:
            return 1, cards1

        game_history.add(round_cards)
        # </history>
        
        c1 = cards1.pop(0)
        c2 = cards2.pop(0)

        if len(cards1) >= c1 and len(cards2) >= c2:
            games_played += 1
            winner, winner_cards = play_game(games_played, cards1[:c1], cards2[:c2])
            if winner == 1:
                cards1.extend([c1, c2])
            elif winner == 2:
                cards2.extend([c2, c1])
        else:
            if c1 > c2:
                cards1.extend([c1, c2])
            elif c2 > c1:
                cards2.extend([c2, c1])
    
    return None


def main():
    global games_played

    lines = get_lines()

    player1_cards, player2_cards = read_cards(lines)

    games_played += 1
    winner, winner_cards = play_game(games_played, player1_cards, player2_cards)

    print(calculate_score(winner_cards))


if __name__ == "__main__":
    main()
