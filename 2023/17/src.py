import heapq
import itertools

infinity = 100000000000000000000


# modeled after https://docs.python.org/3/library/heapq.html#priority-queue-implementation-notes
# allows for updating the priority of an existing task by marking it as "removed" and re-adding it with new priority
class PriorityQueue:
    REMOVED = '<removed-task>'

    def __init__(self):
        self.pq = []
        self.entry_finder = {}
        self.counter = itertools.count()

    def empty(self):
        while self.pq:
            if self.pq[0][-1] == self.REMOVED:
                heapq.heappop(self.pq)
            else:
                break
        return not self.pq

    def add(self, task, priority):
        if task in self.entry_finder:
            self.remove(task)
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heapq.heappush(self.pq, entry)

    def remove(self, task):
        entry = self.entry_finder.pop(task)
        entry[-1] = self.REMOVED

    def pop(self):
        while self.pq:
            priority, count, task = heapq.heappop(self.pq)
            if task is not self.REMOVED:
                del self.entry_finder[task]
                return task
        raise KeyError('pop from an empty priority queue')


def add_step(previous_moves, next_direction):
    count, direction = previous_moves
    # can't reverse direction
    if (direction == "up" and next_direction == "down") or \
       (direction == "down" and next_direction == "up") or \
       (direction == "right" and next_direction == "left") or \
       (direction == "left" and next_direction == "right"):
        return None
    if direction == next_direction:
        # can't go more than 3 steps in the same direction
        if count == 3:
            return None
        return count + 1, direction
    return 1, next_direction


def get_neighbors(coords):
    r, c = coords
    neighbors = [("up", (r - 1, c)), ("right", (r, c + 1)), ("down", (r + 1, c)), ("left", (r, c - 1))]
    return list(filter(lambda point: 0 <= point[1][0] < n_rows and 0 <= point[1][1] < n_cols, neighbors))


def prior_steps_defaults():
    defaults = {}
    for count, direction in itertools.product((1, 2, 3), ("up", "right", "down", "left")):
        defaults[(count, direction)] = infinity
    return defaults


grid_costs = {}
lowest_cost_after_prior_steps = {}
lowest_cost_overall = {}
with open("input.txt") as file:
    lines = file.readlines()
    n_rows, n_cols = len(lines), len(lines[0].strip())
    for row_index in range(n_rows):
        line = lines[row_index].strip()
        for col_index in range(n_cols):
            coords = row_index, col_index
            grid_costs[(coords)] = int(line[col_index])
            lowest_cost_after_prior_steps[(coords)] = prior_steps_defaults()
            lowest_cost_overall[(coords)] = infinity


start = (0, 0)
goal = (n_rows - 1, n_cols - 1)

for count, direction in lowest_cost_after_prior_steps[start]:
    lowest_cost_after_prior_steps[start][count, direction] = 0
lowest_cost_overall[start] = 0

frontier = PriorityQueue()
frontier.add((0, 0), 0)

while not frontier.empty():
    current = frontier.pop()
    if current == goal:
        print(lowest_cost_overall[current])
        break

    for direction, next_node in get_neighbors(current):
        is_any_changes = False
        for prior_steps, lowest_cost in lowest_cost_after_prior_steps[current].items():

            prior_steps_next = add_step(prior_steps, direction)
            if prior_steps_next is None:
                continue

            cost_next_candidate = lowest_cost + grid_costs[next_node]
            cost_next_lowest = lowest_cost_after_prior_steps[next_node][prior_steps_next]
            if cost_next_candidate < cost_next_lowest:
                is_any_changes = True
                lowest_cost_after_prior_steps[next_node][prior_steps_next] = cost_next_candidate
                if cost_next_candidate < lowest_cost_overall[next_node]:
                    lowest_cost_overall[next_node] = cost_next_candidate

        if is_any_changes:
            frontier.add(next_node, lowest_cost_overall[next_node])
