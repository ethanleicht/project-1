import random
import heapq
import math


def read(filepath):
    with open(filepath, 'r') as file:
        for line in file:
            initial_str = line.strip().split(',')
    initial_lst = [0 if i == '_' else int(i) for i in initial_str]
    return initial_lst


def find_possible_moves(empty_index):
    possible_moves = []

    # Define the possible moves (left, right, up down)
    if empty_index % 3 != 0:
        possible_moves.append((empty_index - 1, 'R'))

    if empty_index % 3 != 2:
        possible_moves.append((empty_index + 1, 'L'))

    if empty_index >= 3:
        possible_moves.append((empty_index - 3, 'D'))

    if empty_index < 6:
        possible_moves.append((empty_index + 3, 'U'))

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


# Function to solve the modified 8-puzzle using DFS
def dfs_modified(initial):
    stack = [(initial, [])]
    visited = set()
    node_expansions = 0

    while stack:
        state, path = stack.pop()
        node_expansions += 1

        if sum(state[:3]) == 11:
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


# Function to solve the modified 8-puzzle using BFS
def bfs_modified(initial):
    queue = [(initial, [])]
    visited = set()
    node_expansions = 0

    while queue:
        state, path = queue.pop(0)
        node_expansions += 1

        if sum(state[:3]) == 11:
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


# Function to solve the modified 8-puzzle using UCS
def ucs_modified(initial):
    visited = set()
    queue = [(0, initial, [])]  # Priority queue with cost
    node_expansions = 0

    while queue:
        cost, state, path = heapq.heappop(queue)  # Get the state with the lowest cost
        node_expansions += 1

        if sum(state[:3]) == 11:
            return path, node_expansions

        empty_index = state.index(0)
        possible_moves = find_possible_moves(empty_index)

        visited.add(tuple(state))

        for move, dir in possible_moves:
            new_state = state[:]
            new_state[empty_index], new_state[move] = new_state[move], new_state[empty_index]
            if tuple(new_state) not in visited:
                heapq.heappush(queue, (cost + 1, new_state, path + [str(state[move]) + dir]))

    return None, node_expansions


# Function to solve the modified 8-puzzle using A* with Manhattan Distance Heuristic
def a_star_manhattan_modified(initial):
    visited = set()
    queue = [(0 + manhattan_distance(initial), initial, [])]  # Priority queue with cost and heuristic
    node_expansions = 0

    while queue:
        cost, state, path = heapq.heappop(queue)  # Get the state with the lowest cost + heuristic
        node_expansions += 1

        if sum(state[:3]) == 11:
            return path, node_expansions

        empty_index = state.index(0)
        possible_moves = find_possible_moves(empty_index)

        visited.add(tuple(state))

        for move, dir in possible_moves:
            new_state = state[:]
            new_state[empty_index], new_state[move] = new_state[move], new_state[empty_index]
            if tuple(new_state) not in visited:
                heapq.heappush(queue, (cost + 1 + manhattan_distance(new_state), new_state, path + [str(state[move]) + dir]))

    return None, node_expansions


# Function to solve the modified 8-puzzle using A* with Straight Line Distance Heuristic
def a_star_straight_line_modified(initial):
    visited = set()
    queue = [(0 + straight_line_distance(initial), initial, [])]  # Priority queue with cost and heuristic
    node_expansions = 0

    while queue:
        cost, state, path = heapq.heappop(queue)  # Get the state with the lowest cost + heuristic
        node_expansions += 1

        if sum(state[:3]) == 11:
            return path, node_expansions

        empty_index = state.index(0)
        possible_moves = find_possible_moves(empty_index)

        visited.add(tuple(state))

        for move, dir in possible_moves:
            new_state = state[:]
            new_state[empty_index], new_state[move] = new_state[move], new_state[empty_index]
            if tuple(new_state) not in visited:
                heapq.heappush(queue, (cost + 1 + straight_line_distance(new_state), new_state, path + [str(state[move]) + dir]))

    return None, node_expansions


if __name__ == '__main__':
    #initial = read('input.txt')
    initial = [1,4,2,3,0,5,6,7,8]
    print('Initial state:', initial)
    print()

    # Call the modified 8-puzzle solving functions
    dfs_path, dfs_expansions = dfs_modified(initial)
    bfs_path, bfs_expansions = bfs_modified(initial)
    ucs_path, ucs_expansions = ucs_modified(initial)
    a_star_manhattan_path, a_star_manhattan_expansions = a_star_manhattan_modified(initial)
    a_star_straight_line_path, a_star_straight_line_expansions = a_star_straight_line_modified(initial)

    # Print the paths and node expansions
    if dfs_path:
        print('The solution of Q2.1(DFS) is:\n', ','.join(dfs_path))
        print('DFS Node expansions:', dfs_expansions, '\n\n')
    else:
        print('DFS: No solution found.')

    if bfs_path:
        print('The solution of Q2.2(BFS) is:\n', ','.join(bfs_path))
        print('BFS Node expansions:', bfs_expansions,'\n\n')
    else:
        print('BFS: No solution found.')

    if ucs_path:
        print('The solution of Q2.3 (UCS) is:\n', ','.join(ucs_path))
        print('UCS Node expansions:', ucs_expansions, "\n\n")
    else:
        print('UCS: No solution found.')

    if a_star_manhattan_path:
        print('The solution of Q2.4 (A* Manhatan search) is:\n', ','.join(a_star_manhattan_path))
        print('A* with Manhattan Distance Node expansions:', a_star_manhattan_expansions, '\n\n')
    else:
        print('A* with Manhattan Distance: No solution found.')

    if a_star_straight_line_path:
        print('The solution of Q2.5 (A* Straight line search) is:\n', ','.join(a_star_straight_line_path))
        print('A* with Straight Line Distance Node expansions:', a_star_straight_line_expansions)
    else:
        print('A* with Straight Line Distance: No solution found.')
