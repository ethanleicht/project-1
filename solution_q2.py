import math
import heapq
from collections import deque

def read(filepath):
    with open(filepath,'r') as file:
        for line in file:
            initial_str = line.strip().split(',')
    initial_lst = [0 if i=='_' else int(i) for i in initial_str]
    return initial_lst



def find_possible_moves(empty_index):
    possible_moves = []

    # Define the possible moves (left, right, up down)
    if empty_index % 3 != 0:
        possible_moves.append((empty_index - 1, 'L'))

    if empty_index % 3 != 2:
        possible_moves.append((empty_index + 1, 'R'))

    if empty_index >= 3:
        possible_moves.append((empty_index - 3, 'U'))

    if empty_index < 6:
        possible_moves.append((empty_index + 3, 'D'))

    return possible_moves

# Function to calculate the Manhattan distance heuristic
def manhattan_distance(state):
    total_distance = 0
    for i in range(9):
        if state[i] != 0:
            target_row, target_col = divmod(state[i] - 1, 3)
            current_row, current_col = divmod(i, 3)
            total_distance += abs(target_row - current_row) + abs(target_col - current_col)
    return total_distance

def straight_line_distance(state):
    total_distance = 0
    for i in range(9):
        if state[i] != 0:
            target_row, target_col = divmod(state[i] - 1, 3)
            current_row, current_col = divmod(i, 3)
            distance = math.sqrt((target_row - current_row) ** 2 + (target_col - current_col) ** 2)
            total_distance += distance
    return total_distance

def is_goal(state):
    top_row = state[:3]
    return sum(num for num in top_row if num is not None) == 11

def bfs_modified(initial):
    queue = deque([(initial, [])])
    visited = set()
    node_expansions = 0

    while queue:
        state, path = queue.popleft()
        node_expansions += 1

        if is_goal(state):
            return path, node_expansions

        empty_index = state.index(0)
        possible_moves = find_possible_moves(empty_index)

        visited.add(tuple(state))

        for move, dir in possible_moves:
            new_state = state[:]
            new_state[empty_index], new_state[move] = new_state[move], new_state[empty_index]
            if tuple(new_state) not in visited:
                queue.append((new_state, path + [str(state[move]) + dir]))

    return None, node_expansions

def dfs_modified(initial):
    stack = [(initial, [])]
    visited = set()
    node_expansions = 0

    while stack:
        state, path = stack.pop()
        node_expansions += 1

        if is_goal(state):
            return path, node_expansions

        empty_index = state.index(0)
        possible_moves = find_possible_moves(empty_index)

        visited.add(tuple(state))

        for move, dir in possible_moves:
            new_state = state[:]
            new_state[empty_index], new_state[move] = new_state[move], new_state[empty_index]
            if tuple(new_state) not in visited:
                stack.append((new_state, path + [str(state[move]) + dir]))

    return None, node_expansions

def ucs_modified(initial):
    heap = [(0, initial, [])]
    visited = set()
    node_expansions = 0

    while heap:
        cost, state, path = heapq.heappop(heap)
        node_expansions += 1

        if is_goal(state):
            return path, node_expansions

        empty_index = state.index(0)
        possible_moves = find_possible_moves(empty_index)

        visited.add(tuple(state))

        for move, dir in possible_moves:
            new_state = state[:]
            new_state[empty_index], new_state[move] = new_state[move], new_state[empty_index]
            if tuple(new_state) not in visited:
                heapq.heappush(heap, (cost + 1, new_state, path + [str(state[move]) + dir]))

    return None, node_expansions

def a_star_modified(initial, heuristic):
    heap = [(heuristic(initial), initial, [])]
    visited = set()
    node_expansions = 0

    while heap:
        _, state, path = heapq.heappop(heap)
        node_expansions += 1

        if is_goal(state):
            return path, node_expansions

        empty_index = state.index(0)
        possible_moves = find_possible_moves(empty_index)

        visited.add(tuple(state))

        for move, dir in possible_moves:
            new_state = state[:]
            new_state[empty_index], new_state[move] = new_state[move], new_state[empty_index]
            if tuple(new_state) not in visited:
                heapq.heappush(heap, (heuristic(new_state) + len(path) + 1, new_state, path + [str(state[move]) + dir]))

    return None, node_expansions

if __name__ == '__main__':
    initial = read('input.txt')
    #initial = [1, 4, 2, 3, 0, 5, 6, 7, 8]
    print('Initial state:', initial)
    print()

    # Call the modified 8-puzzle solving functions
    bfs_path, bfs_expansions = bfs_modified(initial)
    dfs_path, dfs_expansions = dfs_modified(initial)
    ucs_path, ucs_expansions = ucs_modified(initial)
    a_star_manhattan_path, a_star_manhattan_expansions = a_star_modified(initial, manhattan_distance)
    a_star_straight_line_path, a_star_straight_line_expansions = a_star_modified(initial, straight_line_distance)

    if dfs_path:
        print('The solution of Q2.1(DFS) is:\n', ','.join(dfs_path))
        print('DFS Node expansions:', dfs_expansions, '\n\n')
    else:
        print('DFS: No solution found.')
    if bfs_path:
        print('The solution of Q2.2(BFS) is:\n', ','.join(bfs_path))
        print('BFS Node expansions:', bfs_expansions, '\n')

    if ucs_path:
        print('The solution of Q2.3 (UCS) is:\n', ','.join(ucs_path))
        print('UCS Node expansions:', ucs_expansions, '\n')

    if a_star_manhattan_path:
        print('The solution of Q2.4 (A* Manhattan search) \n', ','.join(a_star_manhattan_path))
        print('A* (Manhattan) Node expansions:', a_star_manhattan_expansions, '\n')

    if a_star_straight_line_path:
        print('The solution of Q2.5 (A* Straight line search) \n', ','.join(a_star_straight_line_path))
        print('A* (Straight Line) Node expansions:', a_star_straight_line_expansions, '\n')
