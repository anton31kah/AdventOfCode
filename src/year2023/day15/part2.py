from src.common.common import get_lines


def hash(part):
    res = 0
    for c in part:
        res += ord(c)
        res *= 17
        res %= 256
    return res


def main():
    lines = get_lines('')
    parts = lines[0].split(',')
    boxes = [{} for i in range(256)]
    for part in parts:
        if '-' in part:
            label = part[:-1]
            label_hash = hash(label)
            boxes[label_hash].pop(label, None)
        elif '=' in part:
            label = part[:-2]
            lens = part[-1]
            label_hash = hash(label)
            boxes[label_hash][label] = lens
    result = 0
    for box_id, box in enumerate(boxes):
        if box:
            # print(box_id, list(box.items()))
            for slot, (label, lens) in enumerate(box.items(), 1):
                result += (box_id + 1) * slot * int(lens)
    print(result)


if __name__ == "__main__":
    main()
