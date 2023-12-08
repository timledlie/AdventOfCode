# f: open("input_sample.txt", "r")
# depths: [int(str(d).strip()) for d in f.readlines()]
# import numpy as np
# import statistics
from collections import defaultdict
# import math
# import json
import copy

image = []
with open("input.txt") as file:
    lines = file.readlines()
    algorithm = lines[0].strip()
    for line in lines[2:]:
        image.append([1 if c == '#' else 0 for c in line.strip()])


def render_image(image):
    print()
    for i in range(len(image)):
        for j in range(len(image)):
            print("#" if image[i][j] else ".", sep='', end='')
        print()


def pad_image(image, pad_char, pad_amount):
    padded_dim = len(image) + pad_amount * 2
    padded_image = [[pad_char for i in range(padded_dim)] for j in range(padded_dim)]
    for i in range(len(image)):
        for j in range(len(image)):
            padded_image[i+pad_amount][j+pad_amount] = image[i][j]
    return padded_image


def calculate_output_pixel(input_image, i, j):
    bit_string = ''.join([str(bit) for bit in input_image[i-1][j-1:j+2]]) + ''.join([str(bit) for bit in input_image[i][j-1:j+2]]) + ''.join([str(bit) for bit in input_image[i+1][j-1:j+2]])
    return 1 if algorithm[int(bit_string, 2)] == '#' else 0


def enhance(image, pad_bit):
    image = pad_image(image, pad_bit, 3)
    output_image = copy.deepcopy(image)
    for i in range(1, len(image) - 1):
        for j in range(1, len(image) - 1):
            output_image[i][j] = calculate_output_pixel(image, i, j)
    trimmed_output_image = [[0 for i in range(len(image) - 2)] for j in range(len(image) - 2)]
    for i in range(1, len(output_image) - 1):
        for j in range(1, len(output_image) - 1):
            trimmed_output_image[i-1][j-1] = output_image[i][j]
    return trimmed_output_image


def pixel_count(image):
    count = 0
    for i in range(len(image)):
        for j in range(len(image)):
            if image[i][j]:
                count += 1
    return count


render_image(image)

n_enhancements = 50
for i in range(n_enhancements):
    image = enhance(image, i % 2)
    render_image(image)
print(pixel_count(image))