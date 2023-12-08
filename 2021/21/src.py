# f: open("input_sample.txt", "r")
# depths: [int(str(d).strip()) for d in f.readlines()]
# import numpy as np
# import statistics
from collections import defaultdict
# import math
# import json
# import copy

# starting_positions = {1: 4, 2: 8}
starting_positions = {1: 3, 2: 4}
# scores = {1: 0, 2: 0}
# n_rolls = 0
# end_score = 1000
which_players_turn = 1

game_state_counts = defaultdict(int)
game_state_counts[str(starting_positions[1]) + " 0 " + str(starting_positions[2]) + " 0"] = 1
print(game_state_counts)

def is_ongoing_games():
    for game_state, n in game_state_counts.items():
        p1, s1, p2, s2 = game_state.split()
        if n > 0 and s1 != '21' and s2 != '21':
            return True
    return False


# deterministic_die = 1
# def roll_once():
#     global deterministic_die
#     roll = deterministic_die
#     deterministic_die += 1
#     if deterministic_die == 101:
#         deterministic_die = 1
#     return roll
#
#
# def roll_sum():
#     return roll_once() + roll_once() + roll_once()


def move_player(from_position, amount):
    new_position = from_position + (amount % 10)
    if new_position > 10:
        new_position = new_position - 10
    return new_position


move_map = {}
for from_position in range(1, 11):
    for amount in range(3, 10):
        move_map[(from_position, amount)] = move_player(from_position, amount)

moves_in_round = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}

while is_ongoing_games():
    game_state_counts_next = game_state_counts.copy()
    for game_state, n in game_state_counts.items():
        p1, s1, p2, s2 = game_state.split()
        if s1 == "21" or s2 == "21":
            continue
        if which_players_turn == 1:
            for move_amount, move_count in moves_in_round.items():
                new_position = move_map[(int(p1), move_amount)]
                new_score = min(21, int(s1) + new_position)
                new_game_state = str(new_position) + " " + str(new_score) + " " + p2 + " " + s2
                game_state_counts_next[new_game_state] += n * move_count
            game_state_counts_next[game_state] -= n
        else:
            for move_amount, move_count in moves_in_round.items():
                new_position = move_map[(int(p2), move_amount)]
                new_score = min(21, int(s2) + new_position)
                new_game_state = p1 + " " + s1 + " " + str(new_position) + " " + str(new_score)
                game_state_counts_next[new_game_state] += n * move_count
            game_state_counts_next[game_state] -= n
    game_state_counts = game_state_counts_next
    which_players_turn = 2 if which_players_turn == 1 else 1

player_1_wins = player_2_wins = 0
for game_state, n in game_state_counts.items():
    p1, s1, p2, s2 = game_state.split()
    if s1 == "21":
        player_1_wins += n
    elif s2 == "21":
        player_2_wins += n
print(player_1_wins)
print(player_2_wins)

# while scores[1] < end_score and scores[2] < end_score:
#     scores[which_players_turn] += move_player(roll_sum(), which_players_turn)
#     n_rolls += 3
#     which_players_turn = 2 if which_players_turn == 1 else 1
#
# print(scores[which_players_turn] * n_rolls)