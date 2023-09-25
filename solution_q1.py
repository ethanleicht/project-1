import random
import heapq
import math


def read(filepath):
    with open(filepath,'r') as file:
        for line in file:
            initial_str = line.strip().split(',')
    initial_lst = [0 if i=='_' else int(i) for i in initial_str]
    return initial_lst



# Function to print the current state of the puzzle as a string
def print_puzzle(state):
    state_str = ','.join(map(str, state)).replace('0', '_')
    print(state_str)



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



# Function to solve the 8-puzzle using random moves
def dfs(initial, goal):
    state = initial[:]
    path = ''
    node_expansions = 0

    while state != goal:
        empty_index = state.index(0)
        possible_moves = find_possible_moves(empty_index)
        node_expansions += len(possible_moves)

        move, dir = random.choice(possible_moves)

        path += (str(state[move]) + dir + ',')
        state[empty_index], state[move] = state[move], state[empty_index]

    print(path[:-1])
    print('Node expansions:', node_expansions)



# Define the BFS function to solve the puzzle
def bfs(initial, goal):
    queue = [(initial[:], '')]
    visited = set()
    node_expansions = 0

    while queue:
        state, path = queue.pop(0)
        
        if state == goal:
            print(path[:-1])
            print('Node expansions:', node_expansions)
            break

        empty_index = state.index(0)
        possible_moves = find_possible_moves(empty_index)
        node_expansions += len(possible_moves)

        visited.add(tuple(state))

        for move, dir in possible_moves:
            new_state = state[:]
            new_state[empty_index], new_state[move] = new_state[move], new_state[empty_index]
            if tuple(new_state) not in visited:
                queue.append((new_state, path + str(state[move]) + dir + ','))
   


# Define the UCS function to solve the puzzle
def ucs(initial, goal):
    visited = set()
    queue = [(0, initial[:], '')]  # Priority queue with cost
    node_expansions = 0  # Counter to track node expansions

    while queue:
        cost, state, path = heapq.heappop(queue)  # Get the state with the lowest cost

        # Increment the node expansions count for each possible move
        empty_index = state.index(0)
        possible_moves = find_possible_moves(empty_index)
        node_expansions += len(possible_moves)

        if state == goal:
            print(path[:-1])
            print('Node expansions:', node_expansions)

        visited.add(tuple(state))

        for move, dir in possible_moves:
            new_state = state[:]
            new_state[empty_index], new_state[move] = new_state[move], new_state[empty_index]
            if tuple(new_state) not in visited:
                heapq.heappush(queue, (cost + 1, new_state, path + str(state[move]) + dir + ','))  # Add new state to the queue



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

def a_star(initial, goal, heuristic):
    visited = set()
    queue = [(0 + heuristic(initial[:]), initial, '')]  # Priority queue with cost and heuristic
    node_expansions = 0  # Counter to track node expansions

    while queue:
        cost, state, path = heapq.heappop(queue)  # Get the state with the lowest cost + heuristic

        # Increment the node expansions count for each possible move
        empty_index = state.index(0)
        possible_moves = find_possible_moves(empty_index)
        node_expansions += len(possible_moves)

        if state == goal:
            print(path[:-1])
            print('Node expansions:', node_expansions)

        visited.add(tuple(state))

        for move, dir in possible_moves:
            new_state = state[:]
            new_state[empty_index], new_state[move] = new_state[move], new_state[empty_index]
            if tuple(new_state) not in visited:
                heapq.heappush(queue, (cost + 1 + heuristic(new_state), new_state, path + str(state[move]) + dir + ','))  # Add new state to the queue



if __name__ == '__main__':
    # Input initial state as a list
    initial = read('input.txt')
    print('Initial state:', initial)
    print()
    
    # Define the goal state
    goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]  # 0 represents the empty tile
    
    print('The solution of Q1.1 (DFS) is:')
    dfs(initial, goal)
    print()
    
    print('The solution of Q1.2 (BFS) is:')
    bfs(initial, goal)
    print()

    print('The solution of Q1.2 (UCS) is:')
    ucs(initial, goal)
    print()

    print('The solution of Q1.2 (A* Manhattan Distance) is:')
    a_star(initial, goal, manhattan_distance)
    print()

    print('The solution of Q1.2 (A* Straight Line Distance) is:')
    a_star(initial, goal, straight_line_distance)
    print()


