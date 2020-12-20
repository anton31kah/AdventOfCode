import re
from src.common.common import get_lines


def read_tiles(lines):
    tiles = {}

    current_tile_id = None
    current_tile = []

    for line in lines:
        if not line:
            tiles[current_tile_id] = current_tile
            current_tile_id = None
            current_tile = []
            continue

        if line.startswith('Tile'):
            current_tile_id = int(re.search(r'\d+', line).group(0))
        else:
            current_tile.append(line)

    return tiles


def identity(tile):
    return tile


def flip_vertical(tile):
    return tile[::-1]


def flip_horizontal(tile):
    return [row[::-1] for row in tile]


def rotate_90(tile):
    size = len(tile)
    return [[tile[j][i] for j in range(size - 1, -1, -1)] for i in range(size)]


def rotate_180(tile):
    return [row[::-1] for row in tile[::-1]]


def rotate_270(tile):
    size = len(tile)
    return [[tile[j][i] for j in range(size)] for i in range(size - 1, -1, -1)]


def tiles_variations(tiles):
    ops = [identity, flip_vertical, flip_horizontal, rotate_90, rotate_180, rotate_270]
    return {tile_id: [op(tile) for op in ops] for tile_id, tile in tiles.items()}


def are_adjacent(tile1, tile2):
    if tile1[-1] == tile2[0]:
        return ('ud', 'du')  # tile1 above tile2
    if tile2[-1] == tile1[0]:
        return ('du', 'ud')  # tile2 above tile1

    tile1left = [row[0] for row in tile1]
    tile1right = [row[-1] for row in tile1]
    tile2left = [row[0] for row in tile2]
    tile2right = [row[-1] for row in tile2]

    if tile1right == tile2left:
        return ('lr', 'rl')  # tile1 -> tile2
    if tile2right == tile1left:
        return ('rl', 'lr')  # tile2 -> tile1

    return False


def unique(elements, key):
    unique_elements = []
    unique_elements_ids = set()
    for element in elements:
        element_id = key(element)
        if element_id not in unique_elements_ids:
            unique_elements_ids.add(element_id)
            unique_elements.append(element)
    return unique_elements


def main():
    lines = get_lines()

    tiles = read_tiles(lines)

    tiles = tiles_variations(tiles)

    adjacencies = {}

    for id1, tile1_variations in tiles.items():
        t1_adjacencies = adjacencies.setdefault(id1, set())
        for id2, tile2_variations in tiles.items():
            t2_adjacencies = adjacencies.setdefault(id2, set())
            if id1 != id2:
                for tile1 in tile1_variations:
                    for tile2 in tile2_variations:
                        adjacency = are_adjacent(tile1, tile2)
                        if adjacency:
                            dir1, dir2 = adjacency
                            t1_adjacencies.add((dir1, id2))
                            t2_adjacencies.add((dir2, id1))

    corners = []

    for tile_id, variations in adjacencies.items():
        unique_variations = unique(variations, key=lambda tup: tup[1])
        if len(unique_variations) == 2:
            corners.append(tile_id)

    if len(corners) == 4:
        print(corners)
        ids_multiplied = 1
        for tile_id in corners:
            ids_multiplied *= tile_id
        print(ids_multiplied)
    else:
        print(f"no 4 corners, actual count = {len(corners)}, corners = {corners}")


if __name__ == "__main__":
    main()
