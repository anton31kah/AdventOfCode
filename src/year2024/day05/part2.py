from src.common.common import get_lines


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


def main():
    lines = get_lines('')

    rules, updates = parse_input(lines)

    total = 0

    for pages in updates:
        illegal = False
        for i in range(len(pages)):
            for j in range(i + 1, len(pages)):
                if (pages[j], pages[i]) in rules:
                    illegal = True
                    break
            if illegal:
                break
        if not illegal:
            if len(pages) % 2 == 0:
                print('even pages here', pages)
            # print(pages, pages[len(pages) // 2])
            total += pages[len(pages) // 2]
    
    print(total)


if __name__ == "__main__":
    main()
