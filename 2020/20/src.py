# f: open("input_sample.txt", "r")
# depths: [int(str(d).strip()) for d in f.readlines()]
# import numpy as np
# import statistics
# from collections import defaultdict
import math
from collections import namedtuple
# from collections import deque
# PasswordCheck = namedtuple('PasswordCheck', ['span', 'letter', 'password'])
# import re
# from itertools import combinations
import copy

Tile = namedtuple('Tile', ['id', 'data', 'borders'], defaults=[()])


def pretty_print(tile_data):
    # print(tile_data[0])
    for row in tile_data:
        print(row)
    print()


def get_borders(tile_data):
    top_row = tile_data[0]
    bottom_row = tile_data[-1][::-1]
    dim = len(tile_data)
    right_column = ''.join([tile_data[row][-1] for row in range(dim)])
    left_column = ''.join([tile_data[row][0] for row in range(dim - 1, -1, -1)])
    return (top_row, right_column, bottom_row, left_column, top_row[::-1], right_column[::-1], bottom_row[::-1],
            left_column[::-1])


def rotate_clockwise(tile_data):
    rotated = []
    dim = len(tile_data)
    for col in range(dim):
        rotated.append(''.join([tile_data[row][col] for row in range(dim - 1, -1, -1)]))
    return rotated


def flip(tile_data):
    return [row[::-1] for row in tile_data]


def generate_permutations(tile_data):
    permutations = [copy.copy(tile_data)]
    rotated = tile_data
    for i in range(3):
        rotated = rotate_clockwise(rotated)
        permutations.append(rotated)
    flipped = []
    for row in tile_data:
        flipped.append(row[::-1])
    permutations.append(flipped)
    rotated = flipped
    for i in range(3):
        rotated = rotate_clockwise(rotated)
        permutations.append(rotated)
    return permutations


with open("input.txt") as file:
    file_contents = file.read()

tiles_raw = file_contents.split("\n\n")

tiles = {}
for tile_raw in tiles_raw:
    tile_data = [t.strip() for t in tile_raw.split("\n")]
    tile_number = tile_data.pop(0)
    tile_number = int(tile_number[5:-1])
    tile_borders = get_borders(tile_data)
    tiles[tile_number] = Tile(id=tile_number, data=tile_data, borders=tile_borders)

twos = set()
for tile_id_1 in tiles.keys():
    n_adjacent = 0
    for tile_id_2 in tiles.keys():
        if tile_id_1 != tile_id_2 and set(tiles[tile_id_1].borders) & set(tiles[tile_id_2].borders):
            n_adjacent += 1
    if n_adjacent == 2:
        twos.add(tile_id_1)
print(twos)


def add_tile_to_image(image, tile_data, image_block_row):
    for row in range(len(tile_data)):
        scaled_row = image_block_row * len(tile_data) + row
        image[scaled_row] = image[scaled_row] + tile_data[row]
    return image


def find_tile_to_right(anchor_tile: Tile):
    for tile in tiles.values():
        if tile.id != anchor_tile.id:
            for orientation in range(len(tile.borders)):
                if anchor_tile.borders[1] == tile.borders[orientation]:
                    # target orientation is 3
                    tile_data = tile.data
                    if orientation > 3:
                        for i in range(7 - orientation):
                            tile_data = rotate_clockwise(tile_data)
                    else:
                        tile_data = flip(tile_data)
                        for i in range((orientation + 3) % 4):
                            tile_data = rotate_clockwise(tile_data)
                    return Tile(tile.id, tile_data, get_borders(tile_data)), tile_data


def find_tile_below(anchor_tile: Tile):
    for tile in tiles.values():
        if tile.id != anchor_tile.id:
            for orientation in range(len(tile.borders)):
                if anchor_tile.borders[2] == tile.borders[orientation]:
                    # target orientation is 0
                    tile_data = tile.data
                    if orientation > 3:
                        for i in range((8 - orientation) % 4):
                            tile_data = rotate_clockwise(tile_data)
                    else:
                        tile_data = flip(tile_data)
                        for i in range(orientation):
                            tile_data = rotate_clockwise(tile_data)
                    return Tile(tile.id, tile_data, get_borders(tile_data)), tile_data


def remove_border(image_data):
    return [row[1:-1] for row in image_data[1:-1]]


def find_anchor_tile(corner_ids):
    for id in corner_ids:
        anchor_connecting_borders = set()
        anchor_tile = tiles[id]
        for tile_id, tile in tiles.items():
            if tile_id != anchor_tile.id:
                for i in range(8):
                    for j in range(8):
                        if anchor_tile.borders[i] == tile.borders[j]:
                            anchor_connecting_borders.add(i)
        if set([1, 2]) - anchor_connecting_borders == set():
            print("Anchor tile:", anchor_tile.id)
            return anchor_tile


leftmost_tile = current_tile = find_anchor_tile(twos)
n_tiles = len(tiles)
image_block_dim = int(math.sqrt(n_tiles))
image = remove_border(leftmost_tile.data)

for row in range(image_block_dim):
    if row != 0:
        leftmost_tile, tile_data = find_tile_below(leftmost_tile)
        current_tile = leftmost_tile
        for image_row in remove_border(tile_data):
            image.append(image_row)
    for col in range(image_block_dim - 1):
        current_tile, tile_data = find_tile_to_right(current_tile)
        image = add_tile_to_image(image, remove_border(tile_data), row)


def sea_monster_count(im):
    dim = len(im)
    c_monsters = 0
    monster = '#' * 15
    for r in range(2, dim):
        for c in range(0, dim - 20):
            chars = im[r-1][c] + im[r][c+1] +\
                      im[r][c+4] + im[r-1][c+5] + im[r-1][c+6] + im[r][c+7] +\
                      im[r][c+10] + im[r-1][c+11] + im[r-1][c+12] + im[r][c+13] +\
                      im[r][c+16] + im[r-1][c+17] + im[r-1][c+18] + im[r-2][c+18] + im[r-1][c+19]
            if chars == monster:
                c_monsters += 1
    return c_monsters


max_monsters = 0
for permutation in generate_permutations(image):
    # pretty_print(permutation)
    c_monsters = sea_monster_count(permutation)
    print(c_monsters)
    max_monsters = max(max_monsters, c_monsters)

c_on = 0
for row in image:
    c_on += row.count('#')
print(c_on - (15 * max_monsters))