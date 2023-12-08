def print_board(board):
    for line in board:
        for c in line:
            print('{0: <1}'.format(str(c)), end='')
        print()


with open("input.txt") as file:
    text = file.read()

board_text, path_text = text.split("\n\n")

path_text = path_text + "\n"
path = []
i = 0
while True:
    if path_text[i:i+2].isdigit():
        path.append(int(path_text[i:i+2]))
        i += 2
    else:
        path.append(int(path_text[i:i+1]))
        i += 1
    if path_text[i] == "\n":
        break
    path.append(path_text[i:i+1])
    i += 1

board_prelim = [list(line) for line in board_text.split("\n")]

max_line_len = 0
for line in board_prelim:
    max_line_len = max(max_line_len, len(line))

board = []
board.append([' ', ' '] + [' '] * max_line_len)
for line in board_prelim:
    board.append([' '] + line + [' '] * (max_line_len - len(line) + 1))
board.append([' ', ' '] + [' '] * max_line_len)

# for row in range(len(board)):
#     is_inside = False
#     for col in range(len(board[0])):
#         if not is_inside and (board[row][col] in ('.', '#')):
#             is_inside = True
#             start = col
#         elif is_inside and (board[row][col] not in ('.', '#')):
#             end = col - 1
#             board[row][start - 1] = [end, None]
#             board[row][end + 1] = [start, None]
#             break
#
# for col in range(len(board[0])):
#     is_inside = False
#     for row in range(len(board)):
#         if not is_inside and (board[row][col] in ('.', '#')):
#             is_inside = True
#             start = row
#         elif is_inside and (board[row][col] not in ('.', '#')):
#             end = row - 1
#             if isinstance(board[start - 1][col], list):
#                 board[start - 1][col][1] = end
#             else:
#                 board[start - 1][col] = [None, end]
#             if isinstance(board[end + 1][col], list):
#                 board[end + 1][col][1] = start
#             else:
#                 board[end + 1][col] = [None, start]
#             break

dim = 50
for i in range(dim):
    board[0][51 + i] = {}
    board[0][101 + i] = {}
    board[1 + i][151] = {}
    board[51][101 + i] = {}
    board[51 + i][101] = {}
    board[101 + i][101] = {}
    board[151][51 + i] = {}
    board[151 + i][51] = {}
    board[201][1 + i] = {}
    board[101 + i][0] = {}
    board[151 + i][0] = {}
    board[100][1 + i] = {}
    board[1 + i][50] = {}
    board[51 + i][50] = {}

    board[0][51 + i][3] = (151 + i, 1, 0)
    board[0][101 + i][3] = (200, 1 + i, 3)
    board[1 + i][151][0] = (150 - i, 100, 2)
    board[51][101 + i][1] = (51 + i, 100, 2)
    board[51 + i][101][0] = (50, 101 + i, 3)
    board[101 + i][101][0] = (50 - i, 150, 2)
    board[151][51 + i][1] = (151 + i, 50, 2)
    board[151 + i][51][0] = (150, 51 + i, 3)
    board[201][1 + i][1] = (1, 101 + i, 1)
    board[101 + i][0][2] = (50 - i, 51, 0)
    board[151 + i][0][2] = (1, 51 + i, 1)
    board[100][1 + i][3] = (51 + i, 51, 0)
    board[1 + i][50][2] = (150 - i, 1, 0)
    board[51 + i][50][2] = (101, 1 + i, 1)

    # board[1 + i][13][0] = (12 - i, 16, 3)
    # board[5 + i][13][0] = (9, 16 - i, 1)
    # board[8][13 + i][3] = (8 - i, 12, 2)
    # board[9 + i][17][0] = (4 - i, 12, 2)
    # board[13][9 + i][1] = (8, 4 - i, 3)
    # board[13][13 + i][1] = (8 - i, 1, 0)
    # board[9 + i][8][2] = (8, 8 - i, 3)
    # board[9][1 + i][1] = (12, 12 - i, 3)
    # board[9][5 + i][1] = (12 - i, 9, 0)
    # board[5 + i][0][2] = (12, 16 - i, 3)
    # board[4][1 + i][3] = (1, 12 - i, 1)
    # board[4][5 + i][3] = (1 + i, 9, 0)
    # board[1 + i][8][2] = (5, 5 + i, 1)
    # board[0][9 + i][3] = (5, 4 - i, 1)

location = [1, 51]
# location = [1, 9]
orientation = 0

for step in path:
    if isinstance(step, str):
        if step == "R":
            orientation = (orientation + 1) % 4
        else:
            orientation -= 1
            if orientation == -1:
                orientation = 3
    else:
        for i in range(step):
            if orientation == 0:
                location[1] += 1
                cur_tile = board[location[0]][location[1]]
                if cur_tile == '#':
                    location[1] -= 1
                    break
                elif isinstance(cur_tile, dict):
                    if board[cur_tile[orientation][0]][cur_tile[orientation][1]] == '#':
                        location[1] -= 1
                        break
                    else:
                        location = [cur_tile[orientation][0], cur_tile[orientation][1]]
                        orientation = cur_tile[orientation][2]
            elif orientation == 1:
                location[0] += 1
                cur_tile = board[location[0]][location[1]]
                if cur_tile == '#':
                    location[0] -= 1
                    break
                elif isinstance(cur_tile, dict):
                    if board[cur_tile[orientation][0]][cur_tile[orientation][1]] == '#':
                        location[0] -= 1
                        break
                    else:
                        location = [cur_tile[orientation][0], cur_tile[orientation][1]]
                        orientation = cur_tile[orientation][2]
            elif orientation == 2:
                location[1] -= 1
                cur_tile = board[location[0]][location[1]]
                if cur_tile == '#':
                    location[1] += 1
                    break
                elif isinstance(cur_tile, dict):
                    if board[cur_tile[orientation][0]][cur_tile[orientation][1]] == '#':
                        location[1] += 1
                        break
                    else:
                        location = [cur_tile[orientation][0], cur_tile[orientation][1]]
                        orientation = cur_tile[orientation][2]
            elif orientation == 3:
                location[0] -= 1
                cur_tile = board[location[0]][location[1]]
                if cur_tile == '#':
                    location[0] += 1
                    break
                elif isinstance(cur_tile, dict):
                    if board[cur_tile[orientation][0]][cur_tile[orientation][1]] == '#':
                        location[0] += 1
                        break
                    else:
                        location = [cur_tile[orientation][0], cur_tile[orientation][1]]
                        orientation = cur_tile[orientation][2]

print(location, orientation)
print(1000 * location[0] + 4 * location[1] + orientation)