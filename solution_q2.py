import random
import heapq
from collections import deque
import math

def read(filepath):
    with open(filepath, 'r') as file:
        for line in file:
            initial_str = line.strip().split(',')
    initial_lst = [0 if i == '_' else int(i) for i in initial_str]
    return initial_lst

# Function to print the current state of the puzzle as a string
def print_puzzle(state):
    state_str = ",".join(map(str, state)).replace("0", "_")
    print(state_str)

def find_possible_moves(state, empty_index):
    possible_moves = []

    # Define the possible moves (up, down, left, right)
    if empty_index >= 3:
        possible_moves.append(empty_index - 3)
    if empty_index < 6:
        possible_moves.append(empty_index + 3)
    if empty_index % 3 != 0:
        possible_moves.append(empty_index - 1)
    if empty_index % 3 != 2:
        possible_moves.append(empty_index + 1)
    
    return possible_moves

# Function to check if the current state satisfies the new goal test
def is_goal_state(state):
    top_row_sum = sum(state[:3])
    return top_row_sum == 11

def dfs(initial):
    print("DFS path to solution:")

    state = initial[:]
    moves = 0
    node_expansions = 0  # Counter to track node expansions

    while not is_goal_state(state):  # Check the new goal test
        print_puzzle(state)

        empty_index = state.index(0)
        possible_moves = find_possible_moves(state, empty_index)

        # Increment the node expansions count for each possible move
        node_expansions += len(possible_moves)

        move = random.choice(possible_moves)  # Randomly choose a move
        state[state.index(0)], state[move] = state[move], state[state.index(0)]
        moves += 1

    # Print goal state
    print_puzzle(state)

    # Print the number of node expansions
    print("Node expansions:", node_expansions)
    
def bfs(initial):
    print("BFS path to solution:")
    state = initial
    visited = set()
    queue = deque([(state, [])])  # Use a deque as a FIFO queue
    node_expansions = 0  # Counter to track node expansions

    while queue:
        state, path = queue.popleft()  # Get the first state in the queue
        visited.add(tuple(state))

        # Increment the node expansions count for each possible move
        empty_index = state.index(0)
        possible_moves = find_possible_moves(state, empty_index)
        node_expansions += len(possible_moves)

        # Print the current state if needed
        print_puzzle(state)

        if is_goal_state(state):
            print("Solution found!")
            print("Path to solution:")
            for step in path:
                print_puzzle(step)
            return print("Node expansions:", node_expansions)

        for move in possible_moves:
            new_state = state[:]
            new_state[empty_index], new_state[move] = new_state[move], new_state[empty_index]
            if tuple(new_state) not in visited:
                queue.append((new_state, path + [new_state]))  # Add new state to the queue

    print("No solution found!")


def ucs(initial):
    print("UCS path to solution:")
    state = initial
    visited = set()
    priority_queue = [(0, state, [])]  # Priority queue with cost
    node_expansions = 0  # Counter to track node expansions

    while priority_queue:
        cost, state, path = heapq.heappop(priority_queue)  # Get the state with the lowest cost
        if tuple(state) in visited:
            continue

        # Increment the node expansions count for each possible move
        empty_index = state.index(0)
        possible_moves = find_possible_moves(state, empty_index)
        node_expansions += len(possible_moves)

        # Print the current state if needed
        print_puzzle(state)

        if is_goal_state(state):
            print("Solution found!")
            print("Path to solution:")
            for step in path:
                print_puzzle(step)
            return print("Node expansions:", node_expansions)

        visited.add(tuple(state))

        for move in possible_moves:
            new_state = state[:]
            new_state[empty_index], new_state[move] = new_state[move], new_state[empty_index]
            heapq.heappush(priority_queue, (cost + 1, new_state, path + [new_state]))  # Add new state to the queue

    print("No solution found!")


# Function to calculate the Manhattan distance heuristic
def manhattan_distance(state):
    total_distance = 0
    for i in range(9):
        if state[i] != 0:
            target_row, target_col = divmod(state[i] - 1, 3)
            current_row, current_col = divmod(i, 3)
            total_distance += abs(target_row - current_row) + abs(target_col - current_col)
    return total_distance

def a_star_man(initial):
    print("A* (Manhattan distance) path to solution:")
    state = initial
    visited = set()
    priority_queue = [(0 + manhattan_distance(state), state, [])]  # Priority queue with cost and heuristic
    node_expansions = 0  # Counter to track node expansions

    while priority_queue:
        _, state, path = heapq.heappop(priority_queue)  # Get the state with the lowest cost + heuristic
        if tuple(state) in visited:
            continue

        # Increment the node expansions count for each possible move
        empty_index = state.index(0)
        possible_moves = find_possible_moves(state, empty_index)
        node_expansions += len(possible_moves)

        # Print the current state if needed
        print_puzzle(state)

        if is_goal_state(state):
            print("Solution found!")
            print("Path to solution:")
            for step in path:
                print_puzzle(step)
            return print("Node expansions:", node_expansions)

        visited.add(tuple(state))

        for move in possible_moves:
            new_state = state[:]
            new_state[empty_index], new_state[move] = new_state[move], new_state[empty_index]
            heapq.heappush(priority_queue, (len(path) + 1 + manhattan_distance(new_state), new_state, path + [new_state]))  # Add new state to the queue

    print("No solution found!")

def straight_line_distance(state):
    total_distance = 0
    for i in range(9):
        if state[i] != 0:
            target_row, target_col = divmod(state[i] - 1, 3)
            current_row, current_col = divmod(i, 3)
            distance = math.sqrt((target_row - current_row) ** 2 + (target_col - current_col) ** 2)
            total_distance += distance
    return total_distance

def a_star_straight(initial):
    print("A* (Straight Line Distance) path to solution:")
    state = initial
    visited = set()
    priority_queue = [(0 + straight_line_distance(state), state, [])]  # Priority queue with cost and heuristic
    node_expansions = 0  # Counter to track node expansions

    while priority_queue:
        _, state, path = heapq.heappop(priority_queue)  # Get the state with the lowest cost + heuristic
        if tuple(state) in visited:
            continue

        # Increment the node expansions count for each possible move
        empty_index = state.index(0)
        possible_moves = find_possible_moves(state, empty_index)
        node_expansions += len(possible_moves)

        # Print the current state if needed
        print_puzzle(state)

        if is_goal_state(state):
            print("Solution found!")
            print("Path to solution:")
            for step in path:
                print_puzzle(step)
            return print("Node expansions:", node_expansions)

        visited.add(tuple(state))

        for move in possible_moves:
            new_state = state[:]
            new_state[empty_index], new_state[move] = new_state[move], new_state[empty_index]
            heapq.heappush(priority_queue, (len(path) + 1 + straight_line_distance(new_state), new_state, path + [new_state]))  # Add new state to the queue

    print("No solution found!")

if __name__ == "__main__":
    # Input initial state as a list (e.g., [1, 2, 3, 4, 0, 5, 7, 8, 6])
    initial = [8, 1, 4, 5, 2, 6, 3, 7, 0]  # zero represents "_"

    print("The solution of Q2.1 is:")
    print()
    
    print("The solution of Q2.1.a is:")
    dfs(initial)
    print("-" * 100)
    print()


    print("The solution of Q2.1.b is:")
    bfs(initial)
    print("-" * 100)
    print()

    print("The solution of Q2.1.c is:")
    ucs(initial)
    print("-" * 100)
    print()
    
    print("The solution of Q2.1.d is:")
    a_star_man(initial)
    print("-" * 100)
    print()

    print("The solution of Q2.1.e is:")
    a_star_straight(initial)
    print("-" * 100)
