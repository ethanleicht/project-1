import math
import heapq
from collections import deque


# Function to read input file
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
        possible_moves.append((empty_index - 1, 'R'))

    if empty_index % 3 != 2:
        possible_moves.append((empty_index + 1, 'L'))

    if empty_index >= 3:
        possible_moves.append((empty_index - 3, 'D'))

    if empty_index < 6:
        possible_moves.append((empty_index + 3, 'U'))

    return possible_moves


# Function to calculate the Manhattan distance heuristic
def manhattan_distance(state, goal):
    total_distance = 0
    for i in range(9):
        if state[i] != 0:
            target_row, target_col = divmod(goal[state[i]], 3)
            current_row, current_col = divmod(i, 3)
            total_distance += abs(target_row - current_row) + abs(target_col - current_col)
    return total_distance

# Function to calculate the straight line distance heuristic
def straight_line_distance(state, goal):
    total_distance = 0
    for i in range(9):
        if state[i] != 0:
            target_row, target_col = divmod(goal[state[i]], 3)
            current_row, current_col = divmod(i, 3)
            distance = math.sqrt((target_row - current_row) ** 2 + (target_col - current_col) ** 2)
            total_distance += distance
    return total_distance

# Define the DFS function to solve the puzzle
def dfs(initial, goal):
    stack = [(initial, [])]
    visited = set()
    node_expansions = 0

    while stack:
        state, path = stack.pop()
        node_expansions += 1

        if state == goal:
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


# Define the BFS function to solve the puzzle
def bfs(initial, goal):
    queue = deque([(initial, [])])
    visited = set()
    node_expansions = 0

    while queue:
        state, path = queue.popleft()
        node_expansions += 1

        if state == goal:
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

# Define the UCS function to solve the puzzle
def ucs(initial, goal):
    heap = [(0, initial, [])]
    visited = set()
    node_expansions = 0 # Counter to track node expansions

    while heap:
        cost, state, path = heapq.heappop(heap) # Get the state with the lowest cost
        node_expansions += 1

        if state == goal:
            return path, node_expansions

        empty_index = state.index(0)
        possible_moves = find_possible_moves(empty_index)

        visited.add(tuple(state))

        for move, dir in possible_moves:
            new_state = state[:]
            new_state[empty_index], new_state[move] = new_state[move], new_state[empty_index]
            if tuple(new_state) not in visited:
                heapq.heappush(heap, (cost + 1, new_state, path + [str(state[move]) + dir])) # Add new state to the queue
    return None, node_expansions

def a_star(initial, goal, heuristic):
    heap = [(heuristic(initial, goal), initial, [])]
    visited = set()
    node_expansions = 0 # Counter to track node expansions

    while heap:
        _, state, path = heapq.heappop(heap) # Get the state with the lowest cost + heuristic
        node_expansions += 1

        if state == goal:
            return path, node_expansions

        empty_index = state.index(0)
        possible_moves = find_possible_moves(empty_index)

        visited.add(tuple(state))

        for move, dir in possible_moves:
            new_state = state[:]
            new_state[empty_index], new_state[move] = new_state[move], new_state[empty_index]
            if tuple(new_state) not in visited:
                heapq.heappush(heap, (heuristic(new_state, goal) + len(path) + 1, new_state, path + [str(state[move]) + dir]))# Add new state to the queue

    return None, node_expansions


if __name__ == '__main__':
    # Input initial state as a list
    initial = read('input.txt')
    goal = [0, 1, 2, 3, 4, 5, 6, 7, 8] # ) represents the empty tile
    print()

    # Call the modified 8-puzzle solving functions
    dfs_path, dfs_expansions = dfs(initial, goal)
    bfs_path, bfs_expansions = bfs(initial, goal)
    ucs_path, ucs_expansions = ucs(initial, goal)
    a_star_manhattan_path, a_star_manhattan_expansions = a_star(initial, goal, manhattan_distance)
    a_star_straight_line_path, a_star_straight_line_expansions = a_star(initial, goal, straight_line_distance)

    if dfs_path:
        print('The solution of Q1.1(DFS) is:\n', ','.join(dfs_path))
        print('DFS Node expansions:', dfs_expansions, '\n\n')
    else:
        print('DFS: No solution found.')
    if bfs_path:
        print('The solution of Q1.2(BFS) is:\n', ','.join(bfs_path))
        print('BFS Node expansions:', bfs_expansions, '\n')

    if ucs_path:
        print('The solution of Q1.3 (UCS) is:\n', ','.join(ucs_path))
        print('UCS Node expansions:', ucs_expansions, '\n')

    if a_star_manhattan_path:
        print('The solution of Q1.4 (A* Manhattan search) \n', ','.join(a_star_manhattan_path))
        print('A* (Manhattan) Node expansions:', a_star_manhattan_expansions, '\n')

    if a_star_straight_line_path:
        print('The solution of Q1.5 (A* Straight line search) \n', ','.join(a_star_straight_line_path))
        print('A* (Straight Line) Node expansions:', a_star_straight_line_expansions, '\n')
