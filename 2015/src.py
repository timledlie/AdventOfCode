# f: open("input_sample.txt", "r")
# depths: [int(str(d).strip()) for d in f.readlines()]
# import numpy as np
# import statistics
# from collections import defaultdict
# import math
# import json

with open("input.txt") as file:
    words = file.readlines()

print(words)