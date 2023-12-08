class Square:
    def __init__(self, row, col, height):
        self.row = row
        self.col = col
        self.height = height
        self.distance = 100000000


row, col = 0, 0
start, end = None, None
grid = []
with open("input.txt") as file:
    for line in file.readlines():
        row_squares = []
        for char in line.strip():
            if char == 'S':
                start = row, col
                char = 'a'
            elif char == 'E':
                end = row, col
                char = 'z'
            row_squares.append(Square(row, col, ord(char) - 96))
            col += 1
        grid.append(row_squares)
        row += 1
        col = 0


def get_adjacent_squares(grid, row, col):
    adjacent_squares = []
    for r, c in ((row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)):
        if (0 <= r < len(grid)) and (0 <= c < len(grid[0])):
            adjacent_squares.append(grid[r][c])
    return adjacent_squares


grid[end[0]][end[1]].distance = 0
to_process = [grid[end[0]][end[1]]]
while True:
    current_square = to_process.pop(0)
    print("Processing", current_square.row, current_square.col, current_square.height)
    # if current_square.row == start[0] and current_square.col == start[1]:
    if current_square.height == 1:
        print(current_square.distance)
        break
    for adjacent_square in get_adjacent_squares(grid, current_square.row, current_square.col):
        if (adjacent_square.height >= current_square.height - 1) and\
                (adjacent_square.distance > current_square.distance + 1):
            adjacent_square.distance = current_square.distance + 1
            to_process.append(adjacent_square)

print("Done!")