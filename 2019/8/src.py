# from collections import defaultdict
# from collections import namedtuple
# PasswordCheck = namedtuple('PasswordCheck', ['span', 'letter', 'password'])
# import itertools
# import copy

with open("input.txt") as file:
    pixels = file.read().strip()

# width, height = 2, 2
width, height = 25, 6
pixels_per_layer = width * height
output_image = ''
for i in range(pixels_per_layer):
    for layer in range(len(pixels) // pixels_per_layer):
        pixel = pixels[layer * pixels_per_layer + i]
        if pixel != '2':
            output_image = output_image + pixel
            break
output_image = output_image.replace('0', ' ')
for row in range(height):
    print(output_image[row * width: (row + 1) * width])